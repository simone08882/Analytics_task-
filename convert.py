import os
import glob
import json
import shutil
import pyarrow as pa
import pyarrow.parquet as pq

source_folder = "sessions_data"
backup_folder = "json_backup"

# Ensure backup folder exists
if not os.path.exists(backup_folder):
    os.makedirs(backup_folder)

file_list = glob.glob(f"{source_folder}/*.json")

for file_name in file_list:
    try:
        with open(file_name, "r") as file:
            file_data = file.read()

        if not file_data.strip():
            print(f"Skipping empty file: {file_name}")
            continue  

        file_data_json = json.loads(file_data)

        table = pa.Table.from_pylist(file_data_json)
        
        parquet_file_name = file_name.replace(".json", ".parquet")

        if os.path.exists(parquet_file_name):
            print(f"Parquet file already exists: {parquet_file_name}, skipping conversion.")
        else:
            pq.write_table(table, parquet_file_name)
            print(f"Converted: {file_name} → {parquet_file_name}")

        # Move JSON to backup (instead of deleting immediately)
        shutil.move(file_name, os.path.join(backup_folder, os.path.basename(file_name)))
        print(f"Backup saved: {file_name} → {backup_folder}")

    except Exception as e:
        print(f"Error processing {file_name}: {e}")

print("Conversion completed.")
