import pandas as pd

data = {
    "name" : ["Dipu sardar", "Dipa raha", "mahfuja", "Mousumi", "siam", "hello", "world", "torikul"],

    "age" : [12,3,2,3,4,2,34,32],

    "salary" : [10000,20000,30000,4000,3000,2000, 6000, 7000],

    "perfermance score" : [85, 3,4,5,2,3,54,3]

}

dipu = pd.DataFrame(data)

#single codition use for filtering rows
high_salary = dipu[dipu["salary"] > 25000]
print(high_salary)

#Multiple condition use for filtering rows (এইটা অনেক সহজ)
multiple_rows = dipu[(dipu["salary"] >= 6000) & (dipu["salary"] <= 10000) & (dipu["age"] > 12)]  #এইটা অনেক সহজ 
print(multiple_rows)