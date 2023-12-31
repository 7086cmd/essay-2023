import math
import numpy as np
import pandas as pd
import os.path as path
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties


def fn1(x):
    return 359.939478 * math.exp(0.124215 * (x - 1978))


def fn2(x):
    return 345.872895 * math.exp(0.114970 * (x - 1978))


def fn3(x):
    return 173.015491 * math.exp(0.112898 * (x - 1978))


def fn4(x):
    return 145.093811 * math.exp(0.110557 * (x - 1978))


x = np.linspace(1980, 2040, 1000)
y1 = np.array([fn1(i) for i in x])
y2 = np.array([fn2(i) for i in x])
y3 = np.array([fn3(i) for i in x])
y4 = np.array([fn4(i) for i in x])

for i in [2023, 2028, 2038]:
    print(f"{i} & ${fn1(i):.4f}$ & ${fn2(i):.4f}$ & ${fn3(i):.4f}$ & ${fn4(i):.4f}$ \\\\")

font = FontProperties(fname=path.join(path.dirname(__file__), "./SimSun.ttf"), size=14)

title = ["年份", "城镇常住居民人均可支配收入", "城镇常住居民人均消费支出", "农村常住居民人均可支配收入", "农村常住居民人均消费支出"]

plt.plot(x, y1, linewidth=2, linestyle="-", label=title[1])
plt.plot(x, y2, linewidth=2, linestyle="-", label=title[2])
plt.plot(x, y3, linewidth=2, linestyle="-", label=title[3])
plt.plot(x, y4, linewidth=2, linestyle="-", label=title[4])

plt.xlabel(title[0], fontproperties=font)
plt.ylabel("金额/元", fontproperties=font)

plt.xlim(1978, 2045)
plt.ylim(0, 1000000)

plt.legend(prop=font)

plt.savefig(
    path.join(
        path.dirname(__file__),
        f"../figures/result1.eps",
    )
)