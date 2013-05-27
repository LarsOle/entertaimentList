from PyQt4.QtGui import *
from PyQt4.QtCore import *

from CAnimeFrame import CAnimeFrame

class CMainFrame(QWidget):

    def __init__(self, items, parent=None):
        super(CMainFrame, self).__init__()

        self.vBox = QVBoxLayout()
        self.vBox.setAlignment(Qt.AlignTop)
        self.animeList = items        

        newAnimeList = sorted(items, key=lambda anime:anime[1])
        for item in newAnimeList:
            anime = CAnimeFrame((item[0],item[1],item[2],item[3],item[4],item[5],item[6],item[7],item[8], item[9]))
            self.vBox.addWidget(anime) 

        self.setLayout(self.vBox)

    def addAnime(self, labels):
        newAnime = CAnimeFrame((labels[0], labels[1], labels[2], labels[3], labels[4], labels[5], labels[6], labels[7], labels[8], labels[9]))
        self.vBox.addWidget(newAnime)
