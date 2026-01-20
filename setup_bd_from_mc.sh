#!/bin/bash
# Script to set up Brownian Dynamics simulation using MC equilibrated configuration

# Usage: ./setup_bd_from_mc.sh [snapshot_number]
# Example: ./setup_bd_from_mc.sh 110  (uses data/r110v0 and data/u110v0)

SNAPSHOT=${1:-110}  # Default to last snapshot (r110v0)

echo "Setting up BD simulation from MC snapshot ${SNAPSHOT}..."

# Check if files exist
if [ ! -f "data/r${SNAPSHOT}v0" ]; then
    echo "ERROR: data/r${SNAPSHOT}v0 not found!"
    echo "Available snapshots:"
    ls data/r*v0 | tail -10
    exit 1
fi

if [ ! -f "data/u${SNAPSHOT}v0" ]; then
    echo "ERROR: data/u${SNAPSHOT}v0 not found!"
    echo "You need to enable WLC_P__SAVEU=.TRUE. in defines.inc and rerun MC."
    exit 1
fi

# Copy MC snapshot to input directory
echo "Copying configuration files..."
cp "data/r${SNAPSHOT}v0" input/r0
cp "data/u${SNAPSHOT}v0" input/u0

# Switch to BD configuration
echo "Switching to BD configuration..."
cp src/defines_bd.inc src/defines.inc

echo ""
echo "Setup complete! Now run:"
echo "  make clean && make"
echo "  ./wlcsim.exe"
echo ""
echo "This will run BD with:"
echo "  - Initial configuration from MC snapshot ${SNAPSHOT}"
echo "  - 1,000,000 BD timesteps"
echo "  - 100 saved frames (every 10,000 steps)"
echo "  - Explicit binding constraints maintained"
