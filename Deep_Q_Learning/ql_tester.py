from q_learning import Q_Learning
from numpy import genfromtxt
import os
import csv

q_table = genfromtxt(
    f"runs/{sorted(os.listdir('runs'), reverse=True)[0]}", delimiter=',')
ql = Q_Learning(q_table=q_table)
for i in range(100):
    ql.test()
