import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import numpy as np
import pandas as pd
import os.path as path

data = pd.read_csv(path.join(path.dirname(__file__), "./data.csv"), encoding="utf-8")

# Create 4 plots (scatter) of the data (total 4) (line 0 as the x-axis, line :i: as the y-axis)

font = FontProperties(fname=path.join(path.dirname(__file__), "./SimSun.ttf"), size=14)

total = 0


def plotbase(fr: int, to: int):
    global total
    total += 1
    for i in range(fr, to):
        plt.plot(1, i, label=data.columns[i])
        plt.scatter(data.iloc[:, 0], data.iloc[:, i])
        plt.xlabel(data.columns[0], fontproperties=font)
        plt.ylabel("金额/元", fontproperties=font)
        plt.xlim(1978, 2020)
    plt.legend(prop=font)
    plt.savefig(
        path.join(
            path.dirname(__file__),
            f"../figures/plot{str(total)}.eps",
        )
    )
    plt.close()


def plot(x, y):
    global total
    total += 1
    plt.plot(1, 1, y, label=data.columns[y])
    sub = plt.scatter(data.iloc[:, x], data.iloc[:, y])
    if x == 0:
        plt.xlim(1978, 2020)
    plt.xlabel(data.columns[x], fontproperties=font)
    plt.ylabel("金额/万元", fontproperties=font)
    sub.legend_elements()
    if (total % 2 == 0 and total > 4) or total == 4:
        plt.savefig(
            path.join(
                path.dirname(__file__),
                f"../figures/plot{str(total // 2)}.png",
            )
        )
    # print(f"Plot ({data[x].name}, {data[y].name}) saved to figures/plot{str(total)} ([{str(x)}] - [{str(y)}]).png")
    if (total % 2 == 0 and total > 4) or total == 4:
        plt.close()


plotbase(1, 5)
plotbase(1, 3)
plotbase(3, 5)


# plot(1, 2)
# plot(3, 4)

# plot(1, 3)
# plot(1, 4)
