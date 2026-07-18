from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


ROOT = Path(__file__).resolve().parent


def estimate_cradle_to_gate(
    lifecycle_tonnes_per_mw: float, capacity_mw: float, cradle_share: float
) -> float:
    """Estimate turbine-level cradle-to-gate emissions in t CO2e."""

    if lifecycle_tonnes_per_mw <= 0 or capacity_mw <= 0:
        raise ValueError("Lifecycle factor and capacity must be positive.")
    if not 0 <= cradle_share <= 1:
        raise ValueError("cradle_share must be between 0 and 1.")
    return lifecycle_tonnes_per_mw * capacity_mw * cradle_share


def add_stage_shares(frame: pd.DataFrame) -> pd.DataFrame:
    """Validate stage totals and calculate their percentage contributions."""

    required = {"impact_category", "unit", "manufacturing", "plant_setup", "total"}
    missing = required.difference(frame.columns)
    if missing:
        raise ValueError(f"Missing columns: {sorted(missing)}")
    numeric = frame[["manufacturing", "plant_setup", "total"]]
    if (numeric < 0).any().any() or (frame["total"] <= 0).any():
        raise ValueError("Impact values must be non-negative and totals positive.")
    difference = (frame["manufacturing"] + frame["plant_setup"] - frame["total"]).abs()
    if (difference > 1e-9).any():
        raise ValueError("Stage values do not reconcile to total.")
    result = frame.copy()
    result["manufacturing_share"] = result["manufacturing"] / result["total"]
    result["plant_setup_share"] = result["plant_setup"] / result["total"]
    return result


def main() -> None:
    impact = pd.read_csv(ROOT / "data/reference/impact_by_stage.csv")
    impact = add_stage_shares(impact)
    inputs = pd.read_csv(ROOT / "data/reference/scenario_inputs.csv").set_index("parameter")

    factor = float(inputs.loc["lifecycle_emissions_factor", "value"])
    capacity = float(inputs.loc["capacity", "value"])
    scenarios = []
    for name in ("low", "base", "high"):
        share = float(inputs.loc[f"{name}_cradle_to_gate_share", "value"])
        scenarios.append(
            {
                "scenario": name.title(),
                "cradle_to_gate_share": share,
                "estimated_t_co2e": estimate_cradle_to_gate(factor, capacity, share),
            }
        )
    scenario_frame = pd.DataFrame(scenarios)

    tables = ROOT / "outputs/tables"
    figures = ROOT / "outputs/figures"
    tables.mkdir(parents=True, exist_ok=True)
    figures.mkdir(parents=True, exist_ok=True)
    impact.to_csv(tables / "impact_stage_shares.csv", index=False)
    scenario_frame.to_csv(tables / "cradle_to_gate_scenarios.csv", index=False)

    ordered = impact.sort_values("manufacturing_share")
    fig, ax = plt.subplots(figsize=(9, 6))
    ax.barh(ordered["impact_category"], ordered["manufacturing_share"] * 100, color="#167D9A")
    ax.set(title="Manufacturing dominates the cradle-to-gate impact profile", xlabel="Manufacturing share of category total (%)")
    ax.set_xlim(0, 105)
    ax.grid(axis="x", alpha=0.2)
    fig.tight_layout()
    fig.savefig(figures / "manufacturing_share.png", dpi=180, facecolor="white")
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(scenario_frame["scenario"], scenario_frame["estimated_t_co2e"], color=["#6BAED6", "#167D9A", "#0B4558"])
    ax.bar_label(bars, labels=[f"{value:,.0f}" for value in scenario_frame["estimated_t_co2e"]], padding=4)
    ax.set(title="Cradle-to-gate emissions are assumption-sensitive", ylabel="Estimated t CO2e per turbine")
    ax.set_ylim(0, scenario_frame["estimated_t_co2e"].max() * 1.15)
    ax.grid(axis="y", alpha=0.2)
    fig.tight_layout()
    fig.savefig(figures / "cradle_to_gate_scenarios.png", dpi=180, facecolor="white")
    plt.close(fig)

    print(scenario_frame.to_string(index=False))


if __name__ == "__main__":
    main()
