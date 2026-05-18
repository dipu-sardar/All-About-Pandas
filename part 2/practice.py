import pandas as pd

dipu = pd.read_csv("/Users/dipusardar/DIPU/Programming/Pandas/part 2/practice.csv")

print(dipu)

print(dipu.columns)

total_sum = dipu["TotalSpent"].sum()
print(total_sum)









