from PyQt4.QtGui import *
from PyQt4.QtCore import *

class CToolBar(QToolBar):

    def __init__(self, parent=None):
        super(CToolBar, self).__init__()
        self.setMovable(False)

        self.favoriteAction = QAction(self)
        self.favoriteAction.setIcon(QIcon("Icons/favorite.png"))

        self.planAction = QAction(self)
        self.planAction.setIcon(QIcon("Icons/plan.png"))

        self.currentlyAction = QAction(self)
        self.currentlyAction.setIcon(QIcon("Icons/currently.png"))

        self.addAction(self.favoriteAction)
        self.addAction(self.planAction)
        self.addAction(self.currentlyAction)

        self.connect(self.favoriteAction, SIGNAL('triggered()'), self.favoriteOperation) 
        self.connect(self.planAction, SIGNAL('triggered()'), self.planOperation)
        self.connect(self.currentlyAction, SIGNAL('triggered()'), self.currentlyOperation)


    def favoriteOperation(self):
        self.newMarksList = []
        self.activated = False
        for i in range(len(self.parent().cWidget.marksList)):
            if self.parent().cWidget.marksList[i] == "favorite":
                self.parent().cWidget.tabWidget.removeTab(i+1)
                self.activated = True
            else:
                self.newMarksList.append(self.parent().cWidget.marksList[i])
        
        self.parent().cWidget.marksList = self.newMarksList
        if self.activated == False:
            self.parent().cWidget.filterForTag("favorite", 0)

    def planOperation(self):
        self.newMarksList = []
        self.activated = False
        for i in range(len(self.parent().cWidget.marksList)):
            if self.parent().cWidget.marksList[i] == "plan":
                self.parent().cWidget.tabWidget.removeTab(i+1)
                self.activated = True
            else:
                self.newMarksList.append(self.parent().cWidget.marksList[i])
        
        self.parent().cWidget.marksList = self.newMarksList
        if self.activated == False:
            self.parent().cWidget.filterForTag("plan", 0)

    def currentlyOperation(self):
        self.newMarksList = []
        self.activated = False
        for i in range(len(self.parent().cWidget.marksList)):
            if self.parent().cWidget.marksList[i] == "currently":
                self.parent().cWidget.tabWidget.removeTab(i+1)
                self.activated = True
            else:
                self.newMarksList.append(self.parent().cWidget.marksList[i])
        
        self.parent().cWidget.marksList = self.newMarksList
        if self.activated == False:
            self.parent().cWidget.filterForTag("currently", 0)
