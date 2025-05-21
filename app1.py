import streamlit as st

st.set_page_config(page_title="Aprende Python: Estructuras de Control", layout="centered")

st.title("🐍 Aprende Python: Estructuras de Control")

menu = st.sidebar.selectbox(
    "Selecciona una estructura",
    ["if", "elif / else", "for", "while"]
)

if menu == "if":
    st.header("🔹 Estructura `if`")
    st.markdown("""
    La estructura `if` permite ejecutar código solo si se cumple una condición.

    **Sintaxis:**
    ```python
    if condición:
        # código a ejecutar si la condición es verdadera
    ```

    **Ejemplo:**
    """)
    st.code("""
numero = 5
if numero > 0:
    print("El número es positivo")
""", language="python")

    with st.expander("Probar ejemplo"):
        numero = st.number_input("Introduce un número:", value=5)
        if numero > 0:
            st.success("✅ El número es positivo")
        else:
            st.warning("❌ La condición no se cumple")

elif menu == "elif / else":
    st.header("🔹 Estructura `elif` y `else`")
    st.markdown("""
    Se usan para evaluar múltiples condiciones.

    **Sintaxis:**
    ```python
    if condición1:
        # bloque 1
    elif condición2:
        # bloque 2
    else:
        # bloque 3
    ```

    **Ejemplo:**
    """)
    st.code("""
x = 0
if x > 0:
    print("Positivo")
elif x == 0:
    print("Cero")
else:
    print("Negativo")
""", language="python")

    with st.expander("Probar ejemplo"):
        x = st.number_input("Introduce un número (x):", value=0)
        if x > 0:
            st.success("Positivo")
        elif x == 0:
            st.info("Cero")
        else:
            st.warning("Negativo")

elif menu == "for":
    st.header("🔹 Estructura `for`")
    st.markdown("""
    Se usa para iterar sobre secuencias (listas, strings, rangos).

    **Sintaxis:**
    ```python
    for variable in secuencia:
        # código a ejecutar
    ```

    **Ejemplo:**
    """)
    st.code("""
for i in range(1, 6):
    print(i)
""", language="python")

    with st.expander("Probar ejemplo"):
        n = st.slider("¿Hasta qué número quieres contar?", min_value=1, max_value=20, value=5)
        st.write("Resultado:")
        for i in range(1, n + 1):
            st.write(f"{i}")

elif menu == "while":
    st.header("🔹 Estructura `while`")
    st.markdown("""
    Repite el bloque de código **mientras** la condición sea verdadera.

    **Sintaxis:**
    ```python
    while condición:
        # código a ejecutar
    ```

    **Ejemplo:**
    """)
    st.code("""
contador = 0
while contador < 5:
    print(contador)
    contador += 1
""", language="python")

    with st.expander("Probar ejemplo"):
        limite = st.slider("¿Hasta cuánto quieres contar?", min_value=1, max_value=10, value=5)
        st.write("Resultado:")
        contador = 0
        while contador < limite:
            st.write(contador)
            contador += 1
