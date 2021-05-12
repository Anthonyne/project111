import plotly.figure_factory as ff
import plotly.graph_objects as go 
import statistics
import random
import pandas as pd
import csv
df= pd.read_csv('studentMarks.csv')
data=df['Math_score'].tolist()
fig=ff.create_distplot([data], ["Math Scores"],show_hist=False)
fig.show()
mean = statistics.mean(data)
std_deviation = statistics.stdev(data)
print("mean",mean)
print("std",std_deviation)