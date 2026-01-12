#!/usr/bin/env python3
"""
Verify that pinned beads remain at constant distance throughout simulation.
Checks beads 1, 100, 101, 200 (endpoints of two strands).
"""
import numpy as np
import sys
import glob

def verify_pinning(data_dir='data'):
    """Check if pinned beads maintain constant separation."""
    # Find all r files (position snapshots)
    r_files = sorted(glob.glob(f'{data_dir}/r[0-9]*'))
    
    if not r_files:
        print(f"ERROR: No position files found in {data_dir}/")
        return False
    
    print(f"Found {len(r_files)} snapshot files")
    print(f"First: {r_files[0]}, Last: {r_files[-1]}\n")
    
    # Pinned bead indices (0-indexed for Python)
    # Beads 1, 100, 101, 200 → indices 0, 99, 100, 199
    pinned_pairs = np.array([[0,100],[99,199]])
    
    distances = np.zeros((len(r_files),len(pinned_pairs)))
    
    # Read each snapshot
    for i, r_file in enumerate(r_files):
        try:
            # Load positions: shape (NT, 3) where NT=200 beads
            positions = np.loadtxt(r_file)
            
            if positions.shape[0] != 200:
                print(f"WARNING: {r_file} has {positions.shape[0]} beads, expected 200")
                continue
            
            # Calculate distances for pinned pairs
            distances[i,0] = np.linalg.norm(positions[pinned_pairs[0,0]] - positions[pinned_pairs[0,1]])
            distances[i,1] = np.linalg.norm(positions[pinned_pairs[1,0]] - positions[pinned_pairs[1,1]])
        
        except Exception as e:
            print(f"ERROR reading {r_file}: {e}")
            continue
    
    # Analyze results
    print("=" * 70)
    print("PINNING VERIFICATION RESULTS")
    print("=" * 70)
    
    all_pinned = True
    for i in range(len(pinned_pairs)):
        
        dists = distances[:,i]
        mean = np.mean(dists)
        std = np.std(dists)
        min_d = np.min(dists)
        max_d = np.max(dists)
        variation = max_d - min_d
        
        print(f"\n{i}:")
        print(f"  Mean distance: {mean:.6f}")
        print(f"  Std deviation: {std:.6f}")
        print(f"  Min distance:  {min_d:.6f}")
        print(f"  Max distance:  {max_d:.6f}")
        print(f"  Variation:     {variation:.6f}")
        
        # Pinning is successful if variation is very small
        tolerance = 0.01  # Allow 1% of L0 = 3.48 nm
        if variation < tolerance:
            print(f"  ✓ PINNED (variation < {tolerance})")
        else:
            print(f"  ✗ NOT PINNED (variation ={variation:.6f} >= {tolerance})")
            all_pinned = False
    
    print("\n" + "=" * 70)
    if all_pinned:
        print("SUCCESS: All pinned beads maintain constant separation!")
    else:
        print("FAILURE: Pinning constraints not enforced")
    print("=" * 70)
    
    return all_pinned

if __name__ == "__main__":
    data_dir = sys.argv[1] if len(sys.argv) > 1 else 'data'
    success = verify_pinning(data_dir)
    sys.exit(0 if success else 1)
