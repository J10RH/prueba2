import streamlit as st
import random
import numpy as np

# Función para redondear incertidumbre a una sola cifra significativa
def redondear_incertidumbre(incert):
    cifras = int(np.floor(np.log10(abs(incert))))
    primera_cifra = round(incert / (10**cifras))
    incert_red = primera_cifra * 10**cifras
    return incert_red

# Generar una lista de 100 preguntas
def generar_preguntas(n=100):
    unidades = ["m", "kg", "s", "cm", "mm", "L"]
    preguntas = []
    for _ in range(n):
        valor = round(random.uniform(1, 999), random.randint(1, 3))
        incert = round(random.uniform(1, 9.9), 1) * 10**random.randint(-2, 0)
        unidad = random.choice(unidades)
        preguntas.append((valor, incert, unidad))
    return preguntas

# Inicialización de sesión
if "pregunta" not in st.session_state:
    preguntas = generar_preguntas()
    st.session_state.pregunta = random.choice(preguntas)
if "enviado" not in st.session_state:
    st.session_state.enviado = False

# Configuración de página
st.set_page_config(page_title="Incertidumbre y cifras significativas", layout="centered")
st.title("🎯 Evaluación: Incertidumbre con una cifra significativa")

st.info("**Instrucciones:** Escriba correctamente el valor central y la incertidumbre, tal que la incertidumbre tenga **una sola cifra significativa**. Use el símbolo ± para separar.")

# Mostrar pregunta
valor, incert, unidad = st.session_state.pregunta
st.markdown("**Pregunta:**")
st.latex(f"{valor} \\pm {incert}\\;\\text{{{unidad}}}")

# Campo de respuesta
if not st.session_state.enviado:
    respuesta = st.text_input("✏️ Escriba su respuesta (ejemplo: 23.4 ± 0.5 m)", placeholder="valor ± incertidumbre unidad")

    if st.button("Enviar"):
        if respuesta.strip() == "":
            st.warning("Por favor escriba su respuesta antes de enviar.")
        else:
            st.session_state.enviado = True
            st.success("✅ Su respuesta ha sido enviada.")

            # Mostrar la respuesta correcta
            incert_red = redondear_incertidumbre(incert)
            # Redondear el valor central al mismo decimal que la incertidumbre redondeada
            cifras = int(np.floor(np.log10(abs(incert_red))))
            decimales = -cifras if cifras < 0 else 0
            valor_redondeado = round(valor, decimales)
            correcta = f"{valor_redondeado} ± {incert_red} {unidad}"

            st.markdown("### ✔️ Respuesta correcta:")
            st.code(correcta)
else:
    st.info("🛑 Ya ha enviado su respuesta.")
