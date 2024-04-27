import streamlit as st

from streamlit_option_menu import option_menu

import login , posts , myposts , spil
st.set_page_config(
    page_title = "Politik Forum"  , 
) # type: ignore

class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self,title,func):
        self.apps.append({
            "title" : title, 
            "function" : func
        })

    def run():

        with st.sidebar:
            app = option_menu(
                menu_title = 'Politik Forum' , 
                options = ['Login' , 'Posts' , 'My Posts' , 'Spil'] , 
                icons = ['person-circle' , 'chat-fill' ],
                menu_icon = ['chat-text-fill'] , 
                default_index = 1 ,
                styles = {
                    "container" : { "padding" : "5!important" , "background-color" : 'black'} ,
                    "icon" : {"color" : "white" , "font-size" : "23px" } ,
                    "nav-link" : {"color" : "white" , " font-size" : "20px" , "text-align" : "left"} , 
                    "nav-link-selected" : {"background-color" : "red"}
                }
            )
        if app == 'Login':
            login.app()
        if app=='Posts':
            posts.app()
        if app == 'My Posts':
            myposts.app()
        if app == 'Spil':
            spil.app()
    
    run()