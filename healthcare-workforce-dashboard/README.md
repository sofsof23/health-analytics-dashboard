Global Clinician Workforce Burden 🏥

An interactive analytics dashboard exploring global health workforce distribution, with a focus on clinician density, system capacity, and regional disparities — especially across GCC countries.

Built using WHO Global Health Observatory indicators and a Streamlit-based analytics stack.

🔍 Project Summary

Health workforce shortages are not evenly distributed across the world.

While some regions exceed recommended clinician density thresholds, others fall significantly below, creating long-term pressure on health systems and outcomes.

This dashboard explores:

Global clinician density (physicians, nurses, midwives, hospital beds)
Relationships between workforce capacity and health outcomes
Regional disparities across WHO regions
A focused comparative lens on GCC healthcare systems

⚠️ Note: This version currently runs on synthetic mock data while real WHO GHO integration is being finalized.

🎯 Key Questions
Where is clinician workload highest globally?
How does workforce density relate to life expectancy and NCD mortality?
How do GCC countries compare to global benchmarks?
Are high-spending systems necessarily high-capacity systems?
📊 Features
🌍 Global choropleth-style workforce comparisons
📈 Correlation analysis between workforce density and outcomes
🏥 GCC-focused comparative breakdown
📉 Multi-indicator health system visualization
⚡ Interactive filtering via Streamlit
🧠 Insights (Current Mock Analysis)
Workforce density varies significantly across WHO regions
Higher clinician density often correlates with improved life expectancy
GCC countries show high spending but mixed workforce distribution patterns
System capacity is not purely a function of healthcare investment
🚧 Build Status (7-Day Sprint)

This project is being actively developed:

 Day 0 — Repo scaffold + mock data + Streamlit shell
 Day 1 — WHO indicator selection & research framing
 Day 2 — WHO GHO API integration
 Day 3 — Exploratory data analysis & visualization design
 Day 4 — Dashboard logic implementation
 Day 5 — Narrative + GCC deep dive
 Day 6 — UI polish + deployment
 Day 7 — Portfolio release + LinkedIn launch
🗂 Project Structure
healthcare-workforce-dashboard/
├── app.py
├── requirements.txt
├── data/
│   ├── generate_mock.py
│   └── mock_data.csv
├── notebooks/
│   └── 01_eda_scaffold.ipynb
├── .streamlit/
│   └── config.toml
└── README.md
📡 Data Source
WHO Global Health Observatory (GHO)
Indicators:
Physicians per 10,000 population
Nurses & midwives per 10,000 population
Hospital beds per 10,000 population
Life expectancy
NCD mortality rate
UHC service coverage index
🛠 Tech Stack
Python (pandas, numpy)
Streamlit (interactive dashboard)
Plotly (visualization)
WHO GHO API (planned integration)
🚀 Run Locally
git clone https://github.com/<your-username>/healthcare-workforce-dashboard.git
cd healthcare-workforce-dashboard

python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

pip install -r requirements.txt
streamlit run app.py
👤 Author

Safiya Khan
Computer Science (AI), Euclea University — Riyadh

📌 License

MIT License
