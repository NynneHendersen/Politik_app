#Importerer vigtige programmer
import streamlit as st
import firebase_admin

from firebase_admin import credentials
from firebase_admin import auth

#Connecter til firebase (vores database)
cred = credentials.Certificate('politikapp1-a00ae08ce413.json')
firebase_admin.initialize_app(cred)

#stor funktion der "runner" appen
def app():
    st.title('Login Side')
    
    #Opretter username og -email i session_state
    if 'username' not in st.session_state:
        st.session_state.username = ''
    if 'useremail' not in st.session_state:
        st.session_state.useremail = ''

     # Funktion til at logge ind
    def f():
        try:
            user = auth.get_user_by_email(email)
            #print(user.uid)
            st.success('Login Succeded!')

            st.session_state.username = user.uid
            st.session_state.useremail = user.email

            # Sætter 'sign out' til true
            st.session_state.signed_out = True
            st.session_state.sign_out = True

        except:
            st.warning('Login fejlede')

    def t():
        st.session_state.signed_out = False
        st.session_state.sign_out = False
        st.session_state.username = ''

    # Sørger for man kun ser tom login side hvis man ikke er logget ind
    if 'signed_out' not in st.session_state:
        st.session_state.signed_out = False
    if 'sign_out' not in st.session_state:
        st.session_state.sign_out = False

    if not st.session_state['signed_out']:
        choice = st.selectbox('Login/Signup' , ['Login' , 'Signup'])

        # Viser de forskellige sider ved dropdown
        if choice == 'Login':
            email = st.text_input('Email Address')
            password = st.text_input('Password' , type = 'password')
            
            login_btn = st.button('Login' , on_click = f)

        else: 
            email = st.text_input('Email Address')
            password = st.text_input('Password' , type = 'password')
            username = st.text_input('Enter username')

            signup_btn = st.button('Create Account')

            if signup_btn:
                user = auth.create_user(email = email , password = password, uid = username)

                st.success('Account Created')
                st.markdown('Please login with you email and password')

    if st.session_state.sign_out:
        st.text('Name ' + st.session_state.username)
        st.text('Email ' + st.session_state.useremail)
        st.button('Sign out' , on_click = t)
