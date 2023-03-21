
    

aa=input("enter your Email:")
bb=input("enter your Name:")
    

    
    
a=random.randint(1,2)


if (a==1 and Toss=="Odd") or (a==2 and Toss=="Even"):
    print("You won the toss!!")
    while True:
        b=(input("Do you choose to bat or bowl:")).casefold()
        if b=="bat" or b=="bowl":
            pass
        else:
            print('You can choose only bat or bowl')
            continue
        break
    
            
    
    if b=="bat":
        z=1
        print ("-----------------------------------------------\nYour Batting\n")
        
    else:
        z=0
        print ("-----------------------------------------------\nYour Bowling\n")
        
        
else:
    print("You lost the toss!!")
    b=random.randint(1,2)
    if b==1:
        z=0
        print('Computer chose to bat')
        print ("-----------------------------------------------\nYour Bowling\n")
        
    else :
        z=1
        print('Computer chose to bowl')
        print ("-----------------------------------------------\nYour Batting\n")
        
        
your_runs=0
comp_runs=0

for i in[2,3]:
    if z==1:
        while True:
            while True:
                try:  
                    runs=int(input("Enter Runs for Your Batting Turn: "))
                
                except:
                    print("You can only play a number from 1 to 10")
                    continue
                break
            
            
            comp_bowl= random.randint(0,10)

            if runs==comp_bowl:
                print ("You Played: ",runs,", Computer Played: ",comp_bowl)
                print ("You are Out. Your Total Runs= ", your_runs,"\n")
                print("=================================================")
                break
    
            elif runs>10 or runs<0:
                print ("ALERT!! You can only play number >0 or <10 only!")
                continue
    
            else:
                your_runs+=runs
                print ("You Played: ",runs,", Computer Played: ",comp_bowl)
                print ("Your runs now are: ",your_runs,"\n")
                if your_runs > comp_runs and i==3:
                    break
           
        z-=1
    


    elif z==0:
        while True:
            while True:
                try:
            
                    bowl=int(input("Enter Runs for Your Bowling Turn: "))
                except:
                    print("You can only play a number from 1 to 10")
                    continue
                break
            comp_bat= random.randint(0,10)

            if comp_bat==bowl:
                print ("Computer played: ",comp_bat,", Your played: ",bowl)
                print ("The Computer is Out. Computer Runs= ",comp_runs,"\n")
                print("=================================================")
                break

            elif comp_bat!=bowl:
                comp_runs+=comp_bat
                print ("Computer played: ",comp_bat,", You played: ",bowl)
                print ("Computer Runs: ",comp_runs,"\n")

                if comp_runs > your_runs and i==3:
                    break
            else:
                print("Error,You can only play from 0 to 10")    
        z+=1    
       


