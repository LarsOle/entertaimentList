from PyQt4.QtCore import *
from PyQt4.QtGui import *

from CWidget import CWidget
from CMenuBar import CMenuBar
from CToolBar import CToolBar

from sys import argv, exit

class CMainWindow(QMainWindow):
    
    def __init__(self, parent=None):
        super(CMainWindow, self).__init__()

        self.setMinimumSize(800,600)
        self.setWindowTitle("Media Database")

        self.cWidget = CWidget()
        self.cMenuBar = CMenuBar()
        self.cToolBar = CToolBar()

        self.setCentralWidget(self.cWidget)
        self.setMenuBar(self.cMenuBar)
        self.addToolBar(self.cToolBar)

        self.cWidget.listDatabases.append(self.cWidget.fileXML.readXMLFile("animeDatabase.xml","anime",("picture","name","genre","watched","episodes","status","airingdate","type","rating","marks")))
       
        self.cWidget.addTab(self.cWidget.listDatabases[0], "Animes")


if __name__ == "__main__":
    app = QApplication(argv)
    main = CMainWindow()
    main.show() 
    exit(app.exec_())
