import numpy as np
import pandas as pd

class basicmodel:
    def __init__(self,NDF='3M',CNY='middle',CNH=''):
        '''
        
        '''
        #设置数据库位置
        self.data_path = './database/'
        self.data = pd.read_excel(self.data_path'wind_data.xlsx').set_index('Time')