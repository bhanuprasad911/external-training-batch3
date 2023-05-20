import time
#Function for checking rows, columns, and diagonals for winning status
def checkwin(l):
    for i in range(3):
        if (l[i][0]==l[i][1]=="X|" and l[i][2]=="X") or (l[0][0]==l[1][1]=="X|" and l[2][2]=="X") or (l[0][2]=="X" and l[1][1]==l[2][0]=="X|") or (l[0][i]==l[1][i]==l[2][i]=="X|") or (l[0][2]==l[1][2]==l[2][2]=="X"):
            return "X has won"
        elif (l[i][0]==l[i][1]=="O|" and l[i][2]=="O") or (l[0][0]==l[1][1]=="O|" and l[2][2]=="O") or (l[0][2]=="O" and l[1][1]==l[2][0]=="O|") or (l[0][i]==l[1][i]==l[2][i]=="O|") or (l[0][2]==l[1][2]==l[2][2]=="O"):
            return "O has won"

        
#Board initialisation
l=[["   |","   |", "   "], ["   |", "   |", "   "], ["   |", "   |", "   "]]


print("-------TIC TAK TOE--------", end="\n\n")
p1=input("Enter the name of player1: ")
p2=input("Enter the name of player2: ")
print(p1, "plays X")
print(p2, "plays O")
print("Game starts by ", p1)

#Empty board
for i in range(3):
            if i==0 or i==1:
                print(*l[i])
                print("----------")
            else:
                print(*l[i])
# Playing the game
c=0
while True:
    if c%2==0:
        print(p1,"'s turn")
    else:
        print(p2, "'s turn\n")
    time.sleep(1)
    a,b=map(int,input("Enter the position: ").split())
    if 0>a>=2 or 0>b>=2:
        print('invalid position')
    else:
        if l[a][b]=="   |":
            if c%2==0:
                l[a][b]="X|"
                c+=1
            else:
                  l[a][b]="O|"
                  c+=1
        elif l[a][b]=="   ":
            if c%2==0:
                l[a][b]="X"
                c+=1
            else:
                  l[a][b]="O"
                  c+=1      
        else:
            print("invalid position")    
        for i in range(3):
            if i==0 or i==1:
                print(*l[i])
                print("----------")
            else:
                print(*l[i])
# conditions for declaring the winners and end of game
    if c>=5:
        if checkwin(l)=="X has won":
            print("Game won by", p1)
            print("Game over")
            break
        elif  checkwin(l)=="O has won":
            print("Game won by", p2)
            break
        else:
            pass
#condition for draw and end of game
    if c==9 and (checkwin(l)!="X has won" or checkwin(l)!="O has won"):
        print("Draw")
        print("Game over..!")
        break
