from PyQt4 import QtCore, QtGui

class Controller():

    def __init__(self, model, view):
        self.model = model
        self.view = view

    # called from view class
    # def change_running(self, checked):
    #     # put control logic here
    #     self.model.running = checked
    #     self.model.announce_update()