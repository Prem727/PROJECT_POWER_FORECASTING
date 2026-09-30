import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import json
from pathlib import Path

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="PJM Energy Forecasting",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# PROJECT PATH
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

# ============================================================
# PROFESSIONAL LIGHT DASHBOARD STYLE
# ============================================================

st.markdown("""
<style>

/* =========================================================
   MAIN APPLICATION
   ========================================================= */

.stApp {
    background: #f3f6fa;
    color: #172033;
}

/* =========================================================
   STREAMLIT TOP HEADER
   ========================================================= */

header[data-testid="stHeader"] {
    background: #f3f6fa !important;
    height: 60px;
}

[data-testid="stHeader"] {
    background: #f3f6fa !important;
}

[data-testid="stToolbar"] {
    background: transparent !important;
}

[data-testid="stDecoration"] {
    background: #f3f6fa !important;
}

/* =========================================================
   MAIN CONTENT
   ========================================================= */

.block-container {
    padding-top: 2.2rem;
    padding-bottom: 3rem;
    max-width: 1500px;
}

/* =========================================================
   GLOBAL TEXT
   ========================================================= */

h1,
h2,
h3,
h4,
h5,
h6 {
    color: #172033 !important;
    font-weight: 750 !important;
}

p,
li,
span,
label {
    color: #475569;
}

.stMarkdown {
    color: #475569;
}

/* =========================================================
   MAIN TITLE
   ========================================================= */

.main-title {
    font-size: 44px;
    font-weight: 850;
    letter-spacing: -1px;
    color: #172033 !important;
    margin-bottom: 4px;
}

.subtitle {
    color: #64748b !important;
    font-size: 17px;
    margin-bottom: 28px;
}

/* =========================================================
   SIDEBAR
   ========================================================= */

section[data-testid="stSidebar"] {
    background: #111827;
    border-right: 1px solid #1e293b;
}

section[data-testid="stSidebar"] * {
    color: #cbd5e1 !important;
}

section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 {
    color: #ffffff !important;
}

section[data-testid="stSidebar"] .stRadio label {
    color: #cbd5e1 !important;
    font-weight: 500;
}

section[data-testid="stSidebar"] .stRadio label:hover {
    color: #ffffff !important;
}

section[data-testid="stSidebar"] .stCaption {
    color: #94a3b8 !important;
}

/* =========================================================
   HEADERS
   ========================================================= */

h1 {
    font-size: 34px !important;
}

h2 {
    font-size: 27px !important;
    margin-top: 25px !important;
}

h3 {
    font-size: 21px !important;
    margin-top: 20px !important;
}

/* =========================================================
   KPI CARDS
   ========================================================= */

.metric-card {
    background: #ffffff;
    border: 1px solid #dbe3ee;
    border-radius: 16px;
    padding: 20px 22px;
    min-height: 118px;
    box-shadow: 0 4px 14px rgba(15, 23, 42, 0.07);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.metric-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 22px rgba(15, 23, 42, 0.12);
}

.metric-title {
    color: #64748b !important;
    font-size: 13px;
    font-weight: 650;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.metric-value {
    color: #172033 !important;
    font-size: 28px;
    font-weight: 850;
    margin-top: 10px;
}

/* =========================================================
   INFO BOX
   ========================================================= */

.info-box {
    background: #ffffff;
    border: 1px solid #dbe3ee;
    border-left: 4px solid #2563eb;
    border-radius: 12px;
    padding: 18px 20px;
    color: #475569 !important;
    margin: 12px 0 24px 0;
    box-shadow: 0 4px 14px rgba(15, 23, 42, 0.06);
}

/* =========================================================
   FINDING CARDS
   ========================================================= */

.finding-box {
    background: #ffffff;
    border: 1px solid #dbe3ee;
    border-radius: 13px;
    padding: 17px 20px;
    margin-bottom: 13px;
    color: #475569 !important;
    box-shadow: 0 4px 14px rgba(15, 23, 42, 0.06);
}

.finding-box strong {
    color: #172033 !important;
    font-size: 16px;
}

/* =========================================================
   SECTION NOTE
   ========================================================= */

.section-note {
    color: #64748b !important;
    font-size: 14px;
    margin-bottom: 20px;
}

/* =========================================================
   DATAFRAME
   ========================================================= */

div[data-testid="stDataFrame"] {
    border: 1px solid #dbe3ee;
    border-radius: 12px;
    overflow: hidden;
}

/* =========================================================
   DOWNLOAD BUTTON
   ========================================================= */

.stDownloadButton button {
    background: linear-gradient(
        135deg,
        #2563eb,
        #1d4ed8
    ) !important;

    color: #ffffff !important;
    border: none !important;
    border-radius: 9px !important;
    font-weight: 650 !important;
    padding: 10px 18px !important;
    transition: all 0.2s ease;
}

.stDownloadButton button:hover {
    background: linear-gradient(
        135deg,
        #3b82f6,
        #2563eb
    ) !important;

    transform: translateY(-1px);
}

/* =========================================================
   SELECTBOX
   ========================================================= */

div[data-baseweb="select"] > div {
    background-color: #ffffff !important;
    border-color: #cbd5e1 !important;
    color: #172033 !important;
}

/* =========================================================
   RADIO BUTTONS
   ========================================================= */

div[role="radiogroup"] label {
    color: #475569 !important;
}

/* =========================================================
   ALERTS
   ========================================================= */

div[data-testid="stAlert"] {
    border-radius: 10px;
}

/* =========================================================
   DIVIDERS
   ========================================================= */

hr {
    border-color: #dbe3ee !important;
}

/* =========================================================
   CHART CONTAINER
   ========================================================= */

.chart-container {
    background: #ffffff;
    border: 1px solid #dbe3ee;
    border-radius: 14px;
    padding: 8px;
}

/* =========================================================
   SCROLLBAR
   ========================================================= */

::-webkit-scrollbar {
    width: 8px;
}

::-webkit-scrollbar-track {
    background: #f3f6fa;
}

::-webkit-scrollbar-thumb {
    background: #cbd5e1;
    border-radius: 10px;
}

::-webkit-scrollbar-thumb:hover {
    background: #94a3b8;
}

/* =========================================================
   MOBILE
   ========================================================= */

@media (max-width: 900px) {

    .main-title {
        font-size: 32px;
    }

    .subtitle {
        font-size: 15px;
    }

    .metric-value {
        font-size: 23px;
    }
}

</style>
""", unsafe_allow_html=True)

# ============================================================
# HELPERS
# ============================================================

def load_csv(filename):

    path = BASE_DIR / filename

    if not path.exists():
        st.error(f"Missing file: {filename}")
        return None

    return pd.read_csv(path)


def load_json(filename):

    path = BASE_DIR / filename

    if not path.exists():
        st.error(f"Missing file: {filename}")
        return None

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def metric_card(title, value):

    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-title">{title}</div>
            <div class="metric-value">{value}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# PLOTLY LIGHT THEME
# ============================================================

def dark_layout(fig, height=450):

    fig.update_layout(

        height=height,

        paper_bgcolor="#ffffff",

        plot_bgcolor="#ffffff",

        font=dict(
            color="#334155",
            family="Arial"
        ),

        title=dict(
            font=dict(
                color="#172033",
                size=20
            )
        ),

        hovermode="x unified",

        margin=dict(
            l=55,
            r=30,
            t=65,
            b=55
        ),

        xaxis=dict(
            color="#475569",
            gridcolor="#e2e8f0",
            linecolor="#cbd5e1",
            zerolinecolor="#cbd5e1"
        ),

        yaxis=dict(
            color="#475569",
            gridcolor="#e2e8f0",
            linecolor="#cbd5e1",
            zerolinecolor="#cbd5e1"
        ),

        legend=dict(
            font=dict(
                color="#475569"
            ),
            bgcolor="rgba(255,255,255,0)"
        )
    )

    return fig


# ============================================================
# FINDING CARD
# ============================================================

def finding(title, text):

    st.markdown(
        f"""
        <div class="finding-box">
            <strong>{title}</strong><br>
            {text}
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# LOAD ARTIFACTS
# ============================================================

clean_data = load_csv(
    "pjm_clean_hourly_data.csv"
)

forecast_hourly = load_csv(
    "pjm_final_30_day_hourly_forecast.csv"
)

forecast_daily = load_csv(
    "pjm_final_30_day_daily_forecast.csv"
)

history = load_csv(
    "pjm_forecast_history_168.csv"
)

model_comparison = load_csv(
    "pjm_time_series_model_comparison.csv"
)

all_models = load_csv(
    "pjm_all_model_comparison_results.csv"
)

rolling_validation = load_csv(
    "pjm_final_year_rolling_validation.csv"
)

# ============================================================
# XGBOOST BENCHMARK ARTIFACTS
# ============================================================

xgb_validation = load_csv(
    "pjm_xgboost_validation_predictions.csv"
)

xgb_forecast_hourly = load_csv(
    "pjm_xgboost_30_day_hourly_forecast.csv"
)

xgb_forecast_daily = load_csv(
    "pjm_xgboost_30_day_daily_forecast.csv"
)

xgb_feature_importance = load_csv(
    "pjm_xgboost_feature_importance.csv"
)

metadata = load_json(
    "pjm_forecasting_metadata.json"
)

model_info = load_json(
    "pjm_final_time_series_model.json"
)

# ============================================================
# DATE PREPARATION
# ============================================================

for df in [
    clean_data,
    forecast_hourly,
    forecast_daily,
    history,
    xgb_validation,
    xgb_forecast_hourly,
    xgb_forecast_daily
]:

    if df is not None and "Datetime" in df.columns:

        df["Datetime"] = pd.to_datetime(
            df["Datetime"]
        )

# ============================================================
# FEATURE ENGINEERING
# ============================================================

if clean_data is not None:

    clean_data["Hour"] = (
        clean_data["Datetime"].dt.hour
    )

    clean_data["Day"] = (
        clean_data["Datetime"].dt.day
    )

    clean_data["DayOfWeek"] = (
        clean_data["Datetime"].dt.day_name()
    )

    clean_data["Month"] = (
        clean_data["Datetime"].dt.month
    )

    clean_data["MonthName"] = (
        clean_data["Datetime"].dt.month_name()
    )

    clean_data["Year"] = (
        clean_data["Datetime"].dt.year
    )

    clean_data["Season"] = (
        clean_data["Month"].map(
            {
                12: "Winter",
                1: "Winter",
                2: "Winter",

                3: "Spring",
                4: "Spring",
                5: "Spring",

                6: "Summer",
                7: "Summer",
                8: "Summer",

                9: "Autumn",
                10: "Autumn",
                11: "Autumn"
            }
        )
    )

    clean_data["DayType"] = np.where(
        clean_data["Datetime"].dt.dayofweek < 5,
        "Weekday",
        "Weekend"
    )

    clean_data["Rolling24h"] = (
        clean_data["PJMW_MW"]
        .rolling(24)
        .mean()
    )

# ============================================================
# SIDEBAR NAVIGATION
# ============================================================

st.sidebar.title(
    "⚡ PJM Forecasting"
)

st.sidebar.caption(
    "P605 – PJM Hourly Energy Consumption Forecasting"
)

st.sidebar.divider()

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Executive Overview",
        "📊 EDA & Graphs",
        "📈 30-Day Forecast",
        "🤖 Model Comparison",
        "📉 Validation & Errors",
        "🔍 Findings & Insights",
        "🔎 Data Explorer",
        "📘 Methodology",
        "⬇️ Downloads"
    ]
)

st.sidebar.divider()

st.sidebar.markdown(
    "**Production Model**"
)

st.sidebar.success(
    "Seasonal Naive (24h)"
)

# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">'
    '⚡ PJM Energy Consumption Forecast'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Electricity demand intelligence • '
    'Historical analysis • '
    'Time-series modeling • '
    '30-day forecasting'
    '</div>',
    unsafe_allow_html=True
)

# ============================================================
# EXECUTIVE OVERVIEW
# ============================================================

if page == "🏠 Executive Overview":

    st.header(
        "Executive Overview"
    )

    st.markdown(
        """
        <div class="info-box">
        This dashboard combines historical PJM electricity demand
        analysis, exploratory data analysis, classical time-series
        model evaluation, machine-learning benchmarking, validation
        results and the final 30-day production forecast.
        </div>
        """,
        unsafe_allow_html=True
    )

    if clean_data is not None:

        avg_demand = (
            clean_data["PJMW_MW"].mean()
        )

        min_demand = (
            clean_data["PJMW_MW"].min()
        )

        max_demand = (
            clean_data["PJMW_MW"].max()
        )

        data_start = (
            clean_data["Datetime"].min()
        )

        data_end = (
            clean_data["Datetime"].max()
        )

        c1, c2, c3, c4 = st.columns(4)

        with c1:

            metric_card(
                "Historical Average",
                f"{avg_demand:,.0f} MW"
            )

        with c2:

            metric_card(
                "Historical Minimum",
                f"{min_demand:,.0f} MW"
            )

        with c3:

            metric_card(
                "Historical Maximum",
                f"{max_demand:,.0f} MW"
            )

        with c4:

            metric_card(
                "Historical Records",
                f"{len(clean_data):,}"
            )

        # ----------------------------------------------------
        # PROJECT INFORMATION
        # ----------------------------------------------------

        st.subheader(
            "Project Information"
        )

        c1, c2, c3, c4 = st.columns(4)

        with c1:

            metric_card(
                "Data Start",
                data_start.strftime(
                    "%d %b %Y"
                )
            )

        with c2:

            metric_card(
                "Data End",
                data_end.strftime(
                    "%d %b %Y"
                )
            )

        with c3:

            metric_card(
                "Forecast Horizon",
                "30 Days"
            )

        with c4:

            metric_card(
                "Forecast Hours",
                "720"
            )

        # ----------------------------------------------------
        # PRODUCTION MODEL
        # ----------------------------------------------------

        st.subheader(
            "Production Model"
        )

        model_name = metadata.get(
            "production_model",
            "N/A"
        )

        model_family = metadata.get(
            "model_family",
            "N/A"
        )

        seasonal_period = metadata.get(
            "seasonal_period_hours",
            "N/A"
        )

        selection_rule = metadata.get(
            "selection_rule",
            "N/A"
        )

        st.markdown(
            f"""
            <div class="info-box">

            <strong style="color:#172033;">
            {model_name}
            </strong>

            <br><br>

            <strong style="color:#172033;">
            Model Family:
            </strong>
            {model_family}

            <br>

            <strong style="color:#172033;">
            Seasonal Period:
            </strong>
            {seasonal_period} hours

            <br>

            <strong style="color:#172033;">
            Selection Rule:
            </strong>
            {selection_rule}

            </div>
            """,
            unsafe_allow_html=True
        )

        # ----------------------------------------------------
        # HISTORICAL DEMAND
        # ----------------------------------------------------

        st.subheader(
            "Historical Demand"
        )

        fig = go.Figure()

        fig.add_trace(
            go.Scatter(
                x=clean_data["Datetime"],
                y=clean_data["PJMW_MW"],
                mode="lines",
                name="Hourly Demand",
                line=dict(
                    width=1.2
                )
            )
        )

        fig.add_trace(
            go.Scatter(
                x=clean_data["Datetime"],
                y=clean_data["Rolling24h"],
                mode="lines",
                name="24-Hour Rolling Average",
                line=dict(
                    width=2
                )
            )
        )

        fig = dark_layout(
            fig,
            500
        )

        fig.update_layout(
            xaxis_title="Datetime",
            yaxis_title="Demand (MW)"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

# ============================================================
# EDA & GRAPHS
# ============================================================

elif page == "📊 EDA & Graphs":

    st.header(
        "Exploratory Data Analysis"
    )

    if clean_data is None:

        st.warning(
            "Clean dataset is unavailable."
        )

        st.stop()

    st.markdown(
        '<div class="section-note">'
        'Explore the major temporal patterns identified '
        'in the PJM electricity demand data.'
        '</div>',
        unsafe_allow_html=True
    )

    # --------------------------------------------------------
    # HISTORICAL TREND
    # --------------------------------------------------------

    st.subheader(
        "1. Historical Electricity Demand"
    )

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=clean_data["Datetime"],
            y=clean_data["PJMW_MW"],
            mode="lines",
            name="Hourly Demand"
        )
    )

    fig = dark_layout(
        fig,
        450
    )

    fig.update_layout(
        xaxis_title="Datetime",
        yaxis_title="Demand (MW)"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # --------------------------------------------------------
    # HOURLY PATTERN
    # --------------------------------------------------------

    st.subheader(
        "2. Average Demand by Hour"
    )

    hourly = (
        clean_data
        .groupby("Hour")["PJMW_MW"]
        .mean()
        .reset_index()
    )

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=hourly["Hour"],
            y=hourly["PJMW_MW"],
            mode="lines+markers",
            name="Average Demand"
        )
    )

    fig = dark_layout(
        fig,
        400
    )

    fig.update_layout(
        xaxis_title="Hour of Day",
        yaxis_title="Average Demand (MW)"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # --------------------------------------------------------
    # DAY OF WEEK
    # --------------------------------------------------------

    st.subheader(
        "3. Average Demand by Day of Week"
    )

    weekday_order = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]

    weekday = (
        clean_data
        .groupby("DayOfWeek")["PJMW_MW"]
        .mean()
        .reindex(weekday_order)
        .reset_index()
    )

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=weekday["DayOfWeek"],
            y=weekday["PJMW_MW"],
            name="Average Demand"
        )
    )

    fig = dark_layout(
        fig,
        400
    )

    fig.update_layout(
        xaxis_title="Day",
        yaxis_title="Average Demand (MW)"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # --------------------------------------------------------
    # WEEKDAY VS WEEKEND
    # --------------------------------------------------------

    st.subheader(
        "4. Weekday vs Weekend"
    )

    daytype = (
        clean_data
        .groupby("DayType")["PJMW_MW"]
        .mean()
        .reset_index()
    )

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=daytype["DayType"],
            y=daytype["PJMW_MW"],
            name="Average Demand"
        )
    )

    fig = dark_layout(
        fig,
        350
    )

    fig.update_layout(
        xaxis_title="Day Type",
        yaxis_title="Average Demand (MW)"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # --------------------------------------------------------
    # MONTHLY
    # --------------------------------------------------------

    st.subheader(
        "5. Average Demand by Month"
    )

    month = (
        clean_data
        .groupby("Month")["PJMW_MW"]
        .mean()
        .reset_index()
    )

    month_names = {
        1: "Jan",
        2: "Feb",
        3: "Mar",
        4: "Apr",
        5: "May",
        6: "Jun",
        7: "Jul",
        8: "Aug",
        9: "Sep",
        10: "Oct",
        11: "Nov",
        12: "Dec"
    }

    month["MonthName"] = (
        month["Month"].map(
            month_names
        )
    )

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=month["MonthName"],
            y=month["PJMW_MW"],
            name="Average Demand"
        )
    )

    fig = dark_layout(
        fig,
        400
    )

    fig.update_layout(
        xaxis_title="Month",
        yaxis_title="Average Demand (MW)"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # --------------------------------------------------------
    # YEARLY
    # --------------------------------------------------------

    st.subheader(
        "6. Long-Term Yearly Trend"
    )

    yearly = (
        clean_data
        .groupby("Year")["PJMW_MW"]
        .mean()
        .reset_index()
    )

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=yearly["Year"],
            y=yearly["PJMW_MW"],
            mode="lines+markers",
            name="Yearly Average"
        )
    )

    fig = dark_layout(
        fig,
        400
    )

    fig.update_layout(
        xaxis_title="Year",
        yaxis_title="Average Demand (MW)"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # --------------------------------------------------------
    # SEASONAL
    # --------------------------------------------------------

    st.subheader(
        "7. Seasonal Demand Pattern"
    )

    season_order = [
        "Winter",
        "Spring",
        "Summer",
        "Autumn"
    ]

    seasonal = (
        clean_data
        .groupby("Season")["PJMW_MW"]
        .mean()
        .reindex(season_order)
        .reset_index()
    )

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=seasonal["Season"],
            y=seasonal["PJMW_MW"],
            name="Seasonal Average"
        )
    )

    fig = dark_layout(
        fig,
        400
    )

    fig.update_layout(
        xaxis_title="Season",
        yaxis_title="Average Demand (MW)"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # --------------------------------------------------------
    # SEASON BY HOUR
    # --------------------------------------------------------

    st.subheader(
        "8. Seasonal Hourly Pattern"
    )

    season_hour = (
        clean_data
        .groupby(
            ["Season", "Hour"]
        )["PJMW_MW"]
        .mean()
        .reset_index()
    )

    fig = go.Figure()

    for season in season_order:

        temp = season_hour[
            season_hour["Season"] == season
        ]

        fig.add_trace(
            go.Scatter(
                x=temp["Hour"],
                y=temp["PJMW_MW"],
                mode="lines",
                name=season
            )
        )

    fig = dark_layout(
        fig,
        500
    )

    fig.update_layout(
        xaxis_title="Hour of Day",
        yaxis_title="Average Demand (MW)"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # --------------------------------------------------------
    # DISTRIBUTION
    # --------------------------------------------------------

    st.subheader(
        "9. Demand Distribution"
    )

    fig = go.Figure()

    fig.add_trace(
        go.Histogram(
            x=clean_data["PJMW_MW"],
            nbinsx=50,
            name="Demand Distribution"
        )
    )

    fig = dark_layout(
        fig,
        400
    )

    fig.update_layout(
        xaxis_title="Demand (MW)",
        yaxis_title="Frequency"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # --------------------------------------------------------
    # ROLLING 24 HOURS
    # --------------------------------------------------------

    st.subheader(
        "10. 24-Hour Rolling Average"
    )

    recent = clean_data.tail(
        10000
    )

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=recent["Datetime"],
            y=recent["Rolling24h"],
            mode="lines",
            name="24-Hour Rolling Average"
        )
    )

    fig = dark_layout(
        fig,
        450
    )

    fig.update_layout(
        xaxis_title="Datetime",
        yaxis_title="Rolling Average (MW)"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # --------------------------------------------------------
    # HOLIDAY ANALYSIS IF AVAILABLE
    # --------------------------------------------------------

    holiday_columns = [
        "Holiday",
        "IsHoliday",
        "holiday",
        "is_holiday"
    ]

    holiday_column = None

    for column in holiday_columns:

        if column in clean_data.columns:

            holiday_column = column
            break

    if holiday_column is not None:

        st.subheader(
            "11. Holiday vs Non-Holiday Demand"
        )

        holiday_avg = (
            clean_data
            .groupby(holiday_column)["PJMW_MW"]
            .mean()
            .reset_index()
        )

        fig = go.Figure()

        fig.add_trace(
            go.Bar(
                x=holiday_avg[
                    holiday_column
                ].astype(str),

                y=holiday_avg[
                    "PJMW_MW"
                ],

                name="Average Demand"
            )
        )

        fig = dark_layout(
            fig,
            350
        )

        fig.update_layout(
            xaxis_title="Holiday Status",
            yaxis_title="Average Demand (MW)"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

# ============================================================
# 30-DAY FORECAST
# ============================================================

elif page == "📈 30-Day Forecast":

    st.header(
        "30-Day Production Forecast"
    )

    if forecast_hourly is not None:

        avg_forecast = (
            forecast_hourly[
                "Predicted_MW"
            ].mean()
        )

        min_forecast = (
            forecast_hourly[
                "Predicted_MW"
            ].min()
        )

        max_forecast = (
            forecast_hourly[
                "Predicted_MW"
            ].max()
        )

        peak_row = forecast_hourly.loc[
            forecast_hourly[
                "Predicted_MW"
            ].idxmax()
        ]

        # ----------------------------------------------------
        # FORECAST KPI
        # ----------------------------------------------------

        c1, c2, c3, c4 = st.columns(4)

        with c1:

            metric_card(
                "Average Forecast",
                f"{avg_forecast:,.0f} MW"
            )

        with c2:

            metric_card(
                "Minimum",
                f"{min_forecast:,.0f} MW"
            )

        with c3:

            metric_card(
                "Maximum",
                f"{max_forecast:,.0f} MW"
            )

        with c4:

            metric_card(
                "Forecast Peak",
                peak_row["Datetime"].strftime(
                    "%d %b %H:%M"
                )
            )

        # ----------------------------------------------------
        # HOURLY FORECAST
        # ----------------------------------------------------

        st.subheader(
            "Hourly Forecast"
        )

        fig = go.Figure()

        fig.add_trace(
            go.Scatter(
                x=forecast_hourly[
                    "Datetime"
                ],

                y=forecast_hourly[
                    "Predicted_MW"
                ],

                mode="lines",

                name="Predicted Demand"
            )
        )

        fig = dark_layout(
            fig,
            500
        )

        fig.update_layout(
            xaxis_title="Datetime",
            yaxis_title="Predicted Demand (MW)"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        # ----------------------------------------------------
        # HISTORICAL + FUTURE
        # ----------------------------------------------------

        st.subheader(
            "Historical + Future Forecast"
        )

        if history is not None:

            fig = go.Figure()

            fig.add_trace(
                go.Scatter(
                    x=history["Datetime"],
                    y=history.iloc[:, 1],
                    mode="lines",
                    name="Recent History"
                )
            )

            fig.add_trace(
                go.Scatter(
                    x=forecast_hourly[
                        "Datetime"
                    ],

                    y=forecast_hourly[
                        "Predicted_MW"
                    ],

                    mode="lines",

                    name="Future Forecast"
                )
            )

            fig = dark_layout(
                fig,
                500
            )

            fig.update_layout(
                xaxis_title="Datetime",
                yaxis_title="Demand (MW)"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        # ----------------------------------------------------
        # DAILY FORECAST
        # ----------------------------------------------------

        st.subheader(
            "Daily Forecast"
        )

        if forecast_daily is not None:

            st.dataframe(
                forecast_daily,
                use_container_width=True
            )

            st.download_button(
                "⬇️ Download Daily Forecast",

                forecast_daily.to_csv(
                    index=False
                ),

                "pjm_30_day_daily_forecast.csv",

                "text/csv"
            )

# ============================================================
# MODEL COMPARISON
# ============================================================

elif page == "🤖 Model Comparison":

    st.header(
        "Model Comparison"
    )

    st.markdown(
        """
        Multiple forecasting approaches were evaluated.
        XGBoost is included as a machine-learning benchmark,
        while Seasonal Naive (24h) remains the documented
        production model because production selection is
        restricted to classical time-series models.
        """
    )

    # --------------------------------------------------------
    # ALL MODELS
    # --------------------------------------------------------

    if all_models is not None:

        st.subheader(
            "Complete Model Comparison"
        )

        st.dataframe(
            all_models,
            use_container_width=True
        )

        if "MAE" in all_models.columns:

            comparison_plot = all_models.copy()

            comparison_plot = (
                comparison_plot
                .drop_duplicates(
                    subset=["Model"],
                    keep="first"
                )
            )

            fig = go.Figure()

            fig.add_trace(
                go.Bar(
                    x=comparison_plot["Model"],
                    y=comparison_plot["MAE"],
                    name="MAE"
                )
            )

            fig = dark_layout(
                fig,
                450
            )

            fig.update_layout(
                title="Model Comparison by MAE",
                xaxis_title="Model",
                yaxis_title="MAE (MW)"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

    # --------------------------------------------------------
    # XGBOOST BENCHMARK
    # --------------------------------------------------------

    st.subheader(
        "XGBoost Benchmark"
    )

    c1, c2, c3 = st.columns(3)

    with c1:

        metric_card(
            "XGBoost MAE",
            "72.60 MW"
        )

    with c2:

        metric_card(
            "XGBoost RMSE",
            "119.68 MW"
        )

    with c3:

        metric_card(
            "XGBoost MAPE",
            "1.27%"
        )

    st.markdown(
        """
        <div class="info-box">

        <strong style="color:#172033;">
        XGBoost Role:
        </strong>

        Machine-learning benchmark used for comparison.
        It is not the production model.

        </div>
        """,
        unsafe_allow_html=True
    )

    # --------------------------------------------------------
    # XGBOOST FEATURE IMPORTANCE
    # --------------------------------------------------------

    if xgb_feature_importance is not None:

        st.subheader(
            "XGBoost Feature Importance"
        )

        st.dataframe(
            xgb_feature_importance,
            use_container_width=True
        )

        importance_columns = (
            xgb_feature_importance.columns
        )

        if len(importance_columns) >= 2:

            feature_col = importance_columns[0]

            importance_col = importance_columns[1]

            fig = go.Figure()

            fig.add_trace(
                go.Bar(
                    x=xgb_feature_importance[
                        importance_col
                    ],

                    y=xgb_feature_importance[
                        feature_col
                    ],

                    orientation="h",

                    name="Feature Importance"
                )
            )

            fig = dark_layout(
                fig,
                550
            )

            fig.update_layout(
                title="XGBoost Feature Importance",
                xaxis_title="Importance",
                yaxis_title="Feature"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

    # --------------------------------------------------------
    # PRODUCTION MODEL
    # --------------------------------------------------------

    st.subheader(
        "Production Model"
    )

    st.markdown(
        """
        <div class="info-box">

        <strong style="color:#172033;">
        Seasonal Naive (24h)
        </strong>

        <br><br>

        This is the selected production model.

        <br><br>

        XGBoost is retained as a machine-learning benchmark
        and is not used as the documented production model.

        </div>
        """,
        unsafe_allow_html=True
    )

# ============================================================
# VALIDATION & ERRORS
# ============================================================

elif page == "📉 Validation & Errors":

    st.header(
        "Final-Year Rolling Validation"
    )

    if rolling_validation is not None:

        st.markdown(
            """
            Four chronological 30-day validation windows were
            evaluated to examine how the production forecasting
            approach performs across different periods.
            """
        )

        st.dataframe(
            rolling_validation,
            use_container_width=True
        )

        numeric_cols = [
            c
            for c in [
                "MAE",
                "RMSE",
                "MAPE"
            ]
            if c in rolling_validation.columns
        ]

        if numeric_cols:

            st.subheader(
                "Validation Metrics"
            )

            fig = go.Figure()

            for column in numeric_cols:

                fig.add_trace(
                    go.Bar(
                        x=rolling_validation.index.astype(
                            str
                        ),

                        y=rolling_validation[
                            column
                        ],

                        name=column
                    )
                )

            fig = dark_layout(
                fig,
                450
            )

            fig.update_layout(
                xaxis_title="Validation Window",
                yaxis_title="Error"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

    # --------------------------------------------------------
    # XGBOOST VALIDATION
    # --------------------------------------------------------

    st.subheader(
        "XGBoost Benchmark Validation"
    )

    c1, c2, c3 = st.columns(3)

    with c1:

        metric_card(
            "MAE",
            "72.60 MW"
        )

    with c2:

        metric_card(
            "RMSE",
            "119.68 MW"
        )

    with c3:

        metric_card(
            "MAPE",
            "1.27%"
        )

    st.markdown(
        """
        <div class="info-box">

        XGBoost validation uses chronological historical data
        and is included as a machine-learning benchmark.
        The documented production model remains
        Seasonal Naive (24h).

        </div>
        """,
        unsafe_allow_html=True
    )

    if xgb_validation is not None:

        st.subheader(
            "XGBoost Validation Predictions"
        )

        st.dataframe(
            xgb_validation.head(1000),
            use_container_width=True
        )

        if (
            "Datetime" in xgb_validation.columns
            and len(xgb_validation.columns) >= 3
        ):

            actual_candidates = [
                c for c in xgb_validation.columns
                if c.lower() in [
                    "actual",
                    "actual_mw",
                    "pjmw_mw"
                ]
            ]

            prediction_candidates = [
                c for c in xgb_validation.columns
                if c.lower() in [
                    "predicted",
                    "predicted_mw",
                    "prediction"
                ]
            ]

            if actual_candidates and prediction_candidates:

                actual_col = actual_candidates[0]

                prediction_col = prediction_candidates[0]

                fig = go.Figure()

                fig.add_trace(
                    go.Scatter(
                        x=xgb_validation["Datetime"],
                        y=xgb_validation[actual_col],
                        mode="lines",
                        name="Actual"
                    )
                )

                fig.add_trace(
                    go.Scatter(
                        x=xgb_validation["Datetime"],
                        y=xgb_validation[prediction_col],
                        mode="lines",
                        name="XGBoost Predicted"
                    )
                )

                fig = dark_layout(
                    fig,
                    500
                )

                fig.update_layout(
                    title="XGBoost Actual vs Predicted",
                    xaxis_title="Datetime",
                    yaxis_title="Demand (MW)"
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )

# ============================================================
# FINDINGS & INSIGHTS
# ============================================================

elif page == "🔍 Findings & Insights":

    st.header(
        "Findings & Insights"
    )

    if clean_data is not None:

        avg = clean_data[
            "PJMW_MW"
        ].mean()

        max_row = clean_data.loc[
            clean_data[
                "PJMW_MW"
            ].idxmax()
        ]

        min_row = clean_data.loc[
            clean_data[
                "PJMW_MW"
            ].idxmin()
        ]

        # ----------------------------------------------------
        # HOURLY
        # ----------------------------------------------------

        hourly_avg = (
            clean_data
            .groupby("Hour")[
                "PJMW_MW"
            ]
            .mean()
        )

        highest_hour = (
            hourly_avg.idxmax()
        )

        lowest_hour = (
            hourly_avg.idxmin()
        )

        highest_hour_value = (
            hourly_avg.max()
        )

        lowest_hour_value = (
            hourly_avg.min()
        )

        # ----------------------------------------------------
        # WEEKDAY / WEEKEND
        # ----------------------------------------------------

        weekday_avg = (
            clean_data[
                clean_data[
                    "DayType"
                ] == "Weekday"
            ]["PJMW_MW"].mean()
        )

        weekend_avg = (
            clean_data[
                clean_data[
                    "DayType"
                ] == "Weekend"
            ]["PJMW_MW"].mean()
        )

        # ----------------------------------------------------
        # MONTH
        # ----------------------------------------------------

        monthly_avg = (
            clean_data
            .groupby("Month")[
                "PJMW_MW"
            ].mean()
        )

        highest_month = (
            monthly_avg.idxmax()
        )

        lowest_month = (
            monthly_avg.idxmin()
        )

        # ----------------------------------------------------
        # YEAR
        # ----------------------------------------------------

        yearly_avg = (
            clean_data
            .groupby("Year")[
                "PJMW_MW"
            ].mean()
        )

        highest_year = (
            yearly_avg.idxmax()
        )

        lowest_year = (
            yearly_avg.idxmin()
        )

        # ----------------------------------------------------
        # SEASON
        # ----------------------------------------------------

        seasonal_avg = (
            clean_data
            .groupby("Season")[
                "PJMW_MW"
            ].mean()
        )

        highest_season = (
            seasonal_avg.idxmax()
        )

        lowest_season = (
            seasonal_avg.idxmin()
        )

        # ----------------------------------------------------
        # MONTH NAMES
        # ----------------------------------------------------

        month_names = {

            1: "January",
            2: "February",
            3: "March",
            4: "April",
            5: "May",
            6: "June",
            7: "July",
            8: "August",
            9: "September",
            10: "October",
            11: "November",
            12: "December"

        }

        # ----------------------------------------------------
        # FINDINGS
        # ----------------------------------------------------

        finding(
            "⚡ Overall Demand",

            f"The historical average electricity "
            f"demand is {avg:,.0f} MW."
        )

        finding(
            "🕐 Hourly Pattern",

            f"The highest average demand occurs "
            f"around {highest_hour}:00 with approximately "
            f"{highest_hour_value:,.0f} MW, while the lowest "
            f"average occurs around {lowest_hour}:00 with "
            f"approximately {lowest_hour_value:,.0f} MW."
        )

        finding(
            "📅 Weekday vs Weekend",

            f"Average weekday demand is "
            f"{weekday_avg:,.0f} MW compared with "
            f"{weekend_avg:,.0f} MW on weekends."
        )

        finding(
            "📆 Monthly Pattern",

            f"{month_names[highest_month]} has the "
            f"highest average monthly demand, while "
            f"{month_names[lowest_month]} has the lowest."
        )

        finding(
            "📈 Long-Term Pattern",

            f"The highest yearly average in the cleaned "
            f"dataset occurs in {highest_year}, while "
            f"the lowest yearly average occurs in "
            f"{lowest_year}."
        )

        finding(
            "🌦️ Seasonal Pattern",

            f"{highest_season} has the highest average "
            f"seasonal demand, while {lowest_season} "
            f"has the lowest."
        )

        finding(
            "🔺 Historical Peak",

            f"The highest recorded demand is "
            f"{max_row['PJMW_MW']:,.0f} MW at "
            f"{max_row['Datetime']}."
        )

        finding(
            "🔻 Historical Minimum",

            f"The lowest recorded demand is "
            f"{min_row['PJMW_MW']:,.0f} MW at "
            f"{min_row['Datetime']}."
        )

        # ----------------------------------------------------
        # FORECAST INSIGHTS
        # ----------------------------------------------------

        if forecast_hourly is not None:

            forecast_avg = (
                forecast_hourly[
                    "Predicted_MW"
                ].mean()
            )

            forecast_peak = (
                forecast_hourly.loc[
                    forecast_hourly[
                        "Predicted_MW"
                    ].idxmax()
                ]
            )

            finding(
                "🔮 Production Forecast",

                f"The production artifact contains "
                f"720 hourly predictions representing "
                f"a 30-day forecast. The average forecast "
                f"demand is {forecast_avg:,.0f} MW."
            )

            finding(
                "🎯 Forecast Peak",

                f"The highest predicted demand in the "
                f"30-day forecast is "
                f"{forecast_peak['Predicted_MW']:,.0f} MW "
                f"at {forecast_peak['Datetime']}."
            )

        # ----------------------------------------------------
        # XGBOOST BENCHMARK
        # ----------------------------------------------------

        finding(
            "📊 XGBoost Benchmark",

            "XGBoost achieved MAE of 72.60 MW, "
            "RMSE of 119.68 MW and MAPE of 1.27% "
            "on the benchmark validation period."
        )

        # ----------------------------------------------------
        # MODEL
        # ----------------------------------------------------

        finding(
            "🤖 Production Model",

            "The deployed production model is "
            "Seasonal Naive (24h), which uses the value "
            "from the same hour on the previous day."
        )

        finding(
            "📌 Model Selection",

            "The production model was selected using "
            "the lowest MAE among classical time-series "
            "models on chronological validation data."
        )

        # ----------------------------------------------------
        # PROJECT INTERPRETATION
        # ----------------------------------------------------

        st.subheader(
            "What This Means for the Project"
        )

        st.markdown(
            """
            - Electricity demand contains a clear hourly pattern.
            - Demand varies between weekdays and weekends.
            - Monthly and seasonal effects are visible.
            - Long-term yearly variation is present.
            - A 24-hour seasonal forecasting approach is therefore
              directly aligned with the project's strong daily
              demand pattern.
            - XGBoost provides an additional machine-learning
              benchmark for comparison.
            - The production forecast remains based on the
              documented Seasonal Naive (24h) model.
            - The forecast should be interpreted as a demand
              planning estimate rather than a guarantee of future
              electricity consumption.
            """
        )

# ============================================================
# DATA EXPLORER
# ============================================================

elif page == "🔎 Data Explorer":

    st.header(
        "Data Explorer"
    )

    datasets = {

        "Clean Hourly Data":
            clean_data,

        "Forecast History":
            history,

        "Hourly Forecast":
            forecast_hourly,

        "Daily Forecast":
            forecast_daily,

        "Time-Series Model Comparison":
            model_comparison,

        "All Model Comparison":
            all_models,

        "Rolling Validation":
            rolling_validation,

        "XGBoost Validation":
            xgb_validation,

        "XGBoost 30-Day Hourly Forecast":
            xgb_forecast_hourly,

        "XGBoost 30-Day Daily Forecast":
            xgb_forecast_daily,

        "XGBoost Feature Importance":
            xgb_feature_importance
    }

    choice = st.selectbox(
        "Choose a dataset",
        list(
            datasets.keys()
        )
    )

    selected = datasets[
        choice
    ]

    if selected is not None:

        st.write(
            f"**Rows:** {len(selected):,}  |  "
            f"**Columns:** {len(selected.columns)}"
        )

        st.dataframe(
            selected,
            use_container_width=True,
            height=550
        )

# ============================================================
# METHODOLOGY
# ============================================================

elif page == "📘 Methodology":

    st.header(
        "Project Methodology"
    )

    st.subheader(
        "1. Problem Definition"
    )

    st.write(
        "Forecast hourly electricity consumption "
        "using PJM historical demand data."
    )

    st.subheader(
        "2. Exploratory Data Analysis"
    )

    st.write(
        "The project examines hourly, weekly, "
        "monthly, yearly, seasonal and holiday-related "
        "demand patterns."
    )

    st.subheader(
        "3. Model Development"
    )

    st.write(
        "Multiple machine-learning and time-series "
        "approaches were evaluated."
    )

    st.subheader(
        "4. Production Model Selection"
    )

    st.write(
        "The final production candidate is selected "
        "only from classical time-series models using "
        "chronological validation and MAE."
    )

    st.subheader(
        "5. Production Model"
    )

    st.write(
        "Seasonal Naive (24h): the forecast for each "
        "hour uses the observed value from the same "
        "hour on the previous day."
    )

    st.subheader(
        "6. XGBoost Benchmark"
    )

    st.write(
        "XGBoost is included as a machine-learning "
        "benchmark. Its validation results are MAE "
        "72.60 MW, RMSE 119.68 MW and MAPE 1.27%."
    )

    st.subheader(
        "7. Forecast Horizon"
    )

    st.write(
        "The final production artifact contains 720 hourly "
        "forecasts, covering 30 days."
    )

    st.subheader(
        "8. Validation"
    )

    st.write(
        "Four rolling 30-day validation windows are "
        "included to examine model performance across "
        "the final year."
    )

    st.subheader(
        "Project Metadata"
    )

    st.json(
        metadata
    )

# ============================================================
# DOWNLOADS
# ============================================================

elif page == "⬇️ Downloads":

    st.header(
        "Project Downloads"
    )

    st.markdown(
        '<div class="section-note">'
        'Download the deployment-ready forecasting artifacts '
        'and project outputs.'
        '</div>',
        unsafe_allow_html=True
    )

    download_files = {

        "30-Day Hourly Forecast":
            "pjm_final_30_day_hourly_forecast.csv",

        "30-Day Daily Forecast":
            "pjm_final_30_day_daily_forecast.csv",

        "XGBoost Validation Predictions":
            "pjm_xgboost_validation_predictions.csv",

        "XGBoost 30-Day Hourly Forecast":
            "pjm_xgboost_30_day_hourly_forecast.csv",

        "XGBoost 30-Day Daily Forecast":
            "pjm_xgboost_30_day_daily_forecast.csv",

        "XGBoost Feature Importance":
            "pjm_xgboost_feature_importance.csv",

        "Clean Hourly Data":
            "pjm_clean_hourly_data.csv",

        "Model Comparison":
            "pjm_all_model_comparison_results.csv",

        "Time-Series Comparison":
            "pjm_time_series_model_comparison.csv",

        "Rolling Validation":
            "pjm_final_year_rolling_validation.csv",

        "Forecast History":
            "pjm_forecast_history_168.csv",

        "Forecast Metadata":
            "pjm_forecasting_metadata.json",

        "Final Model Information":
            "pjm_final_time_series_model.json"
    }

    for title, filename in download_files.items():

        path = BASE_DIR / filename

        if path.exists():

            with open(
                path,
                "rb"
            ) as f:

                data = f.read()

            st.download_button(

                label=f"⬇️ {title}",

                data=data,

                file_name=filename,

                key=f"download_{filename}"
            )