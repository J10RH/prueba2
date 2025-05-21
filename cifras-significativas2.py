import streamlit as st
import random
import numpy as np
#hola
# Funciones auxiliares para redondeo

def redondear_incertidumbre(inc):
    if inc == 0:
        return 0
    cifras = int(np.floor(np.log10(abs(inc))))
    primera = round(inc / (10 ** cifras))
    return primera * 10 ** cifras

def redondear_valor_central(valor, inc_redondeada):
    cifras = int(np.floor(np.log10(abs(inc_redondeada))))
    decimales = -cifras if cifras < 0 else 0
    return round(valor, decimales)

def generar_preguntas(n=100):
    unidades = ["m", "kg", "s", "cm", "mm", "L", "°C", "mol", "Pa", "W"]
    preguntas = []
    for _ in range(n):
        valor = round(random.uniform(1, 999), random.randint(2, 5))
        inc = round(random.uniform(0.01, 10), random.randint(1, 4))
        unidad = random.choice(unidades)
        preguntas.append((valor, inc, unidad))
    return preguntas

# Inicializar estado de sesión
if "preguntas_totales" not in st.session_state:
    st.session_state.preguntas_totales = generar_preguntas(100)

if "preguntas_mostradas" not in st.session_state:
    st.session_state.preguntas_mostradas = random.sample(st.session_state.preguntas_totales, 5)

if "respuestas" not in st.session_state:
    st.session_state.respuestas = ["" for _ in range(5)]

if "enviado" not in st.session_state:
    st.session_state.enviado = False

st.set_page_config(page_title="Redacción de Incertidumbre", layout="centered")
st.title("Redacción correcta de incertidumbres")

st.markdown("---")
st.markdown("### Instrucciones")
st.info("Redacte correctamente el valor central y la incertidumbre con unidades. La incertidumbre debe tener solo **una cifra significativa**. Puede usar el botón ± para añadir el símbolo correspondiente.")

# Botón ± global
if st.button("Insertar símbolo ±"):
    st.markdown("Copia y pega: `±`")

# Formulario con 5 preguntas
with st.form("formulario_respuestas"):
    for i, (valor, inc, unidad) in enumerate(st.session_state.preguntas_mostradas):
        st.markdown(f"### Caso {i+1}")
        st.latex(f"{valor} \\pm {inc} \\ \text{{{unidad}}}")
        st.session_state.respuestas[i] = st.text_input(f"Respuesta {i+1}",
            value=st.session_state.respuestas[i],
            placeholder="Ejemplo: 12.3 ± 0.3 m",
            key=f"respuesta_{i+1}")

    enviado = st.form_submit_button("Enviar")
    if enviado and not st.session_state.enviado:
        st.session_state.enviado = True
        st.success("✅ Su respuesta ha sido enviada.")

# Mostrar respuestas si se envió
if st.session_state.enviado:
    st.markdown("---")
    st.subheader("Respuestas del estudiante y respuestas correctas")
    for i, (valor, inc, unidad) in enumerate(st.session_state.preguntas_mostradas):
        inc_red = redondear_incertidumbre(inc)
        valor_red = redondear_valor_central(valor, inc_red)
        st.markdown(f"**Caso {i+1}:**")
        st.markdown(f"- Tu respuesta: `{st.session_state.respuestas[i]}`")
        st.markdown(f"- Respuesta correcta: `{valor_red} ± {inc_red} {unidad}`")
