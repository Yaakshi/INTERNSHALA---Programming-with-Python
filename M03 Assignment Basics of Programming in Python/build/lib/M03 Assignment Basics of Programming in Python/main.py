#main

import functions

p1={'name':'Virat Kohli','role':'bat','runs':112,'4':10,'6':0,'balls':119,'field':0}
p2={'name':'du Plessis','role':'bat','runs':120,'4':11,'6':2,'balls':112,'field':0}
p3={'name':'Bhuvneshwar Kumar','role':'bowl','wkts':1,'overs':10,'runs':71,'field':1}
p4={'name':'Yuzvendra Chahal','role':'bowl','wkts':2,'overs':10,'runs':45,'field':0}
p5={'name':'Kuldeep Yadav','role':'bowl','wkts':3,'overs':10,'runs':34,'field':0}

plist=[p1,p2,p3,p4,p5]

scoreboard={}

for p in plist:
    if p['role']=='bat':
        score=functions.batting(p)
        scoreboard[p['name']]=score
        print("'name':{},'batscore':{}".format(p['name'],score))
    else:
        score=functions.bowling(p)
        scoreboard[p['name']]=score
        print("'name':{},'bowlscore':{}".format(p['name'],score))

top_player=max(scoreboard,key=scoreboard.get)

print("The top player is {} with a score of {}".format(top_player,max(scoreboard.values())))
