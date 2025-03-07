import sub1.sub2.importowany
sub1.sub2.importowany.f1()
import sub1.sub2.importowany as importowany
importowany.f1()
from sub1.sub2.importowany import f1, STALA
f1()
print(STALA)

import math
math.sqrt(9)
import math as m
m.sqrt(9)
from math import sqrt
sqrt(9)
import datetime as dt
dt.date.today()

# tak nigdy !!!
# ryzyko napisania się nazw
from urllib import *
from requests import *
