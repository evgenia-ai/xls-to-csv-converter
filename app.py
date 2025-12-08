import streamlit as st
import pandas as pd
import io

st.set_page_config(page_title="XLS/TXT → CSV Converter", page_icon="📄")

st.title("📄 XLS / TXT → CSV Converter (Semicolon Separated)")

uploaded_file = st.file_uploader("Upload XLS, XLSX, or TXT file", type=["xls", "xlsx", "txt"])

if uploaded_file:
    file_name = uploaded_file.name.lower()

    # ---- READ EXCEL FILE ----
    if file_name.endswith((".xls", ".xlsx")):
        df = pd.read_excel(uploaded_file)

    # ---- READ TXT FILE ----
    elif file_name.endswith(".txt"):
        # Try to detect common separators
        content = uploaded_file.read().decode("utf-8")

        if "\t" in content:
            sep = "\t"       # tab-separated
        elif ";" in content:
            sep = ";"        # semicolon-separated
        elif "," in content:
            sep = ","        # comma-separated
        else:
            sep = " "        # fallback: space-separated

        uploaded_file.seek(0)  # reset file pointer
        df = pd.read_csv(uploaded_file, sep=sep)

    # ---- CONVERT TO CSV WITH SEMICOLON ----
    csv_data = df.to_csv(index=False, sep=";").encode("utf-8")

    st.success("File converted successfully!")

    st.download_button(
        label="⬇️ Download CSV file",
        data=csv_data,
        file_name=file_name.replace(".xls", ".csv")
                           .replace(".xlsx", ".csv")
                           .replace(".txt", ".csv"),
        mime="text/csv",
    )

