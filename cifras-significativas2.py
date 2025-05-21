import streamlit as st
import random
import numpy as np

def redondear_incertidumbre(inc):
    if inc == 0:
        return 0
    cifras = int(np.floor(np.log10(abs(inc))))
    primera = round(inc / (10**cifras))
    return primera * 10**cifras

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

# Estado inicial de sesión
if "preguntas_totales" not in st.session_state:
    st.session_state.preguntas_totales = generar_preguntas(100)

if "preguntas_mostradas" not in st.session_state:
    st.session_state.preguntas_mostradas = random.sample(st.session_state.preguntas_totales, 5)

if "respuestas" not in st.session_state:
    st.session_state.respuestas = [""] * 5

if "enviado" not in st.session_state:
    st.session_state.enviado = False

# Layout
st.set_page_config(page_title="Redacción de Incertidumbre", layout="centered")
st.title("🧪 Redacción correcta de incertidumbres")

st.info("Expresa correctamente los siguientes 5 casos. Usa el símbolo **±** con una sola cifra significativa para la incertidumbre, y redondea el valor central en consecuencia.")

st.markdown("Puedes copiar el símbolo desde aquí si lo necesitas:")
st.code("±")

# Formulario interactivo
with st.form("formulario"):
    for i, (valor, incert, unidad) in enumerate(st.session_state.preguntas_mostradas, start=1):
        st.markdown(f"### Caso {i}")
        st.latex(f"{valor} \\pm {incert}\\;\\text{{{unidad}}}")
        
        col1, col2 = st.columns([4, 1])
        with col1:
            st.session_state.respuestas[i-1] = st.text_input(f"Ingrese su respuesta {i}", 
                value=st.session_state.respuestas[i-1],
                key=f"respuesta_{i}",
                placeholder="Ejemplo: 12.3 ± 0.3 m")
        with col2:
            st.markdown("### ")
            if st.button(f"±", key=f"boton_{i}"):
                st.session_state.respuestas[i-1] += " ± "

    enviado = st.form_submit_button("Enviar")

    if enviado and not st.session_state.enviado:
        st.session_state.enviado = True
        st.success("✅ Tus respuestas han sido enviadas correctamente. Solo puedes responder una vez.")

# Mostrar respuestas correctas solo después de enviar
if st.session_state.enviado:
    st.markdown("---")
    st.subheader("✔️ Respuestas correctas")

    for i, (valor, incert, unidad) in enumerate(st.session_state.preguntas_mostradas, start=1):
        incert_red = redondear_incertidumbre(incert)
        valor_red = redondear_valor_central(valor, incert_red)
        st.write(f"**Caso {i}:** `{valor_red} ± {incert_red} {unidad}`")
