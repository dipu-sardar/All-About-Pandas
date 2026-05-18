#df["column_name"],sum()

import pandas as pd

data = {
    "name" : ["Arun", "Barun", "Zack", "Dipu"],
    "age" : [20, 23, 34, 21],
    "salary" : [10000, 9000, 13000, 7000]

}

dipu = pd.DataFrame(data)
print(dipu)

#summetion
sum_of_salary = dipu["salary"].sum()
print(sum_of_salary)

#minimum
minimum_of_salary = dipu["salary"].min()
print(minimum_of_salary)


#Maximum
maximum_of_salary = dipu["salary"].max()
print(maximum_of_salary)
