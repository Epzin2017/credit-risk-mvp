import streamlit as st
import requests

API_URL = "http://localhost:8000"

st.set_page_config(page_title="Global Credit Risk MVP", layout="wide")
st.title("🌍 Global Credit Risk MVP (Sprint 0)")
st.caption("Streamlit UI calling FastAPI mock endpoints.")

with st.sidebar:
    st.header("Status")
    if st.button("Check API (/health)"):
        try:
            r = requests.get(f"{API_URL}/health", timeout=5)
            st.success(r.json())
        except Exception as e:
            st.error(f"API offline: {e}")

st.info("Use the left menu (pages) to navigate.")