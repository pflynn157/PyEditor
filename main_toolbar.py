from PyQt5.QtWidgets import (
	QToolBar,
	QToolButton)
from PyQt5.QtGui import QIcon
from tabpane import TabPane
from file_actions import FileActions

class MainToolBar(QToolBar):
	tabs = 0
	
	def __init__(self, tabPane):
		super().__init__()
		
		self.tabs = tabPane
		
		newButton = QToolButton()
		openButton = QToolButton()
		saveButton = QToolButton()
		saveAsButton = QToolButton()
		cutButton = QToolButton()
		copyButton = QToolButton()
		pasteButton = QToolButton()
		undoButton = QToolButton()
		redoButton = QToolButton()
		
		newButton.setIcon(QIcon.fromTheme("document-new"))
		openButton.setIcon(QIcon.fromTheme("document-open"))
		saveButton.setIcon(QIcon.fromTheme("document-save"))
		saveAsButton.setIcon(QIcon.fromTheme("document-save-as"))
		cutButton.setIcon(QIcon.fromTheme("edit-cut"))
		copyButton.setIcon(QIcon.fromTheme("edit-copy"))
		pasteButton.setIcon(QIcon.fromTheme("edit-paste"))
		undoButton.setIcon(QIcon.fromTheme("edit-undo"))
		redoButton.setIcon(QIcon.fromTheme("edit-redo"))
		
		newButton.clicked.connect(self.newButtonClicked)
		openButton.clicked.connect(self.openButtonClicked)
		saveButton.clicked.connect(self.saveButtonClicked)
		saveAsButton.clicked.connect(self.saveAsButtonClicked)
		cutButton.clicked.connect(self.cutButtonClicked)
		copyButton.clicked.connect(self.copyButtonClicked)
		pasteButton.clicked.connect(self.pasteButtonClicked)
		undoButton.clicked.connect(self.undoButtonClicked)
		redoButton.clicked.connect(self.redoButtonClicked)
		
		self.addWidget(newButton)
		self.addWidget(openButton)
		self.addWidget(saveButton)
		self.addWidget(saveAsButton)
		self.addSeparator()
		self.addWidget(cutButton)
		self.addWidget(copyButton)
		self.addWidget(pasteButton)
		self.addWidget(undoButton)
		self.addWidget(redoButton)
		
	def newButtonClicked(self):
		self.tabs.addNewUntitledTab()

	def openButtonClicked(self):
		FileActions.openFile(self.tabs)
		
	def saveButtonClicked(self):
		FileActions.saveFile(self.tabs)
		
	def saveAsButtonClicked(self):
		FileActions.saveFileAs(self.tabs)
		
	def cutButtonClicked(self):
		edit = self.tabs.getCurrentWidget()
		edit.cut()
		
	def copyButtonClicked(self):
		edit = self.tabs.getCurrentWidget()
		edit.copy()
		
	def pasteButtonClicked(self):
		edit = self.tabs.getCurrentWidget()
		edit.paste()
		
	def undoButtonClicked(self):
		edit = self.tabs.getCurrentWidget()
		edit.undo()
		
	def redoButtonClicked(self):
		edit = self.tabs.getCurrentWidget()
		edit.redo()

 
