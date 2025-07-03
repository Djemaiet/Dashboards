import streamlit as st
col1, col2 = st.columns(2,border=False)

with col2:
    st.title("The Expandables")
    c1, c2, c3= st.columns(3,border=False)
st.write("The Expendables (engl. „die Entbehrlichen“) ist ein Ensemble-Actionfilm, bei dem Sylvester Stallone Regie führte und zusammen mit Dave Callaham das Drehbuch schrieb. Der Film zollt den Actionfilmen der 1980er und 1990er Jahre Tribut und hat eine Reihe bekannter Schauspieler dieses Genres in den Hauptrollen. Dazu gehören Dolph Lundgren, Mickey Rourke, Jet Li und Jason Statham. Außerdem haben Arnold Schwarzenegger und Bruce Willis Kurzauftritte.")

tab1, tab2, tab3 = st.tabs(["Überblick", "Hauptcast", "Media"])

with tab1:
    st.subheader("Kurzer Inhalt")
    st.write("Eine Söldnergruppe um Barney „The Schizo“ Ross wird im Golf von Aden zu Geiseln befreit. Ihr Auftrag führt sie auf die Insel Vilena, wo sie gegen eine Militärdiktatur und einen machthungrigen Ex-CIA-Agenten kämpfen. Während sie versuchen, die Tochter des Diktators zu retten, decken sie eine dunkle Verschwörung auf. Ein actiongeladenes Abenteuer voller Kämpfe, Verrat und Heldentum.")
    
with tab2:
    st.subheader("Besetzung-Hauptrollen")
    st.write("- Sylvester Stallone")
    ("- Jason Statham")
    ("- Dolph Lundgren")
    ("- Jet Li")
    ("- Terry Crews")
    ("- Randy Couture")
    ("- Charisma Carpenter")
    ("- Mickey Rourke")
    ("- Giselle Itié")
    ("- Lauren Jones")
    ("- David Zayas")
    ("- Eric Roberts")
    ("- Steve Austin")
    ("- Gary Daniels")
    ("- Bruce Willis")
    ("- Arnold Schwarzenegger")


with tab3:
    st.subheader("Film(Trailer)")
    st.video("https://youtu.be/OPwwdvjJOwU?si=t4WwPQjAnacu7WrH")

with c1:
    st.metric(label="IMDb Rating", value="6,4/10")

with c2:
    st.metric(label="Erscheinungsjahr", value="2010")


with col1:
    st.image("https://m.media-amazon.com/images/S/pv-target-images/466763dbdc506554f2dfcc5789db787ad8680f5923e7ad07ecd7e8ecd6cb4f80.jpg")

st.sidebar.title("Statistik")
st.sidebar.header("🌐Links")
st.sidebar.write("- [Wikipedia](https://de.wikipedia.org/wiki/The_Expendables#Casting)")


