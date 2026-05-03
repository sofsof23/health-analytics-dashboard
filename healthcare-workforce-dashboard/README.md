# Global Clinician Workforce Burden 🏥

> *Where in the world is clinician workload highest, and how does the GCC compare?*

An interactive dashboard exploring health workforce density across countries, with a comparative lens on Gulf Cooperation Council (GCC) states. Built on data from the WHO Global Health Observatory.

**Status:** 🚧 Scaffold — running on synthetic mock data while real WHO GHO integration is in progress. See [Build plan](#build-plan) below.

---

## Live demo

🔗 _Streamlit Cloud URL — coming once Day 6 is complete._

## Screenshots

_Screenshots will be added once the dashboard hits Day 5._

---

## What this dashboard argues

Health workforce shortages are not evenly distributed. WHO benchmarks suggest a minimum density to meet basic service coverage, yet many regions fall well below it. This dashboard:

1. Visualises clinician density (physicians, nurses, hospital beds) across WHO regions.
2. Correlates workforce capacity with health outcomes (life expectancy, NCD mortality, UHC service coverage).
3. Zooms in on the GCC — a region with high health spending and a rapidly evolving chronic disease burden — and asks how its workforce trajectory compares to global peers.

The findings feed into a parallel project on clinician fatigue at HMG (Saudi Arabia) and a research paper on workforce sustainability.

---

## Run it locally

```bash
git clone https://github.com/<your-username>/healthcare-workforce-dashboard.git
cd healthcare-workforce-dashboard
python -m venv .venv && source .venv/bin/activate    # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

The app will open at http://localhost:8501.

---

## Project structure

```
healthcare-workforce-dashboard/
├── app.py                       # Streamlit app entry point
├── requirements.txt
├── data/
│   ├── generate_mock.py         # Synthetic data generator (scaffold only)
│   └── mock_data.csv            # Replace with real WHO GHO data on Day 2
├── notebooks/
│   └── 01_eda_scaffold.ipynb    # EDA + methodology (Day 3)
├── .streamlit/
│   └── config.toml              # Theme
├── .gitignore
└── README.md
```

---

## Build plan

This repo is being built across a 7-day sprint. Tracking checkboxes here so reviewers can see progress.

- [x] **Day 0** — Repo scaffold, mock data, working Streamlit shell deployed
- [ ] **Day 1** — Indicator selection from WHO GHO catalogue, lock the thesis
- [ ] **Day 2** — Real data pipeline: WHO GHO API ingestion, country/region mapping, cleaning
- [ ] **Day 3** — EDA in `notebooks/01_eda_scaffold.ipynb`, finalise the 4–5 charts that argue the thesis
- [ ] **Day 4** — Replace placeholder charts in `app.py` with real implementations
- [ ] **Day 5** — Narrative text between sections, GCC focus chart, edge-case handling
- [ ] **Day 6** — Visual polish, full README rewrite, deploy to Streamlit Community Cloud
- [ ] **Day 7** — Portfolio entry, LinkedIn announcement, methodology notebook published

---

## Data source

[WHO Global Health Observatory](https://www.who.int/data/gho) — public dataset of global health indicators across all WHO member states. Indicators of interest:

- Medical doctors (per 10,000 population)
- Nursing and midwifery personnel (per 10,000 population)
- Hospital beds (per 10,000 population)
- Life expectancy at birth
- NCD mortality rate (probability of dying between 30 and 70)
- UHC service coverage index

_Final indicator list will be locked on Day 1._

---

## Tech stack

- **Python** (pandas, requests)
- **Streamlit** — app framework
- **Plotly** — interactive charts
- **Streamlit Community Cloud** — free hosting

---

## License

MIT — see `LICENSE`.

## Author

**Safiya Khan** — CS (AI) student at Euclea University, Riyadh.
[Portfolio](https://safiyakhan.netlify.app) · LinkedIn _(add link)_
