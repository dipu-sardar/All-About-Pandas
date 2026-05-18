#sorting data

#sorting data in 1 column -- sort_values()
#df.sort_values(by="Column_name", True/False, inplace=True)

import pandas as pd

data = {
    "name" : ["Arun", "Barun", "Zack", "Dipu"],
    "age" : [20, 23, 34, 21],
    "salary" : [10000, 9000, 13000, 5000]

}

dipu = pd.DataFrame(data)
print(dipu)

#single column sorting
dipu.sort_values(by="name", ascending=True, inplace=True)
print(dipu)

#multiple column sorting
dipu.sort_values(by=["name","age"], ascending=[True, True], inplace=True)
print(dipu)
