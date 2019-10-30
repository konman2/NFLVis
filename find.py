import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import nflgame

def add(table,key):
    if key not in table:
        table[key] = 1.0
    else:
        table[key]+=1.0
    return table


games = [] 
for y in range(2009,2019):
    for w in range(1,18):
        if(y!=2017 and (y != 2018 and w!= 17)):
            games+=nflgame.games(y,week=w)

tds={}
rest = {}
plays = nflgame.combine_plays(games)

count = 0
for p in plays:
    if p.yardline != None and p.down != 0 and p.yards_togo != 0 and p.drive.result != 'Field Goal':
        fpos = 0
        if('MIDFIELD' in str(p.yardline)):
            fpos = 50
        elif('OPP' in str(p.yardline)):
            fpos = 100-int(str(p.yardline)[4:])
        else:
            fpos = int(str(p.yardline)[4:])
        temp = (p.down,p.yards_togo,fpos)
        if p.drive.result == 'Touchdown':
            tds = add(tds,temp)
            # if temp not in tds:
            #     tds[temp] = 1.0
            # else:
            #     tds[temp]+=1.0
        rest= add(rest,temp)
        # if temp not in rest:
        #     rest[temp] = 1.0
        # else:
        #     rest[temp]+=1.0
        
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for i in rest.keys():
    if i in tds:
        # print(i,0)
        # print(i,(tds[i]/rest[i]))
        color = 'ro'
        if i[0] == 2:
            color = 'go'
        elif i[0] == 3:
            color = 'bo'
        elif i[0] == 4:
            color = 'yo'
        plt.plot([i[1]],[i[2]],[tds[i]/rest[i]*100],color)

ax.set_xlabel('Yards to go')
ax.set_ylabel('Field Position')
ax.set_zlabel('TD %')
plt.show()


ans = ''
while(ans != -1):
    ans = int(input("Enter down : "))
    ans2 = int(input("Enter distance : "))
    ans3 = int(input("Enter fpos : "))
    if ans == -1:
        break
    key = (ans,ans2,ans3)
    if key in tds:
        print(tds[key]/rest[key])
    else:
        print(0)



#for p in plays.sort('downs'):
    