<<<<<<< HEAD
# 📊 IT Log Monitoring & Analytics Pipeline

This project demonstrates an **ETL pipeline** using Python, PostgreSQL, and Streamlit for IT log monitoring.

## 🚀 Features
- Extract logs from text file
- Transform logs into structured format
- Load logs into PostgreSQL
- Interactive Streamlit dashboard

## 🏗️ Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Create PostgreSQL DB:
   ```bash
   psql -U postgres
   CREATE DATABASE it_logs;
   ```
3. Run schema:
   ```bash
   psql -U postgres -d it_logs -f database/schema.sql
   ```
4. Run pipeline:
   ```bash
   python pipeline/extract.py
   python pipeline/transform.py
   python pipeline/load.py
   ```
5. Launch dashboard:
   ```bash
   streamlit run dashboard/app.py
   ```
=======
# it-log-pipeline
IT Log Monitoring Dashboard using Python, Streamlit, and PostgreSQL
>>>>>>> a5d8dda9d13cdda5f2bd7da46a8773a1358a515a
