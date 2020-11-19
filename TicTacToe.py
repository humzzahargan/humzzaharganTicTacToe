# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 21:58:37 2020

@author: humzz
"""

"""
i1 i2 i3
i4 i5 i6
i7 i8 i9
"""
i1 = 'i1'
i2 = 'i2'
i3 = 'i3'
i4 = 'i4'
i5 = 'i5'
i6 = 'i6'
i7 = 'i7'
i8 = 'i8'
i9 = 'i9'
current_player = 1
win = False
draw = False

def win_p1():
    if i1 == 'X' and i5 == 'X' and i9 == 'X':
        return True
    if i3 == 'X' and i5 == 'X' and i7 == 'X':
        return True
    if i1 == 'X' and i2 == 'X' and i3 == 'X':
        return True
    if i4 == 'X' and i5 == 'X' and i6 == 'X':
        return True
    if i7 == 'X' and i8 == 'X' and i9 == 'X':
        return True
    if i1 == 'X' and i4 == 'X' and i7 == 'X':
        return True
    if i2 == 'X' and i5 == 'X' and i8 == 'X':
        return True
    if i3 == 'X' and i6 == 'X' and i9 == 'X':
        return True

def win_p2():
    if i1 == 'O' and i5 == 'O' and i9 == 'O':
        return True
    if i3 == 'O' and i5 == 'O' and i7 == 'O':
        return True
    if i1 == 'O' and i2 == 'O' and i3 == 'O':
        return True
    if i4 == 'O' and i5 == 'O' and i6 == 'O':
        return True
    if i7 == 'O' and i8 == 'O' and i9 == 'O':
        return True
    if i1 == 'O' and i4 == 'O' and i7 == 'O':
        return True
    if i2 == 'O' and i5 == 'O' and i8 == 'O':
        return True
    if i3 == 'O' and i6 == 'O' and i9 == 'O':
        return True

def draw():
    if i1 != 'i1' and i2 != 'i2' and i3 != 'i3' and i4 != 'i4' and i5 != 'i5' and i6 != 'i6' and i7 != 'i7' and i8 != 'i8' and i9 != 'i9':
        return True
    else:
        return False
        

def print_board():
    print(str(i1) + " " + str(i2) + " " + str(i3))
    print(str(i4) + " " + str(i5) + " " + str(i6))
    print(str(i7) + " " + str(i8) + " " + str(i9))

def filled_square(str):
    if str == 'i1':
        if i1 != 'i1':
            return True
    if str == 'i2':
        if i2 != 'i2':
            return True
    if str == 'i3':
        if i3 != 'i3':
            return True
    if str == 'i4':
        if i4 != 'i4':
            return True
    if str == 'i5':
        if i5 != 'i5':
            return True
    if str == 'i6':
        if i6 != 'i6':
            return True
    if str == 'i7':
        if i7 != 'i7':
            return True
    if str == 'i8':
        if i8 != 'i8':
            return True
    if str == 'i9':
        if i9 != 'i9':
            return True
    return False

def p1():
    correct_input = False
    while correct_input == False:
        choice = input("Where would you like to place your X? Enter a square from i1 - i9: ")
        schoice = choice
        current_player = 2
        if filled_square(schoice) == False:
            if str(schoice) == 'i1':
                correct_input = True
                i1 = 'X'
            elif str(schoice) == 'i2':
                correct_input = True
                i2 = 'X'
            elif str(schoice) == 'i3':
                correct_input = True
                i3 = 'X'
            elif str(schoice) == 'i4':
                correct_input = True
                i4 = 'X'
            elif str(schoice) == 'i5':
                correct_input = True
                i5 = 'X'
            elif str(schoice) == 'i6':
                correct_input = True
                i6 = 'X'
            elif str(schoice) == 'i7':
                correct_input = True
                i7 = 'X'
            elif str(schoice) == 'i8':
                correct_input = True
                i8 = 'X'
            elif str(schoice) == 'i9':
                correct_input = True
                i9 = 'X'
            else:
                print("Pls try again. Enter a square from i1 - i9: ")
                current_player = 1
        else:
            print("That square is already taken. Pls try again: ")
            current_player = 1

def p2():
    correct_input2 = False
    while correct_input2 == False:
        if current_player == 1:
            choice2 = input("Where would you like to place your X? Enter a square from i1 - i9: ")
            schoice2 = choice2
            current_player = 1
            if filled_square(schoice2) == True:
                if str(schoice2) == 'i1':
                    correct_input2 = True
                    i1 = 'O'
                if str(schoice2) == 'i2':
                    correct_input2 = True
                    i2 = 'O'
                if str(schoice2) == 'i3':
                    correct_input2 = True
                    i3 = 'O'
                if str(schoice2) == 'i4':
                    correct_input2 = True
                    i4 = 'O'
                if str(schoice2) == 'i5':
                    correct_input2 = True
                    i5 = 'O'
                if str(schoice2) == 'i6':
                    correct_input2 = True
                    i6 = 'O'
                if str(schoice2) == 'i7':
                    correct_input2 = True
                    i7 = 'O'
                if str(schoice2) == 'i8':
                    correct_input2 = True
                    i8 = 'O'
                if str(schoice2) == 'i9':
                    correct_input2 = True
                    i9 = 'O'
                else:
                    print("Pls try again. Enter a square from i1 - i9: ")
                    current_player = 2
            else:
                print("That square is already taken. Pls try again: ")
                current_player = 2
    

while win != True or draw != True:
        if win == True:
                break;
        elif draw == True:
                break;
        else:    
                if current_player == 1:
                    print_board()
                    correct_input = False
                    choice = input("Where would you like to place your X? Enter a  from i1 - i9:")
                    current_player = 2
                    if filled_square(choice) == False:
                        if str(choice) == 'i1':
                            correct_input = True
                            i1 = 'X'
                            win = win_p1()
                        elif str(choice) == 'i2':
                            correct_input = True
                            i2 = 'X'
                            win = win_p1()
                        elif str(choice) == 'i3':
                            correct_input = True
                            i3 = 'X'
                            win = win_p1()
                        elif str(choice) == 'i4':
                            correct_input = True
                            i4 = 'X'
                            win = win_p1()
                        elif str(choice) == 'i5':
                            correct_input = True
                            i5 = 'X'
                            win = win_p1()
                        elif str(choice) == 'i6':
                            correct_input = True
                            i6 = 'X'
                            win = win_p1()
                        elif str(choice) == 'i7':
                            correct_input = True
                            i7 = 'X'
                            win = win_p1()
                        elif str(choice) == 'i8':
                            correct_input = True
                            i8 = 'X'
                            win = win_p1()
                        elif str(choice) == 'i9':
                            correct_input = True
                            i9 = 'X'
                            win = win_p1()
                        else:
                            print("Pls try again. Enter a square from i1 - i9: ")
                            current_player = 1
                    else:
                        print("That square is already taken. Pls try again: ")
        if win == True:
                break;
        elif draw() == True:
                break;
        else:
                if current_player == 2:
                    current_player = 1
                    print_board()
                    correct_input2 = False
                    choice2 = input("Where would you like to place your O? Enter a square from i1 - i9: ")
                    current_player = 1
                    if filled_square(choice2) == False:
                        if str(choice2) == 'i1':
                            correct_input2 = True
                            i1 = 'O'
                            win = win_p2()
                        elif str(choice2) == 'i2':
                            correct_input2 = True
                            i2 = 'O'
                            win = win_p2()
                        elif str(choice2) == 'i3':
                            correct_input2 = True
                            i3 = 'O'
                            win = win_p2()
                        elif str(choice2) == 'i4':
                            correct_input2 = True
                            i4 = 'O'
                            win = win_p2()
                        elif str(choice2) == 'i5':
                            correct_input2 = True
                            i5 = 'O'
                            win = win_p2()
                        elif str(choice2) == 'i6':
                            correct_input2 = True
                            i6 = 'O'
                            win = win_p2()
                        elif str(choice2) == 'i7':
                            correct_input2 = True
                            i7 = 'O'
                            win = win_p2()
                        elif str(choice2) == 'i8':
                            correct_input2 = True
                            i8 = 'O'
                            win = win_p2()
                        elif str(choice2) == 'i9':
                            correct_input2 = True
                            i9 = 'O'
                            win = win_p2()
                        else:
                            print("Pls try again. Enter a square from i1 - i9: ")
                            current_player = 2
                    else:
                        print("That square is already taken. Pls try again: ")
                        current_player = 2
if draw() == True:
    print_board()
    print("It's a draw!")
else:
    if win == True:
        if current_player == 1:
            print_board()
            print("Player 2 won!")
        else:
            print_board()
            print("Player 1 won!")