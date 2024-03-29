import random
def shufflematrix(M):
    random.shuffle(M)
    for x in M:
        random.shuffle(x)
    return (M)
def displaymatrix(M):
    print("-------------------------------------------------------------")
    for k in range(len(M)):
        print(k+1,end="\t")
    print()
    print("--------------------------------")
    for r in range (len(M)):
        for c in range (len(M[0])):
            print(M[r][c],end='\t')
        print("|",r+1)
    print("-------------------------------------------------------------")
def sumlist(A):
    s=0
    for i in range (len(A)):
        for j in range (len(A[0])):
            s+=A[i][j]
    return(s)

M=[['A','B','D','E'],
   ['C','F','G','H'],
   ['G','A','C','B'],
   ['D','F','H','E']]
row=len(M)
col=len(M[0])
A=[]
for q in range(row):
    B=[]
    for w in range(col):
        B.append(0)
    A.append(B)

print("---------------------------------------------WELCOME TO THE GAME MATCH THE BOX------------------------------------------------------------------------\nEACH SUCCESS PRODUCES 2 POINTS")
displaymatrix(A)

game = True


while game==True:
    name=(input("ENTER PLAYER NAME:: ").upper())
    inputs = []

    move=0
    points=0
    sum_list=0
    while (sum_list<16):
        keys=[1,2,3,4]
        lst=[]
        
        p1=True

        
        while p1==True:
            try:
                nr1=int(input("ENTER ROW NUMBER FOR FIRST GUESS :: "))

                if nr1 in keys:
                        p1=False
                else : print ("This Row is not Exist")
                
                
            
                
            except:
                print("Kindly Input Integer Values")
             
        p2=True

        
        while p2==True:
            try:
                nc1=int(input("ENTER COLOUMN NUMBER FOR FIRST GUESS :: "))

                if nc1 in keys:
                        p2=False
                else : print ("This Coloumn is not Exist")
            
            except:
                    print("Kindly Input Integer Values")
                
        while [nr1-1,nc1-1] in inputs:
            print ("Already Filled")
            p1=True

        
            while p1==True:
                try:
                    nr1=int(input("ENTER ROW NUMBER FOR FIRST GUESS :: "))

                    if nr1 in keys:
                            p1=False
                    else : print ("This Row is not Exist")
                
                
            
                
                except:
                    print("Kindly Input Integer Values")
             
            p2=True
            while p2==True:
                try:
                    nc1=int(input("ENTER COLOUMN NUMBER FOR FIRST GUESS :: "))

                    if nc1 in keys:
                            p2=False
                    else : print ("This Coloumn is not Exist")
            
                except:
                    print("Kindly Input Integer Values")

            
            
        
        p3=True

        while p3==True:
            try:
                nr2=int(input("ENTER ROW NUMBER FOR SECOND GUESS :: "))
                if nr2 in keys:
                        p3=False
                else : print ("This Row is not Exist")
                    
                    
                
                    
            except:
                print("Kindly Input Integer Values")
            
        p4=True

        while p4==True:
            try:
                nc2=int(input("ENTER COLOUMN NUMBER FOR SECOND GUESS :: "))

                if nc2 in keys:
                        p4=False
                else : print ("This Coloumn is not Exist")
                    
                    
                
                    
            except:
                print("Kindly Input Integer Values")
        while [nr2,nc2]==[nr1,nc1]:
            print("THIS BOX IS ALREADY CHOOSEN AS FIRST BOX")
            p3=True

            while p3==True:
                try:
                    nr2=int(input("ENTER ROW NUMBER FOR SECOND GUESS :: "))
                    if nr2 in keys:
                            p3=False
                    else : print ("This Row is not Exist")
                        
                        
                    
                        
                except:
                    print("Kindly Input Integer Values")
                
            p4=True

            while p4==True:
                try:
                    nc2=int(input("ENTER COLOUMN NUMBER FOR SECOND GUESS :: "))

                    if nc2 in keys:
                            p4=False
                    else : print ("This Coloumn is not Exist")
                        
                        
                    
                        
                except:
                    print("Kindly Input Integer Values")
            
        while [nr2-1,nc2-1] in inputs:
            print ("Already Filled")
            p3=True

            while p3==True:
                try:
                    nr2=int(input("ENTER ROW NUMBER FOR SECOND GUESS :: "))
                    if nr2 in keys:
                            p3=False
                    else : print ("This Row is not Exist")
                        
                        
                    
                        
                except:
                    print("Kindly Input Integer Values")
                
            p4=True

            while p4==True:
                try:
                    nc2=int(input("ENTER COLOUMN NUMBER FOR SECOND GUESS :: "))

                    if nc2 in keys:
                            p4=False
                    else : print ("This Coloumn is not Exist")
                        
                        
                    
                        
                except:
                    print("Kindly Input Integer Values")
        
        nr1=(nr1)-1
        nc1=(nc1)-1
        nr2=(nr2)-1
        nc2=(nc2)-1
        del A[nr1][nc1]
        A[nr1].insert(nc1,M[nr1][nc1])
        del A[nr2][nc2]
        A[nr2].insert(nc2,M[nr2][nc2])
        displaymatrix(A)
        if M[nr1][nc1]==M[nr2][nc2]:
            print("HURRAY...!! YOUR GUESS IS RIGHT...")
            move+=1
            print(name,'Now Your Move is ',move)
            
            points+=2
            print(name,'Now Your Points is ', points)
            del A[nr1][nc1]
            A[nr1].insert(nc1,1)
            del A[nr2][nc2]
            A[nr2].insert(nc2,1)
            displaymatrix(A)
            inputs.append([nr1,nc1])
            inputs.append([nr2,nc2])
        else:
            print("SORRY YOUR ATTEMPT IS MISSED......")
            move+=1
            print(name,'Now Your Move is ',move)
            print(name,'Now Your Points is ', points)
            del A[nr1][nc1]
            
            A[nr1].insert(nc1,0)
            del A[nr2][nc2]
            A[nr2].insert(nc2,0)
            displaymatrix(A)
        sum_list=sumlist(A)
    if move == 8:
        points+=5
    elif move>8 and move<=12:
        points+=3
    
    print(name.upper(),"YOUR TOTAL MOVE IS",move ,"AND",name.upper(),"YOUR TOTAL POINTS IS ",points)
    
    
    qu=input("Do You Want to Continue (Press any key fOr continue / Press 0:For Exit)")
    
    if qu=='0':
        break
        game=False
    else:
        M=shufflematrix(M)
        row=len(M)
        col=len(M[0])
        A=[]
        for q in range(row):
            B=[]
            for w in range(col):
                B.append(0)
            A.append(B)

        displaymatrix(A)
