# Using Brownian Dynamics Configuration

## Recommended Workflow: Start from MC Equilibrated Configuration

### Step 1: Enable saving orientation vectors in MC

The file `src/defines.inc` now has `WLC_P__SAVEU .TRUE.` enabled.

### Step 2: Run a short MC simulation to save both positions and orientations

```bash
make clean && make
./wlcsim.exe
```

This will create files in `data/`: both `r*v0` (positions) and `u*v0` (orientations).

### Step 3: Set up BD from an MC snapshot

Use the provided script:
```bash
./setup_bd_from_mc.sh 110  # Uses snapshot 110 (last frame)
```

Or manually:
```bash
cp data/r110v0 input/r0
cp data/u110v0 input/u0
cp src/defines_bd.inc src/defines.inc
```

### Step 4: Compile and run BD

```bash
make clean && make
./wlcsim.exe
```

## Alternative: Start from Random Configuration

If you want to skip MC equilibration, you can modify `defines_bd.inc` to set:
```fortran
#define WLC_P__FRMFILE .FALSE.
```
Then the BD simulation will initialize using `randomWalkWithBoundary`.

## Key differences: MC (quinn) vs BD (brad)

- **CODENAME**: "brad" (BD) instead of "quinn" (MC)
- **Time-resolved**: Simulates real dynamics with physical time units
- **STEPSPERSAVE**: 10,000 BD timesteps between saves
- **NUMSAVEPOINTS**: 100 frames (instead of 11 MC frames)
- **Initialization**: Can load from MC snapshots using `FRMFILE=.TRUE.`

## What you get:

- Realistic time-dependent trajectories showing polymer relaxation
- Physical time scale (based on DNA friction/viscosity)
- Smooth dynamics instead of discrete configuration sampling
- Total simulation: 1,000,000 BD timesteps

## To switch back to MC:
```bash
git checkout src/defines.inc
# or manually copy your MC version back
```
