"""
Global Clinician Workforce Burden — scaffold dashboard.

This is a SCAFFOLD. It runs on synthetic mock data while the real
WHO Global Health Observatory integration is built across Days 2-7
of the project plan. Replace `data/mock_data.csv` with real GHO
output once Day 2 is complete.

Run locally:
    pip install -r requirements.txt
    streamlit run app.py
"""
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

# ---------------------------------------------------------------------------
# Page config
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="Global Clinician Workforce Burden",
    page_icon="🏥",
    layout="wide",
)

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
GCC_ISO3 = ["SAU", "ARE", "QAT", "KWT", "BHR", "OMN"]
DATA_PATH = Path(__file__).parent / "data" / "mock_data.csv"

# ---------------------------------------------------------------------------
# Data loading  —  TODO Day 2: replace with live WHO GHO ingestion
# ---------------------------------------------------------------------------
@st.cache_data
def load_data() -> pd.DataFrame:
    """Load the mock dataset. Replace with WHO GHO API call on Day 2."""
    return pd.read_csv(DATA_PATH)


df = load_data()

# ---------------------------------------------------------------------------
# Header
# ---------------------------------------------------------------------------
st.title("Global Clinician Workforce Burden 🏥")
st.caption(
    "Where in the world is clinician workload highest, "
    "and how does the GCC compare?"
)

st.warning(
    "**Scaffold version.** This dashboard is currently running on synthetic "
    "mock data. Real WHO Global Health Observatory integration is in progress. "
    "See the README for the 7-day build plan."
)

# ---------------------------------------------------------------------------
# Sidebar filters
# ---------------------------------------------------------------------------
st.sidebar.header("Filters")

years = sorted(df["year"].unique())
year = st.sidebar.select_slider("Year", options=years, value=max(years))

regions = sorted(df["who_region"].unique())
selected_regions = st.sidebar.multiselect(
    "WHO Region", regions, default=regions
)

st.sidebar.divider()
st.sidebar.markdown(
    "**Project status**\n\n"
    "Currently: scaffold with mock data.\n\n"
    "Next: WHO GHO API integration (Day 2)."
)

filtered = df[
    (df["year"] == year) & (df["who_region"].isin(selected_regions))
]

# ---------------------------------------------------------------------------
# KPI strip
# ---------------------------------------------------------------------------
col1, col2, col3, col4 = st.columns(4)
col1.metric("Countries shown", len(filtered))
col2.metric("Avg physicians / 10k", f"{filtered['physicians_per_10k'].mean():.1f}")
col3.metric("Avg nurses / 10k", f"{filtered['nurses_per_10k'].mean():.1f}")
col4.metric("Avg life expectancy", f"{filtered['life_expectancy'].mean():.1f}")

st.divider()

# ---------------------------------------------------------------------------
# Chart 1 — workforce density by WHO region
# TODO Day 4: real chart with proper aggregation, IQR overlay, sample sizes
# ---------------------------------------------------------------------------
st.subheader("1. Clinician density by WHO region")
st.caption("Placeholder chart — to be refined on Day 4.")

chart1 = px.box(
    filtered,
    x="who_region",
    y="physicians_per_10k",
    points="all",
    color="who_region",
    labels={
        "who_region": "WHO Region",
        "physicians_per_10k": "Physicians per 10,000 population",
    },
)
chart1.update_layout(showlegend=False, height=420)
st.plotly_chart(chart1, use_container_width=True)

# ---------------------------------------------------------------------------
# Chart 2 — workforce vs outcomes scatter
# TODO Day 4: regression line, GCC highlight, country labels on outliers
# ---------------------------------------------------------------------------
st.subheader("2. Workforce density vs life expectancy")
st.caption("Placeholder chart — Day 4 will add regression line and outlier labels.")

chart2 = px.scatter(
    filtered,
    x="physicians_per_10k",
    y="life_expectancy",
    color="who_region",
    size="nurses_per_10k",
    hover_data=["country", "uhc_service_coverage"],
    labels={
        "physicians_per_10k": "Physicians per 10,000",
        "life_expectancy": "Life expectancy (years)",
    },
    height=480,
)
st.plotly_chart(chart2, use_container_width=True)

# ---------------------------------------------------------------------------
# Chart 3 — GCC focus (the comparative lens)
# TODO Day 5: peer comparison, global benchmark overlay, narrative annotations
# ---------------------------------------------------------------------------
st.subheader("3. GCC comparative lens — physician density over time")
st.caption("Placeholder chart — Day 5 will add global/regional benchmark lines.")

gcc_df = df[df["iso3"].isin(GCC_ISO3)]
chart3 = px.line(
    gcc_df,
    x="year",
    y="physicians_per_10k",
    color="country",
    markers=True,
    labels={
        "physicians_per_10k": "Physicians per 10,000",
        "year": "Year",
    },
    height=420,
)
st.plotly_chart(chart3, use_container_width=True)

# ---------------------------------------------------------------------------
# Data preview
# ---------------------------------------------------------------------------
with st.expander("Preview the underlying data"):
    st.dataframe(filtered, use_container_width=True)

# ---------------------------------------------------------------------------
# Footer
# ---------------------------------------------------------------------------
st.divider()
st.markdown(
    """
    **About this project.** Built by Safiya Khan as part of a portfolio
    of health-AI work. Real WHO GHO data integration in progress —
    see the 7-day build plan in the repo. Methodology notebook will
    appear in `notebooks/` once Day 3 is complete.
    """
)
