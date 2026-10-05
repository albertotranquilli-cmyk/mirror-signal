# mirror-signal

**Package mirror download logs as a natural experiment for geographic activity composition.**

Status: scaffold 2026-10-05. No results yet.

## The idea

npm, PyPI and crates.io publish **public download logs**. Chinese mirror operators (npmmirror.com, tuna.tsinghua.edu.cn) also expose download statistics. If mirror traffic for Chinese package ecosystems spikes on 调休 make-up workdays — while global registry traffic stays flat — you have a second independent substrate measuring the same phenomenon as tiaoxiu-signal: **calendar adherence of developers**, measured from infrastructure they consume rather than code they produce.

## Why this matters

- **Independent substrate**: GitHub activity (tiaoxiu-signal) vs package consumption (this). If both agree, the finding is not an artifact of GH Archive.
- **Broader coverage**: mirrors capture developers who never touch GitHub (enterprise, air-gapped, copy-paste workflows).
- **Faster signal**: download logs update daily; GH Archive has months of lag and capture loss (as seen in E2).

## Method

1. Fetch public download stats: npmmirror (https://registry.npmmirror.com/-/binary/ or the public stats API), tuna (https://mirrors.tuna.tsinghua.edu.cn/static/json/status.json and per-repo download JSONs), PyPI public dataset (https://pypistats.org/api/packages/<pkg>/recent).
2. Bin by Asia/Shanghai day.
3. Compute make-up-day uplift per mirror/ecosystem.
4. Cross-correlate with tiaoxiu-signal org scores.

## Ethics

Aggregate download counts only. No personal data, no IP addresses, no user attributes.

## Next steps

1. Verify which mirror stats endpoints are still public and stable.
2. Fetch 2023-2026 window.
3. Estimate + placebo + Japanese control.
4. Paper section: "A second substrate confirms the calendar signal".
