# How to Extend This Package

This package is intentionally minimal and can be expanded over time.

## Add new data
1. Put new files under `data/`.
2. Add a one-line description in `README.md` under **Data Files**.
3. Add file paths to `docs/MANIFEST.md`.

## Add new code
1. Put scripts/notebooks in one of:
   - `code/preprocessing/`
   - `code/error_generation/`
   - `code/experiments/`
   - `code/evaluation/`
2. Add a short run note at the top of each script/notebook.
3. Update `README.md` with purpose + entry points.
4. Update `docs/MANIFEST.md`.

## Add new figures
1. Put exported figure files in `figures/`.
2. If used in the paper, ensure they are referenced in `paper/main.tex`.
3. Update `README.md` and `docs/MANIFEST.md`.

## Keep reproducibility clear
- Prefer stable filenames.
- Keep external data sources cited in the paper references.
- Record software/model versions when updating results.
