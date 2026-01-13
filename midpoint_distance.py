#!/usr/bin/env python3
"""
Calculate the distance between midpoints of two DNA chains over time.
"""

import numpy as np
import matplotlib.pyplot as plt
import glob
import os

def read_r_file(filename):
    """Read position data from r*v0 file."""
    data = np.loadtxt(filename)
    # Each row is [x, y, z] for one bead
    return data

def calculate_midpoint_distance(r_data, nb=100):
    """
    Calculate distance between midpoints of two chains.
    
    Parameters:
    -----------
    r_data : ndarray
        Position data with shape (NT, 3) where NT = 2*NB
    nb : int
        Number of beads per chain
    
    Returns:
    --------
    float : Distance between chain midpoints
    """
    # Chain A: beads 0 to nb-1 (0-indexed)
    # Chain B: beads nb to 2*nb-1
    chain_a = r_data[:nb, :]
    chain_b = r_data[nb:, :]
    
    # Calculate midpoints
    midpoint_a = r_data[nb//2,:]
    midpoint_b = r_data[nb + nb//2,:]
    
    # Calculate Euclidean distance
    distance = np.linalg.norm(midpoint_a - midpoint_b)
    
    return distance

def main():
    # Find all r*v0 files
    data_dir = "data"
    r_files = sorted(glob.glob(os.path.join(data_dir, "r*v0")))
    
    if not r_files:
        print("No r*v0 files found in data/")
        return
    
    print(f"Found {len(r_files)} data files")
    
    # Calculate distances for each time point
    distances = []
    time_points = []
    
    for i, r_file in enumerate(r_files):
        r_data = read_r_file(r_file)
        distance = calculate_midpoint_distance(r_data, nb=100)
        distances.append(distance)
        time_points.append(i)
        print(f"Frame {i}: midpoint distance = {distance:.3f} nm")
    
    # Convert to arrays
    time_points = np.array(time_points)
    distances = np.array(distances)
    
    # Save data
    output_file = "midpoint_distances.txt"
    np.savetxt(output_file, np.column_stack([time_points, distances]),
               header="TimePoint Distance(nm)", fmt='%d %.6f')
    print(f"\nData saved to {output_file}")
    
    # Plot
    plt.figure(figsize=(10, 6))
    plt.plot(time_points, distances, 'o-', linewidth=2, markersize=8)
    plt.xlabel('Time Point', fontsize=14)
    plt.ylabel('Midpoint Distance (nm)', fontsize=14)
    plt.title('Distance Between Chain Midpoints Over Time', fontsize=16)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    plot_file = "midpoint_distances.png"
    plt.savefig(plot_file, dpi=150)
    print(f"Plot saved to {plot_file}")
    plt.show()
    
    # Print statistics
    print(f"\nStatistics:")
    print(f"  Mean distance: {np.mean(distances):.3f} nm")
    print(f"  Std deviation: {np.std(distances):.3f} nm")
    print(f"  Min distance:  {np.min(distances):.3f} nm")
    print(f"  Max distance:  {np.max(distances):.3f} nm")

if __name__ == "__main__":
    main()
