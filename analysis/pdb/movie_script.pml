# PyMol movie script for wlcsim DNA simulation
# Load all frames
load analysis/pdb/dna000.pdb, snap
load analysis/pdb/dna001.pdb, snap
load analysis/pdb/dna002.pdb, snap
load analysis/pdb/dna003.pdb, snap
load analysis/pdb/dna004.pdb, snap
load analysis/pdb/dna005.pdb, snap
load analysis/pdb/dna006.pdb, snap
load analysis/pdb/dna007.pdb, snap
load analysis/pdb/dna008.pdb, snap
load analysis/pdb/dna009.pdb, snap
load analysis/pdb/dna010.pdb, snap

# Set up movie
mset 1 -11

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
