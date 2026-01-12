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
load analysis/pdb/dna011.pdb, snap
load analysis/pdb/dna012.pdb, snap
load analysis/pdb/dna013.pdb, snap
load analysis/pdb/dna014.pdb, snap
load analysis/pdb/dna015.pdb, snap
load analysis/pdb/dna016.pdb, snap
load analysis/pdb/dna017.pdb, snap
load analysis/pdb/dna018.pdb, snap
load analysis/pdb/dna019.pdb, snap
load analysis/pdb/dna020.pdb, snap
load analysis/pdb/dna021.pdb, snap
load analysis/pdb/dna022.pdb, snap
load analysis/pdb/dna023.pdb, snap
load analysis/pdb/dna024.pdb, snap
load analysis/pdb/dna025.pdb, snap
load analysis/pdb/dna026.pdb, snap
load analysis/pdb/dna027.pdb, snap
load analysis/pdb/dna028.pdb, snap
load analysis/pdb/dna029.pdb, snap
load analysis/pdb/dna030.pdb, snap
load analysis/pdb/dna031.pdb, snap
load analysis/pdb/dna032.pdb, snap
load analysis/pdb/dna033.pdb, snap
load analysis/pdb/dna034.pdb, snap
load analysis/pdb/dna035.pdb, snap
load analysis/pdb/dna036.pdb, snap
load analysis/pdb/dna037.pdb, snap
load analysis/pdb/dna038.pdb, snap
load analysis/pdb/dna039.pdb, snap
load analysis/pdb/dna040.pdb, snap
load analysis/pdb/dna041.pdb, snap
load analysis/pdb/dna042.pdb, snap
load analysis/pdb/dna043.pdb, snap
load analysis/pdb/dna044.pdb, snap
load analysis/pdb/dna045.pdb, snap
load analysis/pdb/dna046.pdb, snap
load analysis/pdb/dna047.pdb, snap
load analysis/pdb/dna048.pdb, snap
load analysis/pdb/dna049.pdb, snap
load analysis/pdb/dna050.pdb, snap
load analysis/pdb/dna051.pdb, snap
load analysis/pdb/dna052.pdb, snap
load analysis/pdb/dna053.pdb, snap
load analysis/pdb/dna054.pdb, snap
load analysis/pdb/dna055.pdb, snap
load analysis/pdb/dna056.pdb, snap
load analysis/pdb/dna057.pdb, snap
load analysis/pdb/dna058.pdb, snap
load analysis/pdb/dna059.pdb, snap
load analysis/pdb/dna060.pdb, snap
load analysis/pdb/dna061.pdb, snap
load analysis/pdb/dna062.pdb, snap
load analysis/pdb/dna063.pdb, snap
load analysis/pdb/dna064.pdb, snap
load analysis/pdb/dna065.pdb, snap
load analysis/pdb/dna066.pdb, snap
load analysis/pdb/dna067.pdb, snap
load analysis/pdb/dna068.pdb, snap
load analysis/pdb/dna069.pdb, snap
load analysis/pdb/dna070.pdb, snap
load analysis/pdb/dna071.pdb, snap
load analysis/pdb/dna072.pdb, snap
load analysis/pdb/dna073.pdb, snap
load analysis/pdb/dna074.pdb, snap
load analysis/pdb/dna075.pdb, snap
load analysis/pdb/dna076.pdb, snap
load analysis/pdb/dna077.pdb, snap
load analysis/pdb/dna078.pdb, snap
load analysis/pdb/dna079.pdb, snap
load analysis/pdb/dna080.pdb, snap
load analysis/pdb/dna081.pdb, snap
load analysis/pdb/dna082.pdb, snap
load analysis/pdb/dna083.pdb, snap
load analysis/pdb/dna084.pdb, snap
load analysis/pdb/dna085.pdb, snap
load analysis/pdb/dna086.pdb, snap
load analysis/pdb/dna087.pdb, snap
load analysis/pdb/dna088.pdb, snap
load analysis/pdb/dna089.pdb, snap
load analysis/pdb/dna090.pdb, snap
load analysis/pdb/dna091.pdb, snap
load analysis/pdb/dna092.pdb, snap
load analysis/pdb/dna093.pdb, snap
load analysis/pdb/dna094.pdb, snap
load analysis/pdb/dna095.pdb, snap
load analysis/pdb/dna096.pdb, snap
load analysis/pdb/dna097.pdb, snap
load analysis/pdb/dna098.pdb, snap
load analysis/pdb/dna099.pdb, snap
load analysis/pdb/dna100.pdb, snap
load analysis/pdb/dna101.pdb, snap
load analysis/pdb/dna102.pdb, snap
load analysis/pdb/dna103.pdb, snap
load analysis/pdb/dna104.pdb, snap
load analysis/pdb/dna105.pdb, snap
load analysis/pdb/dna106.pdb, snap
load analysis/pdb/dna107.pdb, snap
load analysis/pdb/dna108.pdb, snap
load analysis/pdb/dna109.pdb, snap
load analysis/pdb/dna110.pdb, snap

# Set up movie
mset 1 -111

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
