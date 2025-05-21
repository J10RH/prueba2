import streamlit as st
import random
import numpy as np

# Funciones auxiliares para redondeo

def redondear_incertidumbre(inc):
    if inc == 0:
        return 0
    cifras = int(np.floor(np.log10(abs(inc))))
    primera = round(inc / (10 ** cifras))
    return primera * 10 ** cifras

def redondear_valor_central(valor, inc_redondeada):
    cifras = int(np.floor(np.log10(abs(inc_redondeada))))
    return int(round(valor / (10 ** cifras)) * (10 ** cifras))

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
st.info("Redacte correctamente el valor central y la incertidumbre con unidades. La incertidumbre debe tener solo **una cifra significativa**. Puede usar el símbolo ± que se muestra abajo.")

# Mostrar símbolo ± con opción para copiar
st.markdown("#### Símbolo ± para redactar respuestas")
col1, col2 = st.columns([6, 1])
with col1:
    st.text_input("Símbolo ± (puede copiarlo desde aquí)", value="±", key="simbolo_pm")
with col2:
    st.write("")
    st.write("")
    st.markdown("⬅️ Copie este símbolo")

# Formulario con 5 preguntas
with st.form("formulario_respuestas"):
    respuestas_input = []
    for i, (valor, inc, unidad) in enumerate(st.session_state.preguntas_mostradas):
        st.markdown(f"### Caso {i+1}")
        st.latex(f"{valor} \\pm {inc} \\, \\mathrm{{{unidad}}}")
        respuesta = st.text_input(
            label=f"Redacte correctamente el valor central y la incertidumbre (Caso {i+1})",
            placeholder="Ejemplo: 12.3 ± 0.3 m",
            key=f"respuesta_{i+1}"
        )
        respuestas_input.append(respuesta)

    enviar = st.form_submit_button("Enviar respuestas")
    if enviar and not st.session_state.enviado:
        st.session_state.enviado = True
        st.session_state.respuestas = respuestas_input
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
