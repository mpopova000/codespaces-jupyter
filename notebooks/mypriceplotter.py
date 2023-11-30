import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
def plot_prices(times, prices):
    fig, ax = plt.subplots()
    ax.set_title('Prices')
    ax.set_xlabel('times in days')
    ax.set_ylabel('prices in dollars')
    ax.plot(times, prices)
    return fig, ax
