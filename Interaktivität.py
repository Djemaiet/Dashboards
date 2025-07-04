import streamlit as st

st.title("Interactive Widgets")
st.header("Checkbox:")

#st.checkbox(label="Volljährig", value=False)

#is_adult = st.checkbox(label="Volljährig", value=False)
#if is_adult:
 #   st.write("Benutzer ist volljährig")

def greetings():
    print("Willkommen volljähriger Benutzer!")
    print(f"Status der Checkbox: {st.session_state.adult_check}")

buttons = st.checkbox(label="Volljährig", value=False, on_change=greetings, key="adult_check")
if buttons:
    st.write("Benutzer ist volljährig")

choice = st.radio("Wähle eine Farbe:", ["Rot", "Grün", "Blau"])
st.write("Du hast gewählt:", choice)

if st.button("Nicht mich Klicken"):
    st.write("Warum🤯")

def btn_click():
    print("Button wurde geklickt!")

if st.button("Klicke mich", on_click=btn_click):
    st.write("Dankeschön😍")

city = st.selectbox("Stadt auswählen:", ["Berlin", "München", "Hamburg"])
st.write("Deine Stadt:", city)

foods = st.multiselect("Lieblingsessen:", ["Pizza","Sushi","Salat"])
st.write("Du magst:", foods)

age = st.slider("Wie alt bist du?", 0, 100, 15)
st.write("Alter:", age)

datum = st.date_input("Datum wählen")
zeit = st.time_input("Uhrzeit wählen")
st.write("Ausgewählt:", datum, zeit)






#st.title("BMI Rechner")

#with st.form(key="first_form"):
 #   first_name = st.text_input("Vorname")
  #  second_name = st.text_input("Nachname")
   # age = st.number_input(
    #    "Dein Alter",
     #   min_value=0,        
      #  max_value=120,      
       # value=18,        
        #step=1,           
        #format="%d"
    #)
    #mail = st.text_input("E-Mail")
    #submitted = st.form_submit_button("Absenden")



st.title("BMI Rechner")

with st.form(key="first_form"):
    col1, col2 = st.columns(2)
    with col1:
        first_name = st.text_input("Vorname")
        age = st.number_input(
            "Dein Alter",
            min_value=0,        
            max_value=120,      
            value=18,        
            step=1,           
            format="%d"
        )
        height_cm = st.number_input(
            "Deine Körpergröße in cm",
            min_value=50.0,
            max_value=250.0,
            value=170.0,
            step=0.5,
            format="%.1f"
            )
    with col2:
        second_name = st.text_input("Nachname")
        weight = st.number_input(
            "Dein Gewicht in kg",
            min_value=0.0,        
            max_value=600.0,      
            value=50.5,        
            step=0.1,           
            format="%.1f"
        )

    mail = st.text_input("E-Mail")
    submitted = st.form_submit_button("Absenden")
    
if submitted:
    errors = []
    if not first_name:
        errors.append("Bitte Vorname eingeben.")
    if not second_name:
        errors.append("Bitte Nachname eingeben.")
    if "@" not in mail:
        errors.append("Bitte gültige E-Mail eingeben.")
    
    if errors:
        for err in errors:
            st.error(err)
    else:
        height_m = height_cm / 100
        bmi = weight / (height_m ** 2)
        
        if bmi < 18.5:
            category = "Untergewicht"
        elif bmi < 25:
            category = "Normalgewicht"
        elif bmi < 30:
            category = "Übergewicht"
        elif bmi < 35:
            category = "Adipositas Grad I"
        elif bmi < 40:
            category = "Adipositas Grad II"
        else:
            category = "Adipositas Grad III"

        st.success(f"Hallo {first_name} {second_name}!")
        st.write(f"- **Alter:** {age} Jahre")  
        st.write(f"- **Größe:** {height_cm:.1f} cm")  
        st.write(f"- **Gewicht:** {weight:.1f} kg")  
        st.metric(label="Dein BMI", value=f"{bmi:.1f}", delta=f"{category}")
        
        st.markdown("**Gewichtsklassifikation bei Erwachsenen:**")
        st.markdown("""
        - BMI < 18,5: Untergewicht  
        - BMI 18,5 - 24,9: Normalgewicht  
        - BMI 25 - 29,9: Übergewicht  
        - BMI 30 - 34,9: Adipositas Grad I  
        - BMI 35 - 39,9: Adipositas Grad II  
        - BMI ≥ 40: Adipositas Grad III  
        """)
        st.write("Bei Fragen kann dir dein Arzt weiterhelfen.")