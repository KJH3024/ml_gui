from PyQt5.QtWidgets import *
import sys , pickle
from PyQt5 import uic , QtWidgets 
from data_visualize import data_
from table_display import DataFrameModel

class UI(QMainWindow):
    def __init__(self):
        super(UI , self).__init__()
        uic.loadUi('ui_files/mainwindow.ui' , self)
        
        global data , steps
        data = data_()
        
        
        self.Browse = self.findChild(QPushButton , "Browse")
        self.columns = self.findChild(QListWidget , "listWidget")
        self.table = self.findChild(QTableView, "tableView")
        self.data_shape = self.findChild(QLabel, "shape")
        self.Submit = self.findChild(QPushButton , "Submit")
        self.Target_name = self.findChild(QLabel, "Target_name")
        self.dropcolumn = self.findChild(QComboBox, "drop_column")
        self.drop = self.findChild(QPushButton , "drop")
        self.scaler = self.findChild(QComboBox, "scaler")
        self.scale_btn = self.findChild(QPushButton , "scale_btn")
        
        self.Browse.clicked.connect(self.get_csv)
        self.columns.clicked.connect(self.target)
        self.Submit.clicked.connect(self.set_target)
        self.drop.clicked.connect(self.dropc)
        self.scale_btn.clicked.connect(self.scale_value)
        # self.show()
    def filldetails(self, fleg = 1):
        if fleg == 0:
            self.df = data.read_file(self.file_path)
        
        self.columns.clear()
        self.column_list = data.get_column_list(self.df)
        # print(self.column_list)
        
        for i , j in enumerate(self.column_list):
            stri = f'{j} ------ {str(self.df[j].dtype)}'
            print(stri)
            self.columns.insertItem(i , stri)
            
        x,y = self.df.shape
        self.data_shape.setText(f'({x},{y})')
        self.fill_combo_box()
        
    def fill_combo_box(self):
        self.dropcolumn.clear()
        self.dropcolumn.addItems(self.column_list)
        x = DataFrameModel(self.df)
        self.table.setModel(x)
        
    def target(self):
        self.item = self.columns.currentItem().text().split(' ')[0]
        print(self.columns.currentItem().text().split(' ')[0])
        
    def dropc(self):
        selected = self.dropcolumn.currentText()
        self.df = data.drop_columns(self.df, selected)
        self.filldetails()
        
    def set_target(self):
        self.target_value = self.item
        self.Target_name.setText(self.target_value)
        
    def scale_value(self):
        if self.scaler.currentText() == 'standard scale':
            self.df = data.standardscale(self.df, self.target_value)
        
        elif self.scaler.currentText() == 'minmax scale':
            self.df = data.minmaxscale(self.df, self.target_value)
            
        else:
            self.df = data.powerscale(self.df, self.target_value)
            
        self.filldetails()
        
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