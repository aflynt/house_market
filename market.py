#!/home/aflynt/anaconda3/bin/python
from datetime import date
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
from dateutil.rrule import rrule, WEEKLY, WE
import sys
import statistics as stat

import csv
import matplotlib.pyplot as plt
import numpy as np
plt.rc('text')

csv.register_dialect(\
    'mydialect', delimiter = ',',quotechar = '"', doublequote = True, \
    skipinitialspace = True, lineterminator = '\n' )

houses = [[85, 423],
[117,   1600] ,
[119.9, 1199] ,
[124.5, 1152] ,
[132.5, 1008] ,
[134.9, 1506] ,
[138,   1119] ,
[139.9, 1568] ,
[140,   1072] ,
[149,   1500] ,
[149.9, 2128] ,
[154.9, 1485] ,
[164.9, 1694] ,
[169.9, 1760] ,
[178.0, 1976] ,
[180,   1820] ,
[184.9, 1636] ,
[186.7, 1312] ,
[188.5, 1520] ,
[190,   1591] ,
[197.9, 1880] ,
[199.9, 1376] ,
[199.9, 2029] ,
[199.9, 1620] ,
[199.9, 2643] ,
[203.5, 1376] ,
[204.9, 1500] ,
[205,   1970] ,
[209.9, 1440] ,
[212.9, 1601] ,
[214.9, 1675] ,
[227.9, 2268] ,
[227.9, 2074] ,
[227.9, 1809] ,
[228.9, 1753] ,
[228.9, 1750] ,
[229,   1743] ,
[230,   1980] ,
[230,   1845] ,
[230,   1700] ,
[231,   1526] ,
[242,   2019] ,
[245,   1843] ,
[248,   2036] ,
[250,   2555] ,
[250,   2169] ,
[250,   2141] ,
[250,   2380] ,
[260,   2050] ,
[260,   1945] ,
[265,   2111] ,
[266,   2027] ,
[268,   2136] ,
[269,   2075] ,
[270,   2160] ,
[270,   2104] ,
[271,   2067] ,
[275,   2089] ,
[278,   2057] ,
[280,   2219] ,
[280,   2183] ,
[285,   2342] ,
[286,   2168] ,
[290,   2900] ,
[300,   2324] ,
[300,   3041] ,
[300,   2126] ,
[300,   2249] ,
[300,   2400] ,
[300,   2300] ,
[307,   2270] ,
[310,   2959] ,
[315,   2420] ,
[319,   3161] ,
[329,   2490] ,
[350,   3456] ,
[360,   3238] ,
[370,   3470] ,
[370,   2010] ,
[380,   2695] ,
[393,   2368] ,
[395,   3920] ,
[400,   3178] ,
[450,   3363] ,
[510,   4225] ,
[580,   5074]]

def getVar(inlist, num):
    sublist = []
    for x in inlist:
        sublist.append(int(x[num]))
    return sublist

def ppsf(hp, ha):
    # return ppsf give home price and area
    pp = []
    for p,a in zip(hp,ha):
        pp.append(p/a)
    return pp


hp = getVar(houses,0)
ha = getVar(houses,1)

# scale up home price
for i in range(len(hp)):
    hp[i] *= 1000

#print(h0)
#print(h1)

pp = ppsf(hp, ha)

pmean  = stat.mean(pp)
pstdev = stat.stdev(pp)

print("PPSF average = {:6.2f}, stdev =\
        {:6.2f}".format(pmean,pstdev))

ma0 = 3744
ma1 = 3744
mp0 = 320

ma = [3744, 3744]
mp = [320000, 430000]
mpp = [320000/ma[0], 430000/ma[1]]

print(mpp)

#############################
### 3-day average dailies ###
#############################
plt.plot(ma,mpp,"m-",label="ours")
plt.plot(ha,pp,"k*",label="market")
plt.xlim(0, 5500)
#plt.xticks(np.arange(-35,7,7))
plt.xlabel('Home Size (ft^2)')
plt.ylabel('Home Price/sqft ($/ft^2)')
plt.title('Home Price vs Square Footage')
plt.legend(loc='upper left')
plt.grid(True)
plt.show()

