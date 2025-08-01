import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set(style="whitegrid")

# بارگذاری داده
df = pd.read_csv(r"G:\CovidDataset\Data\covid-data(cleaned).csv")
df['date'] = pd.to_datetime(df['date'])

# ساخت پوشه خروجی
output_dir = "charts_matplotlib"
os.makedirs(output_dir, exist_ok=True)

# کشورها با بیشترین موارد ابتلا
top_cases = df.groupby('country')['total_cases'].max().sort_values(ascending=False).head(10).reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(x='total_cases', y='country', data=top_cases, palette='viridis')
plt.title('Top 10 Countries by Total Cases')
plt.xlabel('Total Cases')
plt.ylabel('Country')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "top_cases.png"))
plt.close()

# کشورها با بیشترین مرگ
top_deaths = df.groupby('country')['total_deaths'].max().sort_values(ascending=False).head(10).reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(x='total_deaths', y='country', data=top_deaths, palette='magma')
plt.title('Top 10 Countries by Total Deaths')
plt.xlabel('Total Deaths')
plt.ylabel('Country')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "top_deaths.png"))
plt.close()

# قاره‌ها بر اساس تعداد ابتلا
continents_cases = df.groupby('continent')['total_cases'].max().sort_values(ascending=False).reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(x='total_cases', y='continent', data=continents_cases, palette='Blues_d')
plt.title('Continents by Total Cases')
plt.xlabel('Total Cases')
plt.ylabel('Continent')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "continents_cases.png"))
plt.close()

# قاره‌ها بر اساس مرگ
continents_deaths = df.groupby('continent')['total_deaths'].max().sort_values(ascending=False).reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(x='total_deaths', y='continent', data=continents_deaths, palette='Reds_d')
plt.title('Continents by Total Deaths')
plt.xlabel('Total Deaths')
plt.ylabel('Continent')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "continents_deaths.png"))
plt.close()
