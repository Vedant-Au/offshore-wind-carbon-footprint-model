# Offshore Wind Carbon Footprint Model

**A transparent cradle-to-gate scenario model for the Vestas V236-15 MW offshore wind turbine.**

[![Quality checks](https://github.com/Vedant-Au/offshore-wind-carbon-footprint-model/actions/workflows/quality.yml/badge.svg)](https://github.com/Vedant-Au/offshore-wind-carbon-footprint-model/actions/workflows/quality.yml)

**Portfolio:** [Digital inclusion](https://github.com/Vedant-Au/ons-census-2031-digital-inclusion-risk) · [Accessibility business case](https://github.com/Vedant-Au/accessible-employee-services-business-case) · [Enterprise risk](https://github.com/Vedant-Au/enterprise-risk-management-framework) · [Workflow automation](https://github.com/Vedant-Au/vfx-workflow-automation-decision-model)

> Portfolio context: this repository develops an MSc group case study into a reproducible analytics project. It is not affiliated with or endorsed by Vestas or Siemens Gamesa, and it does not reproduce the submitted report.

## Recruiter quick scan

| Lens | Evidence |
| --- | --- |
| Decision | Where to focus first to reduce embodied carbon before operation |
| Analysis | Boundary definition, unit-aware calculations and scenario testing |
| Recommendation | Prioritise lower-carbon materials and manufacturing, then logistics |
| Assurance | Explicit limitations, reconciliation checks and reproducible outputs |

**Contribution and provenance:** the source was an MSc group case. This repository is an individual portfolio reconstruction of the analytical model and decision narrative. It uses case-study reference inputs and does not claim product-level LCA assurance.

## Decision question

Where should an offshore-wind manufacturer focus first to reduce embodied carbon before a turbine begins operating?

## Answer first

- The published impact profile used in the case assigns **7.1 of 7.5 g CO2e/kWh** of cradle-to-gate global-warming potential to manufacturing - approximately **94.7%**.
- Applying the report's 70%-80% cradle-to-gate share to its 7,920 t CO2e lifecycle estimate produces a planning range of **5,544-6,336 t CO2e per turbine**.
- The highest-leverage actions are therefore lower-carbon material sourcing and manufacturing improvement, followed by lower-emission logistics and regular LCA refreshes.
- The range is a scenario estimate, not a product declaration. It should be replaced with verified bill-of-material, supplier and logistics data before operational use.

![Stage contribution](outputs/figures/manufacturing_share.png)

![Cradle-to-gate scenarios](outputs/figures/cradle_to_gate_scenarios.png)

## What the model does

1. Validates the public-reference impact table used by the case.
2. Calculates manufacturing and plant-setup shares for each impact category.
3. Converts lifecycle t CO2e/MW into turbine-level emissions.
4. Tests 70%, 75% and 80% cradle-to-gate allocation scenarios.
5. Produces decision-ready tables and charts.

## Skills demonstrated

- Lifecycle-assessment boundary definition
- Carbon accounting and unit-aware modelling
- Scenario and sensitivity analysis
- Data validation and reproducible Python
- Sustainability recommendations with explicit evidence limits

## Reproduce

```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python analysis.py
python -m unittest discover -s tests -v
```

## Repository structure

```text
data/reference/       Case-study reference inputs
docs/                 Methodology and validation notes
outputs/figures/      Recreated decision visuals
outputs/tables/       Scenario and stage-share outputs
tests/                Model and data-quality tests
analysis.py           Reproducible analysis entry point
```

## Responsible interpretation

The impact table is expressed per kWh, while the scenario model estimates turbine-level tonnes using a reported lifecycle factor and an assumed cradle-to-gate share. These are separate analytical views and are not added together. Competitor figures from the academic report are excluded because system boundaries must be aligned before a fair comparison.

See [methodology](docs/METHODOLOGY.md), [validation status](docs/VALIDATION.md), and [asset notice](ASSET_NOTICE.md).
