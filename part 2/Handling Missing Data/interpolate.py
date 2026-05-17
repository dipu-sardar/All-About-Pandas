import pandas as pd
data = {
    "name" : ["Dipu Sardar", "Dipa raha", "mahfuja", "Mousumi", "siam", "hello", "world", "torikul"],

    "age" : [12,3,2,3,None,2,34,32],

    "salary" : [10000,None,30000,4000,3000,2000, 6000, 7000],

    "score" : [85, None,4,5,2,3,54,3]

}

dipu = pd.DataFrame(data)
print(dipu)

#interpolate(method, axis=0/1, interplace=True)
dipu.interpolate(method="linear", axis=0, inplace=True )
print(dipu)
