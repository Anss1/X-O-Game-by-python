a1=["1","2","3"]
a2=["4","5","6"]
a3=["7","8","9"]
mat = [0,1,2,3,4,5,6,7,8,9]
matrix=[a1,a2,a3]
player='X'
coun=1
print('X-O Game By Ans:')




def checkNumber(num):
    i = 0
    j = 0
    while(num > 3):
        i += 1
        num -= 3
    j = num - 1    
    if(matrix[i][j] == "O" or matrix[i][j] == "X"):
        return True





def game():
    print(' ',a1[0],'|',a1[1],'|',a1[2])
    print('','---|---|---')
    print(' ',a2[0],'|',a2[1],'|',a2[2])
    print('','---|---|---')
    print(' ',a3[0],'|',a3[1],'|',a3[2])
    

       


def input1():
    l=0
    k=0
    
    global player
    if(player=='X'):
        a=int(input('player(1)Enter the number you want:'))
    else:
        a=int(input('player(2)Enter the number you want:'))
    x = checkNumber(a)    
    while(x):
        print("Error")
        a = int(input('Enter another number:'))
        x = checkNumber(a)  
    #game play here.....new
    if(a <= 3 and a > 0):
        matrix[0][a-1]=player
    if(a > 3 and a < 10):
        while(a > 3 and a < 10):
            l += 1
            a -= 3
        k = a - 1    
        matrix[l][k]=player




def changerole():
    global player
    if(player=='X'):
        player='O'
    else:
        player='X'
    return(player)   





def win():
    #player 1
    if(matrix[0][0]=='X'and matrix[0][1]=='X' and matrix[0][2]=='X'):
        return 'X'
    if(matrix[1][0]=='X'and matrix[1][1]=='X' and matrix[1][2]=='X'):
        return 'X'
    if(matrix[2][0]=='X'and matrix[2][1]=='X' and matrix[2][2]=='X'):
        return 'X'
    if(matrix[0][0]=='X'and matrix[1][0]=='X' and matrix[2][0]=='X'):
        return 'X'
    if(matrix[0][1]=='X'and matrix[1][1]=='X' and matrix[2][1]=='X'):
        return 'X'
    if(matrix[0][2]=='X'and matrix[1][2]=='X' and matrix[2][2]=='X'):
        return 'X'
    if(matrix[0][0]=='X'and matrix[1][1]=='X' and matrix[2][2]=='X'):
        return 'X'
    if(matrix[0][2]=='X'and matrix[1][1]=='X' and matrix[2][0]=='X'):
        return 'X'
    #player 2
    if(matrix[0][0]=='O' and matrix[0][1]=='O' and matrix[0][2]=='O'):
        return 'O'
    if(matrix[1][0]=='O' and matrix[1][1]=='O' and matrix[1][2]=='O'):
        return 'O'
    if(matrix[2][0]=='O' and matrix[2][1]=='O' and matrix[2][2]=='O'):
        return 'O'
    if(matrix[0][0]=='O' and matrix[1][0]=='O' and matrix[2][0]=='O'):
        return 'O'
    if(matrix[0][1]=='O' and matrix[1][1]=='O' and matrix[2][1]=='O'):
        return 'O'
    if(matrix[0][2]=='O' and matrix[1][2]=='O' and matrix[2][2]=='O'):
        return 'O'
    if(matrix[0][0]=='O' and matrix[1][1]=='O' and matrix[2][2]=='O'):
        return 'O'
    if(matrix[0][2]=='O' and matrix[1][1]=='O' and matrix[2][0]=='O'):
        return 'O'
    return '\n'


print('')
game()
print('')

while(1):
    input1()
    print('')

    game()
    print('')

    if(win()=='X'):
         print('player "X" wins (:')
         break
    elif(win()=='O'):
         print('player "O" wins (:')
         break
    elif(win()!='X' and win()!='O' and coun==9):
         print('game draw (;')
         break
    changerole()
    coun+=1
    
    


