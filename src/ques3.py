import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

df = pd.DataFrame({
  'year': [0, 1, 2, 3, 4],
  'city_income': [343, 387, 478, 458, 495],
})

x = df['year'].values.reshape(-1, 1)
y = df['city_income'].values.reshape(-1, 1)
x_pow = np.power(x, 2)

'''
funtion: $h\\left(x\\right)=\\theta_1 x^2+\\theta_0$
'''

model = LinearRegression()
model.fit(x_pow, y)

b = model.coef_[0][0]
a = model.intercept_[0]

print(f'y = {a:.6f} + {b:.6f} * x^2')

loss = model.score(x_pow, y)

print(f'loss = {loss:.8f}')
