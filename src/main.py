import sys
from PyQt4 import QtCore, QtGui
sys.path.append("view/")
import view

class Launcher(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = view.Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = Launcher()
    myapp.show()
    sys.exit(app.exec_())