import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('vgsales.csv')
df = df.dropna(subset=['Publisher', 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales'])

games_per_publisher = df.groupby('Publisher').size() # count number lines per same publisher

df = df.groupby('Publisher').agg({
    'NA_Sales': 'sum',
    'EU_Sales': 'sum',
    'JP_Sales': 'sum',
    'Other_Sales': 'sum'
}).reset_index()

df['Total_Sales'] = df[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']].sum(axis=1)
df = df.sort_values('Total_Sales', ascending=False).head(10)
df.insert(0, 'Rank', range(1, 11))
df['NA_Sales %'] = ((df['NA_Sales'] / df['Total_Sales']) * 100).apply(lambda x: f"{x:,.2f}%")
df['EU_Sales %'] = ((df['EU_Sales'] / df['Total_Sales']) * 100).apply(lambda x: f"{x:,.2f}%")
df['JP_Sales %'] = ((df['JP_Sales'] / df['Total_Sales']) * 100).apply(lambda x: f"{x:,.2f}%")

df['Games per Publisher'] = df['Publisher'].map(games_per_publisher) # add column with games_per_publisher variable information

df = df.reset_index(drop=True) # index range 1, 11 instead aleatory numbers (example)

ax = df.set_index('Rank')[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']].plot(kind='bar', stacked=True, figsize=(10, 7))
ax.set_title('Top 10 Publishers (1980-2020)', fontsize=14)
ax.set_xlabel('Publisher Rank', fontsize=12)
ax.set_ylabel('Total Sales (Millions)', fontsize=12)
ax.set_xticklabels(df['Publisher'], rotation=45, ha='right')
plt.tight_layout()
plt.show()