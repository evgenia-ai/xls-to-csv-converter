import streamlit as st
import pandas as pd
import io

st.set_page_config(page_title="XLS → CSV Converter", page_icon="📄")

st.title("📄 XLS → CSV Converter (Semicolon Separated)")

uploaded_file = st.file_uploader("Upload XLS or XLSX file", type=["xls", "xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)

    # Convert to CSV with semicolon
    csv_data = df.to_csv(index=False, sep=";").encode("utf-8")

    st.success("File converted successfully!")

    st.download_button(
        label="⬇️ Download CSV file",
        data=csv_data,
        file_name=uploaded_file.name.replace(".xls", ".csv").replace(".xlsx", ".csv"),
        mime="text/csv",
    )
