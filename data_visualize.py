from ast import Pass
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np 
from sklearn.preprocessing import LabelEncoder, StandardScaler, MinMaxScaler, PowerTransformer


class data_:
    
    def read_file(self, filepath):
        return pd.read_csv(str(filepath))
    
    def get_column_list(self , df):
        column_list = []
        
        for i in df.columns:
            column_list.append(i)
        
        return column_list
    
    def drop_columns(self, df , column):
        return df.drop(column, axis=1)
    
    def standardscale(self, df, target):
        sc = StandardScaler()
        x = df.drop(target, axis=1)
        scaled_features = sc.fit_transform(x)
        scaled_features_df = pd.DataFrame(scaled_features, index=x.index, columns=x.columns)
        scaled_features_df[target] = df[target]
        
        return scaled_features_df
    
    def minmaxscale(self, df, target):
        sc = MinMaxScaler()
        x = df.drop(target, axis=1)
        scaled_features = sc.fit_transform(x)
        scaled_features_df = pd.DataFrame(scaled_features, index=x.index, columns=x.columns)
        scaled_features_df[target] = df[target]
        
        return scaled_features_df
    
    def powerscale(self, df, target):
        sc = PowerTransformer()
        x = df.drop(target, axis=1)
        scaled_features = sc.fit_transform(x)
        scaled_features_df = pd.DataFrame(scaled_features, index=x.index, columns=x.columns)
        scaled_features_df[target] = df[target]
        
        return scaled_features_df
    
    def convert_categori(self, df, column):
        le = LabelEncoder()
        df[column] = le.fit_transform(df[column])
        
        return df[column]
    
    def fillmean(self, df, column):
        df[column].fillna(df[column].mean, inplace=True)
        
        return df[column]
    
    def fillna(self, df, column):
        df[column].fillna(0, inplace=True)
        
        return df[column]
    
    def scatter_plot(self,df,x,y,c,marker):
        plt.figure()
        plt.scatter(df[x],df[y],c=c,marker=marker)
        plt.xlabel(x)
        plt.ylabel(y)
        plt.title(y + " vs "+ x)
        plt.show()
        
    def line_plot(self,df,x,y,c,marker):
        plt.figure()
        plt.plot(df[x],df[y],c=c,marker=marker)
        plt.xlabel(x)
        plt.ylabel(y)
        plt.title(y + " vs "+ x)
        plt.show()