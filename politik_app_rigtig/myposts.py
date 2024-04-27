import streamlit as st
from firebase_admin import firestore

def app():
    
    db = firestore.client()

    try:
        st.title('Dine Posts')

        st.write('Under konstruktion')

        # Finder brugerens opslag i databasen
        result = db.collection('Posts').document(st.session_state['username']).get()
        # Konverterer variablen 'resultat' til dictionary
        r = result.to_dict()
        # Finder content (posts) i databasen
        content = r['Content']

        def delete_post(k):
            c = int(k)
            h = content[c]
            try:
                db.collection('Posts').document(st.session_state['username']).update({"Content" : firestore.ArrayRemove([h])})
                st.warning('Dit post er slettet.')
            except:
                st.write('Noget gik galt..')
        
        for c in range(len(content)):
            st.text_area(label = '' , value = content[c])
            st.button('Slet Post' , on_click = delete_post , args = ([c]) , key = c) 
   
    except:
        if st.session_state.username == '':
            st.write('Please Login first')