import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import numpy as np
import pandas as pd
import os.path as path

data = pd.read_csv(path.join(path.dirname(__file__), "./data.csv"), encoding="utf-8")

# Create 4 plots (scatter) of the data (total 4) (line 0 as the x-axis, line :i: as the y-axis)

font = FontProperties(fname=path.join(path.dirname(__file__), "./SimSun.ttf"), size=14)

total = 0


def plot(x: int, y: int):
    global total
    total += 1
    plt.plot(1, y, label=data.columns[y])
    plt.scatter(data.iloc[:, x], data.iloc[:, y])
    plt.xlabel(data.columns[x], fontproperties=font)
    plt.ylabel(data.columns[y], fontproperties=font)
    plt.savefig(
        path.join(
            path.dirname(__file__),
            f"../figures/comparison{str(total)}.eps",
        )
    )
    plt.savefig(
        path.join(
            path.dirname(__file__),
            f"../figures/comparison{str(total)}.png",
        )
    )
    plt.close()

plot(1, 2)
plot(3, 4)

plot(1, 3)
plot(2, 4)
