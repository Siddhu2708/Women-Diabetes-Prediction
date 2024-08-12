import numpy as np
import pickle
import streamlit as st
from streamlit_option_menu import option_menu


st.sidebar.image('doctor.jpeg', use_column_width=True)

# loading the saved models
diabetes_model = pickle.load(open('Diabetes_Logistic_model.pkl', 'rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Women Disease Prediction System',
                          ['Diabetes Prediction'],
                          icons=['activity','heart','person'],
                          default_index=0)

def diabetes_prediction(input_data):

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = diabetes_model.predict(input_data_reshaped)
    print(prediction)

    if prediction[0] == 0 :
      return 'The person is not diabetic'
    else:
      return 'The person is diabetic'

def main():
    # page title
    st.title ('Women Diabetes Prediction App ')

    # getting the input data from the user
    col1, col2 = st.columns (2)

    with col1 :
        Age = st.number_input('Age of the Person', min_value=0, max_value=250 )

    with col2 :
        Pregnancies = st.number_input('Number of Pregnancies', min_value=0, max_value=250)

    with col1 :
        Glucose = st.number_input('Glucose Level', min_value=0, max_value=250)

    with col2 :
        BloodPressure = st.number_input('BloodPressure Value', min_value=0, max_value=250)

    with col1 :
        BMI = st.number_input('BMI value', min_value=0, max_value=250)

    with col2 :
        DiabetesPedigreeFunction = st.number_input ('DiabetesPedigreeFunction', min_value=0, max_value=250 )

    with col1 :
        Insulin = st.number_input('Insulin Level', min_value=0, max_value=250)


     # code for Prediction
    diagnosis = ''
    with col1:
        # creating a button for Prediction
        if st.button ('Diabetes Test Result') :
            diagnosis = diabetes_prediction([Age, Pregnancies, Glucose, BloodPressure, BMI, DiabetesPedigreeFunction, Insulin])

            st.success (diagnosis)

if __name__ == '__main__':
    main()

