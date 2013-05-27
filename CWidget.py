from PyQt4.QtGui import *
from PyQt4.QtCore import *

from CMainFrame import CMainFrame
from XMLFileOperations import XMLFileOperations

from sys import argv, exit

class CWidget(QWidget):

    def __init__(self, parent=None):
        super(CWidget, self).__init__()

        self.databaseInformation = [] 
        self.databaseInformation.append(("animeDatabase.xml", "animeDatabase", "anime", ("picture", "name", "genre", "watched", "episodes", "status", "airingdate", "type", "rating", "marks")))
        self.listDatabases = []
        self.fileXML = XMLFileOperations()
        self.marksList = []

        self.tabWidget = QTabWidget()
        self.tabWidget.setTabsClosable(False)
                                      
        self.vBox = QVBoxLayout()
        self.vBox.addWidget(self.tabWidget)

        self.setLayout(self.vBox)
    
    def addTab(self, items, tabLabel):
        self.mainFrame = CMainFrame(items)
        self.mainFrame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.scrollArea = QScrollArea()
        self.scrollArea.setWidget(self.mainFrame)
        self.scrollArea.setWidgetResizable(True) 
        self.tabWidget.addTab(self.scrollArea, tabLabel) 

    def changeValue(self, mediaList, database):
        for i in range(0, len(self.listDatabases[database])):
            if mediaList[1] == self.listDatabases[database][i][1]:
                self.listDatabases[database][i] = mediaList

    def refreshTab(self, labels):
        self.tabWidget.clear()
        for i in range(0, len(self.listDatabases)):
            self.addTab(labels, self.databaseInformation[i][2])

    def deleteEntry(self, mediaList, database):
        for i in range(0, len(self.listDatabases[database])):
            if mediaList[1] == self.listDatabases[database][i][1]:
                self.listDatabases[database].pop(i)
                break

    def saveDatabase(self, number):
        self.fileXML.writeXMLFile(self.databaseInformation[number][1], self.databaseInformation[number][0], self.databaseInformation[number][2], self.databaseInformation[number][3], self.listDatabases[number])

    def filterForTag(self, tag, database):
        tagList = []
        for item in self.listDatabases[database]:
            if tag in item[9]:
                tagList.append(item)
        self.addTab(tagList, tag)
        self.marksList.append(tag)
