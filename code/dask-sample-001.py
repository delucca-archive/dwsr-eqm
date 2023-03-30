import dask.array as da

# Create a large Dask array
x = da.random.random((10000, 10000), chunks=(1000, 1000))

# Perform element-wise operations in parallel
y = x + x.T

# Compute the result
result = y.compute()
