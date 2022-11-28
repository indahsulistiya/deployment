import numpy as np
import pickle
import pandas as pd
import streamlit as st

from PIL import Image

pickle_in = open("classifier.pkl", "rb")
classifier = pickle.load(pickle_in)

def welcome():
    return "Klasifikasi Penderita Penyakit Jantung"

def predict_note_authentication(Age, RestingBP, Cholesterol, FastingBS, MaxHR, OldPeak, Sex_F, Sex_M, ChestPainType_ASY, ChestPainType_ATA, ChestPainType_NAP, ChestPainType_TA, RestingECG_LVH, RestingECG_Normal, RestingECG_ST, ExerciseAngina_N, ExerciseAngina_Y, ST_Slope_Down, ST_Slope_Flat, ST_Slope_Up)

    """Let's Authenticate the Banks Note
    This is using  docstrings for specifications.
    ---
    parameters:
        - name : Age
          in : query
          type : number
          required : true
        - name : RestingBP
          in : query
          type : number
          required : true
        - name : Cholesterol
          in : query
          type : number
          required : true
        - name : FastingBS
          in : query
          type : number
          required : true
        - name : MaxHR
          in : query
          type : number
          required : true
        - name : OldPeak
          in : query
          type : number
          required : true      
        - name : Sex_F
          in : query
          type : number
          required : true   
        - name : Sex_M
          in : query
          type : number
          required : true  
        - name : ChestPainnType_ASY
          in : query
          type : number
          required : true
        - name : ChestPainType_ATA
          in : query
          type : number
          required : true
        - name : ChestPainType_NAP
          in : query
          type : number
          required : true
        - name : ChestPainType_TA
          in : query
          type : number
          required : true
        - name : RestingECG_LVH
          in : query
          type : number
          required : true
        - name : RestingECG_Normal
          in : query
          type : number
          required : true      
        - name : RestingECG_ST
          in : query
          type : number
          required : true   
        - name : ExerciseAngina_N
          in : query
          type : number
          required : true  
        - name : ExerciseAngina_Y
          in : query
          type : number
          required : true
        - name : ST_Slope_Down
          in : query
          type : number
          required : true
        - name : ST_Slope_Flat
          in : query
          type : number
          required : true
        - name : ST_SLop_Up
          in : query
          type : number
          required : true
    responses :
        200:
            description : The output values
    """
    

    prediction = classifier.predict([[Age, RestingBP, Cholesterol, FastingBS, MaxHR, OldPeak, Sex_F, Sex_M, ChestPainType_ASY, ChestPainType_ATA, ChestPainType_NAP, ChestPainType_TA, RestingECG_LVH, RestingECG_Normal, RestingECG_ST, ExerciseAngina_N, ExerciseAngina_Y, ST_Slope_Down, ST_Slope_Flat, ST_Slope_Up]])
    print(prediction)
    return prediction


def main():
    st.title("Klasifikasi Penderita Penyakit Jantung")
    html_temp = """
    <div style = "background-color:tomato;padding:10px">
    <h2 style = "color:white;text-align:center;">Klasifikasi Penderita Penyakit Jantung </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Age = st.text_inpute("Age", "Type Here") 
    RestingBP = st.text_inpute("RestingBP", "Type Here") 
    Cholesterol = st.text_inpute("Cholesterol", "Type Here") 
    FastingBS = st.text_inpute("FastingBS", "Type Here") 
    MaxHR = st.text_inpute("MaxHR", "Type Here") 
    OldPeak = st.text_inpute("OldPeak", "Type Here") 
    Sex_F = st.text_inpute("Sex_F", "Type Here")
    Sex_M = st.text_inpute("Sex_M", "Type Here") 
    ChestPainType_ASY = st.text_inpute("ChestPainType_ASY", "Type Here") 
    ChestPainType_ATA = st.text_inpute("ChestPainType_ATA", "Type Here") 
    ChestPainType_NAP = st.text_inpute("ChestPainType_NAP", "Type Here") 
    ChestPainType_TA = st.text_inpute("ChestPainType_TA", "Type Here") 
    RestingECG_LVH = st.text_inpute("RestingECG_LVH", "Type Here")
    RestingECG_Normal = st.text_inpute("RestingECG_Normal", "Type Here")
    RestingECG_ST = st.text_inpute("RestingECG_ST", "Type Here")
    ExerciseAngina_N = st.text_inpute("ExerciseAngina_N", "Type Here")
    ExerciseAngina_Y = st.text_inpute("ExerciseAngina_Y", "Type Here")
    ST_Slope_Down = st.text_inpute("ST_Slope_Down", "Type Here")
    ST_Slope_Flat = st.text_inpute("ST_SLope_Flat", "Type Here")
    ST_Slope_Up = st.text_inpute("ST_SLope_Up", "Type Here")
    result = ""
    if st.button("Predict"):
        result = predict_note_authentication(Age, RestingBP, Cholesterol, FastingBS, MaxHR, OldPeak, Sex_F, Sex_M, ChestPainType_ASY, ChestPainType_ATA, ChestPainType_NAP, ChestPainType_TA, RestingECG_LVH, RestingECG_Normal, RestingECG_ST, ExerciseAngina_N, ExerciseAngina_Y, ST_Slope_Down, ST_Slope_Flat, ST_Slope_Up)
    st.success('The Output is {}'.format(result))
    if st.button("About"):
        st.text("Lets Learn")
        st.text("Built with Streamlit
                
if __name=='__main__':
    main()