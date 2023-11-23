import numpy as np
import pandas as pd

class basicmodel:
    def __init__(self,NDF='1',CNY=2):
        self.data_path = './database/'
        self.data = pd.read_excel(self.data_path'wind_data.xlsx').set_index('Time')
