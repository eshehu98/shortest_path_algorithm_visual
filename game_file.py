
# asks the user how big they want the board to be

not_valid_input = True
while not_valid_input:
    asking_question = int(input("how big do you want the board to be? 3x3? 4x4? 5x5? Select any number 1 to 9\n"))
    if asking_question < 10:
        not_valid_input = False
    else:
        print("your input was not within the permitted range")

# sets the height of the board to the answer
height_of_board = asking_question

# sets the width of the board to the answer
width_of_board = asking_question


# prints the height and width of the board
# print("the two variables are height of board, which equals ", height_of_board, " and width of board, which equals ", width_of_board)


# creats the actual board as an empty list
the_actual_board = []


# double for loop fills the board with "0"
# board is not actually two-dimensional even though it is a double for loop
for i in range(height_of_board):
    for j in range(width_of_board):
        the_actual_board.append("0")

# print(the_actual_board)

# defines a function which prints the board
def print_board():
    # declares an iterator outside of the double for loop
    this_iterator = 0
    # creates a double for loop where the board is printed
    for i in range(height_of_board):
        for j in range(width_of_board):
            # in order to make it look like a real board it adds dots
            # the end parameter makes it not go to a newline after printing
            if j == 0:
                print("...", end = "")
            print(the_actual_board[this_iterator], end = "...")
            this_iterator+=1
        # goes to a newline which creates the row    
        print("\n")

# calls the print_board function
print_board()


# creates a boolean which represents the game running
game_is_not_over = True

# defines a variable called player position 
# it represents the player's position on the board in the initial list
player_position = 0


while game_is_not_over:

    # asks the user if he wants to move right or left
    # the answer the user gives changes the player_position variable
    ask = input("What direction do you want to move? type R if right, L if left, and Q to quit.\n")
    if ask == "R":
        player_position += 1
    elif ask == "L":
        player_position -= 1
    elif ask == "Q":
        game_is_not_over = False
    else:
        print("your input did not match any of the options.")
    
    # once the user has selected a direction the list is changed
    # the player's position goes from an "O" to an "X"
    if ask == "R" or ask == "L":
        the_actual_board[player_position] = "X"
        print_board()
   



        
        













# array_of_arrays = [[0,0,0],[0,0,0],[0,0,0]]

# for thing in array_of_arrays:
#     for entry in thing:
#         answer = input("do you want to change this entry?")
#         if answer == "YES" or answer == "yes" or answer == "Yes":
#             print("this entry is ", entry)
#             entry = "X"
#             print("this entry is now ", entry)

# print("array of arrays is now", array_of_arrays)












# from tkinter import *


# root = Tk()
# root.geometry("400x400")

# buttons = []

# for iterator in range(5):
#     print("d")
#     # code that creates button
#     for new_iterator in range(5):
#         #code that creates button
#         print("hello")



# root.mainloop() 