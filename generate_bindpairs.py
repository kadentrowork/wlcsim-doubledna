#!/usr/bin/env python3
"""
Generate bindpairs file for wlcsim explicit binding simulation.

The bindpairs file specifies which beads are bound to each other.
Format: One line per bead (1-indexed), containing the bead number it's bound to,
        or -1 if unbound.

Usage:
    python3 generate_bindpairs.py --pairs "1:101,2:102,99:199,100:200" --total 200
    python3 generate_bindpairs.py --file pairs.txt --total 200
"""

import argparse
import sys
import os

def parse_pairs(pair_string):
    """
    Parse pair string like "1:101,2:102,99:199,100:200"
    Returns list of tuples [(bead1, bead2), ...]
    """
    pairs = []
    for pair in pair_string.split(','):
        pair = pair.strip()
        if ':' not in pair:
            print(f"Warning: Invalid pair format '{pair}', expected 'bead1:bead2'")
            continue
        bead1, bead2 = pair.split(':')
        pairs.append((int(bead1), int(bead2)))
    return pairs

def read_pairs_from_file(filename):
    """
    Read pairs from file. Each line should contain: bead1 bead2
    Lines starting with # are comments.
    """
    pairs = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            parts = line.split()
            if len(parts) >= 2:
                pairs.append((int(parts[0]), int(parts[1])))
    return pairs

def generate_bindpairs(pairs, total_beads, output_file='input/bindpairs'):
    """
    Generate bindpairs file from list of bead pairs.
    
    Parameters
    ----------
    pairs : list of tuples
        List of (bead1, bead2) pairs to bind. Bead numbers are 1-indexed.
    total_beads : int
        Total number of beads in the simulation
    output_file : str
        Path to output file
        
    Note
    ----
    This generates the 'bindpairs' file used when WLC_P__NETWORK = .FALSE.
    If you're using WLC_P__NETWORK = .TRUE., you would need to generate
    'network_start_index' and 'other_beads' files instead (not implemented here).
    """
    # Create output directory if it doesn't exist
    output_dir = os.path.dirname(output_file)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created directory: {output_dir}")
    
    # Initialize all beads as unbound (-1)
    bindpairs = [-1] * total_beads
    
    # Set up binding pairs (reciprocal)
    for bead1, bead2 in pairs:
        # Convert to 0-indexed for array
        idx1 = bead1 - 1
        idx2 = bead2 - 1
        
        # Validate indices
        if idx1 < 0 or idx1 >= total_beads:
            print(f"Error: Bead {bead1} is out of range (1-{total_beads})")
            sys.exit(1)
        if idx2 < 0 or idx2 >= total_beads:
            print(f"Error: Bead {bead2} is out of range (1-{total_beads})")
            sys.exit(1)
        
        # Check if already bound
        if bindpairs[idx1] != -1:
            print(f"Warning: Bead {bead1} already bound to bead {bindpairs[idx1]}, overwriting...")
        if bindpairs[idx2] != -1:
            print(f"Warning: Bead {bead2} already bound to bead {bindpairs[idx2]}, overwriting...")
        
        # Set reciprocal binding
        bindpairs[idx1] = bead2
        bindpairs[idx2] = bead1
    
    # Write to file
    with open(output_file, 'w') as f:
        for bp in bindpairs:
            f.write(f"{bp}\n")
    
    # Print summary
    bound_count = sum(1 for x in bindpairs if x != -1)
    print(f"Generated bindpairs file: {output_file}")
    print(f"Total beads: {total_beads}")
    print(f"Bound beads: {bound_count}")
    print(f"Binding pairs: {len(pairs)}")
    print(f"\nBound pairs:")
    for bead1, bead2 in sorted(pairs):
        print(f"  Bead {bead1} ↔ Bead {bead2}")

def main():
    parser = argparse.ArgumentParser(
        description='Generate bindpairs file for wlcsim explicit binding',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Bind ends of two 100-bead chains
  python3 generate_bindpairs.py --pairs "1:101,2:102,99:199,100:200" --total 200
  
  # Bind from a file
  python3 generate_bindpairs.py --file pairs.txt --total 200
  
  # Pairs file format (pairs.txt):
  # bead1 bead2
  1 101
  2 102
  99 199
  100 200
        """
    )
    
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--pairs', type=str, 
                       help='Comma-separated bead pairs (1-indexed), e.g., "1:101,2:102"')
    group.add_argument('--file', type=str,
                       help='File containing bead pairs (one pair per line)')
    
    parser.add_argument('--total', type=int, required=True,
                        help='Total number of beads in simulation')
    parser.add_argument('--output', type=str, default='input/bindpairs',
                        help='Output file path (default: input/bindpairs)')
    
    args = parser.parse_args()
    
    # Parse pairs
    if args.pairs:
        pairs = parse_pairs(args.pairs)
    else:
        pairs = read_pairs_from_file(args.file)
    
    if not pairs:
        print("Error: No valid pairs specified")
        sys.exit(1)
    
    # Generate bindpairs file
    generate_bindpairs(pairs, args.total, args.output)

if __name__ == '__main__':
    main()
