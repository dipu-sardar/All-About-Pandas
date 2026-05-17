import pandas as pd
data = {
    "name" : ["Dipu sardar", "Dipa raha", "mahfuja", "Mousumi", "siam", "hello", "world", "torikul"],

    "age" : [12,3,2,3,4,2,34,32],

    "salary" : [10000,20000,30000,4000,3000,2000, 6000, 7000],

    "score" : [85, 3,4,5,2,3,54,3]

}

dipu = pd.DataFrame(data)
print(dipu)

#.loc[]
#df.loc[row_index, "column_name"] = new_value
dipu.loc[0, "salary"] = 50000 #change the salary ammount 
dipu.loc[0, "name"] = "Anisul Islam" #change the name 

print(dipu)



