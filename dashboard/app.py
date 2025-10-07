import streamlit as st
import psycopg2
import pandas as pd
from datetime import datetime
from streamlit_autorefresh import st_autorefresh

# -----------------------------
# DATABASE CONNECTION FUNCTION
# -----------------------------
def get_data():
    conn = psycopg2.connect(
        dbname="it_logs",
        user="postgres",
        password="it-logs-db.c3asc2aaqshq.eu-north-1.rds.amazonaws.com",  # ✅ your real PostgreSQL password
        host="localhost",
        port="5432"
    )
    df = pd.read_sql("SELECT * FROM logs ORDER BY timestamp DESC", conn)
    conn.close()
    return df


# -----------------------------
# STREAMLIT DASHBOARD
# -----------------------------
st.set_page_config(page_title="IT Log Dashboard", layout="wide", page_icon="📊")

# Auto-refresh every 10 seconds
st_autorefresh(interval=10000, key="datarefresh")

st.title("📊 IT Log Monitoring Dashboard")

# Fetch data
df = get_data()

if df.empty:
    st.warning("⚠️ No log data found in database.")
    st.stop()

# Convert timestamp column to datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])

# -----------------------------
# COLOR-CODE FUNCTION
# -----------------------------
def highlight_level(val):
    color = ''
    if val == 'ERROR':
        color = 'red'
    elif val == 'WARN':
        color = 'orange'
    elif val == 'INFO':
        color = 'green'
    return f'color: {color}; font-weight: bold;'


# -----------------------------
# RAW LOGS SECTION
# -----------------------------
st.subheader("🧾 Raw Logs")
st.dataframe(df.style.applymap(highlight_level, subset=['level']), use_container_width=True)

# -----------------------------
# DATE RANGE FILTER
# -----------------------------
st.subheader("📅 Filter by Date Range")
col1, col2 = st.columns(2)
with col1:
    start_date = st.date_input("Start Date", df['timestamp'].min().date())
with col2:
    end_date = st.date_input("End Date", df['timestamp'].max().date())

filtered_df = df[
    (df['timestamp'].dt.date >= start_date) &
    (df['timestamp'].dt.date <= end_date)
]

# -----------------------------
# LOG LEVEL FILTER
# -----------------------------
st.subheader("⚙️ Filter by Log Level")
log_levels = df['level'].unique()
selected_levels = st.multiselect("Select Log Levels", log_levels, default=log_levels)

filtered_df = filtered_df[filtered_df['level'].isin(selected_levels)]

st.subheader("🔍 Filtered Logs")
st.dataframe(filtered_df.style.applymap(highlight_level, subset=['level']), use_container_width=True)

# -----------------------------
# ANALYTICS SECTION
# -----------------------------
st.subheader("📈 Log Analytics")

# Logs per Level
st.markdown("**Log Level Distribution**")
st.bar_chart(filtered_df['level'].value_counts())

# Logs over Time
st.markdown("**Error Frequency Over Time**")
time_chart = (
    filtered_df.groupby(filtered_df['timestamp'].dt.strftime('%Y-%m-%d %H:%M'))['level']
    .count()
    .reset_index(name='count')
)
st.line_chart(time_chart.set_index('timestamp')['count'])

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("---")
st.caption("👩‍💻 Developed by Snehal | Powered by Streamlit, PostgreSQL & Python 🚀")


