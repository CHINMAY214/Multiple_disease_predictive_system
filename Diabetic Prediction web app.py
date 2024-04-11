# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 13:07:14 2024

@author: HP
"""

import numpy as np
import pickle
import streamlit as st


# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")


with st.sidebar:
    st.image("data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBwgHBgkIBwgKCgkLDRYPDQwMDRsUFRAWIB0iIiAdHx8kKDQsJCYxJx8fLT0tMTU3Ojo6Iys/RD84QzQ5OjcBCgoKDQwNGg8PGjclHyU3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3N//AABEIAJQA5gMBIgACEQEDEQH/xAAbAAEAAgMBAQAAAAAAAAAAAAAABAUBAgYDB//EAEUQAAEDAgMEBQgHBQcFAAAAAAEAAgMEEQUSIRMxQVEGFBVhkSIyUlRxgaHRB1OTscHh8CMzQnOSFjQ2Q7Li8SRiY2R0/8QAGQEBAAMBAQAAAAAAAAAAAAAAAAIDBAEF/8QAKBEAAwACAQQCAQMFAAAAAAAAAAECAxExBBITIUFRFCJh0TKRweHw/9oADAMBAAIRAxEAPwD7gBYAcllEQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAERYQGUWFgyMG9wHvQGyLzM8VwM4utgQRoUBsiLBIAJO6yAyvGSeNm91zyCjz1JcbMNm8+aiF3MWPNWTjb5K6vRNdWD+Fh961647g0eKig3R17aKzxyQ72SxWO9AeK2FYP4mkewqCy4abhbFd8cnVTLBtTG42zW9oXsCDuN1TXW7Hubq029ig8X0dWT7LdFBiq3D95YjmFLje17btN1W5aLFSZuiIonQiIgCIiAIiIAiIgCIiALSR4Y0uduC3UKuccwZwXZW2cb0jylqHyaDRvJeJPG4WVi61KUihvZoAHkm+7kvSGV7CMpS6aJpMIsoZhJHfjxXjWS5W5QdTvXI4zjOIU2IvpqOZsMcbGuccgcXE+1VzsZxR5zOryT/LZ8lZj6G6/UuCNdQl6Oy38/BYyi/HwXG9rYn6+fsm/JO1sT9fP2TfktH4eT7RV5kdnoOfgl/1ZcZ2tifr5+yb8ljtbE/Xz9m35Ln4eT7R3zL6O1/W5a3XIR4lir81q+2Vpdqxg/BbMr8WcYwK8XkFxdrBb26aKP4tr5Q8yOtsjdBqqPo9iVZVVU9PVyNlDGhzXhoB32tpoVelU3Dl6ZZLVLZlM7o/KaSCie1Q0SJlLU7TSQjMpV1U9w0UylqM3kPOo3FU3GuC2a3yS0RFUTCIiAIiIAiIgCIiAKvrgdqOVtFYKPVRZ2XG8blKHpka4K9ZQhRq+odS0kk7WhxZbQ7t4H4rUvZRwSCtomF7g0cfgqttRizhduG3B1Gv5r1irMYhuRhQ17z80cvXphV7KXHIx/aOpYRoIo/uUfYM9AKfWUWKVWIy1jqF7XSNa0tG4ALXqGJ+oPW/HkmYSbRTUNveiFsGeiE2DPRCm9QxP1FyjVgqqOwnp8hdctDipPNKW9iMdXSlL2zz2DPRCbBnohR+0HW/dtv7SrJrczQdNRfRQxdVGT+lmjqehzdMk8i5Iuwj9EeCGnjOmQeC1xfEKbCaN1TVOs0aNa3V0juTe9QKXB+kOOxipxCr7FoXathiAMxbzJOjf1orXkS9tmVRsu+jjQ3GKhoFhsR966U7+HiuHj6EYVe8eP4qyfjKys1+6y3mHSnoww1LKnt/DG6yRvaGVEbeYO5360Cx5dXW0/7l0rS0dtwWhdppvUTB8VpMZw+Kuw+TPBJ4tPEEcCFMyC97qjWuSRngs7t2h5rQSxZsm1bm5XW6DZYU0wkYLnyhvXsFVQuLJgb6cVag3Wa50y+XtGURFAkEREAREQBEWEBT47iM1E6NkIF3gkuI5LGEYz1p+wqQGy8CNzvktOlTG9XiefODrAc1zRJikBaTv1IPxWzFhm8f7mXJkcWd3LTxSanQ8wqrG6YSYbNHCS+U2sARzC54VM7TmE0mmuriV0EEplp2ScXi654qxtNsLIr2kiEzEscjYGto47AWGn+5Z7Vx71SL+n/crAOs27uCh4Ri9DjFOJ8Pn2jOILSxzfa0gELvdHzKO6r7IbukWKNqDTuhhEzW5nNyG4B3cVt29i/1EH9B+ahzi/Seq/kM+5S8q0+PHpPtK+6vsycexb6iH+g/NV2LT1+J5TNA28YIbk03+/uVhk7kLbJ2Y9aSJxkuLVb4OcNDV6nYu/qCvI2WjYCLGwXvkWQ3UHvVeHDOLejX1nX31aStJaOYwSmZ0g6WVdfUjPQ4Q/Y07d7TMPOcRxsR9yvWMnx2oe+R7o6VjrNbu/RVd9GzmQ4HiDpTZ7a+czE9x1uumlrWijFRSN2wLg2zbjjYlSyZHNMyTHdpI8HYPRQwm5kYA0lz9odBz5L0E9Ph8FNELvbJ5r7aHvXjVbZ8uKt8ss6tZg4Xy8F4Yo4RYJSF4s5pZYHf5uqpi3kpSy/LhnFj7t+/9FIQzop02ZsQWYXjTTmY0eTHUN105Zh+Kn9K8eqqalgjwWnE880mUmRxY1gDSbk2vwCgfSGSabo2RpKcRhtztbVdDh1JBKQKiISMd51+AUsi3j7lz/BRLStKuCooHyzwQvkZspnNBcwG4BXW7rXI109pVdXUsVHXhws1oN2jn+rr16o6oqo6qZ7mhmrWA7+8qGSm5TSGKZ7mm9E1WVM/PCD7lW+73qZQE5HA8Cqsi9bLY5JaIioLQiIgCIiAIi8JJHZstggKfpTCXxxTAkhlw4DlzXOkb7711c4Ej3NeLi1rFcxUR7KpfGDcNda69Dpn+nRhzr3s8mk69ytMPr2RRNhluANA7kqpw8q43Lbgr6lUtMqmmvZ1cTc7gGi/3KtwLB2UwqqmB4kEjyxpykHK1xAHuXN4l0hxbDq98Ec8bYhGHMzRXuCAfH5K0wXpQI+jzGPJdXR3a0ZDa19CfcvOzy4Xkfwb+nt5G8U/IlF+lFUP/Cz7lNcLNJ7lVYfPLWY3NPNbavp2F1hYK4ePId7Ctyrcy/2RnuHLqSEXu9Io2RzXs1vdwBWhcLnUeKNIMkYBF84Vulo86HXeiVOCIyQbFR87t2YqXUj9kbKFmHMLk+0W9R3KvRQYPUs6PdLKukq7R4fjLtpDIdGtnPnNPtufFXw6xgE7mmNz6OQ3BA3fI/eo1fhdHjUTqOtYHxuabEHVh0sQeBUCnqOlHRxnV5KYY9h7RaORr8s7W8nA7/iuVz/g0Ym6hHX0NfDXZjT5iWC5BCg1VFUV2JjrAtSReU2x87uXMRfSRhcd2wYFiLJnGxa1kYBPK+b8FpX1vSPpIw07ohguHO/eFr808g5dw17lCMdzXpaLaaa/UzGJVn9o+mDHUztph2EAsa8DR87t/tAH3FX9dj9DgeGvqauXKSMsbWglz32NgAuXZscIijpKWGTZNBtsx8T3rYVMVYTBLTPc12p2jQWla30jaSXBR5J3t8nNQdP8eMmfEJoq5pdmDZowzJ3AsA09oK77oh08h6Q1zaCahfTVbmFzcrs7DYa67wuUx/BqEYXUSQUsTJWtzBzW2Om9Q/o6pnNxE4g3yXBwiaRv1ILvwTJ00OfS4JzkXJ9nJ5W96k4e47RzTbdfRR3DXTRS6BurnHfuXkZP6TRHJMWViyys5eEREAQosFAaue1pGZwB7yvOaeGGxle1pO5QsWpXSftWG4aNWqovoL7+aujEqW9lV5HPotXuD3E7wTdc9iFM6Cck6teS4H8FYRzOaCGu3cFvM+KakkE+5ovfv5rTG4ZReqRzdVUx0zPKJLj5rRqVmKUinEs9oTxBdoF51XV6dr53MBe4AeTvPILGHUcc8ruuPL5Yt8DhowcNOP3Ldqe3ZnW9ny+vrcVqsZniqK2aaYy7NhzWFr+SAB7V1HR3D8fwfFoK3bl0DZLTNcwytc3c4W59/AqTVUVJiv0g0cmGvp5WxNHWNnK3SRmbS3O2Xcu5gw+SmZIBdwfI6Q6+kb2UXlx1PbpaNGqT3wQqKsp63pFUS07jkdC0AOFjcdylSYo2nrHU1XHsbn9lIXXa8cLngV411HTztLpxkewEiQHK5vfdRMKlimmkjxBpn6w39jJI2wlaOFjuKh2rW18ENtPTJ5ZiDjmNNRH3lTaaGzGGWKJs3ER7lUCkpgABgdQABvupFBTwMqozHhcsJbez3O0ao0vX/fydXJY1AlMDjA1jn/wh/mn2qv2dd6tReJU+vY19I9r4HTggfs273aqrhoaWR+V2FSRgjznk2UZZ217LeOJjRdrGtPNoWxHNRKSmpqVz3Qw7MvFnaqcFB8kkfJo6COPpP1HrN2R1Fmy2HlW1t+C7m9tb6DiuGZ/i4n/3nf6iu4futz0W7JwtlN8lHVQyyvvFUOiGugC8eqVV/wC+u/pV7FCGCxAJvyVthdJBkdUTMYWjQAtBVldV2TwVqNs4mSjnkY5jq0uDgQRbevDolTT0E4gmpHQxvna5p2rZABcbzofgvopycIowP5Y0XmI4w67Y2B3pBoCz5Opd/BYp7VotC4CxJGu5WFC39kXXvmK55rHPcGgak6BdHRQ7CBrL3PFebmWlo1Y/bPdERZi8IiIAiIgNXNDgQRodFU1WFljS6F12jUtcrhYIvv3KU054I1PccqbEXHim+4O74FXVZQRuYXxsAcOSpiNVti1ZlqXJSiNlRjEjgLQ0ws0f953n3K4pqVk0hlewGwtqPOHJUeGTubtW9Wnk2lQ4ukaBZuttbm66ekFoG9+9X5XpaOQvZiKjpYXB8NNDG8A2LIwCvZxDQXvIDQCS4m1u8qLitU6jw+eeNoe9jdAdQubwStrMar+r4lrStGctDQBIQRYO5t7u7VUzibl0uETq9NIvmFmKUz5NiREdInP/AM1vO3Lkq/EqbrFK5rfJljOeM8WuG5dD7x4qmxGbq0xtBNKC7dE29tFPFXs5aJWGVXXaCCc73NGa3Pj8VKXDR1Tqd0sQndGBK6zcxFhcr07Qd64/7Qq/8Vv2mVLMl60dqsEXBBXF9oP9cf8AaFO0HeuP+0Kfi19nfKvo6x7C3gto3c1y9LiropBmqczT5wc666QOFgQbg7iOKqyY3HIVbPmDP8XH/wC53+oruHee0cQLrk6qiezpvIyGNzmtqGykgbgQHH4ldYP3h04LRkaaSI2esEZkeR7yVYsY2JuVujd5XjRNDIQbau1K9hrq7/hZqe2SlaA8rU7uS9I2F5s0XW8MO03vspUUTIvNOp796qdaJqTbD6S07XE3I1VwFHomZYy4+c7VSFjyVujTE6RlERQJhERAEREAREQHjUMdJBIxrspcLAqoOD1B/wA2PxPyV6sWUptzwRcplEMFnG58Xx+S27HqPrYx7CVd2Syn5r+znYkUZweoIsZY7cRcrAwSYXyviBPK6vbJZc81/Y7EUfY9R9ZH8U7Gn+tj8T8leWSyeax2IouxJdfKhud+n5J2JL6UPh+SvbBLBd89/ZzxyUXYcvpQ+H5LHYcvpQ+H5K+sEsE89/Y8clF2JL6UPh+SyMFnAttIrAWG/RXlglk81v5O+OSi7Fn4SRa+35LPYs3pxX9/yV5ZLJ5r+znjko+xqj6yL4p2NUfWx/H5K8sllzzWPHJR9j1A3SsHvPyTsep+tj+KvCqnFsZiw3EMNpJGf318jdoXANjDI3PJPgnktneyUScNpJKXOJHh2a1gCTZTlSjpTge0pYxitLnq2B8DRJrI07nAcu9a/wBrMC2Lpe04Nm213621OUHdqL6X3KL2/Z1NIvEVTU9IsJpJKllViNNE6lyicPfbIXeaD3mxsN61m6TYJBTU9TNi1FHBU32MjpmgSW325248lHTO7RcIo9HWQV1NHVUc0c9PIM0csbg5rhzBCIdJCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIDC4H6TKSPEK3BqGcuEU4rGuLDYj/AKd508ERSjkjXBR9Aap2NYtUVFYyMSSdHae5jba18wNuW4KP0AZT4zglVh1bSxujbh0kG0Dnl5aHZRvcQNwOgGoRFPZW0iBR1c0H0f4d0rcRNihxhk73Si7ZHZdlqO5p013q46HSdaxjAK+VjNrWx4rUyNA8kOL4hZo4CzR8URdoJezrvorOf6PsDJ9W/EoiKllqP//Z")
    st.title("Prediction App")
    choice = st.radio("Navigation",["Diabetic-Prediction","Heart-disease-Prediction","Parkinson-Prediction"])
    st.info("This Application allows you to check the Diabetics , heart-disease, Parkinson's disease")
st.write("Hello world")


# loading the saved model
loaded_model = pickle.load(open("Diabetics_model.sav","rb"))
heart_disease_model = pickle.load(open("heart_disease_model.sav","rb"))
parkinsons_model = pickle.load(open("parkinsons_model.sav","rb"))



# creating a function for Prediction

def diabetes_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The person is not diabetic'
    else:
      return 'The person is diabetic'
    print("Thank you soo much")
  
    
  
def main():
    
    
    # giving a title
    #st.title('Diabetes Prediction Web App')
    
    
    # getting the input data from the user
    
    if choice == "Diabetic-Prediction":
        Pregnancies = st.text_input('Number of Pregnancies')
        Glucose = st.text_input('Glucose Level')
        BloodPressure = st.text_input('Blood Pressure value')
        SkinThickness = st.text_input('Skin Thickness value')
        Insulin = st.text_input('Insulin Level')
        BMI = st.text_input('BMI value')
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
        Age = st.text_input('Age of the Person')
        # code for Prediction
        diagnosis = ''
        # creating a button for Prediction
        
        if st.button('Diabetes Test Result'):
            diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
        st.success(diagnosis)
        
        
    if choice == "Heart-disease-Prediction":
        st.title('Heart Disease Prediction using ML')
        
        col1, col2, col3 = st.columns(3)

        with col1:
            age = st.text_input('Age')

        with col2:
            sex = st.text_input('Sex[1-Male],[2-Female]')

        with col3:
            cp = st.text_input('Chest Pain types')

        with col1:
            trestbps = st.text_input('Resting Blood Pressure')

        with col2:
            chol = st.text_input('Serum Cholestoral in mg/dl')

        with col3:
            fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

        with col1:
            restecg = st.text_input('Resting Electrocardiographic results')

        with col2:
            thalach = st.text_input('Maximum Heart Rate achieved')

        with col3:
            exang = st.text_input('Exercise Induced Angina')

        with col1:
            oldpeak = st.text_input('ST depression induced by exercise')

        with col2:
            slope = st.text_input('Slope of the peak exercise ST segment')

        with col3:
            ca = st.text_input('Major vessels colored by flourosopy')

        with col1:
            thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

        # code for Prediction
        heart_diagnosis = ''

        # creating a button for Prediction
        if st.button('Heart Disease Test Result'):

                    user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        
                    user_input = [float(x) for x in user_input]
        
                    heart_prediction = heart_disease_model.predict([user_input])
        
                    if heart_prediction[0] == 1:
                        heart_diagnosis = 'The person is having heart disease'
                    else:
                        heart_diagnosis = 'The person does not have any heart disease'
        
        st.success(heart_diagnosis)
    
    #For Parkison
    if choice == "Parkinson-Prediction":
        st.title("Parkinson's Disease Prediction using ML")

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            fo = st.text_input('MDVP:Fo(Hz)')

        with col2:
            fhi = st.text_input('MDVP:Fhi(Hz)')

        with col3:
            flo = st.text_input('MDVP:Flo(Hz)')

        with col4:
            Jitter_percent = st.text_input('MDVP:Jitter(%)')

        with col5:
            Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

        with col1:
            RAP = st.text_input('MDVP:RAP')

        with col2:
            PPQ = st.text_input('MDVP:PPQ')

        with col3:
            DDP = st.text_input('Jitter:DDP')

        with col4:
            Shimmer = st.text_input('MDVP:Shimmer')

        with col5:
            Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

        with col1:
            APQ3 = st.text_input('Shimmer:APQ3')

        with col2:
            APQ5 = st.text_input('Shimmer:APQ5')

        with col3:
            APQ = st.text_input('MDVP:APQ')

        with col4:
            DDA = st.text_input('Shimmer:DDA')

        with col5:
            NHR = st.text_input('NHR')

        with col1:
            HNR = st.text_input('HNR')

        with col2:
            RPDE = st.text_input('RPDE')

        with col3:
            DFA = st.text_input('DFA')

        with col4:
            spread1 = st.text_input('spread1')

        with col5:
            spread2 = st.text_input('spread2')

        with col1:
            D2 = st.text_input('D2')

        with col2:
            PPE = st.text_input('PPE')

        # code for Prediction
        parkinsons_diagnosis = ''

        # creating a button for Prediction    
        if st.button("Parkinson's Test Result"):

            user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                          RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                          APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

            user_input = [float(x) for x in user_input]

            parkinsons_prediction = parkinsons_model.predict([user_input])

            if parkinsons_prediction[0] == 1:
                parkinsons_diagnosis = "The person has Parkinson's disease"
            else:
                parkinsons_diagnosis = "The person does not have Parkinson's disease"

        st.success(parkinsons_diagnosis)
        
    
if __name__ == '__main__':
    main()