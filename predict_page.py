import streamlit as st
import pickle
import numpy as np

# LOAD FILE WIHT, FETCH MODEL OF ML, COUNTRY AND EDUCATION
def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

regressor = data["model"]
le_country = data["le_country"]
le_education = data["le_education"]


# BUILD PREDICITON 
def show_predict_page():
    st.title("Softwate Developer to Predict Salaray")

    st.write(""" ### Calculate the Salary (Machine Learn Model DecisionTreeRegressor) """)


    countries = (
        "United States of America",                                                                                 
        "Germany",                                                 
        "United Kingdom of Great Britain and Northern Ireland",    
        "India",                                                   
        "Canada",                                                  
        "France",                                                  
        "Brazil",                                                  
        "Spain",                                                   
        "Netherlands" ,                                            
        "Australia",                                               
        "Italy",                                                   
        "Poland",                                                  
        "Sweden" ,                                                 
        "Russian Federation",                                     
        "Switzerland",                                             
        "Turkey",                                                  
        "Israel",                                                  
        "Austria",                                                 
        "Norway",                                                  
        "Portugal",                                                
        "Denmark ",                                                
        "Belgium",                                                 
        "Finland",                                                 
        "Mexico",                                                  
        "New Zealand",                                             
        "Greece",                                                  
        "South Africa",                                            
        "Pakistan",                                                
        "Czech Republic", 
    )

    education_ = (
        "Master’s degree",
        "Bachelor’s degree", 
        "Less than a Bachelors",
        "Post grad",
    )

    country = st.selectbox("Country",countries)
    education = st.selectbox("Education Level", education_)

    # start =0; max =50; default = 3
    experience = st.slider("Years of Experience", 0, 50, 3)

    # if true en click the button
    ok = st.button("Calculate Salary")
    if ok:
        X = np.array([[country, education, experience]])
        
        ## change the 3 options (country, education, experience) into a float
        X[:, 0] = le_country.transform(X[:,0])
        X[:, 1] = le_education.transform(X[:,1])
        X = X.astype(float)

        salary = regressor.predict(X)
        # Show the salary value only with 2 decimals
        st.subheader(f"The estimate salary is ${salary[0]:.2f}, year.")

