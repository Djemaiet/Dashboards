import streamlit as st
import pandas as pd

# Datei laden (Pfad anpassen!)
df = pd.read_csv("teams.csv")


# Erste Zeilen anzeigen
print(df.head())


st.title("NHL Teams")



team_filter = st.sidebar.text_input("Teamname enthält:")
if team_filter:
    df =df[df["Team"].str.contains(team_filter, case =False, na= False)]

Jahresbereich = st.sidebar.slider("Jahresbereich filtern", 
                
                  min_value= 1990, 
                  max_value= 2011,
                 value=[1990, 2011])
df = df[(df["Jahr"] >= Jahresbereich[0]) & (df["Jahr"] <= Jahresbereich[1])]
st.dataframe(df)

