from PyQt4.QtGui import *
from PyQt4.QtCore import *

from CWidget import CWidget
from CDialogs import addMediaDialog 

class CMenuBar(QMenuBar):
    
    def __init__(self, parent=None):
        super(CMenuBar, self).__init__()

        self.file = self.addMenu("&File")
        self.database = self.addMenu("&Database")
        self.help = self.addMenu("&Help")

        self.newAction = QAction("New", self)
        self.newAction.setIcon(QIcon("Icons/new.png"))
        self.saveAction = QAction("Save", self)
        self.saveAction.setIcon(QIcon("Icons/save.png"))
        self.exitAction = QAction("Exit", self)
        self.exitAction.setIcon(QIcon("Icons/exit.png"))

        self.addAction = QAction("Add Media", self)
        self.addAction.setIcon(QIcon("Icons/addMedia.png"))

        self.helpAction = QAction("help", self)
        self.aboutAction = QAction("about", self)

        self.file.addAction(self.newAction)
        self.file.addAction(self.saveAction)
        self.file.addSeparator()
        self.file.addAction(self.exitAction)

        self.database.addAction(self.addAction)

        self.help.addAction(self.helpAction)
        self.help.addAction(self.aboutAction)        

        self.connect(self.addAction, SIGNAL("triggered()"), self.addOperation)
        self.connect(self.saveAction, SIGNAL("triggered()"), self.saveOperation)
        self.connect(self.exitAction, SIGNAL("triggered()"), qApp, SLOT("quit()"))
        self.connect(self.aboutAction, SIGNAL("triggered()"), qApp, SLOT("aboutQt()"))

    def saveOperation(self):
        for i in range(len(self.parent().cWidget.listDatabases)):
            self.parent().cWidget.saveDatabase(i);
        print("save complete!")

    def addOperation(self):
        animeList = []
        dialog = addMediaDialog()
        dialog.exec()
        if dialog.editName.text(): 
            animeList = ("no info", dialog.editName.text(), "no info", "0", "0", "no info", "no info", "no info", "no info", "none")
            self.parent().cWidget.listDatabases[0].append(animeList)
            self.parent().cWidget.tabWidget.widget(0).widget().addAnime(animeList)
