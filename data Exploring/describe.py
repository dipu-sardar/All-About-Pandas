#Describe method

#step-1 smple data frame

import pandas as pd

data = {
    "name" : ["Dipu sardar", "Dipa raha", "mahfuja", "Mousumi", "siam", "hello", "world", "torikul"],

    "age" : [12,3,2,3,4,2,34,32],

    "salary" : [3000,200,399,299,1333,23343, 30000, 40000],

    "perfermance score" : [85, 3,4,5,2,3,54,2]

}

dipu = pd.DataFrame(data)

print(dipu)


#এখন দেখব describe এর কাজ কি? 
print("Describtive Statistics")
print(dipu.describe())