import numpy as np
import pandas as pd

class basicmodel:
    def __init__(self,NDF='1',CNY=2):
        self.datapath = './database/'
        self.data = pd.read_excel('./database/wind_data.xlsx').set_index('指标名称')
