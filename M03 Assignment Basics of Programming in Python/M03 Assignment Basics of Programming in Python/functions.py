#functions

def batting(player):
    runs=player['runs']
    strike_rate=runs/player['balls']
    fields=player['field']
    batscore=(10*fields if fields>=1 else 0)+(runs//2)+(5 if runs>=50 else 0)+(10 if runs>=100 else 0)+(2 if strike_rate>=80/100 and strike_rate<=1 else 0)+(4 if strike_rate>1 else 0)+(player['4'])+(player['6']*2)
    return batscore
    return {'name':player['name'],'batscore':batscore}


def bowling(player):
    wkts=player['wkts']
    eco_rate=player['runs']/player['overs']
    fields=player['field']
    bowlscore=(10*fields if fields>=1 else 0)+(wkts*10)+(5 if wkts>=3 else 0)+(10 if wkts>=5 else 0)+(4 if eco_rate>=3.5 and eco_rate<=4.5 else 0)+(7 if eco_rate>=2 and eco_rate<3.5 else 0)+(10 if eco_rate<2 else 0)
    return bowlscore
    return {'name':player['name'],'bowlscore':bowlscore}
