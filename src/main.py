import sys
from PyQt4 import QtCore, QtGui

from model.game import Game
from model.player import Player
from controller.controller import Controller
from view.view import View

class App(QtGui.QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        P1 = Player("Bob")
        P2 = Player("Albert")
        self.model = Game(P1, P2)
        self.view = View(self.model)
        self.controller = Controller(self.model, self.view)
        self.view.show()

if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec_())