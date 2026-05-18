"""
pd.merge(data_frame1, data_frame2, on="Column_name", how="type of join")

"""

import pandas as pd

#customers dataframe
df_customers = pd.DataFrame ({
    'customerID' : [1,2,3],
    'name' : ['Ramesh', "Suresh", "Kalpesh"]
})

#order dataframe
df_orders = pd.DataFrame({
    'customerID' : [1,2,4],
    'OrderAmount' : [250, 450, 550]
})

#merge
merge_korbo = pd.merge(df_customers, df_orders, on="customerID", how="inner")
print(merge_korbo)
