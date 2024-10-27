import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import numpy as np
import pandas as pd
import os.path as path

data = pd.read_csv(path.join(path.dirname(__file__), "./data.csv"), encoding="utf-8")

# Create 4 plots (scatter) of the data (total 4) (line 0 as the x-axis, line :i: as the y-axis)

font = FontProperties(fname=path.join(path.dirname(__file__), "./SourceHanSerifSC-Medium.otf"), size=14)

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
    plt.savefig(
        path.join(
            path.dirname(__file__),
            f"../figures/plot{str(total)}.png",
        )
    )
    plt.close()


plotbase(1, 5)
plotbase(1, 3)
plotbase(3, 5)
