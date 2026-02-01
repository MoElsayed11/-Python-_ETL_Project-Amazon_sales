# -Python-_ETL_Project-Amazon_sales
This project is a **Python-based ETL (Extract, Transform, Load) pipeline** designed to process CSV data and load it into a **PostgreSQL database**. It demonstrates a modular, reusable, and production-ready structure suitable for data engineering workflows.

# Python ETL Pipeline Project

## Project Description
This project is a **Python-based ETL (Extract, Transform, Load) pipeline** designed to process CSV data and load it into a **PostgreSQL database**. It demonstrates a modular, reusable, and production-ready structure suitable for data engineering workflows.

**Key Features:**
- Extract data from CSV files.
- Clean and transform data using Pandas.
- Handle missing values, duplicates, and basic data validation.
- Load processed data into PostgreSQL.
- Logging of each step for traceability.
- Modular and reusable Python functions.

**Use Case:**  
This ETL project can be adapted for e-commerce, sales, or product datasets to prepare data for analytics, reporting, or machine learning tasks.

---

## Project Structure

python_etl_project/
│
├─ etl/
│ ├─ init.py
│ ├─ extract.py # CSV extraction functions
│ ├─ transform.py # Data cleaning functions
│ ├─ load.py # Load data into PostgreSQL
│ └─ config_loader.py # Load configuration from YAML
│
├─ config/
│ └─ config.yaml # Paths, logging, and database config
│
├─ data/
│ ├─ raw/ # Raw input CSV files
│ └─ processed/ # Processed/cleaned CSV files
│
├─ logs/ # Log files
├─ main.py # Main ETL pipeline script
├─ requirements.txt # Python dependencies
└─ README.md




---

## Installation & Setup

1. **Clone the repository:**
```bash
git clone https://github.com/<your-username>/python_etl_project.git
cd python_etl_project

python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt

PostgreSQL setup:

Create a database in PostgreSQL (e.g., python_etl)

Update config/config.yaml with your database credentials:

database:
  host: localhost
  port: 5432
  user: your_username
  password: your_password
  database: python_etl


Place your raw CSV files in data/raw/ (e.g., sales_raw.csv).

Running the ETL Pipeline
.\venv\Scripts\python.exe main.py


Pipeline Steps:

Extract data from CSV

Clean and transform data

Save cleaned data in data/processed/

Load data into PostgreSQL

Logs are saved in logs/etl.log

Sample Output

After running the pipeline, the cleaned data will look like:

product_id	product_name	price	rating	...
B07JW9H4J1	Wayona USB	299	4.5	...
B098NS6PVG	Ambrane USB	349	4.3	...
B096MSW6CT	Sounce USB	199	4.6	...

Logs example:

2026-01-29 15:08:42,160 - INFO - Starting data cleaning
2026-01-29 15:08:42,190 - INFO - Removed 0 duplicate rows
2026-01-29 15:08:42,216 - INFO - Data cleaning finished. Final row count: 1463

Contributing

Feel free to fork the repo and add new functionality such as:

Support for API data extraction

Loading to other databases (SQL Server, MySQL)

Advanced transformations or feature engineering

License

This project is MIT Licensed. You can use it freely in your portfolio or personal projects.


---

If you want, I can **also create a ready-to-use `config.yaml` file** that matches this README so you can just run the project without editing anything.  

Do you want me to do that next?
