import mers_Script_2_EV as EV
import merwin_Script_1_Stat as ST
import math 

def ContinueOrExit():
    select = int(input("\nDo you want to try again? \n[1] Yes  [2] No \nOption: "))
    if select == 1: main()
    elif select == 2: exit()
    else: 
        print("Invalid!!")
        ContinueOrExit()
        

def main():

    print("------------------Hello !! Welcome To The Pokemon STAT & EV Calculator------------------\n\n")
    while True:
        base = int ( input ("Base HP: "))
        level = int ( input ("Level: "))
        ev = int ( input ("EV must be [0 - 255] \nEV: "))
        iv = int ( input ("IV must be [0 - 31] \nIV: "))
            
        if iv > 31:
            print("IV exceeds\n")  
            main() 

        if ev > 255:
            print("EV exceeds\n") 
            main()

        else:    
            print("Proceeding.....")
            break

    while True:
        print("\nChoose a Pokemon calculator type \n[1] EV Calculator \n[2] Stat Calculator ")
        choice = int(input("\nInput your choice: "))
    
        if choice == 1:
            stats = int(input("Stats: "))
            pick = int(input("[1] Beneficial [2] Hindering \nModidier: "))
            if pick == 1:
                md = 1.1

            elif pick == 2:
                md = 0.9

            else:
                print("Invalid Input!!")
            
            totalEV = EV.evComputed.computeEV(base, iv, ev, level, md, stats)
            if totalEV <=500:
                print("Total EV:", totalEV)
            
            else:
                print("Pokemon's Total EV Exceeds...")
            ContinueOrExit()
        

        elif choice == 2:
            se = int(input("\nCompute other stats? [1] Yes [2] No \nSelect: "))
            if se == 1: 
                sel = str(input("\n[att] [def] [spatt] [spdef] [spd]\nWhat Stat would you like to compute?: "))    
                if sel == 'att': 
                    sta = 'Attack'   
                    sele = int(input("\n[1] Beneficial [2] Hindering \nNature: "))   
                    if sele == 1:
                        nature = 1.1

                    elif sele == 2:
                        nature = 0.9
                
                if sel == 'def':
                    sta = 'Defense'    
                    sele = int(input("\n[1] Beneficial [2] Hindering \nNature: "))   
                    if sele == 1:
                        nature = 1.1

                    elif sele == 2:
                        nature = 0.9
                
                if sel == 'spatt':  
                    sta = 'Special Attack'  
                    sele = int(input("\n[1] Beneficial [2] Hindering \nNature: "))   
                    if sele == 1:
                        nature = 1.1

                    elif sele == 2:
                        nature = 0.9

                if sel == 'spdef':  
                    sta = 'Special Defense'  
                    sele = int(input("\n[1] Beneficial [2] Hindering \nNature: "))   
                    if sele == 1:
                        nature = 1.1

                    elif sele == 2:
                        nature = 0.9

                if sel == 'spd':    
                    sta = 'Speed'
                    selec = int(input("\n[1] Beneficial [2] Hindering \nNature: "))   
                    if sele == 1:
                        nature = 1.1

                    elif sele == 2:
                        nature = 0.9
                
                other = ST.statcomputation.otStat(base, ev, level, iv, nature)
                if other <= 510:
                    print("\nComputing", sta,"Value =", other)
                
                else:
                    print("Pokemon's Total EV Exceeds!")
                ContinueOrExit()

            elif se == 2:
                chp = ST.statcomputation.health(base, ev, level, iv)
                if chp <= 510:
                    print ("HP Value:", chp)
                else:
                    print("Pokemon's Total EV Exceeds!")
                ContinueOrExit()

            else:
                print("Invalid Input!!!")
                       
        else:
            print("Invalid Input!!!")

main()