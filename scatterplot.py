import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.read_excel("output.xlsx", index_col=0)  
x = dataframe[['Name']]
print(x)
y = dataframe[['Market Cap']]
print(y)
data = {'apple': 10, 'orange': 15, 'lemon': 5, 'lime': 20}
names = list(x)
values = list(y)

fig, axs = plt.subplots(1, 6, figsize=(15, 3), sharey=True)
horizontal_stack = pd.concat([x, y], axis=1)
dataframe.plot(kind='bar' , x='Name')


