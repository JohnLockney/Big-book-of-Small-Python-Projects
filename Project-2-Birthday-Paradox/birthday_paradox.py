#!/usr/bin/env python

""" Birthday Paradox Simulation, by Al Sweigart al@inventwithpython.com
Explore the surprising probabilities of teh "Birthday Paradox"
More info at https://en.wikipedia.org/wiki/Birthday_problem
View this code at https://nostarch.com/big-book-small-python-projects
Tags: short, math, simulation
"""
import datetime, random

def getBirthdays(numberOfBirthdays):
    """Returns a list of of number random date objects for birthdays """
    birthdays = []
