"""Shared plot style for course notebooks.

`import figure_style as fs` applies the style and exposes

color_list : list[str]  hex color strings in plot-cycle order
fullwidth  : float      full page width (in) for letter paper, 0.5 in margins
fullheight : float      full page height (in)
fsize      : int        base font size used throughout

Requires the Fira Sans font (system-installed).
"""

import matplotlib.pyplot as plt
import seaborn as sns


def figure_style(title_fontsize=10, label_fontsize=10, tick_fontsize=10):

    fsize = 10
    lw = 1.0

    # set_theme resets the context; font sizes/linewidths applied via rcParams below
    sns.set_theme(style="ticks", palette="deep", font="Fira Sans")

    color_list = ['#4C2882', '#367588', '#A52A2A', '#C39953', '#2A52BE', '#006611']
    plt.rcParams['axes.prop_cycle'] = plt.cycler(color=color_list)

    plt.rcParams.update({
        'axes.grid': True,
        'font.size': fsize,
        'axes.titlesize': title_fontsize,
        'axes.labelsize': label_fontsize,
        'xtick.labelsize': tick_fontsize,
        'ytick.labelsize': tick_fontsize,
        'legend.fontsize': label_fontsize,
        'grid.linewidth': lw,
        'xtick.major.width': lw,
        'ytick.major.width': lw,
    })

    # Full page figure size (assuming letter paper with 0.5 inch margins)
    fullwidth = 7.5
    fullheight = 10

    return color_list, fullwidth, fullheight, fsize


color_list, fullwidth, fullheight, fsize = figure_style()
