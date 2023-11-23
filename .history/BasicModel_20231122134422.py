import numpy as np
import pandas as pd

class basicmodel:
    def __init__(self,NDF='3M',CNY='middle',CNH='close'):
        '''
        CNY:'middle','NEX'\n
        CNH:'middle','NEX'\n
        NDF:'3M','1M','6M'\n
        '''
        #设置数据库位置
        self.data_path = './database/'
        self.data = pd.read_excel(self.data_path+'wind_data.xlsx').set_index('Time')
        columns_name = ['中国:中间价:美元兑人民币','USDCNH:即期汇率定盘价','USDCNY:NDF:3个月']
        #NDF
        if NDF == '1M':
            columns_name[2] = 'USDCNY:NDF:1个月'
        elif NDF == '6M':
            columns_name[2] = 'USDCNY:NDF:6个月'
        #CNY
        if CNY == 'NEX':
            columns_name[0] = 'USDCNY:即期汇率'
        #CNH
        if CNH == 'NEX':
            columns_name[1] = 'USDCNH:即期汇率'
        self.data = self.data[columns_name]

