import streamlit as st
import random
import numpy as np

# Función para generar un valor central y su incertidumbre
def generar_pregunta():
    valor_central = round(random.uniform(1, 999), random.randint(1, 3))
    # incertidumbre con una o dos cifras significativas, para responder con solo una
    exponente = random.randint(-2, 1)
    incertidumbre = round(random.uniform(1, 9.9), 1) * 10**exponente
    return valor_central, incertidumbre

# Cargar pregunta aleatoria para cada sesión
if "pregunta" not in st.session_state:
    st.session_state.pregunta = generar_pregunta()
if "enviado" not in st.session_state:
    st.session_state.enviado = False

st.set_page_config(page_title="Incertidumbre - Evaluación", layout="centered")
st.title("🧪 Evaluación: Cifras significativas e incertidumbre")

st.info("**Instrucciones**: Redacte correctamente el valor central y su incertidumbre, tal que la incertidumbre se escriba con **una sola cifra significativa**.")

valor, incert = st.session_state.pregunta
st.markdown(f"**Pregunta:** ¿Cómo se debe reportar el siguiente valor con su incertidumbre?\n\n")
st.latex(f"{valor} \\pm {incert}")

if not st.session_state.enviado:
    respuesta = st.text_input("Ingrese su respuesta aquí (ejemplo: 23.4 ± 0.5)")

    if st.button("Enviar"):
        if respuesta.strip() == "":
            st.warning("Por favor, escriba una respuesta antes de enviar.")
        else:
            st.session_state.enviado = True
            # Aquí puedes guardar la respuesta si deseas (por ejemplo en un archivo o base de datos)
            st.success("✅ Su respuesta ha sido enviada. No se permite un segundo intento.")
else:
    st.info("🛑 Ya ha enviado su respuesta. No puede volver a intentarlo.")
