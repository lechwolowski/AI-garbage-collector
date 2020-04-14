from q_learning import Q_Learning
from numpy import genfromtxt
import os
import csv
import numpy as np

q_table = genfromtxt(
    f"runs/{sorted(os.listdir('runs'), reverse=True)[0]}", delimiter=',')
# ql = Q_Learning(q_table=q_table)
ql = Q_Learning()
ql.run(epochs=10000, epsilon=0.7, epsilon_step=0.00006, gamma=0.7)
# ql.test()
