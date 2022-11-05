import matplotlib.dates as mdates
from matplotlib import pyplot as plt
from matplotlib.dates import DateFormatter

COLORS = ["red", "purple", "green", "black", "blue"]


def plot_series(*args,
                labels=None, fig_length=4):
    fig, ax = plt.subplots(figsize=(10, fig_length))
    time = args[0].index

    if labels is None:
        labels = [a.name for a in args]

    for i, series in enumerate(args):
        ax.plot(time, series, color=COLORS[i % len(COLORS)], alpha=0.5, label=labels[i])
        fig.autofmt_xdate()

        ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=4))
        ax.xaxis.set_major_formatter(DateFormatter("%m-%d"))
    title = "Tiktok Data - @pazpazTheCoder"

    ax.set_title(title)
    plt.grid(True)

    if len(args) > 1:
        plt.legend()
    plt.show()


def plot_two_axis(series1, *args,
                  titles, fig_length=4):
    fig, ax = plt.subplots(ncols=2, nrows=1, figsize=(12, fig_length))
    ax = ax.ravel()

    ax[0].plot(series1.index, series1, color=COLORS[0], alpha=0.5, label=series1.name)
    fig.autofmt_xdate()

    ax[0].xaxis.set_major_locator(mdates.WeekdayLocator(interval=4))
    ax[0].xaxis.set_major_formatter(DateFormatter("%m-%d"))
    if titles is not None and len(titles) == 2:
        ax[0].set_title(titles[0])
    ax[0].grid(True)

    labels = [a.name for a in args]
    for i, s in enumerate(args):
        ax[1].plot(s.index, s, color=COLORS[(i+1 % len(COLORS))], alpha=0.5, label=labels[i])

    ax[1].xaxis.set_major_locator(mdates.WeekdayLocator(interval=4))
    ax[1].xaxis.set_major_formatter(DateFormatter("%m-%d"))
    if titles is not None and len(titles) == 2:
        ax[1].set_title(titles[1])

    ax[1].grid(True)

    plt.legend()
    plt.tight_layout()
    plt.show()
