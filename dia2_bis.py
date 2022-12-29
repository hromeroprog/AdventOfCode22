# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 09:58:42 2022

@author: romer
"""
def point_game(his_play, my_play):
    if his_play == "rock":
        if my_play =="rock":
            return 3
        elif my_play =="paper":
            return 6
        else: return 0
    if his_play == "scissors":
        if my_play =="rock":
            return 6
        elif my_play =="paper":
            return 0
        else: return 3
    if his_play == "paper":
        if my_play =="rock":
            return 0
        elif my_play =="paper":
            return 3
        else: return 6
     
def get_my_play(his_play, result):
    if result == "Y":
        return his_play
    elif result == "X":
        if his_play == "rock":
            return "scissors"
        elif his_play == "scissors":
            return "paper"
        else:
            return "rock"
    else:
        if his_play == "rock":
            return "paper"
        elif his_play == "scissors":
            return "rock"
        else:
            return "scissors"
        
    
with open("input.txt") as file:
    lines = [line[:-1] for line in file.readlines()]
    
points_form = {"rock": 1, "paper":2, "scissors":3}

equality_other = {"A":"rock", "B": "paper", "C": "scissors"}

total_points = 0
for line in lines:
    other,res = line.split(" ")
    other = equality_other[other]
    me = get_my_play(other, res)
    print(f"Plays: {other} I play {me} ({res}) which results in +{point_game(other, me) + points_form[me]}")
    total_points += point_game(other, me) + points_form[me]



