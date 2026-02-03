End-to-End Crypto Data Engineering Pipeline

An end-to-end data engineering pipeline that ingests cryptocurrency market data from the CoinGecko API, stores raw data as JSON, cleans and transforms it using PySpark, loads it into a database, orchestrates the workflow using Apache Airflow, and performs downstream analysis.

This project is built to mirror real-world data engineering workflows.

Project Overview

The pipeline follows a modern data engineering architecture:

1.Extract raw crypto market data from CoinGecko

2.Store raw data as partitioned JSON files

3.Transform & clean data using PySpark

4.Load cleaned data into a database

5.Orchestrate the full workflow using Airflow

6.Analyze data for insights and reporting

Architecture
CoinGecko API
      ↓
Raw Data Ingestion (Python)
      ↓
Raw JSON Storage (Bronze)
      ↓
PySpark Cleaning & Transformation
      ↓
Database (Postgres)
      ↓
Analytics & Insights
