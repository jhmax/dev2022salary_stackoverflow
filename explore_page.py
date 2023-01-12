import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def shorten_categories(categories, cutoff):
    categorical_map = {}
    for i in range(len(categories)):
        if categories.values[i] >= cutoff:
            categorical_map[categories.index[i]] = categories.index[i]
        else:
            categorical_map[categories.index[i]] = 'Other'
    return categorical_map

def clean_experience(x):
    if x ==  'More than 50 years':
        return 50
    if x == 'Less than 1 year':
        return 0.5
    return float(x)

def clean_education(x):
    if 'Bachelor’s degree' in x:
        return 'Bachelor’s degree'
    if 'Master’s degree' in x:
        return 'Master’s degree'
    if 'Professional degree' in x or 'Other doctoral' in x:
        return 'Post grad'
    return 'Less than a Bachelors'

# ONCE EXECUTE for the first time load_data(), this decorator avoid to executed all over again the page, improving the performance of this app
@st.cache

## ALL THE CHANGES in df
def load_data():
    df = pd.read_csv("survey_results_public.csv")
    df = df[["Country", "EdLevel", "YearsCode", "Employment", "ConvertedCompYearly"]]
    df = df[df["ConvertedCompYearly"].notnull()]
    df = df.dropna()
    df = df[df["Employment"] == "Employed, full-time"]
    df = df.drop("Employment", axis=1)

    country_map = shorten_categories(df.Country.value_counts(), 400)
    df["Country"] = df["Country"].map(country_map)
    df = df[df["ConvertedCompYearly"] <= 250000]
    df = df[df["ConvertedCompYearly"] >= 10000]
    df = df[df["Country"] != "Other"]

    df["YearsCode"] = df["YearsCode"].apply(clean_experience)
    df["EdLevel"] = df["EdLevel"].apply(clean_education)
    df = df.rename({"ConvertedCompYearly": "Salary"}, axis=1)
    return df

df = load_data()


def show_explore_page():
    st.title("Explore Sofware Engineer Salaries")

    st.write(
        """
        ### STACK OVERFLOW developer survey 2022

        
        """
    )

    data = df["Country"].value_counts()

    fig1, ax1 = plt.subplots()
    ax1.pie(data, labels=data.index, autopct="%0.2f%%", shadow=True, startangle=200)
    ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.write("""#### Most representative countries """)
    st.pyplot(fig1)


    # MEAN SARALRY
    st.write("#")
    st.write(
        """
    #### Mean Salary Based On Country
    """
    )
    data = df.groupby(["Country"])["Salary"].mean().sort_values()
    # st.area_chart(data)
    st.area_chart(data, 0, 500)


    # EXPERIENCE
    st.write(
        """
    #### Mean Salary Based On Experience (0 to 50 years)
    """
    )
    data = df.groupby(["YearsCode"])["Salary"].mean().sort_values(ascending=True)
    st.line_chart(data)

