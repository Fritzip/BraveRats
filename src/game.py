#! /usr/bin/python2
# -*- coding: utf-8 -*-

import numpy as np
import sys

from player import *

class Game():
    
    def __init__(self, p1,p2):
        self.ps = {1 : {"p" : p1, "cards" : range(8), "bonus" : [], "points" : 0, "color" : "red"},
                   2 : {"p" : p2, "cards" : range(8), "bonus" : [], "points" : 0, "color" : "blue"}}
        self.l_rounds = []
        self.m_results = np.matrix([[0,0,0,0,0,2,0,0],
                                    [0,0,2,1,2,2,2,3],
                                    [0,1,0,1,2,2,2,2],
                                    [0,2,2,0,1,2,1,2],
                                    [0,1,1,2,0,2,2,2],
                                    [1,1,1,1,1,0,2,2],
                                    [0,1,1,2,1,1,0,2],
                                    [0,4,1,1,1,1,1,0]])
        self.d_results = {0 : self.nullifie, 1 : self.update_scores, 2 : self.update_scores,
                          3 : self.game_over, 4 : self.game_over}
                                   
    def run(self):
        for round in xrange(8) :
            print "-> Round %s/8" % (round+1)
            card_p1 = self.ps[1]["p"].choose_card(self.ps[1]["cards"])
            card_p2 = self.ps[2]["p"].choose_card(self.ps[2]["cards"])
            self.update_cards(card_p1,card_p2)
            win_round = self.evaluate_round(card_p1,card_p2)
            win = self.ps[win_round]["p"].name if win_round != "?" else "Nullified"
            print "(%s) %s / %s (%s) => %s" % (self.ps[1]["p"].name,card_p1,card_p2,self.ps[2]["p"].name,win)
            print "%s : %s, %s : %s" % (self.ps[1]["p"].name,self.ps[1]["points"],self.ps[2]["p"].name,self.ps[2]["points"])
            print self.l_rounds
            
    def update_cards(self,card_p1,card_p2):
        self.ps[1]["cards"].remove(card_p1)
        self.ps[2]["cards"].remove(card_p2)   
                 
    def evaluate_round(self,card_p1,card_p2):
        result = self.m_results[card_p1,card_p2]
        win_round = self.d_results[result](result%2+(1-result%2)*2) ## TODO: Améliorer calcul
        self.update_round(card_p1,card_p2,win_round)
        return win_round
        
    def update_scores(self,player):
        if self.l_rounds and self.l_rounds[-1][-1] == "?" : 
            self.l_rounds[-1][-1] = player
            self.ps[player]["points"] += 1
        self.ps[player]["points"] += 1
        if self.ps[player]["points"] >= 4 : self.game_over(player)
        else : return player
    
    def nullifie(self,val):
        return "?"
               
    def update_round(self,card_p1,card_p2,win):
        self.l_rounds.append([(card_p1,card_p2),win])
        
    def game_over(self,player):
        print "Game Over : %s win !!!" % self.ps[player]["p"].name
        sys.exit()
        
        
if __name__ == '__main__' : 

    P1 = Player("Bob")
    P2 = Player("Albert")
    G = Game(P1,P2)
    G.run()
