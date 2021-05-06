import random
from itertools import islice
import os
import discord



if not os.path.isdir("Роли"):
     os.mkdir("Роли")

if not os.path.isdir("Бункер"):
     os.mkdir("Бункер")

#coding: "utf-8"


player_count = 1

a = 29
b = 9
bb = 1
c = 29
cc = 9
d = 53
e = 29
f = 29
g = 34
h = 29
i = 24
j = 24
k = 24




while player_count < 11 :
    

    r_bio = random.randint(0,a)
    r_fertility = random.randint(0,b)
    r_body = random.randint(0,bb)
    r_health = random.randint(0,c)
    r_stage = random.randint(0,cc)
    r_job = random.randint(0,d)
    r_hobby = random.randint(0,e)
    r_phobia = random.randint(0,f)
    r_extra_info = random.randint(0,g)
    r_charact = random.randint(0,h)
    r_baggage = random.randint(0,i)
    r_card1 = random.randint(0,j)
    r_card2 = random.randint(0,k)
    


    bf = open("BIO.txt", 'rt', encoding="utf-8")
    lines_b = bf.readlines()
    bioo = (lines_b[r_bio])
    bf.close
    bf = open("BIO.txt", 'w', encoding="utf-8")
    for line in lines_b:
        if line!= (lines_b[r_bio]):
            bf.write(line)
    bf.close
    bf = open("BIO.txt", 'rt', encoding="utf-8")
    linesss = bf.readlines()
    linesss = linesss[:-1]
    player_stats = open (("Роли/player {0}.txt").format(player_count),"a")
    player_stats.write (bioo)
    a-=1
    player_stats.close



    ff = open("FERTILITY.txt", 'rt', encoding="utf-8")
    lines_f = ff.readlines()
    fert = (lines_f[r_fertility])
    ff.close
    ff = open("FERTILITY.txt", 'w', encoding="utf-8")
    for line in lines_f:
        if line!= (lines_f[r_fertility]):
            ff.write(line)
    ff.close
    ff = open("FERTILITY.txt", 'rt', encoding="utf-8")
    linesss = ff.readlines()
    linesss = linesss[:-1]
    player_stats = open (("Роли/player {0}.txt").format(player_count),"a")
    player_stats.write (fert)
    b-=1
    player_stats.close

    

    player_stats = open (("Роли/player {0}.txt").format(player_count),"a")
    player_stats.write ("--------------------------\n")
    player_stats.close



    hef = open("HEALTH.txt", 'rt', encoding="utf-8")
    lines_he = hef.readlines()
    heal = (lines_he[r_health])
    hef.close
    hef = open("HEALTH.txt", 'w', encoding="utf-8")
    for line in lines_he:
        if line!= (lines_he[r_health]):
            hef.write(line)
    hef.close
    hef = open("HEALTH.txt", 'rt', encoding="utf-8")
    linesss = hef.readlines()
    linesss = linesss[:-1]
    player_stats = open (("Роли/player {0}.txt").format(player_count),"a")
    player_stats.write (heal[:-2])
    c-=1
    player_stats.close



    sf = open("STAGE.txt", 'rt', encoding="utf-8")
    lines_s = sf.readlines()
    stag = (lines_s[r_stage])
    player_stats = open (("Роли/player {0}.txt").format(player_count),"a")
    player_stats.write (stag)
    cc-=1
    player_stats.close



    jf = open("JOB.txt", 'rt', encoding="utf-8")
    lines_j = jf.readlines()
    jobb = (lines_j[r_job])
    jf.close
    jf = open("JOB.txt", 'w', encoding="utf-8")
    for line in lines_j:
        if line!= (lines_j[r_job]):
            jf.write(line)
    jf.close
    jf = open("JOB.txt", 'rt', encoding="utf-8")
    linesss = jf.readlines()
    linesss = linesss[:-1]
    player_stats = open (("Роли/player {0}.txt").format(player_count),"a")
    player_stats.write (jobb)
    d -= 1
    player_stats.close



    hof = open("HOBBY.txt", 'rt', encoding="utf-8")
    lines_ho = hof.readlines()  
    hobb = (lines_ho[r_hobby])
    hof.close
    hof = open("HOBBY.txt", 'w', encoding="utf-8")
    for line in lines_ho:
        if line!= (lines_ho[r_hobby]):
            hof.write(line)
    hof.close
    hof = open("HOBBY.txt", 'rt', encoding="utf-8")
    linesss = hof.readlines()
    linesss = linesss[:-1]
    player_stats = open (("Роли/player {0}.txt").format(player_count),"a")
    player_stats.write (hobb)
    e -= 1
    player_stats.close



    pf = open("PHOBIA.txt", 'rt', encoding="utf-8")
    lines_p = pf.readlines()
    phob = (lines_p[r_phobia])
    pf.close
    pf = open("PHOBIA.txt", 'w', encoding="utf-8")
    for line in lines_p:
        if line!= (lines_p[r_phobia]):
            pf.write(line)
    pf.close
    pf = open("PHOBIA.txt", 'rt', encoding="utf-8")
    linesss = pf.readlines()
    linesss = linesss[:-1]
    player_stats = open (("Роли/player {0}.txt").format(player_count),"a")
    player_stats.write (phob)
    f -= 1
    player_stats.close



    ef = open("EXTRA INFO.txt", 'rt', encoding="utf-8")
    lines_e = ef.readlines()
    extr = (lines_e[r_extra_info])
    ef.close
    ef = open("EXTRA INFO.txt", 'w', encoding="utf-8")
    for line in lines_e:
        if line!= (lines_e[r_extra_info]):
            ef.write(line)
    ef.close
    ef = open("EXTRA INFO.txt", 'rt', encoding="utf-8")
    linesss = ef.readlines()
    linesss = linesss[:-1]
    player_stats = open (("Роли/player {0}.txt").format(player_count),"a")
    player_stats.write (extr)
    g -= 1
    player_stats.close



    chf = open("CHARACT.txt", 'rt', encoding="utf-8")
    lines_ch = chf.readlines()    
    char = (lines_ch[r_charact])
    chf.close
    chf = open("CHARACT.txt", 'w', encoding="utf-8")
    for line in lines_ch:
        if line!= (lines_ch[r_charact]):
            chf.write(line)
    chf.close
    chf = open("CHARACT.txt", 'rt', encoding="utf-8")
    linesss = chf.readlines()
    linesss = linesss[:-1]
    player_stats = open (("Роли/player {0}.txt").format(player_count),"a")
    player_stats.write(char)
    h -= 1
    player_stats.close



    baf = open("BAGGAGE.txt", 'rt', encoding="utf-8")
    lines_ba = baf.readlines()    
    bagg = (lines_ba[r_baggage])
    baf.close
    baf = open("BAGGAGE.txt", 'w', encoding="utf-8")
    for line in lines_ba:
        if line!= (lines_ba[r_baggage]):
            baf.write(line)
    baf.close
    baf = open("BAGGAGE.txt", 'rt', encoding="utf-8")
    linesss = baf.readlines()
    linesss = linesss[:-1]
    player_stats = open (("Роли/player {0}.txt").format(player_count),"a")
    player_stats.write(bagg)
    i -= 1
    player_stats.close
    


    c1f = open("CARD1.txt", 'rt', encoding="utf-8")
    lines_c1 = c1f.readlines()    
    car1 = (lines_c1[r_card1])
    c1f.close
    c1f = open("CARD1.txt", 'w', encoding="utf-8")
    for line in lines_c1:
        if line!= (lines_c1[r_card1]):
            c1f.write(line)
    c1f.close
    c1f = open("CARD1.txt", 'rt', encoding="utf-8")
    linesss = c1f.readlines()
    linesss = linesss[:-1]
    player_stats = open (("Роли/player {0}.txt").format(player_count),"a")
    player_stats.write(car1)
    j -= 1
    player_stats.close



    c2f = open("CARD2.txt", 'rt', encoding="utf-8")
    lines_c2 = c2f.readlines()    
    car2 = (lines_c2[r_card2])
    c2f.close
    c2f = open("CARD2.txt", 'w', encoding="utf-8")
    for line in lines_c2:
        if line!= (lines_c2[r_card2]):
            c2f.write(line)
    c2f.close
    c2f = open("CARD2.txt", 'rt', encoding="utf-8")
    linesss = c2f.readlines()
    linesss = linesss[:-1]
    player_stats = open (("Роли/player {0}.txt").format(player_count),"a")
    player_stats.write(car2)
    k -= 1
    player_stats.close





    #print (lines_ba)
    #print (len(lines_stats_ba))
    #print (baggage_count)
    player_count += 1


l = 9
m = 6
n = 7
o = 3
p = 8
ItEm1 = 0
ItEm3 = 0

r_square = random.randint(0,l)
r_time = random.randint(0,m)
r_item1 = random.randint(0,n)
r_item2 = random.randint(0,o)
r_item3 = random.randint(0,p)


sqf = open("SQUARE.txt", 'rt', encoding="utf-8")
lines_sq = sqf.readlines()
squa = (lines_sq[r_square])
sqf.close
sqf = open("SQUARE.txt", 'w', encoding="utf-8")
for line in lines_sq:
    if line!= (lines_sq[r_square]):
        sqf.write(line)
sqf.close
sqf = open("SQUARE.txt", 'rt', encoding="utf-8")
linesss = sqf.readlines()
linesss = linesss[:-1]
bunker_stats = open ("Бункер/bunker.txt","a")
bunker_stats.write (squa)
bunker_stats.close



tif = open("TIME.txt", 'rt', encoding="utf-8")
lines_ti = tif.readlines()
time = (lines_ti[r_time])
tif.close
tif = open("TIME.txt", 'w', encoding="utf-8")
for line in lines_ti:
    if line!= (lines_ti[r_time]):
        tif.write(line)
tif.close
tif = open("TIME.txt", 'rt', encoding="utf-8")
linesss = tif.readlines()
linesss = linesss[:-1]
bunker_stats = open ("Бункер/bunker.txt","a")
bunker_stats.write (time)
bunker_stats.close


while ItEm1 < 2:
    i1f = open("ITEM1.txt", 'rt', encoding="utf-8")
    lines_i1 = i1f.readlines()
    ite1 = (lines_i1[r_item1])
    i1f.close
    i1f = open("ITEM1.txt", 'w', encoding="utf-8")
    for line in lines_i1:
        if line!= (lines_i1[r_item1]):
            i1f.write(line)
    i1f.close
    i1f = open("ITEM1.txt", 'rt', encoding="utf-8")
    linesss = i1f.readlines()
    linesss = linesss[:-1]
    bunker_stats = open ("Бункер/bunker.txt","a")
    bunker_stats.write (ite1)
    bunker_stats.close

    ItEm1 +=1



i2f = open("ITEM2.txt", 'rt', encoding="utf-8")
lines_i2 = i2f.readlines()
ite2 = (lines_i2[r_item2])
i2f.close
i2f = open("ITEM2.txt", 'w', encoding="utf-8")
for line in lines_i2:
    if line!= (lines_i2[r_item2]):
        i2f.write(line)
i2f.close
i2f = open("ITEM2.txt", 'rt', encoding="utf-8")
linesss = i2f.readlines()
linesss = linesss[:-1]
bunker_stats = open ("Бункер/bunker.txt","a")
bunker_stats.write (ite2)
bunker_stats.close



while ItEm3 < 2:
    i3f = open("ITEM3.txt", 'rt', encoding="utf-8")
    lines_i3 = i3f.readlines()
    ite3 = (lines_i3[r_item3])
    i3f.close
    i3f = open("ITEM3.txt", 'w', encoding="utf-8")
    for line in lines_i3:
        if line!= (lines_i3[r_item3]):
            i3f.write(line)
    i3f.close
    i3f = open("ITEM3.txt", 'rt', encoding="utf-8")
    linesss = i3f.readlines()
    linesss = linesss[:-1]
    bunker_stats = open ("Бункер/bunker.txt","a")
    bunker_stats.write (ite3)
    bunker_stats.close

    ItEm3 +=1
#print (lines_f)
#print (lines_stats_ba)

