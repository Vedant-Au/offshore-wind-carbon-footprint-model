# Where Is the Carbon Before an Offshore Turbine Operates?

## A cradle-to-gate boundary and scenario study for the Vestas V236-15 MW

[![Quality checks](https://github.com/Vedant-Au/offshore-wind-carbon-footprint-model/actions/workflows/quality.yml/badge.svg)](https://github.com/Vedant-Au/offshore-wind-carbon-footprint-model/actions/workflows/quality.yml)

**Team of 6** · Managing Business Operations, MSc Business Analysis and Consulting (University of Strathclyde) · Jan–Feb 2026 · ISO 14040/14044, GWP100

> **The emissions sit in manufacturing, and mostly in steel.** Foundations contribute **25%** of cradle-to-gate global warming potential and the tower **13%**. Steel is roughly **82.9%** of total turbine mass, so the footprint is largely a steel procurement question rather than a turbine design question.

| Component | Share of cradle-to-gate GWP |
| --- | ---: |
| Foundations | 25% |
| Tower | 13% |
| Blades | 9% |
| Site cables | 9% |
| Nacelle | 7% |
| Gear and main shaft | 5% |
| Set-up stage (installation vessels) | 4% |
| Offshore substation | 3% |

Carbon dioxide accounts for **92%** of the impact and methane **6%**. Sulphur hexafluoride, despite a very high global warming potential per unit, contributes about **1%** because so little is used.

That makes the first management question clear: focus supplier and engineering effort on steel, materials and manufacturing before optimising the smaller set-up contribution.

![One-page summary](one-pager.png)

## Boundary before number

```mermaid
flowchart LR
    A["Raw materials"] --> B["Processing"]
    B --> C["Manufacturing"]
    C --> D["Transport"]
    D --> E["Offshore setup"]
```

This is a **cradle-to-gate** view. Operations, maintenance and end-of-life sit outside the scenario. That distinction matters because carbon figures with different system boundaries cannot be ranked as though they measure the same thing.

| Included in the model | Not claimed by the model |
| --- | --- |
| Published stage-intensity reference table | Verified product carbon footprint |
| Manufacturing/setup contribution by impact category | Supplier-specific bill of materials |
| 70%, 75% and 80% allocation scenarios | Whole-life competitor comparison |
| Unit and reconciliation checks | Abatement cost or engineering feasibility |

## Two calculations—kept deliberately separate

### Impact-category view

`manufacturing share = manufacturing / (manufacturing + plant setup)`

This ratio comes from a published stage-intensity reference table used for scenario modelling. It is a different measure from the component shares above and is not used as a headline finding.

### Turbine planning view

`cradle-to-gate t CO2e = 528 t CO2e/MW × 15 MW × allocation share`

The second view produces **5,544-6,336 t CO2e per turbine** across the 70%-80% range. It is a planning scenario, not an extra quantity to add to the per-kWh profile.

![Cradle-to-gate scenarios](outputs/figures/cradle_to_gate_scenarios.png)

## Decision implications

1. Engage steel, composite and component suppliers on verified embodied-carbon data.
2. Test lower-carbon material and manufacturing alternatives against cost and technical constraints.
3. Address logistics after the dominant manufacturing hotspots are understood.
4. Refresh the model when supplier and bill-of-material evidence replaces reference assumptions.

The underlying MSc assessment was a six-person team project. The work covered defining the boundary, applying ISO 14040/14044 logic, converting intensity factors into turbine scenarios and rejecting invalid competitor comparisons. The [one-page summary](one-pager.pdf) gives the full picture.

## Calculation audit

The full formula trail is in [boundary and calculations](docs/BOUNDARY_CALCULATIONS.md); reconciliations and interpretation checks are in [model checks](docs/MODEL_CHECKS.md).

```bash
pip install -r requirements.txt
python analysis.py
python -m unittest discover -s tests -v
```

> **Use with care:** reference inputs come from an academic case, not a verified inventory. The work is not affiliated with or endorsed by Vestas or Siemens Gamesa. See [ASSET_NOTICE.md](ASSET_NOTICE.md).
