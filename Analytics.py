import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from Extract_BQ import *


def analytic_1_use_rate():
    id, rate = BQ_GET_A1_USERATE()

    x_pos = np.arange(len(id))
    plt.bar(x_pos, rate, align='center', alpha=0.5)
    plt.xticks(x_pos, id, size=8)
    plt.ylabel('USE_RATE')
    plt.title('Use rate of seven stealth heroes')
    plt.draw()
    plt.show()

def analytic_1_ban_rate():
    id, rate, avg = BQ_GET_A1_BANRATE()

    x_pos = np.arange(len(id))
    plt.bar(x_pos, rate, align='center', alpha=0.5)
    plt.xticks(x_pos, id)
    plt.ylabel('BAN_RATE')
    plt.title('Ban rate of seven stealth heroes')
    plt.axhline(y=avg, color="red")
    plt.draw()
    plt.show()

def analytic_1_good_data():
    id, val = BQ_GET_A1_GOODDATA()

    x_pos = np.arange(len(id))
    plt.bar(x_pos, val, align='center', alpha=0.5)
    plt.xticks(x_pos, id, size=8)
    plt.ylabel('FIRST_VAL')
    plt.title('First val of seven stealth heroes')
    plt.draw()
    plt.show()

def analytic_1_opponent_headache():
    id, val = BQ_GET_A1_OPPNENTHEADACHE()

    x_pos = np.arange(len(id))
    plt.bar(x_pos, val, align='center', alpha=0.5)
    plt.xticks(x_pos, id, size=8)
    plt.ylabel('SECOND_VAL')
    plt.title('Second val of seven stealth heroes')
    plt.draw()
    plt.show()

def analytic_2_rate_value():
    name, rate, face = BQ_GET_USERATEANDFACEVALUE()
    x_pos = np.arange(len(name))
    plt.plot(x_pos, rate, 'bo-' ,label = 'use_rate')
    plt.plot(x_pos, face, 'y.--', label = 'face_value')
    plt.title('USE_RATE & FACE_VALUE')
    # plt.xlabel('hero_name')
    plt.ylabel('value')
    plt.legend()
    plt.draw()
    plt.show()

def analytic_3_rate_bfury():
    dis = BQ_GET_DISTRIBUTION_BFURY()
    plt.figure(figsize=(5, 5))
    plt.title('Buy bfury distribution')
    labels = 'With Bfury', 'Without Bfury'
    colors = ['dodgerblue', 'lime']
    plt.pie(dis, labels=labels, colors = colors,autopct='%1.1f%%')
    plt.legend()
    plt.show()
    # pie chat
    # plt.figure(figsize=(5, 5))
    # plt.title('Game time distribution')
    # labels = '(16:40, 27:20]', '(27:20, 38:00]', '(38:00, 48:40]', '(48:40, 59:20]', '(59:20, 70:00]'
    # # colors = ['']
    # plt.pie(count, labels=labels, autopct='%1.1f%%')
    # plt.show()

def analytic_3_winrate_bfury():
    rate = BQ_GET_WIN_RATE_BFURY()
    x_x = ['With Bfury', 'Without Bfury']
    x_pos = np.arange(len(x_x))
    plt.bar(x_pos, rate, align='center', alpha=0.5)
    plt.xticks(x_pos, x_x, size=8)
    plt.ylabel('WIN_RATE')
    plt.title('WIN_RATE With Bfury & Without Bfury')
    for a ,b in zip(x_pos, rate):
        plt.text(a, b+0.05, '%.2f' %b,ha='center', va= 'bottom',fontsize=7)
    plt.legend()
    plt.draw()
    plt.show()

def analytic_3_time_withbfury():
    time, avg = BQ_GET_TIME_WITHBFURY()
    object = ['(16:40, 27:20]', '(27:20, 38:00]', '(38:00, 48:40]', '(48:40, 59:20]', '(59:20, 70:00]']
    x_pos = np.arange(len(object))
    plt.bar(x_pos, time, align='center', alpha=0.5)
    plt.xticks(x_pos, object, size=6)
    plt.ylabel('MATCH_COUNT')
    plt.title('Time distribution with bfury')
    for a ,b in zip(x_pos, time):
        plt.text(a, b+0.05, '%.2f' %(b * 100 / np.sum(time)),ha='center', va= 'bottom',fontsize=7)
    plt.text(3, 20000, 'avg = %.2f' % avg, fontsize=12)
    plt.show()

    plt.show()

def analytic_3_time_withoutbfury():
    time, avg = BQ_GET_TIME_WITHOUTBFURY()
    object = ['(16:40, 27:20]', '(27:20, 38:00]', '(38:00, 48:40]', '(48:40, 59:20]', '(59:20, 70:00]']
    x_pos = np.arange(len(object))
    plt.bar(x_pos, time, align='center', alpha=0.5)
    # plt.axhline(y=avg, color="red")
    plt.xticks(x_pos, object, size=6)
    plt.ylabel('MATCH_COUNT')
    plt.title('Time distribution without bfury')
    for a ,b in zip(x_pos, time):
        plt.text(a, b+0.05, '%.2f' %(b * 100 / np.sum(time)),ha='center', va= 'bottom',fontsize=7)
    plt.text(3, 1200, 'avg = %.2f'%avg, fontsize = 12)
    plt.show()

def analytic_3_minute():
    minute, all, win = BQ_GET_MINUTE()
    win_rate = []
    for i in range(len(all)):
        win_rate.append(round(win[i] * 100 / all[i], 2))

    x_pos = np.arange(len(minute))
    plt.plot(x_pos, win_rate, 'y', label='win_rate')
    plt.xticks(x_pos, minute, size=6)
    plt.xlabel('minute')
    plt.ylabel('win rate')
    plt.title('Purchase time & win_rate')
    plt.legend()
    plt.draw()
    plt.show()
    # lose = []
    # for i in range(len(all)):
    #     lose.append(all[i] - win[i])
    #
    # x_pos = np.arange(len(minute))
    # width = 0.35
    # # fig, ax = plt.subplots()
    # rects1 = plt.bar(x_pos - width/2, win, width, label='win')
    # rects1 = plt.bar(x_pos + width/2, lose, width, label='lose')
    # plt.ylabel('number')
    # plt.xlabel('miute')
    # plt.xticks(x_pos, minute, size=6)
    # plt.title('number of win & lose in minute')
    # for a, b in zip(x_pos, win):
    #     plt.text(a-width/2, b+0.05, '%.f' %b,ha='center', va= 'bottom',fontsize=7 )
    # for a, b in zip(x_pos, lose):
    #     plt.text(a + width / 2, b + 0.05, '%.f' % b, ha='center', va='bottom', fontsize=7)
    # plt.legend()
    # plt.show()





def analytic_3_team():
    gold, xp = BQ_GET_TEAM()
    g = []
    x = []
    count = 0
    for i in gold.keys():
        g = gold[i]
        count += 1
        if (count == 6):
            break
    count = 0
    for i in xp.keys():
        x = xp[i]
        count += 1
        if (count == 6):
            break
    # g = gold.values()[0]
    # x = xp.values()[0]
    x_pos = np.arange(len(g))

    plt.title("Economy & Experience Curve(Forward for Radiant)")

    # plt.xlabel('competing time')
    plt.plot(x_pos, g, 'y', label='Economic')
    plt.plot(x_pos, x, 'g', label='Experience')

    # my_x_ticks = np.arange(-4, 55, 4)
    plt.xticks(x_pos)

    plt.legend()
    plt.grid()
    plt.draw()
    plt.show()

def analytic_3_team_curve():
    gold, xp = BQ_GET_TEAM()
    g = []
    x = []
    for i in gold.keys():
        if len(gold[i]) > 15:
            g_c = round((gold[i][14] - gold[i][5]) / 10 , 2)
            x_c = round((xp[i][14] - xp[i][5]) / 10 , 2)
            g.append(g_c)
            x.append(x_c)

    y_g = [0, 0]
    y_x = [0, 0]
    for t in g:
        if t > 0:
            y_g[0] += 1
        else:
            y_g[1] += 1

    for t in x:
        if t > 0:
            y_x[0] += 1
        else:
            y_x[1] += 1

    width = 0.35
    x_pos = np.arange(1)
    # fig, ax = plt.subplots()
    rects1 = plt.bar(x_pos - width/2, y_g, width, label='Positive')
    rects1 = plt.bar(x_pos + width/2, y_x, width, label='Negative')
    plt.ylabel('count')
    # plt.xlabel('miute')
    # plt.xticks(x_pos, minute, size=6)
    plt.title('number of Postive curve & Negative curve')
    for a, b in zip(x_pos, y_g):
        plt.text(a-width/2, b+0.05, '%.f' %b,ha='center', va= 'bottom',fontsize=7 )
    for a, b in zip(x_pos, y_x):
        plt.text(a + width / 2, b + 0.05, '%.f' % b, ha='center', va='bottom', fontsize=7)
    plt.legend()
    plt.show()

    # sub  = (max(g_c) - min(g_c)) / 5
    # y_g = [0, 0, 0, 0, 0]
    # for temp in g_c:
    #     if temp <= min(g_c) + sub:
    #         y_g[0] += 1
    #     elif min(g_c) + sub < temp <= min(g_c) + 2*sub:
    #         y_g[1] += 1
    #     elif min(g_c) + 2*sub < temp <= min(g_c) + 3*sub:
    #         y_g[2] += 1
    #     elif min(g_c) + 3*sub < temp <= min(g_c) + 4*sub:
    #         y_g[3] += 1
    #     elif min(g_c) + 4*sub < temp <= min(g_c) + 5*sub:
    #         y_g[4] += 1


def analytic_3_equip():
    items, val = BQ_GET_EQUIP()
    x_pos = np.arange(len(items))

    plt.bar(x_pos, val, align='center', alpha=0.5)
    plt.xticks(x_pos, items)
    plt.title("Top 10 equipment purchased(AM)")
    plt.xlabel('item_name')
    plt.ylabel('numbers')
    plt.legend()
    plt.show()

def analytic_4_effect():
    id, gold, xp, radiant = BQ_GET_EFFECT()
    count = [0, 0, 0, 0]
    win = [0, 0, 0, 0]
    lose = []
    for i in range(len(id)):
        # + +
        if gold[i] >= 0 and xp[i] >= 0:
            count[0] += 1
            if radiant[i] is True:
                win[0] += 1
        # + -
        elif gold[i] >= 0 and xp[i] < 0:
            count[1] += 1
            if radiant[i] is True:
                win[1] += 1
        # - -
        elif gold[i] < 0 and xp[i] < 0:
            count[2] += 1
            if radiant[i] is True:
                win[2] += 1
        else:
            count[3] += 1
            if radiant[i] is True:
                win[3] += 1
    for i in range(len(count)):
        lose.append(count[i] - win[i])

    x_pos = np.arange(len(count))
    xlabel = ['+/+', '+/-', '-/-', '-/+']
    width = 0.35
    rects1 = plt.bar(x_pos - width/2, win, width, label='win')
    rects1 = plt.bar(x_pos + width/2, lose, width, label='lose')
    plt.ylabel('number')
    plt.xticks(x_pos, xlabel, size=6)
    for a, b in zip(x_pos, win):
        plt.text(a-width/2, b+0.05, '%.f' %b,ha='center', va= 'bottom',fontsize=7 )
    for a, b in zip(x_pos, lose):
        plt.text(a + width / 2, b + 0.05, '%.f' % b, ha='center', va='bottom', fontsize=7)
    plt.legend()
    plt.show()


def analytic_4_count():
    count = BQ_GET_COUNT()
    win = [0, 0, 0, 0]
    lose = [0, 0, 0, 0]
    win[0] = count['pp+']
    lose[0] = count['pp-']
    win[1] = count['pn+']
    lose[1] = count['pn-']
    win[2] = count['nn+']
    lose[2] = count['nn-']
    win[3] = count['np+']
    lose[3] = count['np-']
    x_pos = np.arange(len(win))
    xlabel = ['+/+', '+/-', '-/-', '-/+']
    width = 0.35
    rects1 = plt.bar(x_pos - width / 2, win, width, label='win')
    rects1 = plt.bar(x_pos + width / 2, lose, width, label='lose')
    plt.ylabel('number')
    plt.xticks(x_pos, xlabel, size=6)
    for a, b in zip(x_pos, win):
        plt.text(a - width / 2, b + 0.05, '%.f' % b, ha='center', va='bottom', fontsize=7)
    for a, b in zip(x_pos, lose):
        plt.text(a + width / 2, b + 0.05, '%.f' % b, ha='center', va='bottom', fontsize=7)
    plt.legend()
    plt.show()

def analytic_4_gold():
    lose = BQ_GET_GOLD()
    xlabels = ['0~5k', '5k~10k', '10k~15k', '15k~20k', '>20k']
    lost = [0, 0, 0, 0, 0]
    lost[0] = lose[1]
    lost[1] = lose[2]
    lost[2] = lose[3]
    lost[3] = lose[4]
    lost[4] = lose[5]

    x_pos = np.arange(len(lost))
    plt.bar(x_pos, lost, align='center', alpha=0.5)
    plt.xticks(x_pos, xlabels, size=6)
    plt.title('Distribution of economic gap')
    for a, b in zip(x_pos, lost):
        plt.text(a,  b + 0.05, '%.f' % b, ha='center', va='bottom', fontsize=7)
    plt.legend()
    plt.show()

def analytic_4_xp():
    lose = BQ_GET_XP()
    xlabels = ['0~5k', '5k~10k', '10k~15k', '15k~20k', '>20k']
    lost = [0, 0, 0, 0, 0]
    lost[0] = lose[1]
    lost[1] = lose[2]
    lost[2] = lose[3]
    lost[3] = lose[4]
    lost[4] = lose[5]

    x_pos = np.arange(len(lost))
    plt.bar(x_pos, lost, align='center', alpha=0.5)
    plt.xticks(x_pos, xlabels, size=6)
    plt.title('Distribution of experience gap')
    for a, b in zip(x_pos, lost):
        plt.text(a, b + 0.05, '%.f' % b, ha='center', va='bottom', fontsize=7)
    plt.legend()
    plt.show()

def analytic_4_d():
    val = BQ_GET_D()
    xlabels = ['0~5k', '5k~10k', '10k~15k', '15k~20k', '>20k']
    v = [0, 0, 0, 0, 0]

    v[0] = val[1]
    v[1] = val[2]
    v[2] = val[3]
    v[3] = val[4]
    v[4] = val[5]

    x_pos = np.arange(len(v))
    plt.bar(x_pos, v, align='center', alpha=0.5)
    plt.xticks(x_pos, xlabels, size=6)
    plt.title('Distribution of economic gap')
    for a, b in zip(x_pos, v):
        plt.text(a, b + 0.05, '%.f' % b, ha='center', va='bottom', fontsize=7)
    plt.legend()
    plt.show()

def analytic_4_hero():
    id, val = BQ_GET_HERO()
    x_pos = np.arange(len(id))

    plt.bar(x_pos, val, align='center', alpha=0.5)
    plt.xticks(x_pos, id, size = 6)
    plt.title("Top 10 most occurrences heros(loser)")
    for a, b in zip(x_pos, val):
        plt.text(a, b + 0.05, '%.f' % b, ha='center', va='bottom', fontsize=7)
    plt.legend()
    plt.show()

def analytic_top1():
    normal, hard, veryhard = BQ_GET_TOP1()
    all = normal + hard + veryhard
    val = []
    name = ['normal', 'hard', 'veryhard']
    color = ['green', 'yellow', 'red']
    val.append(normal)
    val.append(hard)
    val.append(veryhard)
    x_pos = np.arange(3)

    plt.bar(x_pos, val, color=color, align='center', alpha=0.5)
    plt.xticks(x_pos, name, size = 6)
    plt.title('DOTA2 competition level distribution')
    for a, b in zip(x_pos, val):
        plt.text(a, b + 0.05, '%.f' % b, ha='center', va='bottom', fontsize=7)
    plt.legend()
    plt.show()

def analytic_top2():
    kill, death, assists = BQ_GET_TOP2()
    val = []
    name = ['kill', 'death', 'assists']
    color = ['red', 'black', 'green']
    val.append(kill)
    val.append(death)
    val.append(assists)
    x_pos = np.arange(3)

    plt.bar(x_pos, val, color=color, align='center', alpha=0.5)
    plt.xticks(x_pos, name, size = 6)
    plt.title('DOTA2 hero data')
    for a, b in zip(x_pos, val):
        plt.text(a, b + 0.05, '%.f' % b, ha='center', va='bottom', fontsize=7)
    plt.legend()
    plt.show()

if __name__ == '__main__':
    # analytic_1_use_rate()
    # analytic_1_ban_rate()
    # analytic_1_good_data()
    # analytic_1_opponent_headache()
    # analytic_2_rate_value()
    # analytic_3_rate_bfury()
    # analytic_3_winrate_bfury()
    # analytic_3_time_withbfury()
    # analytic_3_time_withoutbfury()
    # analytic_3_minute()
    # analytic_3_team()
    # analytic_3_team_curve()
    # analytic_3_equip()
    # analytic_4_effect()
    # analytic_4_count()
    # analytic_4_gold()
    # analytic_4_xp()
    # analytic_4_d()
    # analytic_4_hero()
    # analytic_top1()
    analytic_top2()
