🏥 Global Clinician Workforce Burden

An interactive analytics dashboard exploring global health workforce distribution, focusing on clinician density, system capacity, and regional disparities, with a comparative lens on GCC healthcare systems.

Built using WHO Global Health Observatory (GHO) indicators, Python, and a Streamlit-based analytics stack.

🔍 Project Overview

Healthcare workforce shortages are unevenly distributed across the world.

While some regions exceed recommended clinician density thresholds, others fall significantly below, placing long-term pressure on health systems, service delivery, and population outcomes.

This dashboard explores and visualizes:

Global clinician density (physicians, nurses, midwives, hospital beds)
Relationships between workforce capacity and health outcomes
Regional disparities across WHO regions
A focused comparison of GCC healthcare systems vs global benchmarks

⚠️ Note: This version currently runs on synthetic mock data. Real WHO GHO integration is in progress.

🎯 Key Questions:
Where is clinician workload highest globally?
How does workforce density relate to life expectancy and NCD mortality?
How do GCC countries compare to global healthcare benchmarks?
Are high healthcare expenditures aligned with workforce capacity?

📊 Features:
🌍 Global workforce distribution visualizations
📈 Correlation analysis between workforce and health outcomes
🏥 GCC regional comparative dashboard
📉 Multi-indicator health system analytics
⚡ Interactive filtering via Streamlit

🧠 Key Insights (Mock Data Stage):
Workforce density varies significantly across WHO regions
Higher clinician density generally correlates with improved life expectancy
GCC countries show high healthcare spending but uneven workforce distribution
System capacity is not solely determined by investment levels
🚧 Development Roadmap (7-Day Sprint)
Day	Milestone
Day 0	Repo scaffold + mock data + Streamlit shell
Day 1	WHO indicator selection & research framing
Day 2	WHO GHO API integration
Day 3	Exploratory data analysis & visualization design
Day 4	Dashboard logic implementation
Day 5	Narrative layer + GCC deep dive
Day 6	UI polish + deployment
Day 7	Portfolio release + LinkedIn launch

🗂 Project Structure:
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

📡 Data Source:
WHO Global Health Observatory (GHO)

Key indicators used:

Physicians per 10,000 population
Nurses & midwives per 10,000 population
Hospital beds per 10,000 population
Life expectancy at birth
NCD mortality rate
UHC service coverage index
🛠 Tech Stack
Python (pandas, numpy)
Streamlit (interactive dashboard)
Plotly (data visualization)
WHO GHO API (planned integration)


🚀 Run Locally
git clone https://github.com/<your-username>/healthcare-workforce-dashboard.git
cd healthcare-workforce-dashboard

python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

pip install -r requirements.txt
streamlit run app.py


👤 Author:
Safiya Khan
B.Sc. Computer Science (AI) — Euclea University, Riyadh

📄 License

MIT License
