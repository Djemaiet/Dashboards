import pandas as pd
import streamlit as st

st.title("Dashboard: Kennzahlen 2024")
st.header(" Finanzen")
st.metric(label="Umsatz", value="2,5 Mio", delta="+4%")

st.header("Kunden")
st.metric(label="Kundenzahl", value="8.420", delta="+120")

st.header("Mitarbeitende")
st.metric(label="Zufriedenheit", value="87%", delta="-2%")


st.title("Medien Einfügen")
st.header("Bilder")
st.subheader("Eine Elektromagnetische Welle")

#Bilder hinzufügen
st.image(
"https://th.bing.com/th/id/OIP.iH_OFGcp3vb6rT23uafFBwHaEB?w=326&h=180&c=7&r=0&o=7&dpr=1.5&pid=1.7&rm=3",
caption="Elektromagnetische Welle",
use_container_width=False)

st.subheader("Das sichtbare Spektrum:")

st.image(
"http://www.thermoglass.de/_sites/thermoglass/upload/images/615fc0ca95c1ddfecd813f81774e6f34_11-zareni-graf-wiki-de.png",
caption="Sichtbare Spektrum der elektromagnetischen Welle",
use_container_width=False)

#Videos hinzufügen
st.subheader("Animation der elektromagnetischen Welle:")
st.video("https://www.youtube.com/watch?v=aCTRjVEmeC0")

#Medien hochladen
st.subheader("Video hochladen:")
uploaded = st.file_uploader("Lade eine Videodatei hoch", type=["mp4", "mov"])
if uploaded:
    st.video(uploaded)

    #Medien downloaden
#st.subheader("Bild downloaden:")
#st.download_button(
    #label="Bild herunterladen",
    #data=open("assets/test_bild.png", "rb").read(),
    #file_name="mein_bild.png",
    #mime="image/png"

#Grundlegende Layouts in Streamlit
#tab1, tab2, tab3, =st.tabs(["Tab 1","Tab 2","Tab 3"])
#with tab1:
#    st.write("You are in Tab 1")

#with tab2:
 #   st.write("You are in Tab 2")

#with tab3:
 #   st.write("You are in Tab 3") 


#with tab1:
 #   st.write("You are in Tab 1")
    
#with tab2:
  #  st.write("You are in Tab 2")
    
#with tab3:
   # st.write("You are in Tab 3")

#col1, col2 = st.columns(2)
#with col1:
   # st.header("Column 1")
   # st.write("Content for column 1")
#with col2:
 #   st.header("Column 2")
  #  st.write("Content for column 2")


st.sidebar.title("This is the Sidebar")
st.sidebar.write("You can place elements like buttons and text here.")
sidebar_input = st.sidebar.text_input("Enter something in the sidebar:")

tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])

with tab1:
    st.write("You are in Tab 1")
    
with tab2:
    st.write("You are in Tab 2")
    
with tab3:
    st.write("You are in Tab 3")

col1, col2 = st.columns(2)
with col1:
    st.header("Column 1")
    st.write("Content for column 1")
with col2:
    st.header("Column 2")
    st.write("Content for column 2")

with st.container(border=True):
    st.write("This is inside a container.")
    st.write("You can think of containers as a grouping for elements.")
    st.write("Containers help manage sections of the page.")

placeholder = st.empty()
placeholder.write("This is an empty placeholder, useful for dynamic content.")

if st.button("Update Placeholder"):
    placeholder.write("The content of this placeholder has been updated")

with st.expander("Expand for more details"):
    st.write("This is additional information that is hidden by default.")
    st.write("You can use expanders to keep your interface cleaner.")

#Button mit pop up fenster
st.write("Hover over this button for a tooltip")
st.button("Button with Tooltip", help="This is a tooötip or popover on hover!")

#sidebarn eingefügter text anzeigen lassen 
#if sidebar_input:
   # st.write(f"You entered in the sidebar: {sidebar_input}")
#Abkürzung import streamlit as st

#exp = st.expander("Details")
#exp.write("Einige zusätzliche Informationen")

#sidebar = st.sidebar
#sidebar.write("Inhalt in der Sidebar")

#col1, col2 = st.columns(2)
#col1.write("In Spalte 1")
#col2.write("In Spalte 2")

#container = st.container()
#container.write("In einem Container")



#Terminal eingabe für Streamlit:  python -m streamlit run LieblingsFilm.py