# PLAN.md — mirror-signal roadmap

Status: 2026-10-05.

## Step 0 — scaffold (done)

## Step 1 — verify public endpoints

- npmmirror stats: https://registry.npmmirror.com/-/binary/ (directory listing) and any JSON stats API
- tuna status: https://mirrors.tuna.tsinghua.edu.cn/static/json/status.json
- pypistats: https://pypistats.org/api/packages/requests/recent
- crates.io: https://crates.io/api/v1/crates (no per-day download log public; skip or use lib.rs stats)

## Step 2 — fetch

`src/fetch_mirrors.py`: download daily stats for 2023-2026 into data/raw/.

## Step 3 — estimate

Same estimator as tiaoxiu-signal: make-up-day uplift, placebo, controls.

## Step 4 — cross-correlate

Join with tiaoxiu-signal s values. Target: show that mirror uplift and GitHub s agree in sign and rank for the same ecosystems.
