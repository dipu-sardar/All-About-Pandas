"""
কিভাবে missing ভ্যালু findout করতে হয়। 
"""


import pandas as pd
data = {
    "name" : [None, "Dipa raha", "mahfuja", "Mousumi", "siam", "hello", "world", "torikul"],

    "age" : [12,3,2,3,None,2,34,32],

    "salary" : [10000,None,30000,4000,3000,2000, 6000, 7000],

    "score" : [85, None,4,5,2,3,54,3]

}

dipu = pd.DataFrame(data)
print(dipu)

print(dipu.isnull())

#কতগুলো মিসিং ভ্যালু আচ্ছে তা দেখতে 
print(dipu.isnull().sum())
