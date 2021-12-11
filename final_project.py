#!/usr/bin/env python3
# # -*- coding: utf-8 -*-
""" SodokuSolver """
__author__="Carl Powaza"


import sys


################Utility functions are here

def printboard(grid):
    for i in range(0,len(grid)):
        for j in grid[i]:
            print(" ",j,end="")
        print("")

def createGrid(txtfile):
    with open(txtfile, 'r') as my_file:
       string =my_file.read()
    temp = string.split("\n")
    grid=[[],[],[],[],[],[],[],[],[]]
    for i in range(0,9):
        grid[i]=temp[i].split(" ")
    return grid
    


#returns a t/f based on if val is already found in local grid
def squareChecker(y,x,grid,val):

    #find x coordinate for box center
    if(x <3):
        x = 0
    elif(x >2 and x < 6):
        x =3
    elif(x>5):
        x =6
    #find y coordinate for box center
    if(y <3):
        y = 0
    elif(y >2 and y < 6):
        y =3
    elif(y>5):
        y =6       
    #now loop over all the elements in the cube
    for col in range(0,3):
        for row in range(0,3):
            if(grid[col+y][row+x]==val):
                    return True

    return False

#checks if it is safe to put val into grid[col][row]
def safeCheck(grid,row,col,val):

    #check box
    bool  = True

    #helper function that finds and compares the vals in cube 
    if squareChecker(col,row,grid,val):
        bool = False
               
    #check row
    for i in range(0,9):
        if grid[col][i]==val:
            bool = False
    #check col
    for i in range(0,9):
        if grid[i][row]==val:
            bool = False   

   
    return bool


def solution(grid,row,col):
  


    #base Case \\ we are at the end of the grid and its time to end recursion
    if col >7 and row >7:
        for i in range(1,10):
            grid[col][row]= str(0)
            if safeCheck(grid,row,col,str(i)):
                 grid[col][row]= str(i)
                 break
        printboard(grid)
        return True
    
    if col ==9:
        col=0
        row+=1
    
    if grid[col][row]!='0':  #if this value isn't empty; then theres nothing to do
        solution(grid,row,col+1)
    else:
        for i in range(1,10):# loop from 1 - 9 
            grid[col][row]= str(0)
            if safeCheck(grid,row,col,str(i)):#checks if safe to place i
                grid[col][row]= str(i)
                solution(grid,row,col+1)


    
#########################################Main below this

arginput = sys.argv[1]; 

def main():
    print("     ","--Sudoku Solver--")
    
    if(arginput =="help"):
        print("      ","--help--")    
        print("      ","This program takes in an unsolved board") 
        print("      ","from the command line, solves it then displays") 
        print("      ","Type in the number for an action and press enter")
        print("      ","-----how to setup file-----")
        print("      ","The file should contain only numbers")
        print("      ","with spaces between, and new lines for every new row.")
        print("      ","Run the file from command line by typing")
        print("      ","py final_project.py file.txt")
        print("      ","Where file is the name of the text file.")
        print("      ","For Example")
        print("      ","py final_project example.txt")
        print()
        exit()
    grid = createGrid(arginput)
    print()

    print("      ","Unsolved board:")
    printboard(grid)
    print()
    print("      ","Solved board:")
    solution(grid,0,0)
    print()



  
        

 

main()

























"""
    print("   ","--Sudoku Solver--")
    while(True):
        print("   ","--Select a command--")
        print("1:  ","Show Unsolved Board")
        print("2:  ","Solve and show board")
        print("3:  ","Pick a new file")
        print("4:  ","Help")
        reply = input()
        if reply == 1:
            print("   ","unsolved board here")
        if reply == 2:
            print("   ","solved board here")
        if reply ==3:
            print("   ","please type in the file here: ",end="")

        if reply == 4 or reply=="help":
            print("   ","--help--")    
            print("   ","This program takes in a unsolved board") 
            print("   ","from the command line, solves it then displays") 
            print("   ","Type in the number for an action and press enter")
            print("   ","-----how to setup file")
            print("   ","The file should contain only numbers")
            print("   ","with spaces between, and new lines for every new row")
        print("   ","Press enter to continue..",end="")
        input()
   
"""