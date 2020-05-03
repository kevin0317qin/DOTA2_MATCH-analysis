import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from Extract_BQ import *
from PIL import Image

def time_distribution():
    df = pd.read_csv("Resources/DOTA_MATCHES.csv", usecols=[2])
    count = [0, 0, 0, 0, 0]
    for index, row in df.iterrows():
        if row['duration'] > 1000 and row['duration'] <= 1640:
            count[0] += 1
        elif row['duration'] > 1640 and row['duration'] <= 2280:
            count[1] += 1
        elif row['duration'] > 2280 and row['duration'] <= 2920:
            count[2] += 1
        elif row['duration'] > 2920 and row['duration'] <= 3560:
            count[3] += 1
        elif row['duration'] > 3560 and row['duration'] <= 4200:
            count[4] += 1

    # pie chat
    # plt.figure(figsize=(5, 5))
    # plt.title('Game time distribution')
    # labels = '(16:40, 27:20]', '(27:20, 38:00]', '(38:00, 48:40]', '(48:40, 59:20]', '(59:20, 70:00]'
    # # colors = ['']
    # plt.pie(count, labels=labels, autopct='%1.1f%%')
    # plt.show()

    # histogram
    plt.figure(figsize=(7, 7))
    object = ['(16:40, 27:20]', '(27:20, 38:00]', '(38:00, 48:40]', '(48:40, 59:20]', '(59:20, 70:00]']
    x_pos = np.arange(len(object))
    plt.bar(x_pos, count, align='center', alpha=0.5)
    plt.xticks(x_pos, object, )
    plt.ylabel("Time Duration")
    plt.title("Time distribution")
    plt.draw()
    plt.show()


def win_distribution():

    object, rate, avg = BQ_GET_WINRATE()

    x_pos = np.arange(len(object))
    # plt.imshow(img, )
    plt.bar(x_pos, rate, align='center', alpha=0.5)
    plt.xticks(x_pos, object)
    plt.ylabel('WIN_RATE')
    plt.title('Win rate of top five and bottom five')
    plt.axhline(y=avg, color="red")
    plt.draw()
    plt.show()

def win_distribution_30():
    object, rate, avg = BQ_GET_WINRATE_TOP30()
    plt.figure(figsize=(7, 7))
    plt.barh(object[::-1], rate[::-1], height=0.7, color='steelblue', alpha=0.8)
    plt.title("Win rate of top 15 and bottom 15")
    plt.ylabel('WIN_RATE')
    plt.draw()
    plt.show()


def use_distribution():
    object, rate, avg = BQ_GET_USERATE()

    x_pos = np.arange(len(object))

    plt.bar(x_pos, rate, align='center', alpha=0.5)
    # plt.text(object, linespacing=1)
    plt.xticks(x_pos, object, size=8)
    plt.ylabel('USE_RATE')
    plt.title('Use rate of top five and bottom five')
    plt.axhline(y=avg, color="red")
    plt.text(4.8, 11, "avg rate")
    plt.draw()
    plt.show()

def use_distribution_30():
    object, rate, avg = BQ_GET_USERATE()

    plt.figure(figsize=(7, 7))
    plt.barh(object[::-1], rate[::-1], height=0.7, color='steelblue', alpha=0.8)
    plt.title("Use rate of top 15 and bottom 15")
    plt.ylabel('USE_RATE')
    plt.draw()
    plt.show()


def match_advantages():
    minute, gold, xp = BQ_GET_ADVANTAGES()

    # minute = np.array(minute)
    # gold = np.array(gold)
    # xp = np.array(xp)
    plt.title("Economy & Experience Curve(Forward for Radiant)")

    plt.xlabel('competing time')
    plt.plot(minute, gold, 'y', label='Economic')
    plt.plot(minute, xp, 'g', label='Experience')

    my_x_ticks = np.arange(-4, 55, 4)
    plt.xticks(my_x_ticks)

    plt.legend()
    plt.grid()
    plt.draw()
    plt.show()


if __name__ == '__main__':
    # time_distribution()
    # win_distribution()
    # win_distribution_30()
    # use_distribution()
    use_distribution_30()
    # match_advantages()