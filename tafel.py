import streamlit as st
print("Code wird erneut ausgeführt")
st.title("Tag 2 wird interaktiv")

is_adult = st.checkbox(label="Volljährig")

print(is_adult)

if is_adult:
    st.write("Benutzer ist Volljährig")