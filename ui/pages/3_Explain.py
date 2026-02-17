import json
from pathlib import Path
import streamlit as st
import requests

API_URL = "http://localhost:8000"

def load_countries():
    data = json.loads(Path("config/countries.json").read_text(encoding="utf-8"))
    return data["countries"]

st.header("🧠 Explain (mock)")
countries = load_countries()

country = st.selectbox("Country", countries, index=0)
horizon = st.selectbox("Horizon (years)", [1, 2, 3], index=2)
question = st.text_area("Question", value="Explain the forecast trend and possible drivers.")

if st.button("Explain (mock)"):
    r = requests.post(
        f"{API_URL}/v1/decision/explain",
        json={"country": country, "horizon_years": horizon, "question": question},
        timeout=10
    )
    st.json(r.json())