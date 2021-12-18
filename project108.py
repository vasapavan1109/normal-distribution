import pandas as pd
import plotly.express as px
import csv
import plotly.figure_factory as ff
df = pd.read_csv(r"normaldistribution.csv")
fig = ff.create_distplot([df["Avg Rating"].tolist()],["Project108"])
fig.show()