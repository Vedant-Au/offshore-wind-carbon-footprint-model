# GitHub setup

## Create and upload

1. On GitHub, select **New repository**.
2. Name it `offshore-wind-carbon-footprint-model`, set it to **Public**, and do not add a README, licence or `.gitignore`.
3. Select **uploading an existing file** on the empty-repository page.
4. In Finder, open the extracted project folder. Press **Command + Shift + .** so `.github` and `.gitignore` are visible.
5. Drag everything *inside* the project folder into GitHub. Do not upload the ZIP or the outer folder.
6. Wait for every file to finish staging. Confirm that `.github/workflows/quality.yml`, `.gitignore`, `README.md`, `analysis.py`, `data`, `docs`, `outputs` and `tests` are present.
7. Use commit message `Add offshore wind carbon footprint scenario model`, select **Commit directly to the main branch**, and select **Commit changes**.

## Verify and present

1. On the repository homepage, confirm the README renders both charts.
2. Open **Actions** and confirm the `quality` workflow passes. A first run can take a few minutes.
3. From the **About** gear, add description `Cradle-to-gate carbon scenario model for a 15 MW offshore wind turbine.`
4. Add topics: `sustainability`, `carbon-accounting`, `life-cycle-assessment`, `python`, `scenario-analysis`, `offshore-wind`.
5. Pin the repository only when targeting sustainability, energy or carbon-analysis roles.
