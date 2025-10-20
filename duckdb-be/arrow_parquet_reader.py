import pyarrow.parquet as pq
import pyarrow as pa
import pyarrow.ipc as ipc


# Load the Parquet file
file_path = "data/raw/transactions_data.parquet"
parquet_file = pq.ParquetFile(file_path)


print("=== FILE SCHEMA ===")
print(parquet_file.schema_arrow)
print("\n=== METADATA ===")
print(parquet_file.metadata)


table = parquet_file.read()



print("\n=== FIRST 5 VALUES PER COLUMN ===")
for name, col in zip(table.column_names, table.columns):
    print(f"{name}: {col.to_pylist()[:5]}")
'''

file_path = "data/raw/transactions_data.arrow"

with pa.memory_map(file_path, "r") as source:
    reader = ipc.RecordBatchFileReader(source)

    print("=== FILE SCHEMA ===")
    print(reader.schema)

    print("\n=== METADATA ===")
    print(reader.metadata)

    print("\n=== NUMBER OF BATCHES ===")
    print(reader.num_record_batches)

    table = reader.read_all()

    print("\n=== FIRST 5 VALUES PER COLUMN ===")
    for name, col in zip(table.column_names, table.columns):
        print(f"{name}: {col.to_pylist()[:5]}")
'''