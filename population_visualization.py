import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  
import plotly.express as px

# Load dataset
url = 'https://raw.githubusercontent.com/datasets/population/master/data/population.csv'
df = pd.read_csv(url)

# Filter year range
df = df[(df['Year'] >= 2000) & (df['Year'] <= 2020)]

# Clean data
df = df.dropna(subset=['Value'])
df.rename(columns={'Value': 'Population'}, inplace=True)

# --- Bar Chart: Top 10 Most Populous Countries in 2020 ---
top_2020 = df[df['Year'] == 2020].sort_values(by='Population', ascending=False).head(10)

plt.figure(figsize=(12, 6))
sns.barplot(data=top_2020, x='Country Name', y='Population', palette='viridis')
plt.xlabel('Country')
plt.ylabel('Population')
plt.xticks(rotation=45)
plt.title('Top 10 Most Populous Countries in 2020')
plt.tight_layout()
plt.show()

# ---- Histogram: Population Distribution in 2020 ----
pop_2020 = df[df['Year'] == 2020]

plt.figure(figsize=(10, 5))
sns.histplot(pop_2020['Population'], bins=30, kde=True)  
plt.title('Population Distribution Across Countries (2020)')
plt.xlabel('Population')
plt.ylabel('Number of Countries')
plt.tight_layout()
plt.show()

# ---- Line Chart: Population Growth for Selected Countries ----
selected_countries = ['India', 'China', 'Bangladesh', 'Japan', 'Russia', 'Indonesia']
df_selected = df[df['Country Name'].isin(selected_countries)]

plt.figure(figsize=(12, 6))
for country in selected_countries:
    country_data = df_selected[df_selected['Country Name'] == country]
    plt.plot(country_data['Year'], country_data['Population'], label=country)

plt.title('Population Growth (2000-2020)')
plt.xlabel('Year')
plt.ylabel('Population')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# ---- Choropleth Map: Population by Country in 2020 ----
choropleth_data = df[df['Year'] == 2020]

fig = px.choropleth(choropleth_data, 
                    locations="Country Code", 
                    color="Population", 
                    hover_name="Country Name", 
                    color_continuous_scale=px.colors.sequential.Plasma,
                    title="World Population by Country (2020)")

fig.show()