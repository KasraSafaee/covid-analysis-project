import dash
from dash import dcc, html
import dash.dependencies
import plotly.express as px
import pandas as pd

# خواندن داده
df = pd.read_csv(r"G:\CovidDataset\Data\covid-data(cleaned).csv")
df['date'] = pd.to_datetime(df['date'])

# محاسبه کشورها
top_cases = df.groupby('country')['total_cases'].max().sort_values(ascending=False).reset_index()
top_deaths = df.groupby('country')['total_deaths'].max().sort_values(ascending=False).reset_index()

# ترکیب و مرتب‌سازی کشورها
countries_by_deaths = pd.merge(top_cases, top_deaths, on='country', how='outer')
countries_by_deaths = countries_by_deaths.sort_values('total_deaths', ascending=False).reset_index(drop=True)
countries_by_case = countries_by_deaths.sort_values('total_cases', ascending=False).reset_index(drop=True)

# rolling average
df['rolling_deaths'] = df.groupby("country")["new_deaths"].transform(lambda x: x.rolling(window=14).mean())

# top 5 کشور از نظر مرگ
top5_countries = countries_by_deaths.head(5)['country'].values
df_top5 = df[df['country'].isin(top5_countries)]

# محاسبه آماری برای قاره‌ها
df_population = df.groupby('country').tail(1).groupby("continent")["population"].sum()
continents_cases = df.groupby('continent')['total_cases'].max().sort_values(ascending=False).reset_index()
continents_deaths = df.groupby('continent')['total_deaths'].max().sort_values(ascending=False).reset_index()
continents_by_deaths = pd.merge(continents_cases, continents_deaths, on='continent', how='outer')
continents_by_deaths = pd.merge(continents_by_deaths, df_population, on='continent', how='left')
continents_by_deaths = continents_by_deaths.dropna(subset=['continent'])

# Dash App
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("🌍 COVID-19 Global Dashboard", style={"textAlign": "center"}),

    html.H2("☠️ Top 15 Countries by Total Deaths"),
    dcc.Graph(
        figure=px.bar(countries_by_deaths.head(15),
                      x='country', y='total_deaths',
                      color='country',
                      title="Top 15 Countries by Total Deaths")
    ),

    html.H2("📈 Top 15 Countries by Total Cases"),
    dcc.Graph(
        figure=px.bar(countries_by_case.head(15),
                      x='total_cases', y='country',
                      orientation='h', color='country',
                      title="Top 15 Countries by Total Cases")
    ),

    html.H2("📉 14-Day Rolling Average of Deaths (Top 5 Countries)"),
    dcc.Graph(
        figure=px.line(df_top5, x='date', y='rolling_deaths', color='country',
                       title="Rolling Average Deaths (14 Days)")
    ),

    html.H2("📊 New Cases Over Time for Top 5 Countries"),
    dcc.Graph(
        figure=px.area(df_top5, x='date', y='new_cases', color='country',
                       title="New COVID-19 Cases Over Time")
    ),

    html.H2("🧭 Total Deaths by Continent"),
    dcc.Graph(
        figure=px.pie(continents_by_deaths, names='continent', values='total_deaths',
                      title="Total Deaths by Continent")
    ),

    html.H2("🌐 Total Cases by Continent"),
    dcc.Graph(
        figure=px.bar(continents_by_deaths,
                      x='continent', y='total_cases',
                      color='continent', title="Total Cases by Continent")
    ),

    html.H2("🎛 Interactive: Select a Country to View New Cases Over Time"),
    dcc.Dropdown(
        id='country-dropdown',
        options=[{"label": c, "value": c} for c in sorted(df["country"].dropna().unique())],
        value='Iran'
    ),
    dcc.Graph(id="country-time-series")
])

# Callback برای آپدیت نمودار تعاملی
@app.callback(
    dash.dependencies.Output("country-time-series", "figure"),
    [dash.dependencies.Input("country-dropdown", "value")]
)
def update_country_plot(selected_country):
    dff = df[df["country"] == selected_country]
    return px.line(dff, x="date", y="new_cases", title=f"New Cases Over Time: {selected_country}")

# اجرای سرور
if __name__ == "__main__":
    app.run(debug=True)
