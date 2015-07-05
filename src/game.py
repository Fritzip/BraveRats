#! /usr/bin/python2
# -*- coding: utf-8 -*-

import numpy as np
import sys

from player import *

class Game():
    
    def __init__(self, p1, p2):
        self.ps = {1 : {"p" : p1, "cards" : range(8), "card" : -1, "bonus" : {"victories" : 0, "round_pts" : 0}, "points" : 0, "color" : "red"},
                   2 : {"p" : p2, "cards" : range(8), "card" : -1, "bonus" : {"victories" : 0, "round_pts" : 0}, "points" : 0, "color" : "blue"}}

        self.cur = {"reveal_first" : 0, "diff_scr" : 0}

        self.l_rounds = []

        self.m_results = np.array([[ [[ ],0],   [[ ],0],   [[2  ],0],   [[   ],0],   [[   ],0],   [[],5],   [[2  ],0],   [[],0]  ],
                                    [ [[ ],0],   [[ ],5],   [[2  ],5],   [[2  ],5],   [[2  ],5],   [[],5],   [[2  ],5],   [[],3]  ],
                                    [ [[1],0],   [[1],5],   [[   ],5],   [[1,2],5],   [[1,2],5],   [[],5],   [[1,2],5],   [[],2]  ],
                                    [ [[ ],0],   [[1],5],   [[1,2],5],   [[1  ],5],   [[1,2],5],   [[],5],   [[1,2],5],   [[],2]  ],
                                    [ [[ ],0],   [[1],5],   [[1,2],5],   [[1,2],5],   [[1,2],5],   [[],5],   [[1,2],5],   [[],2]  ],
                                    [ [[ ],5],   [[ ],5],   [[   ],5],   [[   ],5],   [[   ],5],   [[],5],   [[   ],5],   [[],2]  ],
                                    [ [[1],0],   [[1],5],   [[1,2],5],   [[1,2],5],   [[1,2],5],   [[],5],   [[1,2],5],   [[],2]  ],
                                    [ [[ ],0],   [[ ],4],   [[   ],1],   [[   ],1],   [[   ],1],   [[],1],   [[   ],1],   [[],5]  ]])

    def run(self):
        card = []
        for round in xrange(8) :
            print "-> Round %s/8" % (round+1)
            #TODO reveal first
            self.ps[1]["card"] = self.ps[1]["p"].choose_card(self.ps[1]["cards"])
            self.ps[2]["card"] = self.ps[2]["p"].choose_card(self.ps[2]["cards"])
            self.update_cards()
            #TODO reinitialize reveal first here
            win_round = self.evaluate_round()
            print "win_round = ", win_round
            win = self.ps[win_round]["p"].name if win_round != "?" else "Nullified"
            self.reinitialize()
            print "(%s) %s / %s (%s) => %s" % (self.ps[1]["p"].name, self.ps[1]["card"], self.ps[2]["card"], self.ps[2]["p"].name,win)
            print "%s : %s, %s : %s" % (self.ps[1]["p"].name, self.ps[1]["points"], self.ps[2]["p"].name, self.ps[2]["points"])
            print self.l_rounds

    def reinitialize(self):
        for player in [1,2]:
            self.ps[player]["bonus"]["victories"] = 0

    def update_cards(self):
        self.ps[1]["cards"].remove(self.ps[1]["card"])
        self.ps[2]["cards"].remove(self.ps[2]["card"])

    def evaluate_round(self):
        self.cur["diff_scr"] = self.ps[1]["card"] + self.ps[1]["bonus"]["round_pts"] - self.ps[2]["card"] + self.ps[2]["bonus"]["round_pts"]

        for player in [1,2]: self.ps[player]["bonus"]["round_pts"] = 0

        result = self.m_results[self.ps[1]["card"]][self.ps[2]["card"]]
        for i in result[0]: self.apply_power(i)

        return self.get_winner(result[1])

    def get_winner(self, val):
        if val == 0:
            win_round = self.nullifie()
        elif val <= 2:
            win_round = self.update_scores(val)
        elif val <= 4:
            win_round = self.game_over(val - 2)
        elif val == 5:
            if self.cur["diff_scr"] != 0: win_round = self.update_scores(((np.sign(-self.cur["diff_scr"])+1)/2)+1)
            else: win_round = self.nullifie()
        else:
            print "C'est impossible !!"
       
        self.update_round(win_round)
        return win_round

    def apply_power(self, player):
        if self.ps[player]["card"] == 2: # reveal card
            self.cur["reveal_first"] = (player%2)+1
            print "%s must reveal first next round"% self.ps[(player%2)+1]["p"].name
        elif self.ps[player]["card"] == 3: # lowest wins
            self.cur["diff_scr"] = -self.cur["diff_scr"]
            print "Lowest wins"
        elif self.ps[player]["card"] == 4: # +2 victories
            self.ps[player]["bonus"]["victories"] = 1
            print "Count 2 victories if you win : %s"% self.ps[player]["p"].name
        elif self.ps[player]["card"] == 6: # +2 round pts next round
            self.ps[player]["bonus"]["round_pts"] = 2
            print "+2 next round for %s"% self.ps[player]["p"].name
        else: 
            print "C'est impossible !!"

    def update_scores(self, player):
        if self.l_rounds and self.l_rounds[-1][-1] == "?" : 
            self.l_rounds[-1][-1] = player
            self.ps[player]["points"] += 1
        self.ps[player]["points"] += 1 + self.ps[player]["bonus"]["victories"]
        if self.ps[player]["points"] >= 4 : self.game_over(player)
        else : return player
    
    def nullifie(self):
        return "?"

    def update_round(self, win):
        self.l_rounds.append([(self.ps[1]["card"], self.ps[2]["card"]), win])
        
    def game_over(self, player):
        print "Game Over : %s win !!!" % self.ps[player]["p"].name
        sys.exit()
        
        
if __name__ == '__main__' : 

    P1 = Player("Bob")
    P2 = Player("Albert")
    G = Game(P1,P2)
    G.run()
