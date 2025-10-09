import pandas as pd

# dataframes
df = pd.DataFrame(
    {
        "Name":[
             "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age":[22,35,58],
        "sex":["male","female","female"]
    }
)
print(df)

# series (NB: Every column in a dataframe is a series) -> seies has no clumn labels
ages= pd.Series([22,35,58],name="Age")
print(ages)
print(df['Age'].max())

import pandas as pd
import numpy as np

### ===============================
### 1. CREATE DATAFRAMES & SERIES
### ===============================
# From dictionary
data = {
    "name": ["Alice", "Bob", "Charlie", "Diana"],
    "age": [25, 30, 35, 40],
    "city": ["NY", "Paris", "London", "Berlin"]
}
df = pd.DataFrame(data)
print(df)

# From list
s = pd.Series([1, 2, 3, 4], name="numbers")
print(s)

# From numpy
arr = np.arange(9).reshape(3, 3)
df2 = pd.DataFrame(arr, columns=["A", "B", "C"])
print(df2)

### ===============================
### 2. INSPECTION
### ===============================
print(df.head(2))       # first rows
print(df.tail(2))       # last rows
print(df.info())        # info
print(df.describe())    # summary stats
print(df.shape)         # (rows, cols)
print(df.columns)       # column labels
print(df.index)         # row labels

### ===============================
### 3. INDEXING & SELECTION
### ===============================
print(df["name"])           # select column
print(df[["name","city"]])  # multiple columns
print(df.iloc[1])           # row by index
print(df.loc[1])            # row by label
print(df.loc[0:2, ["name","age"]])  # slice rows & cols

# Boolean indexing
print(df[df["age"] > 30])
# Query method
print(df.query("age < 35"))

### ===============================
### 4. MODIFYING DATA
### ===============================
df["country"] = ["US", "FR", "UK", "DE"]   # add col
df.loc[0, "age"] = 26                     # update value
df.drop("country", axis=1, inplace=True)  # drop col
df.drop(1, axis=0, inplace=True)          # drop row

### ===============================
### 5. SORTING & RANKING
### ===============================
print(df.sort_values(by="age", ascending=False))
print(df.sort_index())
print(df["age"].rank())

### ===============================
### 6. STATISTICS & FUNCTIONS
### ===============================
print(df["age"].mean(), df["age"].sum())
print(df["age"].min(), df["age"].max())

# Apply functions
print(df["age"].apply(lambda x: x*2))
print(df.applymap(lambda x: str(x).upper()))

### ===============================
### 7. GROUPBY & AGGREGATION
### ===============================
data = {
    "dept": ["IT","IT","HR","HR","Finance","Finance"],
    "salary": [5000,6000,4000,4500,7000,7200],
    "bonus": [500,600,400,450,700,750]
}
df3 = pd.DataFrame(data)

print(df3.groupby("dept").mean())     # group mean
print(df3.groupby("dept")["salary"].sum())  # group sum
print(df3.groupby("dept").agg({"salary":["mean","max"], "bonus":"sum"}))

### ===============================
### 8. MERGING, JOINING, CONCAT
### ===============================
df_a = pd.DataFrame({"id":[1,2,3], "name":["A","B","C"]})
df_b = pd.DataFrame({"id":[1,2,4], "score":[90,80,70]})

print(pd.merge(df_a, df_b, on="id", how="inner"))  # inner join
print(pd.merge(df_a, df_b, on="id", how="left"))   # left join

# Concatenation
print(pd.concat([df_a, df_b], axis=0))  # stack rows
print(pd.concat([df_a, df_b], axis=1))  # stack cols

### ===============================
### 9. PIVOT & CROSSTAB
### ===============================
sales = pd.DataFrame({
    "city":["NY","NY","Paris","Paris"],
    "year":[2020,2021,2020,2021],
    "sales":[100,150,200,250]
})
print(sales.pivot(index="city", columns="year", values="sales"))
print(pd.crosstab(sales["city"], sales["year"]))

### ===============================
### 10. HANDLING MISSING DATA
### ===============================
df_nan = pd.DataFrame({"A":[1, np.nan, 3], "B":[4,5,np.nan]})
print(df_nan.isnull())
print(df_nan.dropna())              # drop missing
print(df_nan.fillna(0))             # fill missing

### ===============================
### 11. STRING OPERATIONS
### ===============================
df_str = pd.DataFrame({"name":["alice","BOB","Charlie"]})
print(df_str["name"].str.upper())
print(df_str["name"].str.contains("a"))
print(df_str["name"].str.replace("a","@"))

### ===============================
### 12. DATETIME
### ===============================
dates = pd.date_range("2023-01-01", periods=6, freq="D")
ts = pd.DataFrame({"date":dates, "sales":np.arange(6)})
print(ts.set_index("date").resample("2D").sum())

### ===============================
### 13. MULTI-INDEX
### ===============================
arrays = [
    ["A","A","B","B"],
    [1,2,1,2]
]
multi_index = pd.MultiIndex.from_arrays(arrays, names=("letter","number"))
df_multi = pd.DataFrame(np.random.randn(4,2), index=multi_index, columns=["val1","val2"])
print(df_multi)
print(df_multi.loc["A"])
print(df_multi.xs(1, level="number"))

### ===============================
### 14. EXPORT / IMPORT
### ===============================
df.to_csv("data.csv", index=False)          # save
pd.read_csv("data.csv")                     # load

df.to_excel("data.xlsx", index=False)
pd.read_excel("data.xlsx")

df.to_json("data.json")
pd.read_json("data.json")
