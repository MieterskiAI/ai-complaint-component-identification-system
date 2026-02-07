# Example Analysis Output (synthetic)

> Format: **Elimination → Top 1–2 components → Reasoning**

## Case: CMP-2025-0007 (HV-2000-AX)

**Eliminated**
- Control board: no error codes, intermittent start aligns with mechanical load rather than logic failure.
- Power cable/connector: stable power reported, symptoms appear under load not at idle.

**Top candidates**
1. **Motor coupling**
2. **Bearing set (front)**

**Reasoning**
- Vibration increases with load and time-on-task, consistent with coupling wear or bearing fatigue.
- Noise appears after load threshold, pointing to mechanical imbalance rather than electrical faults.

---

## Case: CMP-2025-0011 (PMP-320-Z)

**Eliminated**
- Inlet filter: pressure drop is paired with visible leak, not just flow restriction.
- Control valve: symptom appears only during continuous operation, indicating mechanical seal degradation.

**Top candidates**
1. **Rear seal kit**
2. **Shaft gasket**

**Reasoning**
- Visible liquid at rear seal area suggests seal wear or gasket failure.
- Pressure drop under continuous duty aligns with progressive leak rather than sudden blockage.

---

## Case: CMP-2025-0019 (DRV-110-S)

**Eliminated**
- Main power module: unit starts and runs for 15 minutes, indicating power delivery is stable.
- Control firmware: no reported error codes or update events.

**Top candidates**
1. **Cooling fan assembly**
2. **Air intake filter**

**Reasoning**
- Overheating with low airflow suggests obstructed intake or underperforming fan.
- Shutdown after 15 minutes matches thermal protection behavior.
