import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('vgsales.csv')
df = df.dropna(subset=['Year', 'Genre', 'Global_Sales'])
df = df.filter(items=['Year', 'Genre', 'Global_Sales'])
df = df.groupby(['Year', 'Genre']).agg({'Global_Sales': 'sum'}).reset_index()
df = df.pivot(index='Year', columns='Genre', values='Global_Sales')

plt.figure(figsize=(12, 8))
ax = df.plot(kind='line', marker='o', linewidth=2, markersize=6, figsize=(12, 6))
plt.title('Global Sales Per Year and Genre', fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Global Sales (Millions)', fontsize=14)
plt.legend(title='Genre', title_fontsize=12, fontsize=10, loc='upper left')
plt.grid(True, linestyle='--', alpha=0.7)
plt.style.use('ggplot')
plt.show()