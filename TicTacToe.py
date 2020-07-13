board={'9':' ','8':' ','7':' ',
	'4':' ','5':' ','6':' ',
	'1':' ','2':' ','3':' '}
#Game Board For Player 1
def print_board1(ch):
	board[ch]='*'
	print(board['7'] + '|' + board['8'] + '|' +board['9'])
	print("______")
	print(board['4'] + '|' + board['5'] + '|' +board['6'])
	print("______")
	print(board['1'] + '|' + board['2'] + '|' +board['3'])
	if(board['9']==board['8']==board['7']=="*" or board['4']==board['5']==board['6']=="*" or board['1']==board['2']==board['3']=="*" or board['9']==board['5']==board['1']=="*" or board['1']==board['5']==board['9']=="*"):
		print("player 1 wins")
		exit(0)
	start2()



#Game Board For Player 2
def print_board2(ch):
	board[ch]='•'
	print(board['7'] + '|' + board['8'] + '|' +board['9'])
	print("______")
	print(board['4'] + '|' + board['5'] + '|' +board['6'])
	print("______")
	print(board['1'] + '|' + board['2'] + '|' +board['3'])
	if(board['9']==board['8']==board['7']=="•" or board['4']==board['5']==board['6']=="•" or board['1']==board['2']==board['3']=="•" or board['9']==board['5']==board['1']=="•" or board['1']==board['5']==board['9']=="•"):
		print("Player 2 WINS")
		exit(0)
	
	start1()
# Starts for Player 1
def start1():
	print("\n")
	ch=input("Please Enter position:  ")
	if(board[ch]==' '):
		print_board1(ch)
	else:
		print("Sorry Try another One")
		start1()

#Starts for Player 2
def start2():
	print("\n")
	ch=input("Please Enter position:  ")
	if(board[ch]==' '):
		print_board2(ch)
	else:
		print("Sorry Try another One")
		start2()




name1=input("Enter Player1 Name:: ")
name2=input("Enter Player2 Name:: ")
print("\n")
print("Welcome ",name1,"and ",name2)
print("\n")
print("--------------------------TIC TAC TOE-----------------------")
print("\n",name1,"plays First then",name2)
start1()
