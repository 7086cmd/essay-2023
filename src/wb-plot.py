
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import numpy as np
import pandas as pd
import os.path as path

def plotbase(name: str, start_bit: int, start_yr: int, end_yr: int):
    
    data = pd.read_csv(path.join(path.dirname(__file__), f"./wb-{name.lower()}pc.csv"), encoding="utf-8")

    # Create 4 plots (scatter) of the data (total 4) (line 0 as the x-axis, line :i: as the y-axis)

    font = FontProperties(fname=path.join(path.dirname(__file__), "./SourceHanSerifSC-Medium.otf"), size=14)

    plt.plot(1, 1, label=name)
    plt.scatter(data.iloc[start_bit:, 4], data.iloc[start_bit:, 10])
    plt.xlabel(data.columns[0], fontproperties=font)
    plt.ylabel("Amount / USD", fontproperties=font)
    plt.xlim(start_yr, end_yr)
    plt.legend(prop=font)
    plt.savefig(
        path.join(
            path.dirname(__file__),
            f"../figures/plot-wb-{name.lower()}.eps",
        )
    )
    plt.savefig(
        path.join(
            path.dirname(__file__),
            f"../figures/plot-wb-{name.lower()}.png",
        )
    )
    plt.close()

plotbase('GDP', 20, 1978, 2023)
plotbase('PPP', 0, 1990, 2023)