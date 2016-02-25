#!/usr/bin/env python
'''
Created on Jul 15th, 2015

@author: Lillie Schachter

Requires Button module, which should be available from the same place
   as this file
Requires the graphics module, available from
   http://www.rose-hulman.edu/class/cs/resources/Python/graphics.html
'''
from graphics import *

from button import Button

WIN_WIDTH = 600
WIN_HEIGHT = 600
COORD_MIN = 0
COORD_MAX = 96
OFFSET = 14

PLAYERS = ['x','o']
NUM_BOXES = 9
WINNERS = [
   (0,1,2),(3,4,5),(6,7,8),(0,4,8),
   (6,4,2),(0,3,6),(1,4,7),(2,5,8)
   ]

def check_winner(choices,current,outcome):
   over = False
   for combo in WINNERS:
      full = True
      for button in combo:
         if choices[button]!= current:
            full = False
            break
      if full:
         outcome.setText(current.capitalize()+' Wins \nClick to Close')
         over = True
         break
   return over

def draw_x(window,point):
    minX = point.getX() - OFFSET
    maxX = point.getX() + OFFSET
    minY = point.getY() - OFFSET
    maxY = point.getY() + OFFSET
    line1 = Line(Point(minX,maxY),Point(maxX,minY))
    line1.draw(window)
    line2 = Line(Point(minX,minY),Point(maxX,maxY))
    line2.draw(window)

def draw_o(window,point):
    circle = Circle(point,OFFSET)
    circle.draw(window)

def find_clicked_button(window,buttons,player):
   done = False
   pt = window.getMouse()
   for button in buttons:
      if button.is_clicked(pt):
         eval('draw_'+player+'(window, button.center)')
         button.deactivate()
         done = True
         break
   return button.name, done

def next_turn(window, player, buttons):   
   done = False
   while not done:
      buttonNum, done = find_clicked_button(window,buttons, player)
   return buttonNum

def display_outcome():
   centerNum = COORD_MAX//2
   outcome = Text(Point(centerNum,centerNum),'')
   outcome.setSize(OFFSET)
   outcome.setStyle('bold')
   return outcome

def make_grid(window):
   buttons = []
   index = 0
   
   step = COORD_MAX//3
   start = step//2
   end = int(COORD_MAX - (start*.5))
   
   for row in range(start, end, step):
      for column in range (start, end, step):
         button = Button(window, Point(row,column),step,step,index)
         buttons.append(button)
         index +=1
   return buttons

def run_game(window):
   buttons = make_grid(window)  
   moves= [[None]for __ in range(NUM_BOXES)]
   outcome = display_outcome()
   outcome.draw(window)
   
   over = False
   numClicked = 0

   while not over and numClicked < NUM_BOXES:
      player = numClicked%2
      choiceNum = next_turn(window,PLAYERS[player],buttons)
      current = PLAYERS[player]
      moves[choiceNum]= current
      if numClicked >= 4:
         over = check_winner(moves,current,outcome)
      if numClicked >= (NUM_BOXES - 1) and not over:
         outcome.setText('No one wins. \nClick to close.')
      numClicked+=1

def main():
   window= GraphWin('Tic Tac Toe',WIN_WIDTH,WIN_HEIGHT)
   window.setCoords(COORD_MIN,COORD_MIN,COORD_MAX,COORD_MAX)

   run_game(window)
   
   window.getMouse()
   window.close()

if __name__ == '__main__':
   main()
