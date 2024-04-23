from colorama import init, Fore, Style, Back
init(autoreset=True)

# פונקציית בדיקה אם יש זכיה
def Check(current_column,current_row,current_player):
    # מוודא שורה אופקית מלאה
    for column in range(current_column-3,current_column+1):
        if(-1 < column < 7 and current_player == cubic[current_row][column] == cubic[current_row][column+1] == cubic[current_row][column+2] == cubic[current_row][column+3]):
            return True
    # מוודא שורה אנכית מלאה
    if current_row<7 and (current_player == cubic[current_row][current_column] == cubic[current_row+1][current_column] == cubic[current_row+2][current_column] == cubic[current_row+3][current_column]):
        return True
    # מוודא שורה אלכסונית יורדת לימין מלאה
    for row,column in zip(range(current_row-3,current_row+1), range(current_column-3,current_column+1)):
        if 7 > column > -1 and 7 > row > -1 and (current_player == cubic[row][column] == cubic[row+1][column+1] == cubic[row+2][column+2] == cubic[row+3][column+3]):
            return True
    # מוודא שורה אלכסונית יורדת לשמאל מלאה
    for row,column in zip(range(current_row-3,current_row+1), range(current_column+3,current_column-1,-1)):
        if 10 > column > -1 and 7 > row > -1 and (current_player == cubic[row][column] == cubic[row+1][column-1] == cubic[row+2][column-2] == cubic[row+3][column-3]):
            return True
    return False

# פונקציית הדפסת מבנה המשחק  
def Display():
    pice = [Fore.RED + '● ',Fore.GREEN + '● ',Fore.YELLOW + '- ']
    # מבנה המשחק
    print('\n       ',Fore.CYAN + '_'*49)
    for row in range(10):
        print('       ', end = '')
        for column in range(10):
                print(Fore.CYAN + '│',pice[cubic[row][column]] ,end = '')
        print(Fore.CYAN +'│')
    # תחתית
    print(Fore.CYAN +'       │',end = '')
    for i in range(1,10):
        print(' '+Fore.YELLOW + str(i) , end = '  ')
    print(Fore.YELLOW +'10',Fore.CYAN +'│')

# מוודא קבלת ערך עמודה תקף מהמשתמש
def get_valid_column(players_name,player):
    while True:
        try:
            column = int(input(F'\n{players_name[player]} Enter the column you chose (1 to 10): ')) - 1
            if column < 0 or column > 9:
                print("Invalid column. Please enter a number between 1 and 10.")
            elif cubic[0][column] != -1:
                print('column full. Please chose anather column.')
            else:
                return column
        except ValueError:
            print("Invalid input. Please enter a number.")

# פונקציית הצבה במיקום הנבחר
def Placement(useIN,player):
    for row in range(9,-1,-1):
        if (cubic[row][useIN] == -1):
            cubic[row][useIN] = player
            Display()
            return row

# פונקציית המשתמש
def User():
    players_name = [Fore.RED + input('\nFirst player enter your name:  ' + Fore.RED) + Style.RESET_ALL  ,  Fore.GREEN + input(Style.RESET_ALL + 'second player enter your name:  '+ Fore.GREEN) + Style.RESET_ALL]
    Display()
    player = 0
    # לולאת ריצה עד סיום המערך 10*10 או בניצחון
    for turn in range(100):
        # קבלת מיקום עמודה תקף מהמשתמש
        useIN = get_valid_column(players_name,player)
        # הצבה במקום הנבחר
        row = Placement(useIN,player)
        # בדיקת זכיה
        if(turn > 5 and Check(useIN,row,player)):
            print(F'\n\n{players_name[player]} congratulation, you are the winer!\n')
            return
        player = (player + 1) %2
    # בסיום הריצה ללא מנצחים
    print('\n   >> ther are no winers!\n\n  ',Fore.GREEN + '>> try again...\n\n')

# # # # Main # # # #       
cubic = [[-1 for j in range(10)] for i in range(10)]
User()