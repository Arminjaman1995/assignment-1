import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Data Source: https://github.com/fivethirtyeight/data/blob/master/terrorism/eu_terrorism_fatalities_by_country.csv
# Load data from CSV file into a pandas DataFrame
pandas_df = pd.read_csv("./eu_terrorism_fatalities_by_country.csv")


def line_plot(df):
    """Create a line plot of countries over time
    params: data
    """
    for country in df.columns[1:]:
        plt.plot(df["iyear"], df[country], marker="o", label=country)

    plt.xlabel("Year")
    plt.ylabel("Count")
    plt.title("Count of Incidents by Country over the Years")
    plt.legend()
    plt.tight_layout()
    plt.show()


def bar_chart(df):
    """Calculate total incidents by country
    param: data
    """
    df["Total"] = df.sum(axis=1)
    df_sorted = df.sort_values(by="Total", ascending=False)
    top_5_countries = df_sorted.head(5)
    plt.figure(figsize=(10, 6))
    bars = plt.bar(
        top_5_countries.columns[1:], top_5_countries.iloc[0, 1:], color="red"
    )

    # Adding data labels to each bar
    for bar, country in zip(bars, top_5_countries.columns[1:]):
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height(),
            str(top_5_countries.loc[top_5_countries.index[0], country]),
            ha="center",
            va="bottom",
            fontsize=8,
            color="black",
        )

    plt.xlabel("Country")
    plt.ylabel("Total Incidents")
    plt.title("Top 5 Countries by Total Incidents")
    plt.show()


def heatmap(df):
    """Create a heatmap of incidents by country and year
    param: data
    """
    df.set_index("iyear", inplace=True)

    # Plotting the data for every 5 years
    plt.figure(figsize=(12, 8))
    plt.imshow(df.T, cmap="Blues", aspect="auto", interpolation="none")
    plt.colorbar(label="Incidents")
    plt.xticks(range(0, len(df.index), 5), df.index[::5])
    plt.yticks(range(len(df.columns)), df.columns)

    plt.xlabel("Year")
    plt.ylabel("Country")
    plt.title("Incidents by Country and Year (Heatmap, Every 5 Years)")
    plt.show()


# Call the functions
line_plot(df=pandas_df)
bar_chart(df=pandas_df)
heatmap(df=pandas_df)
