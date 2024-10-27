import math
import numpy as np
import pandas as pd
import os.path as path
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

data = pd.read_csv(path.join(path.dirname(__file__), "./data.csv"), encoding="utf-8")

# Create 4 plots (scatter) of the data (total 4) (line 0 as the x-axis, line :i: as the y-axis)

font = FontProperties(fname=path.join(path.dirname(__file__), "./SourceHanSerifSC-Medium.otf"), size=14)

total = 0


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


plt.legend(prop=font)

plt.xlabel("年份", fontproperties=font)
plt.ylabel("金额/元", fontproperties=font)

def plotbase(fr: int, to: int):
    global total
    total += 1
    for i in range(fr, to):
        plt.plot(1, i, label=data.columns[i])
        plt.scatter(data.iloc[:, 0], data.iloc[:, i])


plt.xlim(1978, 2020)
plt.ylim(0, 40000)

plotbase(1, 5)
plotbase(1, 3)
plotbase(3, 5)

plt.savefig(
    path.join(
        path.dirname(__file__),
        f"../figures/combine-1.eps",
    )
)

plt.savefig(
    path.join(
        path.dirname(__file__),
        f"../figures/combine-2.png",
    )
)