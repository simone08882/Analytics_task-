import pyarrow as pa
import pyarrow.parquet as pq
import json
import glob
import os

file_pattern = "sessions_data/*.json"

file_list = glob.glob(file_pattern)

for file_name in file_list:
    with open(f"{file_name}", "r+") as file:
        file_data = file.read()

    file_data_json = json.loads(file_data)

    # converting json to parquet
    table = pa.Table.from_pylist(file_data_json)

    pq.write_table(table, f"{file_name.replace('.json', '')}.parquet")

    # removing the json file
    os.remove(f"{file_name}")