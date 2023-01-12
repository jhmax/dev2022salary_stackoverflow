import streamlit as st
import pandas as pd

def clean_education(x):
    if 'Bachelor’s degree' in x:
        return 'Bachelor’s degree'
    if 'Master’s degree' in x:
        return 'Master’s degree'
    if 'Professional degree' in x or 'Other doctoral' in x:
        return 'Post grad'
    return 'Less than a Bachelors'

## LOAD DATA
@st.cache
def load_data():
    df = pd.read_csv("survey_results_public.csv")
    df = df[["Country", "EdLevel", "YearsCode", "Employment", "ConvertedCompYearly", "LanguageHaveWorkedWith"]]
    df = df[df["ConvertedCompYearly"].notnull()]   #detects if values are not missing for either a single value (scalar) or array-like objects.
    df = df.dropna() # Remove all rows wit NULL values from the DataFrame
    df = df[df["Employment"] == "Employed, full-time"]
    df["EdLevel"] = df["EdLevel"].apply(clean_education)
    return df

df = load_data()

def load_survey():
    st.title("""
    Softwate Developer to Predict Salaray
    #
    """)

    st.write(df)

    # Filter data
    st.write("#")
    st.subheader("Filter Data")

    country_sort = sorted(df.Country.unique()) #
    selected_country = st.multiselect("Country", country_sort)

    unique_EdLevel = sorted(df.EdLevel.unique()) #
    selected_EdLevel = st.multiselect("Education Level", unique_EdLevel, unique_EdLevel)

    df_filter_data = df[
        (df.Country.isin(selected_country)) & (df.EdLevel.isin(selected_EdLevel))
        ] 

    # Result
    st.write("")
    st.write("Result")
    st.write(df_filter_data)

