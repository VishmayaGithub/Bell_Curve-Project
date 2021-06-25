import csv
import numpy as np
import pandas as pd
import plotly.figure_factory as ff
import plotly_express as px

read = pd.read_csv('data.csv')
bell_curve = ff.create_distplot([read['Avg Rating']],['Avergae rating'] , show_hist=False)
bell_curve.show()

figure = px.bar(read , x = 'Mobile Brand' , y = 'Avg Rating')
figure.show() 