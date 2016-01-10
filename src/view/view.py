from PyQt4 import QtCore, QtGui

from ui_view import Ui_MainWindow

class View(QtGui.QMainWindow):

    # properties to read/write widget value
    # @property
    # def running(self):
    #     return self.ui.pushButton_running.isChecked()
    # @running.setter
    # def running(self, value):
    #     self.ui.pushButton_running.setChecked(value)

    def __init__(self, model):
        self.model = model
        super(View, self).__init__()
        self.ui_view = Ui_MainWindow()
        self.ui_view.setupUi(self)
        # register func with model for future model update announcements
        # self.model.subscribe_update_func(self.update_ui_from_model)

    # def build_ui(self):
    #     self.ui = Ui_MainView()
    #     self.ui.setupUi(self)
    #     # connect signal to method 
    #     self.ui.pushButton_running.clicked.connect(self.on_running)

    # def on_running(self):
    #     self.main_ctrl.change_running(self.running)

    # def update_ui_from_model(self):
    #     self.running = self.model.running