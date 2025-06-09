import streamlit as st

st.set_page_config(page_title="Marcha Química de Cationes", layout="centered")

# Diccionario de compuestos problema (puedes ampliarlo)
muestras = {
    "Muestra 1: Nitrato de plata (AgNO3)": ["Grupo I"],
    "Muestra 2: Nitrato de plomo (Pb(NO3)2)": ["Grupo I", "Grupo II"],
    "Muestra 3: Cloruro de mercurio(I) (Hg2Cl2)": ["Grupo I"],
    "Muestra 4: Sulfato de cobre (CuSO4)": ["Grupo II"],
    "Muestra 5: Nitrato de cadmio (Cd(NO3)2)": ["Grupo II"],
    "Muestra 6: Nitrato férrico (Fe(NO3)3)": ["Grupo III"],
    "Muestra 7: Nitrato de aluminio (Al(NO3)3)": ["Grupo III"],
    "Muestra 8: Nitrato de bario (Ba(NO3)2)": ["Grupo IV"],
    "Muestra 9: Nitrato de calcio (Ca(NO3)2)": ["Grupo IV"],
    "Muestra 10: Cloruro de potasio (KCl)": ["Grupo V"],
    "Muestra 11: Nitrato de sodio (NaNO3)": ["Grupo V"],
    "Muestra 12: Cloruro de amonio (NH4Cl)": ["Grupo V"]
}

st.title("🧪 Marcha Química de Cationes")
st.write("Simulador interactivo de análisis cualitativo")

# Selección de muestra
seleccion = st.selectbox("Selecciona una muestra:", list(muestras.keys()))
grupos_presentes = muestras[seleccion]

# Función para mostrar resultado
def evaluar_paso(nombre_grupo, justificacion):
    if nombre_grupo in grupos_presentes:
        st.success(f"✅ Resultado positivo: {justificacion}")
    else:
        st.error(f"❌ Resultado negativo: {justificacion}")

# Paso 1
with st.expander("🔹 Paso 1: Adición de HCl diluido"):
    if st.button("Evaluar Paso 1"):
        evaluar_paso("Grupo I", "Se observa un precipitado blanco, indicando la presencia de cloruros insolubles como AgCl o PbCl2.")

# Paso 2
with st.expander("🔹 Paso 2: Adición de H2S en medio ácido"):
    if st.button("Evaluar Paso 2"):
        evaluar_paso("Grupo II", "Aparece un precipitado de color oscuro (negro o marrón), indicando la presencia de sulfuros insolubles como CuS o PbS.")

# Paso 3
with st.expander("🔹 Paso 3: Adición de NH4OH y NH4Cl"):
    if st.button("Evaluar Paso 3"):
        evaluar_paso("Grupo III", "Se forma un precipitado gelatinoso, característico de hidróxidos como Fe(OH)3 o Al(OH)3.")

# Paso 4
with st.expander("🔹 Paso 4: Adición de (NH4)2CO3"):
    if st.button("Evaluar Paso 4"):
        evaluar_paso("Grupo IV", "Se observa un precipitado blanco, que corresponde a carbonatos como BaCO3 o CaCO3.")

# Paso 5
with st.expander("🔹 Paso 5: Identificación de cationes del Grupo V"):
    if st.button("Evaluar Paso 5"):
        evaluar_paso("Grupo V", "No hay precipitación, pero se identifican mediante pruebas específicas como flama (Na, K) o liberación de amoníaco (NH4⁺).")

# Paso 6 (Adicional: Confirmación o test específico)
with st.expander("🔹 Paso 6: Confirmación específica"):
    if st.button("Evaluar Paso 6"):
        st.info("Usa pruebas adicionales como reacción con KSCN para Fe³⁺, o prueba de flama para Na⁺ y K⁺.")

