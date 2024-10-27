import pandas as pd
import numpy as np
import os.path as path
from sklearn.linear_model import LinearRegression

data = pd.read_csv(path.join(path.dirname(__file__), "./data.csv"), encoding="utf-8")

# replace the first column of each row with the (year - 1978)

data['年份'] = data['年份'] - 1978

def regression(line: int):
    x = data.iloc[:, 0].values.reshape(-1, 1)
    y = data.iloc[:, line].values.reshape(-1, 1)
    
    y_log = np.log(y)
    
    model = LinearRegression()
    model.fit(x, y_log)
    
    b = model.coef_[0][0]
    a = np.exp(model.intercept_[0])
    
    print(f'y = {a:.6f} * e^({b:.6f} * x)')
    
    loss = model.score(x, y_log)
    
    print(f'loss = {loss:.8f}')

for i in range(1, 5):
    regression(i)
