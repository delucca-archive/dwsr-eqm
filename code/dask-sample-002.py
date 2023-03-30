import dask.dataframe as dd
import pandas as pd

# Read a large CSV file in chunks
df = dd.read_csv("large_data.csv", blocksize="64MB")

# Perform parallel groupby and aggregation operations
result = df.groupby("column_name").agg({"other_column": "sum"})

# Compute the result
result = result.compute()
