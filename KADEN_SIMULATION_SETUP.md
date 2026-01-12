# Kaden's DNA Simulation Setup

## Summary
Your defines file from before the weekend was not found in git history or the workspace. I've created TWO versions based on your description.

## Files Created

### Version 1: Loop with Kinks (Original Request)
1. **[input/example_defines/Kaden_DNA_kinks.inc](input/example_defines/Kaden_DNA_kinks.inc)** - Defines file for loop
2. **[input/ab_kaden_two_kinks](input/ab_kaden_two_kinks)** - Chemical sequence file specifying kink positions

### Version 2: Pinned Strands (Preferred - CURRENT)
1. **[input/example_defines/Kaden_DNA_pinned.inc](input/example_defines/Kaden_DNA_pinned.inc)** - Defines file for pinned strands
2. **[input/bindpairs_kaden](input/bindpairs_kaden)** - Specifies which beads are pinned together

## Configuration Details

### Approach 1: Loop with Kinks (Current Implementation)

**Key Parameters Modified:**
- `WLC_P__RING = .TRUE.` - Creates a closed DNA loop
- `WLC_P__ELASTICITY_TYPE = "nucleosomes"` - Enables kinking capability
- `WLC_P__CHEM_SEQ_FROM_FILE = .TRUE.` - Reads kink positions from file
- `WLC_P__NB = 200` - 200 beads in the loop
- `WLC_P__L = 690.0_dp` - Total length ~690 nm

**Kink Positions:**
- First kink: bead 50 (25% around loop)
- Second kink: bead 150 (75% around loop)
- Kink angle: ~175 degrees (achieved by setting wrapped bp = 147, which uses nucleosome geometry)

**How It Works:**
The nucleosome elasticity type uses pre-calculated rotation matrices and translation vectors from `input/nucleosomeR` and `input/nucleosomeT`. When a bead is marked as type 1 (nucleosome/kink) with 147 wrapped base pairs, it creates the characteristic nucleosome kink angle, which is approximately 175 degrees based on the nucleosome crystal structure geometry.

### Approach 2: Two Strands with Pinned Ends (**IMPLEMENTED**)

**Configuration:** [input/example_defines/Kaden_DNA_pinned.inc](input/example_defines/Kaden_DNA_pinned.inc)

**Key Parameters:**
- `WLC_P__RING = .FALSE.` - Two separate linear strands
- `WLC_P__NP = 2` - Two separate polymers
- `WLC_P__NB = 100` - 100 beads per strand
- `WLC_P__L = 345.0_dp` - ~345 nm per strand
- `WLC_P__NETWORK = .TRUE.` - Enable bead pinning
- `WLC_P__ELASTICITY_TYPE = "constant"` - Regular DNA elasticity (no kinks)

**Pinning Configuration:** [input/bindpairs_kaden](input/bindpairs_kaden)

The bindpairs file uses 1-based indexing where:
- Polymer 1: beads 1-100 (indices 0-99 in file)
- Polymer 2: beads 101-200 (indices 100-199 in file)

**Pinned beads:**
- Bead 1 (index 0) ↔ Bead 101 (index 100) - First bead of each strand
- Bead 2 (index 1) ↔ Bead 102 (index 101) - Second bead of each strand  
- Bead 99 (index 98) ↔ Bead 199 (index 198) - Second-to-last bead of each strand
- Bead 100 (index 99) ↔ Bead 200 (index 199) - Last bead of each strand

**Advantages of Network Approach:**
- More physically realistic for two separate DNA strands
- Easier to adjust tension at pinning points
- No need for nucleosome kinking complications
- Can visualize individual strands

**Advantages of Ring Approach:**
- Simpler topology
- Naturally enforces connectivity
- Better for studying conformational dynamics of closed loops

## Next Steps

**To use the pinned strands version (recommended):**

1. The defines file is ready at: [input/example_defines/Kaden_DNA_pinned.inc](input/example_defines/Kaden_DNA_pinned.inc)
2. The bindpairs file is ready at: [input/bindpairs_kaden](input/bindpairs_kaden)
3. When running, you'll need to ensure the simulation reads from `bindpairs_kaden`

**To switch back to loop with kinks version:**
- Use [input/example_defines/Kaden_DNA_kinks.inc](input/example_defines/Kaden_DNA_kinks.inc)
- Copy [input/ab_kaden_two_kinks](input/ab_kaden_two_kinks) to `input/ab`

## Bindpairs File Format

The [input/bindpairs_kaden](input/bindpairs_kaden) file has one line per bead:
- Line number = bead index (0-based)
- Value = index of partner bead, or -1 if no partner
- Total 200 lines (100 beads × 2 polymers)

**Example:**
```
Line 0:  100  → Bead 0 (first bead of strand 1) pinned to bead 100 (first bead of strand 2)
Line 1:  101  → Bead 1 (second bead of strand 1) pinned to bead 101 (second bead of strand 2)
Line 98: 198  → Bead 98 (2nd-last of strand 1) pinned to bead 198 (2nd-last of strand 2)
Line 99: 199  → Bead 99 (last of strand 1) pinned to bead 199 (last of strand 2)
Line 100: 0   → Bead 100 (first of strand 2) pinned to bead 0 (reciprocal)
Line 101: 1   → Bead 101 (second of strand 2) pinned to bead 1 (reciprocal)
Line 198: 98  → Bead 198 (2nd-last of strand 2) pinned to bead 98 (reciprocal)
Line 199: 99  → Bead 199 (last of strand 2) pinned to bead 99 (reciprocal)
```

## Notes

### Pinned Strands Version
- Two separate DNA strands, each 100 beads long (~345 nm)
- Last 2 beads on each end are pinned together (4 pinning points total)
- Uses regular "constant" elasticity (no kinks needed)
- Total system: 200 beads across 2 polymers

### Loop with Kinks Version  
- Single closed loop of 200 beads (~690 nm circumference)
- Two kinks at beads 50 and 150 (opposite sides of loop)
- Kinks use nucleosome geometry to create ~175° angle
- The exact angle depends on the pre-computed nucleosome rotation matrices
