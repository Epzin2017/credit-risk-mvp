import streamlit as st
import requests

API_URL = "http://localhost:8000"

st.header("📚 Knowledge (mock)")
files = st.file_uploader("Upload docs (PDF/MD/TXT)", accept_multiple_files=True)
tags = st.text_input("Tags (optional)", value="npl,definition")

if st.button("Ingest (mock)") and files:
    multipart = [("files", (f.name, f.getvalue())) for f in files]
    r = requests.post(f"{API_URL}/v1/knowledge/ingest", files=multipart, data={"tags": tags})
    st.json(r.json())

st.divider()

question = st.text_area("Question", value="What is NPL and why does it rise in crises?")
if st.button("Query (mock)"):
    r = requests.post(f"{API_URL}/v1/knowledge/query", json={"question": question, "top_k": 4}, timeout=10)
    st.json(r.json())