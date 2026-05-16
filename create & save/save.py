#কিভাবে pandas এর data সেভ করতে হয়।
"""
এখেনে একটা ভালো জিনিস শিখলাম, সেটা হলো dictionary বানিয়ে এক্সেল এর মতো শিট বানানো যায়. খুব ই সিম্পল 

"""
import pandas as pd

data =  {
    "name" : ['dipu', 'mahfuja', 'siam'],
    "age" : [20, 30, 40], 
    "city" : ["barishal", "dhaka", "rongpur"]

}

df = pd.DataFrame(data)

print(df)


df.to_excel("output.xlsx", index = False) #যদি আমি ইনডেক্স নাম্বার না চাই তাহলে "," দিয়ে index = false লিখতে হবে।








