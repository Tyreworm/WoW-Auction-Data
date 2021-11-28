# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 18:03:20 2021

@author: 
"""

import json
import csv

target_mats=[172097,172094,172096,172089,171829,171830,171831,171832,171428,170554,168589,168586,168583,173033,173034,173035,173036,173037]
target_mat_names=["Heavy Callous Hide","Callous Hide","Heavy Desolate Leather","Desolate Leather","Solenium Ore","Oxxein Ore","Phaedrum Ore","Sinvyr Ore","Shadowghast Ingot","Vigil's Torch","Marrowroot","Rising Glory","Widowbloom","Iridescent Amberjack","Silvergill Pike","Pocked Bonefish","Spinefin Piranha","Elysian Thade"]
item_auctions=[]
target_auctions=[]

target_totals=[]
for line in target_mats:
    target_totals.append(0)

with open('14.json') as f:
  data = json.load(f)
  
auction_data=data["auctions"]

for line in auction_data:
    
    
    if "buyout" in line.keys():
        price=line["buyout"]
    else:
        price=line["unit_price"]
    
    
    item_auctions.append([line["item"]["id"],line["quantity"],price,line["time_left"]])
    
item_auctions=sorted(item_auctions,key=lambda x: (x[0],x[2]), reverse=False)    

with open('Item_auctions.csv', 'w') as f:
    write = csv.writer(f)
    write.writerows(item_auctions)
    
for line in item_auctions:
    if line[0] in target_mats:
        item_position=target_mats.index(line[0])
        line.append(target_mat_names[item_position])
        target_totals[item_position]=target_totals[item_position]+line[1]
        line.append(target_totals[item_position])
        target_auctions.append(line)


deleted_auctions=[]
for line in target_auctions:   
    item_position=target_mats.index(line[0])
    percent_check=line[5]/target_totals[item_position]
    total_percent=line[1]/target_totals[item_position]
    if percent_check>0.95 and total_percent<0.1:
        deleted_auctions.append(line)
    line.pop(5)
        
for line in deleted_auctions:
    target_auctions.remove(line)
    

with open('Target_auctions.csv', 'w') as f:
    write = csv.writer(f)
    write.writerows(target_auctions)

 

   
    


    