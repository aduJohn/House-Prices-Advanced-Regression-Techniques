import pandas
import numpy
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import datetime
from dateutil.relativedelta import relativedelta

class DataUtils():
    @staticmethod
    def columns_nan_description(df):
        if not isinstance(df,pandas.DataFrame):
            raise Exception('Please insert a pandas dataframe')

        number_of_rows = len(df)
        number_of_columns = len(df.columns)
        number_of_null_columns = len(df.columns[df.isnull().any()])
        print(f'There are {number_of_columns} columns and {number_of_null_columns} ({number_of_null_columns/number_of_columns*100:.2f}%) of them have null values.')
        for column in df.columns:
            if df[column].isnull().any():
                number_of_null_values = df[column].isnull().sum()
                print(f'{column} - {number_of_null_values} values are null - {number_of_null_values/number_of_rows*100:.2f}%')
    
    @staticmethod
    def column_description(column):
        data_description_path = Path('data//input//data_description.txt')
        if not data_description_path.exists():
            raise Exception('The data description file does not exit in "data/input" directory!')
        
        with open(data_description_path,'r') as handle:
            column_found = False
            while line:= handle.readline():
                if column in line:
                    column_found = True
                    print(line)
                if not line[0].isalpha() and column_found:
                    print(line)
                if column not in line and line[0].isalpha():
                    column_found = False
        
    @staticmethod
    def rmse(predictions, targets):
        return numpy.sqrt(((predictions - targets) ** 2).mean())
    
    @staticmethod
    def get_cmap(n, name='magma'):
        '''Returns a function that maps each index in 0, 1, ..., n-1 to a distinct 
        RGB color; the keyword argument name must be a standard mpl colormap name.'''
        return plt.cm.get_cmap(name, n)

    @staticmethod
    def years_between(date1, date2):
        time_difference = relativedelta(date2, date1)   
        difference_in_years = time_difference.years
        return difference_in_years
    
    @staticmethod
    def real_sale_price(us_inflation_rates,nominal_sale_price,real_year,nominal_year):
        real_sale_price = nominal_sale_price
        if real_year < nominal_year:
            if real_year in us_inflation_rates.index:
                denominator = 1
                for cpi in us_inflation_rates.loc[real_year:nominal_year-1]:
                    denominator *= 1+cpi
                real_sale_price = nominal_sale_price / denominator
        return real_sale_price

                


