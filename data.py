import streamlit as st
import pandas as pd
import time

# Streamlit app title
st.title("📊 Advanced Dataset Cleaner")

# Instructions
st.write("""
Welcome to the **Advanced Dataset Cleaner**! This app allows you to:
1. Upload your dataset in CSV format.
2. Clean the dataset by:
   - Replacing missing values.
   - Removing duplicates.
   - Replacing special characters.
   - Standardizing hyphens and spaces.
3. Visualize the cleaning progress and the results.
4. Download the cleaned dataset.

**Let's get started! 🚀**
""")

# File uploader
uploaded_file = st.file_uploader("Upload your dataset (CSV)", type=["csv"])

if uploaded_file is not None:
    try:
        # Read the uploaded CSV file
        dataset = pd.read_csv(uploaded_file)
        st.write("### Initial Dataset Preview")
        st.dataframe(dataset.head())
        
        # Visualize missing values before cleaning
        st.write("### Missing Values Per Column (Before Cleaning)")
        missing_values_before = dataset.isnull().sum()
        st.bar_chart(missing_values_before)

        # Initialize progress bar
        progress = st.progress(0)
        
        # Start cleaning process
        st.write("### Cleaning in Progress...")
        
        # Step 1: Replace missing values
        time.sleep(1)  # Simulate time taken
        dataset = dataset.fillna(0)
        progress.progress(33)
        
        # Step 2: Convert columns with mixed types to string
        for col in dataset.columns:
            if not pd.api.types.is_numeric_dtype(dataset[col]):
                dataset[col] = dataset[col].astype(str)
        time.sleep(1)  # Simulate time taken
        progress.progress(66)
        
        # Step 3: Remove special characters and standardize spaces
        for col in dataset.columns:
            if pd.api.types.is_string_dtype(dataset[col]):
                dataset[col] = dataset[col].str.replace(r"[+*-]", " ", regex=True).str.strip()
        dataset = dataset.replace("-", 0)
        dataset = dataset.replace(" ", 0)

        # Step 4: Remove duplicate rows
        dataset = dataset.drop_duplicates()
        progress.progress(100)

        st.success("🎉 Cleaning Complete!")

        # Visualize missing values after cleaning
        st.write("### Missing Values Per Column (After Cleaning)")
        missing_values_after = dataset.isnull().sum()
        st.bar_chart(missing_values_after)
        
        # Display cleaned dataset
        st.write("### Cleaned Dataset Preview")
        st.dataframe(dataset.head())
        
        # Allow users to download cleaned dataset
        csv = dataset.to_csv(index=False)
        st.download_button(
            label="📥 Download Cleaned Dataset",
            data=csv,
            file_name="cleaned_dataset.csv",
            mime="text/csv",
        )
    except Exception as e:
        st.error(f"Error processing the dataset: {e}")
else:
    st.info("Please upload a CSV file to get started.")

# Footer
st.write("---")
st.write("💻 **Developed with Streamlit** | 🚀 Optimized for user-friendly cleaning.")
