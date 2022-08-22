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