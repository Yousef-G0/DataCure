import streamlit as st
import pandas as pd

# Streamlit app title
st.title("Dataset Cleaner")

# Instructions
st.write("""
Upload your CSV file, and this app will clean the dataset by:
- Replacing missing values.
- Converting columns to appropriate types.
- Removing special characters.
- Replacing hyphens with 0.
- Removing duplicate rows.
You can download the cleaned dataset afterward.
""")

# File uploader
uploaded_file = st.file_uploader("Upload your dataset (CSV)", type=["csv"])

if uploaded_file is not None:
    try:
        # Read the uploaded CSV file
        dataset = pd.read_csv(uploaded_file)
        st.write("### Initial Dataset Preview:")
        st.dataframe(dataset.head())

        # Preprocessing steps
        dataset = dataset.fillna(0)  # Replace missing values with 0
        
        # Convert columns with mixed types to strings
        for col in dataset.columns:
            if not pd.api.types.is_numeric_dtype(dataset[col]):
                dataset[col] = dataset[col].astype(str)
        
        # Remove special characters (+, *, -) and trim whitespace
        for col in dataset.columns:
            if pd.api.types.is_string_dtype(dataset[col]):
                dataset[col] = dataset[col].str.replace(r"[+*-]", " ", regex=True).str.strip()
        
        # Replace hyphens and spaces with 0
        dataset = dataset.replace("-", 0)
        dataset = dataset.replace(" ", 0)

        # Remove duplicate rows
        dataset = dataset.drop_duplicates()

        # Display cleaned dataset preview
        st.write("### Cleaned Dataset Preview:")
        st.dataframe(dataset.head())
        
        # Summary of missing values after processing
        st.write("### Missing Values After Preprocessing:")
        st.write(dataset.isnull().sum())

        # Download cleaned dataset
        csv = dataset.to_csv(index=False)
        st.download_button(
            label="Download Cleaned Dataset",
            data=csv,
            file_name="cleaned_dataset.csv",
            mime="text/csv",
        )
        st.success("Preprocessing complete. Download your cleaned dataset!")
    except Exception as e:
        st.error(f"Error processing the dataset: {e}")
else:
    st.info("Please upload a CSV file to get started.")
