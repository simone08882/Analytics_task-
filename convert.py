import pyarrow as pa
import pyarrow.parquet as pq
import json
import glob
import os
import shutil 

source_folder = "sessions_data"
backup_folder = "json_backup"

if not os.path.exists(backup_folder):
    os.makedirs(backup_folder)

file_list = glob.glob(f"{source_folder}/*.json")

for file_name in file_list:
    with open(file_name, "r") as file:
        file_data = file.read()

    file_data_json = json.loads(file_data)

    table = pa.Table.from_pylist(file_data_json)
    parquet_file_name = file_name.replace(".json", ".parquet")

    pq.write_table(table, parquet_file_name)

    shutil.copy(file_name, os.path.join(backup_folder, os.path.basename(file_name)))

    os.remove(file_name)

    print(f"Converted: {file_name} → {parquet_file_name} (Backup saved in {backup_folder})")
