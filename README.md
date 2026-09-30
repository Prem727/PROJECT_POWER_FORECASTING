\# ⚡ PJM Hourly Energy Consumption Forecasting



An end-to-end machine learning and time-series forecasting project for analyzing and forecasting hourly electricity consumption using historical PJM energy demand data.



The project includes exploratory data analysis (EDA), time-series model comparison, validation, error analysis, and an interactive Streamlit dashboard for forecasting the next 30 days of hourly electricity demand.



\---


## How to Run the Project

### 1. Run Locally

To run the application on your computer:

```bash
cd C:\Energy_Forecasting
pip install -r requirements.txt
python -m streamlit run app.py
```

After running the command, open:

```text
http://localhost:8501
```

The local application uses the trained Random Forest model stored in the project folder.


### Online Deployment

The project is deployed online using Streamlit Community Cloud.

**Live Application:**  
https://powerforcasting.streamlit.app/

No local installation is required to use the online application.



\## 📌 Project Overview



Electricity demand changes continuously based on factors such as:



\- Hour of the day

\- Day of the week

\- Weekday vs weekend behavior

\- Seasonal patterns

\- Long-term yearly trends

\- Holidays

\- Historical demand patterns



The objective of this project is to understand these patterns and build a forecasting system capable of predicting future hourly electricity consumption.



\### Project ID



\*\*P605 – PJM Hourly Energy Consumption Forecasting\*\*



\### Forecast Horizon



\*\*30 days / 720 hourly predictions\*\*



\### Production Model



\*\*Seasonal Naive (24-hour)\*\*



The production model predicts each hour using the electricity demand observed at the same hour on the previous day.



\---



\# 🎯 Project Objectives



The major objectives of this project are:



1\. Analyze historical PJM hourly electricity consumption.

2\. Identify hourly consumption patterns.

3\. Analyze weekday and weekend differences.

4\. Study holiday effects.

5\. Identify seasonal patterns.

6\. Analyze long-term yearly trends.

7\. Compare multiple forecasting and machine learning approaches.

8\. Select a suitable classical time-series forecasting model.

9\. Validate the selected model using chronological validation.

10\. Generate a 30-day hourly forecast.

11\. Generate daily forecast summaries.

12\. Build an interactive forecasting dashboard.

13\. Make the project available for local and online use.



\---



\# 📊 Dataset



The project uses the \*\*PJM hourly electricity consumption dataset\*\*.



\### Dataset Features



| Column | Description |

|---|---|

| `Datetime` | Date and time of electricity consumption |

| `PJMW\_MW` | Electricity consumption in megawatts (MW) |



\### Historical Data



The original dataset contains approximately:



\- \*\*143,206 hourly records\*\*

\- \*\*2 columns\*\*

\- Historical period from \*\*2002 to 2018\*\*

\- Electricity demand measured in \*\*MW\*\*



The dataset was cleaned and prepared before model development.



\---



\# 🔎 Exploratory Data Analysis



The project performs extensive exploratory data analysis to understand electricity consumption behavior.



The following areas were analyzed:



\### Hourly Consumption



Electricity demand varies significantly throughout the day.



The analysis identifies:



\- Lowest-demand hours

\- Highest-demand hours

\- Daily consumption patterns



\### Weekday vs Weekend



Electricity demand patterns differ between:



\- Weekdays

\- Weekends



This helps identify changes in electricity usage associated with working and non-working days.



\### Monthly Trends



Monthly electricity consumption was analyzed to identify seasonal demand changes throughout the year.



\### Yearly Trends



Year-by-year demand was analyzed to understand long-term changes in electricity consumption.



\### Seasonal Analysis



The data was grouped into:



\- Winter

\- Spring

\- Summer

\- Autumn



Seasonal hourly patterns were also analyzed.



\### Holiday Analysis



Holiday and non-holiday electricity demand were compared to identify differences in consumption behavior.



\### Demand Distribution



The distribution of electricity consumption was analyzed using statistical summaries and visualizations.



\### Rolling Demand



A rolling 24-hour demand measure was used to observe short-term trends and smooth hourly fluctuations.



\---



\# 📈 Important EDA Findings



Some important historical patterns identified during the analysis include:



\- Electricity demand changes significantly by hour.

\- Evening hours generally show higher electricity demand.

\- Weekday demand is higher than weekend demand in the analyzed dataset.

\- Seasonal demand patterns are clearly visible.

\- Winter shows strong electricity demand.

\- Holiday periods generally show different demand behavior compared with normal days.

\- The dataset contains a small number of unusual/high-demand observations.

\- Electricity consumption shows both short-term daily seasonality and longer-term trends.



\---



\# 🧹 Data Preparation



The data preparation process includes:



1\. Loading the PJM dataset.

2\. Converting `Datetime` into pandas datetime format.

3\. Sorting records chronologically.

4\. Checking missing values.

5\. Checking duplicate timestamps.

6\. Investigating time gaps.

7\. Cleaning the time-series data.

8\. Creating time-based features.

9\. Preparing chronological training and validation datasets.



\### Engineered Time Features



The project uses features such as:



\- Hour

\- Day

\- Day of Week

\- Month

\- Month Name

\- Year

\- Season

\- Day Type

\- Rolling 24-hour demand



\---



\# 🤖 Model Comparison



Multiple approaches were considered during the project.



The project includes comparison of machine learning and time-series approaches such as:



\- Decision Tree

\- Random Forest

\- XGBoost

\- PCA-based analysis

\- LSTM / Deep Learning approaches

\- Classical time-series forecasting models



Machine-learning models were useful as benchmarks, while the final production model was selected from the classical time-series models according to the project requirement.



\---



\# 🕒 Final Production Model



\## Seasonal Naive (24h)



The final production model is:



\*\*Seasonal Naive with a 24-hour seasonal period\*\*



The model uses the value from the same hour on the previous day as the forecast.



For example:



```text

Monday 10:00 AM

&#x20;       ↓

Tuesday 10:00 AM forecast

