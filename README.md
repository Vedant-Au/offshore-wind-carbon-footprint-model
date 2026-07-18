# Offshore Wind Carbon Footprint Model

**A boundary-conscious cradle-to-gate scenario model for the Vestas V236-15 MW offshore turbine.**

[![Quality checks](https://github.com/Vedant-Au/offshore-wind-carbon-footprint-model/actions/workflows/quality.yml/badge.svg)](https://github.com/Vedant-Au/offshore-wind-carbon-footprint-model/actions/workflows/quality.yml)

**Role:** Team Lead, sustainability and emissions assessment  
**Decision:** where should a manufacturer intervene first to reduce embodied carbon before operation?

## Finding

Manufacturing is the dominant intervention point in the case evidence:

- It accounts for **7.1 of 7.5 g CO2e/kWh**, or **94.7%**, of the published cradle-to-gate global-warming profile used by the case.
- Applying the report's 70%-80% cradle-to-gate allocation to its lifecycle estimate produces a planning range of **5,544-6,336 t CO2e per turbine**.
- The first priorities are therefore lower-carbon material sourcing and manufacturing improvement, followed by lower-emission logistics and recurring LCA refreshes.

![Stage contribution](outputs/figures/manufacturing_share.png)

![Cradle-to-gate scenarios](outputs/figures/cradle_to_gate_scenarios.png)

## What I led

I led the underlying MSc assessment: defining the cradle-to-gate boundary, applying ISO 14040/14044 logic, converting reported intensity factors to turbine-level scenarios and challenging competitor comparisons where system boundaries were not aligned.

The repository turns that work into a reproducible Python implementation that:

1. validates the reference impact table;
2. calculates manufacturing and plant-setup shares by impact category;
3. converts lifecycle t CO2e/MW into turbine-level emissions;
4. tests 70%, 75% and 80% cradle-to-gate allocation scenarios; and
5. produces traceable tables and figures.

## Analytical judgement

The per-kWh impact profile and the turbine-level scenario are **separate views**. They are not added together. Competitor figures are also excluded from the implementation because comparing lifecycle results with different boundaries would create false precision.

That boundary discipline is the main analytical choice in this model: a narrower, defensible comparison is more useful than a broader but invalid benchmark.

See the [methodology](docs/METHODOLOGY.md) and [validation notes](docs/VALIDATION.md) for formulas and reconciliation checks.

## Reproduce the model

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python analysis.py
python -m unittest discover -s tests -v
```

```text
data/reference/       Case-study reference inputs
docs/                 Methodology and validation notes
outputs/figures/      Decision visuals
outputs/tables/       Scenario and stage-share outputs
tests/                Model and data-quality tests
analysis.py           Reproducible analysis entry point
```

## Evidence boundary

The range is a scenario estimate, not a product declaration. It should be replaced with verified bill-of-material, supplier and logistics data before operational use. This work is not affiliated with or endorsed by Vestas or Siemens Gamesa; see [ASSET_NOTICE.md](ASSET_NOTICE.md).
