from PyQt4.QtCore import *
from PyQt4.QtGui import *

class addMediaDialog(QDialog):

    def __init__(self, parent=None):
        super(addMediaDialog, self).__init__()

        self.setMaximumSize(0,0)
        self.gridLayout = QGridLayout()
        self.vBox = QVBoxLayout()
        self.setWindowTitle("Add media")
        
        self.labelName = QLabel("Name:")

        self.editName = QLineEdit()
        
        self.gridLayout.addWidget(self.labelName, 0, 0)

        self.gridLayout.addWidget(self.editName, 0, 1)

        self.buttonBox = QDialogButtonBox(self)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.vBox.addLayout(self.gridLayout)
        self.vBox.addWidget(self.buttonBox)

        self.setLayout(self.vBox)

        QObject.connect(self.buttonBox, SIGNAL("accepted()"), self.accept)
        QObject.connect(self.buttonBox, SIGNAL("rejected()"), self.reject)
        QMetaObject.connectSlotsByName(self)

class editMediaDialog(QDialog):
    
    def __init__(self, labels, parent=None):
        super(editMediaDialog, self).__init__()

        self.setMaximumSize(0,0)
        self.gridLayout = QGridLayout()
        self.vBox = QVBoxLayout()
        self.setWindowTitle("edit Media")
    
        self.labelName = QLabel("<b>" + labels[1] + "</b>")
        self.font = QFont()
        self.font.setPointSize(13) 
        self.labelName.setFont(self.font)

        self.comboBoxStatus = QComboBox()
        self.comboBoxStatus.addItem("Airring")
        self.comboBoxStatus.addItem("Finished Airring")

        self.comboBoxType = QComboBox()
        self.comboBoxType.addItem("TV")
        self.comboBoxType.addItem("OVA")
        self.comboBoxType.addItem("Movie")

        self.labelCurrent = QLabel("Current episodes: ")
        self.currentEdit = QLineEdit()
        self.currentEdit.setMinimumWidth(20)
        self.currentEdit.setText(labels[3])

        self.labelMax = QLabel("Episodes: ")
        self.maxEdit = QLineEdit()
        self.maxEdit.setMinimumWidth(20)
        self.maxEdit.setText(labels[4])

        self.labelAirring = QLabel("Airring Date: ")
        self.airringEdit = QLineEdit()
        self.airringEdit.setMinimumWidth(90)
        self.airringEdit.setText(labels[6])

        self.labelGenre = QLabel("Genre: ")
        self.genreEdit = QLineEdit()
        self.genreEdit.setMinimumWidth(70)
        self.genreEdit.setText(labels[2])

        self.labelRating = QLabel("Rating: ")
        self.ratingEdit = QLineEdit()
        self.ratingEdit.setMinimumWidth(20)
        self.ratingEdit.setText(labels[8])

        self.gridLayout.addWidget(self.labelAirring, 0, 0)
        self.gridLayout.addWidget(self.airringEdit, 0, 1)
        self.gridLayout.addWidget(self.labelGenre, 0, 2)
        self.gridLayout.addWidget(self.genreEdit, 0, 3)
        self.gridLayout.addWidget(self.labelCurrent, 1, 0)
        self.gridLayout.addWidget(self.currentEdit, 1, 1)
        self.gridLayout.addWidget(self.labelMax, 1, 2)
        self.gridLayout.addWidget(self.maxEdit, 1, 3)
        self.gridLayout.addWidget(self.labelRating, 2, 0)
        self.gridLayout.addWidget(self.ratingEdit, 2, 1)
        

        self.buttonBox = QDialogButtonBox(self)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.vBox.addWidget(self.labelName)
        self.vBox.addWidget(self.comboBoxStatus)
        self.vBox.addWidget(self.comboBoxType)
        self.vBox.addLayout(self.gridLayout)
        self.vBox.addWidget(self.buttonBox)

        self.setLayout(self.vBox)

        QObject.connect(self.buttonBox, SIGNAL("accepted()"), self.accept)
        QObject.connect(self.buttonBox, SIGNAL("rejected()"), self.reject)
        QMetaObject.connectSlotsByName(self)
