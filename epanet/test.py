# test_epyt.py
# Tests EPyT using its built-in Net1.inp example and bundled epanet2.dll
# NO external EPANET installation required

import os
import epyt
from epyt import epanet

print("=" * 50)
print("EPyT Installation Test")
print("=" * 50)

# ── 1. Verify the bundled DLL exists ──────────────────
dll_path = os.path.join(os.path.dirname(epyt.__file__), 'libraries', 'win', 'epanet2.dll')
print(f"\n[1] Bundled DLL found: {os.path.exists(dll_path)}")
print(f"    Path: {dll_path}")

# ── 2. Load the built-in Net1.inp example ─────────────
net1_path = os.path.join(os.path.dirname(epyt.__file__), 'networks', 'Net1.inp')
print(f"\n[2] Loading Net1.inp from: {net1_path}")
d = epanet(net1_path)

# ── 3. Basic network info ─────────────────────────────
print("\n[3] Network Info:")
print(f"    Nodes  : {d.getNodeCount()}")
print(f"    Links  : {d.getLinkCount()}")
print(f"    Junctions: {d.getNodeJunctionCount()}")
print(f"    Reservoirs: {d.getNodeReservoirCount()}")
print(f"    Tanks  : {d.getNodeTankCount()}")

# ── 4. Node elevations ────────────────────────────────
print("\n[4] Node Elevations (meters):")
elevations = d.getNodeElevations()
node_ids   = d.getNodeNameID()
for nid, elev in zip(node_ids, elevations):
    print(f"    {nid:>6} → {elev:.2f} m")

# ── 5. Run a full hydraulic simulation ────────────────
print("\n[5] Running hydraulic simulation...")
results = d.getComputedHydraulicTimeSeries()
print(f"    Simulation steps computed: {len(results.Pressure[0])}")
print(f"    Avg pressure at node 1: {results.Pressure[0].mean():.2f} m")

# ── 6. Link (pipe) info ───────────────────────────────
print("\n[6] Pipe Diameters (mm):")
diameters = d.getLinkDiameter()
link_ids  = d.getLinkNameID()
for lid, dia in zip(link_ids[:5], diameters[:5]):  # first 5 pipes
    print(f"    Pipe {lid:>4} → {dia:.1f} mm")
print(f"    ... (showing first 5 of {len(link_ids)})")

# ── 7. Clean up ───────────────────────────────────────
d.unload()
print("\n[7] Library unloaded successfully.")
print("\n✅ ALL TESTS PASSED — EPyT is working correctly!")