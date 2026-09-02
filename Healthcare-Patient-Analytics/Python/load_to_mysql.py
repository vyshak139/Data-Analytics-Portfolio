# ==========================================
# Healthcare Analytics Project
# Load CSV Files into MySQL Database
# ==========================================

import os
import pandas as pd
from sqlalchemy import create_engine

# ==========================================
# Database Configuration
# ==========================================

DB_USER = "root"
DB_PASSWORD = "pass5311"
DB_HOST = "localhost"
DB_PORT = "3306"
DB_NAME = "HealthcareAnalyticsDB"

engine = create_engine(
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

print("✅ Connected to MySQL Successfully!")

# ==========================================
# Folder containing all CSV files
# ==========================================

DATA_FOLDER = "/Users/vaishakvs/Documents/Data Analytics Project/Healthcare-Patient-Analytics/Tables"

# ==========================================
# Read patients.csv
# ==========================================

patients_file = os.path.join(DATA_FOLDER, "patients.csv")

df = pd.read_csv(patients_file)

print("✅ Patients file loaded successfully!")
print(f"Rows: {len(df)}")
print(f"Columns: {len(df.columns)}")

# ==========================================
# List of CSV files to import
# ==========================================

tables = [
    "patients",
    "encounters",
    "providers",
    "organizations",
    "conditions",
    "medications",
    "payers"
]

# ==========================================
# Import all tables
# ==========================================

for table in tables:

    file_path = os.path.join(DATA_FOLDER, f"{table}.csv")

    print(f"\n📂 Reading {table}.csv ...")

    df = pd.read_csv(file_path)

    print(f"Rows: {len(df)}")
    print(f"Columns: {len(df.columns)}")

    df.to_sql(
        name=table,
        con=engine,
        if_exists="replace",
        index=False
    )

    print(f"✅ {table} imported successfully!")

print("\n🎉 All tables imported successfully!")

# ==========================================
# Export MySQL Tables to CSV
# ==========================================

import os
import pandas as pd

EXPORT_FOLDER = "/Users/vaishakvs/Documents/Data Analytics Project/Healthcare-Patient-Analytics/ExportedCSV"

os.makedirs(EXPORT_FOLDER, exist_ok=True)

tables = [
    "patients",
    "encounters",
    "providers",
    "organizations",
    "conditions",
    "medications",
    "payers"
]

for table in tables:
    df = pd.read_sql(f"SELECT * FROM {table}", engine)
    output = os.path.join(EXPORT_FOLDER, f"{table}.csv")
    df.to_csv(output, index=False)
    print(f"✅ Exported {table}.csv")

print("\n🎉 All tables exported successfully!")