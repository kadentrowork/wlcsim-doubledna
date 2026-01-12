#!/usr/bin/env python
"""
Simple script to create a PyMol movie from wlcsim DNA simulation data.
This script works with constant elasticity DNA (no nucleosomes).

Usage:
    python make_movie.py [--pymol /path/to/pymol] [--frames 111] [--start 0]
"""

import numpy as np
import os
import argparse
from analysis.r2pdb import mkpdb, save_pdb

def create_movie(data_path='data/', pdb_path='analysis/pdb/', 
                 start_frame=0, num_frames=111, channel=0,
                 pymol_exe='pymol'):
    """
    Create PDB files and launch PyMol movie for DNA simulation.
    
    Parameters
    ----------
    data_path : str
        Path to the data directory containing r*v* and u*v* files
    pdb_path : str
        Path where PDB files will be saved
    start_frame : int
        Starting frame number
    num_frames : int
        Number of frames to include
    channel : int
        Channel/replica number (the 'v' in r*v*)
    pymol_exe : str
        Path to PyMol executable
    """
    
    # Create PDB directory if it doesn't exist
    os.makedirs(pdb_path, exist_ok=True)
    
    print(f"Creating {num_frames} PDB files...")
    
    for frame in range(start_frame, start_frame + num_frames):
        r_file = os.path.join(data_path, f'r{frame}v{channel}')
        
        if not os.path.exists(r_file):
            print(f"Warning: {r_file} not found, skipping...")
            continue
        
        # Load position data
        r = np.loadtxt(r_file)
        
        # Determine number of polymers (NP=2 in your case)
        # Each polymer has NB beads (100 in your case)
        n_total = len(r)
        n_polymers = 2  # From your defines.inc: WLC_P__NP 2
        n_beads = n_total // n_polymers  # 100 beads per polymer
        
        # Create chain labels (A for first polymer, B for second)
        chains = ['A'] * n_beads + ['B'] * n_beads
        
        # Create connectivity - beads connected within each polymer
        connect = []
        for p in range(n_polymers):
            offset = p * n_beads
            for i in range(n_beads - 1):
                connect.append((offset + i, offset + i + 1))
        
        # Generate PDB
        lines = mkpdb(r, connect=connect, chain=chains, topology='linear')
        
        # Save PDB file
        pdb_file = os.path.join(pdb_path, f'dna{frame:03d}.pdb')
        save_pdb(pdb_file, lines)
        
        if (frame - start_frame) % 20 == 0:
            print(f"  Created frame {frame - start_frame + 1}/{num_frames}")
    
    print("PDB files created!")
    
    # Create PyMol script
    pymol_script = os.path.join(pdb_path, 'movie_script.pml')
    with open(pymol_script, 'w') as f:
        f.write(f"""# PyMol movie script for wlcsim DNA simulation
# Load all frames
""")
        for frame in range(start_frame, start_frame + num_frames):
            f.write(f'load {pdb_path}dna{frame:03d}.pdb, snap\n')
        
        f.write(f"""
# Set up movie
mset 1 -{num_frames}

# Enable reading of CONECT records for bonds
set connect_mode, 1

# Show as spheres with sticks for bonds
show spheres, snap
show sticks, snap
hide lines, snap

# Color chains differently  
color red, chain A
color blue, chain B

# Set sphere size (beads)
set sphere_scale, 1.0

# Set stick radius (bonds between beads)
set stick_radius, 0.3

# Set background
bg_color white

# Focus only on chain A (first polymer)
orient chain A
zoom chain A, -20

# Hide chain B to reduce clutter (comment out next line to show both)
# hide everything, chain B

# Play movie
mplay
""")
    
    print(f"PyMol script created: {pymol_script}")
    print(f"\nTo view the movie, run:")
    print(f"  {pymol_exe} {pymol_script}")
    print(f"\nOr to run directly:")
    
    # Launch PyMol
    response = input("Launch PyMol now? [y/N]: ")
    if response.lower() == 'y':
        os.system(f'{pymol_exe} {pymol_script}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create PyMol movie from wlcsim DNA data')
    parser.add_argument('--data', default='data/', help='Path to data directory')
    parser.add_argument('--pdb', default='analysis/pdb/', help='Path for PDB output')
    parser.add_argument('--start', type=int, default=0, help='Starting frame')
    parser.add_argument('--frames', type=int, default=111, help='Number of frames')
    parser.add_argument('--channel', type=int, default=0, help='Channel/replica number')
    parser.add_argument('--pymol', default='pymol', help='Path to PyMol executable')
    
    args = parser.parse_args()
    
    create_movie(
        data_path=args.data,
        pdb_path=args.pdb,
        start_frame=args.start,
        num_frames=args.frames,
        channel=args.channel,
        pymol_exe=args.pymol
    )
