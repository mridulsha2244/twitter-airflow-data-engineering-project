# twitter-airflow-data-engineering-project
Self-made Project

## Overview

This project showcases a complete data engineering pipeline built using Apache Airflow to automate the extraction, transformation, and loading (ETL) of Twitter data. The goal is to collect tweets, process and clean the data, and store it in a structured format for future analysis or reporting.

## Key Objectives

- Automate Twitter data ingestion using Airflow DAGs
- Clean and transform raw tweet data using Python
- Store processed data in a centralized location (CSV, database, or S3)
- Ensure pipeline scalability, maintainability, and reusability

## Tech Stack & Tools
	                
Apache Airflow	      Workflow orchestration and scheduling
Twitter API (v2)	    Real-time data extraction
Python	              Data extraction, cleaning, and transformation
Pandas	              Data manipulation and processing
S3 / CSV	            Data storage options

 ## Pipeline Workflow

Start DAG
   │
   ├── Extract: Fetch tweets using Twitter API
   │
   ├── Transform: Clean text, parse timestamps, extract hashtags
   │
   └── Load: Save to database, CSV file, or cloud (S3)
End DAG

## Author

Mridul Sharma
Data Engineer | Python | Big Data | AWS | SQL
