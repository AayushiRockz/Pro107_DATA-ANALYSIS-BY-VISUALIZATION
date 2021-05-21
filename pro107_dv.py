import pandas as pd
import plotly.express as px

df = pd.read_csv('pro107_data.csv')

mean = df.groupby(['student_id','level'],as_index=False)["attempt"].mean()

print(mean)

fig  =px.scatter(mean, x="student_id",  y="level", color='attempt',size="attempt",color_continuous_scale=px.colors.cyclical.HSV)
fig.show()