#!/usr/bin/env python
'''
Created on Jul 15th, 2015

@author: Lillie Schachter

Requires the graphics module, available from
   http://www.rose-hulman.edu/class/cs/resources/Python/graphics.html
'''

from graphics import *
import math

class Button:

    """A button is a labeled rectangle in a window.
    It is enabled or disabled with the activate()
    and deactivate() methods. The isClicked(pt) method
    returns true if the button is enabled and pt is inside it."""

    def __init__(self, win, center, width, height, name):
        """ Creates a rectangular button, eg:
        qb = Button(myWin, centerPoint, width, height, "black", 'Quit') """ 
        self.center = center
        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        self._xmax, self._xmin = x+w, x-w
        self._ymax, self._ymin = y+h, y-h
        p1 = Point(self._xmin, self._ymin)
        p2 = Point(self._xmax, self._ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.draw(win)
        self.name = name
        self.active = True
        self.win=win

    def is_clicked(self, pt):
        "Returns true if button active and pt is inside"
        pX = pt.getX()
        pY = pt.getY()
        return (self.active and
                self._xmin <= pX <= self._xmax and
                self._ymin <= pY <= self._ymax)

    def activate(self):
        "Sets this button to 'active'."
        self.active = True
             

    def deactivate(self):
        "Sets this button to 'inactive'."
        self.active = False

