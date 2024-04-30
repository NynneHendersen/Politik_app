import streamlit as st
from firebase_admin import firestore

def app():
    st.title('Alle Opslag')

    # Laver session_state varibel for databasen
    if 'db' not in st.session_state:
        st.session_state.db = ''
        
    # Laver session_state varibel for brugernavnet
    if 'username' not in st.session_state:
        st.session_state.username = ''
        
    db = firestore.client()
    st.session_state.db = db

    # Variabel til tekst i post felt
    ph = ''

    if st.session_state.username == '':
        ph = 'Login for at poste '
    else:
        ph = 'Post din mening'
    
    # Opretter et text area hvor man skriver sit post og giver den placeholder teksten 'ph'
    post = st.text_area(label = ' :orange[+ New Post]' , placeholder = ph , height = None , max_chars = 500)

    # Opretter liste med forbudte ord / udtryk
    forbudte_ord = ["fuck", "shit", "lort", "damn", "asshole", "piss", "bitch", "cunt", "motherfucker", "ass", "bastard", "bullshit", "cock", "dick", "pussy" , "røvhul", "skiderik", "fjols", "klaphat", "idiot", "svin", 
        "kælling", "dumrian", "møgkælling", "fanden", "helvede", "pik", "fisse", 
        "skvat", "drittsekk", "døgenigt", "bøsserøv", "luder", "skod", "pikhoved", 
        "møgfisse", "fissehår", "pis", "skide", "bolle", "nar", "tåbe", "svans",
        "spade", "bonderøv", "fede", "lallende", "taber", "mongol", "spasser" , "prick", "slut", "wanker", 
        "twat", "nigger", "spastic", "retard", "whore", "hoe", "sucker", 
        "fuckface", "shithead", "douchebag", "jerk", "arsehole", "crap", "bollocks", 
        "tosser", "gobshite", "bellend", "numbnuts", "dickhead" , "f*ck" , "sl*t" , "m*gk*lling" , "m*gkælling" , "piksutter" , "r*v" ]
    
    # Opret et opslag når man trykker på 'Post'-knap
    if st.button('Post' , use_container_width = 20):
        # Tjekker om der står tekst i 'post'-feltet
        if post != '':
            # Tjekker om forbudte ord bliver brugt
            if any(word in post.lower() for word in forbudte_ord):
                # Hvis de bruges skrives dette:
                st.warning("Dit opslag indeholder forbudte ord. Fjern dem for at lægge dit opslag op og bidrage til den gode tone :)") 
           
            # Hvis ikke lægges postet op
            else:

                # Opretter data til nyt dokument i databasen 'Posts' med postet som dokument ID
                data = {"Content": post, 'Username': st.session_state.username}
                
                # Specificerer et dokument ID 
                document_id = post

                # Tilføjer dokument til databasen med værdien data
                db.collection('Posts').document(post).set(data)
            
            st.success('Post Uploaded!')
    
    # Hvis ikke der står noget i 'post'-feltet skrives dette:
    else:
        st.write("Du skal skrive noget for at lave et opslag.")
    
    st.divider()
    st.header(' :black[Seneste Posts]')

    # Henter alle documents fra databasen 'Posts'
    docs = db.collection('Posts').get()

    #Laver et loop som finder hvert opslag i databasen og poster det
    for doc in docs:

        # Laver doc dokumentet om til en dictionary 
        d = doc.to_dict()

        try:

            #post_comments = d['Comments'] 
            post_content = d['Content']
            post_username = d['Username']
            post_d =st.text_area(label = '***:red[Postet af:]***' + ':blue[{}]'.format(post_username), value = post_content , height = 20)

            comment = st.text_input(label = 'Skriv en kommentar' , key = doc.id)
            comment_button = st.button('Tilføj Kommentar' , key = doc.id + '_button')

            if comment_button:
                if comment != '':
                    # Tjekker om forbudte ord bliver brugt
                    if any(word in comment.lower() for word in forbudte_ord):
                        # Hvis de bruges skrives dette:
                        st.warning("Dit opslag indeholder forbudte ord. Fjern dem for at lægge dit opslag op og bidrage til den gode tone :)") 
                    # Ellers tilføjes ny kommentar til databasen
                    else:
                        #Tilføjer en ny kommentar til arrayet 'Comments' for det pågældende dokument (post)
                        db.collection('Posts').document(doc.id).update({'Comments': firestore.ArrayUnion([comment])})
                        st.succes('Kommentar tilføjet')
            
            post_comments = d['Comments'] 
            
            for comment_text in post_comments:
                st.text_area(label='Kommentar:', value=comment_text, height=20)   
            
            st.divider()
            
        except:
            pass
    

                    
                

    
