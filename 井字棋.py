theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
printBoard(theBoard)
def check(a,st):
        while 1:
            try:
                while  theBoard[a]!=' ':
                    print('''重复的位置，请'''+st+'''重新落子''')
                    a=str(input())
                return a
            except:
                print('''错误的指令，请'''+st+'''重新落子''')
                a=str(input())
                continue
import copy
def check_win(C):
    bo=copy.copy(theBoard)
    i=0
    for s in bo:
        bo[s]=i
        i+=1
    print(bo)
    

while 1:
    print('''白方落子''')
    a=str(input())
    a=check(a,'''白方''')
   #print('a'+theBoard[a]+'a')
    theBoard[a]='O'
    printBoard(theBoard)
    print('''黑方落子''')
    a=str(input())
    a=check(a,'黑方')
    theBoard[a]='X'    
    printBoard(theBoard)
