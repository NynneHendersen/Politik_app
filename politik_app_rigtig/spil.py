import random
import streamlit as st 
import pandas as pd

def app():
    #Laver session state variabler til right-answer-variabel
    if 'rightanswer' not in st.session_state:
        st.session_state.rightanswer=0
    
    #
    if 'csvdata' not in st.session_state:
        st.session_state.csvdata=pd.read_csv("qa.csv", sep=';')

    #print udskriver til consollen på server
    #print(st.session_state)

    #Laver datafram variabel, hvor vi storer data fra csv fil
    df=st.session_state.csvdata

    st.title('Velkommen til Politik-Quizzen')
    st.write('Her kan du quizze dig selv i din viden om politik.')
    st.write('Hvis du undrer dig over noget, så skriv endelig et opslag med dine spørgsmål')

    text_area = st.empty()

    # Funktioner når man klikker på knapperne
    def click_button1():
        st.warning('Det er forkert')
        #forsøg på at vise en text area med info beskeden
        #text_area.text_area(df.iloc[st.session_state.rightanswer][3], "Write a number")
        #df.iloc(row,column)
        st.write(df.iloc[st.session_state.rightanswer][3])
    def click_button2():
        st.success('DET ER RIGTIGT!')
        st.write(df.iloc[st.session_state.rightanswer][3])


    print("Den forrige række var: " + str(st.session_state.rightanswer))

    # Generer et tilfældigt tal på indenfor de data der er i qa.csv
    rowtowshow=random.randint(0, df.last_valid_index())
    print("Den næste række har index: " + str(rowtowshow) + " " + str(df.iloc[rowtowshow]))

    # Gemmer det spørsmål vi skal vise næste gang så vi kan vise rette info tekst ved fejl
    st.session_state.rightanswer=rowtowshow

    # Vis det næste spørgsmål
    question_area = st.text_area(label = 'Spørgsmål' , value = df.iloc[rowtowshow][0])
    # Denne randon skal benytttes til at bytte rundt på rigtigt og forkert tilfældigt så rækkefølgen ikke er den samme hver gang
    randInteger=random.randint(0, 1)
    if randInteger == 0:
        button1 = st.button(df.iloc[rowtowshow][1] , use_container_width = 20 , key = 'button1', on_click=click_button1)
        button2 = st.button(df.iloc[rowtowshow][2] , use_container_width = 20 , key = 'button2', on_click=click_button2)
    else:
        button2 = st.button(df.iloc[rowtowshow][2] , use_container_width = 20 , key = 'button2', on_click=click_button2)
        button1 = st.button(df.iloc[rowtowshow][1] , use_container_width = 20 , key = 'button1', on_click=click_button1)