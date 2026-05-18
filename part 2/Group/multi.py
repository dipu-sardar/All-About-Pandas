#যদি multiple কলাম থাকে তাহলে কিভাবে গ্রুপ করব? 

import pandas as pd

data = {
    "name" : ["Dipu Sardar", "Dipa raha", "mahfuja", "Mousumi", "Dipu Sardar", "hello", "world", "torikul"],

    "age" : [12,3,2,3,12,2,34,32],

    "salary" : [10000,20000,30000,4000,3000,2000, 6000, 7000],

    "score" : [85, 3,4,5,2,3,54,3]

}

dipu = pd.DataFrame(data)
print(dipu)

#if need to multiple column groupping.
grouped = dipu.groupby(["age","name"])['salary'].sum()
print(grouped)
