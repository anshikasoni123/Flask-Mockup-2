import pandas as pd
import numpy as np

df = pd.read_csv('articles.csv')

df = df.sort_values('totalEvents',ascending=True)
output = df[['contentId','title','timestamp','totalEvents']].head(20)
print(output)