#! /usr/bin/python2
# -*- coding: utf-8 -*-

CARDS = ["Magicien",
        "Princesse",
        "Espion",
        "Assassin",
        "Ambassadeur",
        "Sorcier",
        "General",
        "Prince"]

POWERS = ["The round is nullified",
        "Against the prince you win",
        "Next round your opponents reveal his card", # todo
        "The lowest streigth wins",
        "This round count 2 victories if you win it",
        "Nullified opponent's card power",
        "+2 for your next round", 
        "You win the round"]

class Player():
    
    def __init__(self, name):
        self.name = name
      
    def choose_card(self, cards):
        print "%s, choose a card to play" % self.name
        for c in cards : print "- (%s) %s (%s)" %(c,CARDS[c],POWERS[c])
        #while True :
            #try :
        choice = input("Choice : ")
                #if choice-1 in cards : break
                
            #except : continue
        return choice
           