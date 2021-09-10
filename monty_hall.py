# Monty Hall problem
# 'type: console program' 
# Copyright notice: This code is Open Source and should remain so.
import math
import sys
import random
print("Pre ukončenie programu stlač 0")
# enter numbers in the console.
def get_input():
    while True:
        try:
            input_string=sys.stdin.readline()
            number_int=int(input_string)
        except Exception:
            print("Zadaj prosím iba celočíselné hodnoty")
            continue
        break
    return number_int

#  function Monty hall
def monty_hall(velkost):
    #  defining the necessary constants.    
    field=[]    
    n_celkom=0; moderator=0; car=0; first=0; second=0
    for j in range(1,velkost+1):
        car=random.randint(1,3)            
        first=random.randint(1,3)
        if car==1: moderator=random.randint(2,3)
        if car==2:
            zoznam=[1,3] 
            moderator=random.choice(zoznam)
        if car==3: moderator=random.randint(1,2)            
        if first==moderator:
            if first==1: second=random.randint(2,3)
            if first==2:                    
                second=random.choice(zoznam)
            if first==3: second=random.randint(1,2)
        if first!=moderator:
            if first==1 and moderator==2: second=3
            if first==1 and moderator==3: second=2
            if first==2 and moderator==1: second=3
            if first==2 and moderator==3: second=1
            if first==3 and moderator==1: second=2
            if first==3 and moderator==2: second=1
        if second==car: n_celkom+=1
        volume=round((n_celkom/velkost)*100,2)
    print(volume)
    return volume        

# Infinite while loop console. Main program
while True:
    print("Zadaj počet hier")
    velkost=get_input()   
    # end of program (0)   
    if velkost == 0:
        break
    print("Výsledky pokusov v %:")
    # call monty hall function
    monty_hall(velkost)