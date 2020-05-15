from sys import argv
hours, rate = argv[1:]

print(f'Заработная плата за месяц составила {int(hours) * int(rate) + 0.15 * (int(hours) * int(rate))} руб., '
      f'включая премию в размере {0.15 * (int(hours) * int(rate))} руб.')