# এটা interpolite এর একটা উধারণ 

import pandas as pd

data = {
    "Time" : [1,2,3,4,5],
    "Values" : [10, None, 30, None, 50]
}

dipu = pd.DataFrame(data)
print("Before Interpolition")
print(dipu)

print("After Interpolition")
dipu["Values"] = dipu["Values"].interpolate(method="linear")
print(dipu)