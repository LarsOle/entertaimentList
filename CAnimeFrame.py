from PyQt4.QtCore import *
from PyQt4.QtGui import *

from FetchInformation import FetchInformation
from CDialogs import editMediaDialog

class CAnimeFrame(QFrame):
    
    def __init__(self, labels, parent=None):
        super(CAnimeFrame, self).__init__()

        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.setStyleSheet("CAnimeFrame{border: 1px solid black}")

        self.labels = labels
        self.gBox = QGridLayout()
        self.gBox2 = QGridLayout()
        self.gBox3 = QGridLayout()
        self.gBox4 = QGridLayout()
        self.gBox5 = QGridLayout()
     
        self.setFixedHeight(89)         
        self.gBox2.setColumnStretch(1, 1)

        self.pixmap = QPixmap()
        self.pixmap.load(labels[0])
    
        self.font = QFont()
        self.font.setPointSize(13) 

        self.labelPicture = QLabel()
        self.labelPicture.setFixedWidth(50)
        self.labelPicture.setScaledContents(True)
        self.labelPicture.setPixmap(self.pixmap)
        self.labelPicture.setStyleSheet("border: 1px solid black")

        self.labelName = QLabel("<b>" + labels[1] + "</b>", self)
        self.labelName.setFont(self.font)
        self.labelName.setFixedHeight(25)

        self.labelGenre = QLabel("<b>Genre: </b>" + labels[2], self)
        self.labelAirring = QLabel("<b>Current episodes: </b>" + labels[3], self)
        self.labelComplete = QLabel("<b>Episodes: </b>" + labels[4], self)
        self.labelStatus = QLabel("<b>status: </b>" + labels[5], self)
        self.labelAiringDate = QLabel("<b>Airing Date: </b>" + labels[6])
        self.labelType = QLabel("<b>Type: </b>" + labels[7])
        self.labelRating = QLabel("<b>Rating: </b>" + labels[8])
        self.gBox5.addWidget(self.labelName, 0, 0)

        self.favoriteLabel = QLabel()
        self.favoritePix = QPixmap("Icons/favorite.png")
        self.favoriteLabel.setPixmap(self.favoritePix)
        self.favoriteLabel.setFixedWidth(10)
        self.favoriteLabel.setFixedHeight(10)
        self.favoriteLabel.setScaledContents(True)
        self.favoriteLabel.setContextMenuPolicy(Qt.CustomContextMenu)
        if "favorite" in self.labels[9]:
            self.gBox5.addWidget(self.favoriteLabel, 0, 2)
                     
        self.currentlyLabel = QLabel()
        self.currentlyPix = QPixmap("Icons/currently.png")
        self.currentlyLabel.setPixmap(self.currentlyPix)
        self.currentlyLabel.setFixedWidth(15)
        self.currentlyLabel.setFixedHeight(15)
        self.currentlyLabel.setScaledContents(True)
        self.currentlyLabel.setContextMenuPolicy(Qt.CustomContextMenu)
        if "currently" in self.labels[9]:
            self.gBox5.addWidget(self.currentlyLabel, 0, 3)

        self.planLabel = QLabel()
        self.planPix = QPixmap("Icons/plan.png")
        self.planLabel.setPixmap(self.planPix)
        self.planLabel.setFixedWidth(15)
        self.planLabel.setFixedHeight(15)
        self.planLabel.setScaledContents(True)
        self.planLabel.setContextMenuPolicy(Qt.CustomContextMenu)
        if "plan" in self.labels[9]:
            self.gBox5.addWidget(self.planLabel, 0, 4)

        self.gBox.addWidget(self.labelStatus, 0, 0)
        self.gBox.addWidget(self.labelAirring, 0, 1)
        self.gBox.addWidget(self.labelComplete, 0, 2)
        self.gBox.addWidget(self.labelGenre, 1, 3)
        self.gBox.addWidget(self.labelAiringDate, 1, 1)
        self.gBox.addWidget(self.labelType, 1, 2)
        self.gBox.addWidget(self.labelRating, 1, 0)

        self.gBox3.addLayout(self.gBox5, 0, 0)
        self.gBox3.addLayout(self.gBox, 1, 0)

        self.gBox2.addWidget(self.labelPicture, 1, 0)
        self.gBox2.addLayout(self.gBox3, 1, 1)

        self.setLayout(self.gBox2)

        self.favoriteLabel.customContextMenuRequested.connect(self.deleteFavorite)
        self.planLabel.customContextMenuRequested.connect(self.deletePlan)
        self.currentlyLabel.customContextMenuRequested.connect(self.deleteCurrently)
        self.customContextMenuRequested.connect(self.provideContextMenu)

    def provideContextMenu(self, position):
        self.context = QMenu()
        if not "favorite" in self.labels[9] or not "currently" in self.labels[9] or not "plan" in self.labels[9]:
            self.marks = QMenu("marks")
            self.context.addMenu(self.marks)
        if int(self.labels[3]) < int(self.labels[4]):
            self.addEpisode = self.context.addAction("add episode")
            self.addEpisode.setIcon(QIcon("Icons/plus.png"))
        self.fetchAction = self.context.addAction("fetch Information")
        self.fetchAction.setIcon(QIcon("Icons/fetch.png"))
        self.editAction = self.context.addAction("edit information")
        self.editAction.setIcon(QIcon("Icons/edit.png"))
        self.deleteAction = self.context.addAction("delete")
        self.deleteAction.setIcon(QIcon("Icons/delete.png"))
        if not "favorite" in self.labels[9]:
            self.favoriteAction = self.marks.addAction("favorite")
            self.favoriteAction.setIcon(QIcon("Icons/favorite.png"))
        if not "plan" in self.labels[9]:
            self.planAction = self.marks.addAction("plan to watch") 
            self.planAction.setIcon(QIcon("Icons/plan.png"))
        if not "currently" in self.labels[9]:
            self.currentlyAction = self.marks.addAction("currently watching")
            self.currentlyAction.setIcon(QIcon("Icons/currently.png"))

        action = self.context.exec_(self.mapToGlobal(position))
        if self.fetchAction == action:
            self.fetchInformation()
        if self.deleteAction == action:
            self.deleteFrame()
        if self.editAction == action:
            self.editInformation()
        if int(self.labels[3]) < int(self.labels[4]):
            if self.addEpisode == action:
                self.addOperation()
        if not "favorite" in self.labels[9]:
            if self.favoriteAction == action:
                self.favoriteOperation()
        if not "plan" in self.labels[9]:
            if self.planAction == action:
                self.planOperation()
        if not "currently" in self.labels[9]:
            if self.currentlyAction == action:
                self.currentlyOperation()

    def fetchInformation(self):
        information = FetchInformation(self.labels, "larsole12", "Shandra13")
        self.labels = information.fetchInformation()
        self.parent().parent().parent().parent().parent().parent().changeValue(self.labels, 0)
        self.labelComplete.setText("<b>Episodes: </b>" + self.labels[4])
        self.labelStatus.setText("<b>status: </b>" + self.labels[5],)
        self.labelAiringDate.setText("<b>Airing Date: </b>" + self.labels[6])
        self.labelType.setText("<b>Type: </b>" + self.labels[7])
        self.labelRating.setText("<b>Rating: </b>" + self.labels[8])
        self.pixmap.load(self.labels[0])
        self.labelPicture.setPixmap(self.pixmap)
        
    def deleteFrame(self): 
        self.parent().parent().parent().parent().parent().parent().deleteEntry(self.labels, 0)
        self.setParent(None)

    def addOperation(self):
        newLabels = []
        for i in range(0, len(self.labels)):
            if i == 3:
                newLabels.append(str(int(self.labels[3]) + 1))   
            if i != 3:
                newLabels.append(self.labels[i]) 
        self.parent().parent().parent().parent().parent().parent().changeValue(newLabels, 0)
        self.labels = newLabels
        self.labelAirring.setText("<b>Current episodes: </b>" + self.labels[3])

    def favoriteOperation(self):
        newLabels = []
        for i in range(0, len(self.labels)):
            if i == 9:
                newLabels.append(self.labels[9] + "favorite")   
            if i != 9:
                newLabels.append(self.labels[i]) 
        self.parent().parent().parent().parent().parent().parent().changeValue(newLabels, 0)
        self.labels = newLabels
        self.gBox5.addWidget(self.favoriteLabel, 0, 1)

    def deleteFavorite(self):
        newLabels = []
        for i in range(0, len(self.labels)):
            if i == 9:
                newLabels.append(self.labels[9].replace("favorite", ""))   
            if i != 9:
               newLabels.append(self.labels[i]) 
        self.parent().parent().parent().parent().parent().parent().changeValue(newLabels, 0)
        self.labels = newLabels
        self.favoriteLabel.setParent(None) 

    def planOperation(self):
        newLabels = []
        for i in range(0, len(self.labels)):
            if i == 9:
                newLabels.append(self.labels[9] + "plan")   
            if i != 9:
                newLabels.append(self.labels[i]) 
        self.parent().parent().parent().parent().parent().parent().changeValue(newLabels, 0)
        self.labels = newLabels
        self.gBox5.addWidget(self.planLabel, 0, 3)

    def deletePlan(self):
        newLabels = []
        for i in range(0, len(self.labels)):
            if i == 9:
                newLabels.append(self.labels[9].replace("plan", ""))   
            if i != 9:
               newLabels.append(self.labels[i]) 
        self.parent().parent().parent().parent().parent().parent().changeValue(newLabels, 0)
        self.labels = newLabels
        self.planLabel.setParent(None)

    def currentlyOperation(self):
        newLabels = []
        for i in range(0, len(self.labels)):
            if i == 9:
                newLabels.append(self.labels[9] + "currently")   
            if i != 9:
                newLabels.append(self.labels[i]) 
        self.parent().parent().parent().parent().parent().parent().changeValue(newLabels, 0)
        self.labels = newLabels
        self.gBox5.addWidget(self.currentlyLabel, 0, 2) 

    def deleteCurrently(self):
        newLabels = []
        for i in range(0, len(self.labels)):
            if i == 9:
                newLabels.append(self.labels[9].replace("currently", ""))   
            if i != 9:
               newLabels.append(self.labels[i]) 
        self.parent().parent().parent().parent().parent().parent().changeValue(newLabels, 0)
        self.labels = newLabels
        self.currentlyLabel.setParent(None)

    def editInformation(self):
        newLabels = []
        dialog = editMediaDialog(self.labels)
        dialog.exec()
        if dialog.airringEdit.text() and dialog.genreEdit.text() and dialog.currentEdit.text() and dialog.maxEdit.text() and dialog.ratingEdit.text():
            newLabels.append(self.labels[0])
            newLabels.append(self.labels[1])
            newLabels.append(dialog.genreEdit.text())
            newLabels.append(dialog.currentEdit.text())
            newLabels.append(dialog.maxEdit.text())
            newLabels.append(dialog.comboBoxStatus.currentText())
            newLabels.append(dialog.airringEdit.text())
            newLabels.append(dialog.comboBoxType.currentText())
            newLabels.append(dialog.ratingEdit.text())
            newLabels.append(self.labels[9])
            self.labels = newLabels
            self.parent().parent().parent().parent().parent().parent().changeValue(newLabels, 0)
            self.labelComplete.setText("<b>Episodes: </b>" + self.labels[4])
            self.labelGenre.setText("<b>Genre: </b>" + self.labels[2])
            self.labelStatus.setText("<b>status: </b>" + self.labels[5],)
            self.labelAiringDate.setText("<b>Airing Date: </b>" + self.labels[6])
            self.labelType.setText("<b>Type: </b>" + self.labels[7])
            self.labelRating.setText("<b>Rating: </b>" + self.labels[8])
            self.labelAirring.setText("<b>Current episodes: </b>" + self.labels[3])
