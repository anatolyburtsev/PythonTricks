import hypothesis
import pandas as pd
import pandera as pa
from pandera import Column, Check, check_io

available_fruits = ["apple", "banana", "orange"]
nearby_stores = ["Aldi", "Walmart"]

in_schema = pa.DataFrameSchema(
    {
        "name": Column(str, Check.isin(available_fruits)),
        "store": Column(str, Check.isin(nearby_stores)),
        "price": Column(int, Check.in_range(min_value=0, max_value=5)),
    }
)

out_schema = pa.DataFrameSchema(
    {
        "name": Column(str, Check.isin(available_fruits)),
        "price": Column(float, Check.in_range(min_value=0, max_value=5)),
    }
)


@check_io(fruits_df=in_schema, out=out_schema)
def fruit_mean_price(fruits_df: pd.DataFrame):
    return fruits_df.groupby("name")["price"].mean().reset_index()


print(in_schema.strategy(size=10).example())



@hypothesis.given(in_schema.strategy(size=10))
def test_combine_fruits(df):
    fruit_mean_price(df)
