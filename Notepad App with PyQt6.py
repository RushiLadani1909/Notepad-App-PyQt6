#PRACTICAL -- 14

from PyQt6.QtWidgets import *
#QMenuBar,QMenu,QMainWindow, QTextEdit,QMainWindow, QGridLayout,QHBoxLayout,QVBoxLayout,QMessageBox,QPushButton,QWidget,QApplication,QLabel)
import sys
from PyQt6.QtGui import QAction,QIcon

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("NOTEPAD")
        self.setGeometry(100,100,600,400)

        self.current_file = None

        self.edit_field = QTextEdit(self)
        self.setCentralWidget(self.edit_field)

        # create a menubar
        menubar = QMenuBar(self)
        menubar.setNativeMenuBar(False)
        self.setMenuBar(menubar)

        #creating file menu
        file = QMenu("FILE",self)
        menubar.addMenu(file)

        #create actions
        new_action = QAction("NEW        (ctrl+N)",self)
        file.addAction(new_action)
        new_action.triggered.connect(self.new_file)

        open_action = QAction("OPEN       (ctrl+O)",self)
        file.addAction(open_action)
        open_action.triggered.connect(self.open_file)

        save_action = QAction("SAVE         (ctrl+s)", self)
        file.addAction(save_action)
        save_action.triggered.connect(self.save_file)

        save_as_action = QAction("SAVE AS   (ctrl+sft+s)", self)
        file.addAction(save_as_action)
        save_as_action.triggered.connect(self.save_as_file)


        #ctreating edit menu
        edit_menu = QMenu("EDIT",self)
        menubar.addMenu(edit_menu)

        undo_action = QAction("UNDO",self)
        edit_menu.addAction(undo_action)
        undo_action.triggered.connect(self.edit_field.undo)

        redo_action = QAction("REDO",self)
        edit_menu.addAction(redo_action)
        redo_action.triggered.connect(self.edit_field.redo)

        cut_action = QAction("CUT", self)
        edit_menu.addAction(cut_action)
        cut_action.triggered.connect(self.edit_field.cut)

        paste_action = QAction("PASTE", self)
        edit_menu.addAction(paste_action)
        paste_action.triggered.connect(self.edit_field.paste)

        copy_action = QAction("COPY", self)
        edit_menu.addAction(copy_action)
        copy_action.triggered.connect(self.edit_field.copy)



        # exit_file1 = QMenu("EXIT", self)
        # menubar.addMenu(exit_file1)
        # exit_file1.triggered.connect(self.exit_file)


    def new_file(self):
        print("Created new file")
        self.edit_field.clear()
        self.current_file = None

    def open_file(self):
        print("opening a file")
        file_path,_ = QFileDialog.getOpenFileName(self,"open File","","Text File(*.txt) ;;Python file(*.py);;Pdf file(*.pdf);;All files(*)")
        with open(file_path,"r") as file:
            text = file.read()
            self.edit_field.setText(text)

    def save_as_file(self):
        print("saving a file")
        file_path,_ = QFileDialog.getSaveFileName(self,"SAVE FILE","","Text File(*.txt);; Python file(*.py);;Pdf file(*.pdf);;All files(*)")
        if file_path:
            with open(file_path,"w") as file:
                file.write(self.edit_field.toPlainText())
            self.current_file = file_path

    def save_file(self):
        print("save file as")
        if self.current_file:
            with open(self.current_file,"w") as file:
                file.write(self.edit_field.toPlainText())
        else:
            self.save_as_file()



app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())