from PySide6.QtWidgets import QMainWindow, QToolBar
from PySide6.QtGui import QIcon, QAction

class BaseMainWindow(QMainWindow):
    def __init__(self, title, icon, width, height):
        super().__init__()
        self.setWindowTitle(title)
        self.setWindowIcon(QIcon(icon))
        self.resize(width, height)

        self.toolBar = None
    
    def addMenuAction(self, menuName, actionName, handler=None):
        menu = None

        for action in self.menuBar().actions():
            if action.menu() and action.text() == menuName:
                menu = action.menu()
        if menu == None:
            menu = self.menuBar().addMenu(menuName)
        
        a = QAction(actionName, self)
        if handler:
            a.triggered.connect(handler)
        menu.addAction(a)

    def addMenuSeparator(self, menuName):
        for action in self.menuBar().actions():
            if action.menu() and action.text() == menuName:
                action.menu().addSeparator()
    
    def addToolbarAction(self, icon, tooltip, handler):
        if not self.toolBar:
            self.toolBar = QToolBar()
            self.toolBar.setMovable(False)
            self.addToolBar(self.toolBar)
        action = QAction(QIcon(icon), tooltip, self)
        action.triggered.connect(handler)
        self.toolBar.addAction(action)