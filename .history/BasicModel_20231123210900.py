import numpy as np
import pandas as pd
import arch

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
        self.data.columns = ['CNY','CNH','NDF']
    
    def ret(self):
        '''
        获取收益率数据
        '''
        price = self.data.dropna()
        self.ret_data = (price - price.shift(1))/price.shift(1)
        self.ret_data = self.ret_data.dropna()

    def AR_GARCH(self,lags=[1,0,1]):
        '''
        利用AR-GARCH模型获得白噪声残差\n
        lags是模型滞后阶数，默认为AR(1)+GARCH(1,1)联合估计
        '''
        self.std_index = pd.DataFrame()
        for se in ['CNY','CNH','NDF']:
            argarch_model = arch.arch_model(self.ret_data[se],mean='AR',lags=1,vol='GARCH',p=1,o=0,q=1)
            res = argarch_model.fit()
            self.std_index = pd.concat([self.std_index,res.std_resid],axis=1)

        
