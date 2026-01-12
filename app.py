import streamlit as st
import pandas as pd

# Page Title
st.set_page_config(page_title="SAP iXp Data Prep Prototype")
st.title("📊 AI Data Preparation & Semantic Mapping")
st.markdown("Developed for SAP iXp Internship Application")

# 1. THE "RAW" DATA 
raw_json_data = [
    {"sys_id": "DE_01", "status_code": 101, "runtime_ms": 15600},
    {"sys_id": "US_02", "status_code": 404, "runtime_ms": 2100},
    {"sys_id": "DE_01", "status_code": 101, "runtime_ms": 8900},
    {"sys_id": "UK_03", "status_code": 500, "runtime_ms": 12400},
]

st.header("1. Raw JSON Dataset")
st.write("This is the 'messy' data an LLM might hallucinate on:")
st.json(raw_json_data)

# 2. THE TRANSFORMATION LOGIC 
st.header("2. Semantic Transformation (The 'Math' Step)")

# Mapping cryptic codes to human-readable text
status_mapping = {
    101: "Success: Upgrade Complete",
    404: "Error: Resource Not Found",
    500: "Critical: System Timeout"
}

# Creating the Dataframe (Table)
df = pd.DataFrame(raw_json_data)

# Applying Logic: Convert ms to seconds & Map status codes
df['Status_Description'] = df['status_code'].map(status_mapping)
df['Runtime_Seconds'] = df['runtime_ms'] / 1000

# 3. THE "AI-READY" OUTPUT
st.subheader("Cleaned Relational View")
st.write("This table is now optimized for an LLM to answer questions accurately:")
st.dataframe(df[['sys_id', 'Status_Description', 'Runtime_Seconds']])

# 4. INTERVIEW HIGHLIGHT
st.success("**Why this matters for SAP:** I normalized units (ms to sec) and removed ambiguity from status codes. This prevents the LLM from 'guessing' what 101 or 15600 means.")
