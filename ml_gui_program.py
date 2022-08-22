from PyQt5.QtWidgets import *
import sys , pickle
from PyQt5 import uic , QtWidgets 
from data_visualize import data_


class UI(QMainWindow):
    def __init__(self):
        super(UI , self).__init__()
        uic.loadUi('ui_files/mainwindow.ui' , self)
        
        global data , steps
        data = data_()
        
        
        self.Browse = self.findChild(QPushButton , "Browse")
        self.columns = self.findChild(QListWidget , "listWidget")
        
        self.Browse.clicked.connect(self.get_csv)
        
        # self.show()
    def filldetails(self, fleg = 1):
        if fleg == 0:
            self.df = data.read_file(self.file_path)
        
        self.columns.clear()
        self.column_list = data.get_column_list(self.df)
        # print(self.column_list)
        
        for i , j in enumerate(self.column_list):
            stri = f'{j}------{str(self.df[j].dtype)}'
            print(stri)
            self.columns.insertItem(i , stri)
    
    def get_csv(self):
        self.file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open File", "", "csv(*.csv)")
        self.columns.clear()
        
        if self.file_path !="":
            self.filldetails(0)
    
    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = UI()
    window.show()
    
    
    sys.exit(app.exec_())