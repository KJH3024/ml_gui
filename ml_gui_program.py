from PyQt5.QtWidgets import *
import sys , pickle
from PyQt5 import uic , QtWidgets 
from data_visualize import data_
from table_display import DataFrameModel
import linear_reg, logistic_reg, mlp, RandomForest, add_steps

class UI(QMainWindow):
    def __init__(self):
        super(UI , self).__init__()
        uic.loadUi('ui_files/mainwindow.ui' , self)
        
        global data , steps
        data = data_()
        steps = add_steps.add_steps()
        
        
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
        self.cat_column = self.findChild(QComboBox, "cat_column")
        self.convert_btn = self.findChild(QPushButton , "convert_btn")
        self.empty_column = self.findChild(QComboBox, "empty_column")
        self.fill_mean = self.findChild(QPushButton , "fill_mean")
        self.fill_uknown = self.findChild(QPushButton , "fill_uknown")
        self.scatter_x = self.findChild(QComboBox, "scatter_x")
        self.scatter_y = self.findChild(QComboBox, "scatter_y")
        self.scatter_marker = self.findChild(QComboBox, "scatter_marker")
        self.scatter_c = self.findChild(QComboBox, "scatter_c")
        self.scatter_btn = self.findChild(QPushButton , "scatter_btn")
        self.line_x = self.findChild(QComboBox, "line_x")
        self.line_y = self.findChild(QComboBox, "line_y")
        self.line_marker = self.findChild(QComboBox, "line_marker")
        self.line_c = self.findChild(QComboBox, "line_c")
        self.line_btn = self.findChild(QPushButton , "line_btn")
        self.model_select = self.findChild(QComboBox, "model_select")
        self.train_btn = self.findChild(QPushButton , "train_btn")
        
        self.Browse.clicked.connect(self.get_csv)
        self.columns.clicked.connect(self.target)
        self.Submit.clicked.connect(self.set_target)
        self.drop.clicked.connect(self.dropc)
        self.scale_btn.clicked.connect(self.scale_value)
        self.convert_btn.clicked.connect(self.convert_cat)
        self.fill_mean.clicked.connect(self.fillmean)
        self.fill_uknown.clicked.connect(self.fill_na)
        self.scatter_btn.clicked.connect(self.scatter_plot)
        self.line_btn.clicked.connect(self.line_plot)
        self.train_btn.clicked.connect(self.model_train)
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
        
        self.cat_column.clear()
        self.cat_column.addItems(self.column_list)
        
        self.empty_column.clear()
        self.empty_column.addItems(self.column_list)
        
        self.scatter_x.clear()
        self.scatter_x.addItems(self.column_list)
        
        self.scatter_y.clear()
        self.scatter_y.addItems(self.column_list)
        
        self.line_x.clear()
        self.line_x.addItems(self.column_list)
        
        self.line_y.clear()
        self.line_y.addItems(self.column_list)
        
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
        
    def convert_cat(self) :
        selected = self.cat_column.currentText()
        self.df[selected] = data.convert_categori(self.df, selected)
        self.filldetails()
        
    def fillmean(self):
        selected = self.empty_column.currentText()
        type = self.df[selected].dtype
        if type != 'object':
            self.df[selected] = data.fillmean(self.df, selected)
            self.filldetails()
        else:
            print('datatype is object')
        
    def fill_na(self):
        selected = self.empty_column.currentText()
        self.df[selected] = data.fillna(self.df, selected)
        self.filldetails()
        
    def get_csv(self):
        self.file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open File", "", "csv(*.csv)")
        self.columns.clear()
        
        if self.file_path !="":
            self.filldetails(0)
            
    def scatter_plot(self):
        x = self.scatter_x.currentText()
        y = self.scatter_y.currentText()
        marker = self.scatter_marker.currentText()
        c = self.scatter_c.currentText()
        data.scatter_plot(df=self.df, x=x, c=c, y=y, marker=marker)
        
    def line_plot(self):
        x = self.line_x.currentText()
        y = self.line_y.currentText()
        marker = self.line_marker.currentText()
        c = self.line_c.currentText()
        data.line_plot(df=self.df, x=x, c=c, y=y, marker=marker)
        
    def model_train(self):
        myModel = {'LinearRegression': linear_reg, 'randomforrest' : RandomForest, 'rogisticRegression' : logistic_reg, 'MLP' : mlp}
        selected = self.model_select.currentText()
        self.win = myModel[selected].UI(self.df, self.target_value, steps)
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = UI()
    window.show()
    
    
    sys.exit(app.exec_())