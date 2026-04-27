import streamlit as st
from groq import Groq

# 1. Configuración de la página
st.set_page_config(
    page_title="Selector de Modelos IA",
    page_icon="🤖"
)

# 2. Lista de modelos de IA (criterio: usar listas)
MODELOS = [
    "Llama 3.1 8B",
    "Llama 3.2 3B",
    "Mixtral 8x7B",
    "Gemma 2 9B"
]

# 3. Barra lateral con selectbox
st.sidebar.title("Configuración")
modelo_seleccionado = st.sidebar.selectbox(
    "Elegí el modelo de IA:",
    MODELOS
)

# 4. Leer API Key desde secrets
api_key = st.secrets.get("CLAVE_API")

# 5. Contenido principal
st.title("Aplicación Web con Streamlit")
st.write(f"✅ Modelo seleccionado: **{modelo_seleccionado}**")

# 6. Verificación de conexión con Groq (condicional)
if api_key:
    st.success("✅ Conexión con Groq lista")
    cliente = Groq(api_key=api_key)
else:
    st.error("❌ No se encontró la API Key de Groq")