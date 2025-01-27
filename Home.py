import streamlit as st
import pandas as pd
import time
import streamlit.components.v1 as components  # For custom HTML embedding

st.markdown(
    """
    <style>
    .main {
        background: linear-gradient(135deg, #FFDEE9 0%, #B5FFFC 100%);
        padding: 10px;
        border-radius: 10px;
        margin: auto;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar navigation
st.sidebar.title("📂 Navigation")
options = ["🏠 Home", "📊 Data", "🚧 Coming Soon"]
choice = st.sidebar.radio("Go to:", options)

if choice == "🏠 Home":
    st.title("📊 Advanced Dataset Cleaner")

    # Home Lottie Animation
    home_html = """
    <script src="https://unpkg.com/@dotlottie/player-component@2.7.12/dist/dotlottie-player.mjs" type="module"></script>
    <dotlottie-player 
        src="https://lottie.host/3c69ca49-bcd9-4ed3-8500-4b6aebd1893b/NchDQmEK2l.lottie" 
        background="transparent" 
        speed="1" 
        style="width: 300px; height: 300px" 
        loop 
        autoplay>
    </dotlottie-player>
    """
    components.html(home_html, height=350)

    # Welcome message
    st.write("""
    Welcome to the **Advanced Dataset Cleaner**! This app allows you to:
    - Upload your dataset in CSV format.
    - Clean the dataset by handling missing values, duplicates, and special characters.
    - Standardize spaces and hyphens.
    - Visualize the progress and download cleaned results.

    **Let's make your data cleaner and better! 🚀**
    """)

elif choice == "📊 Data":
    st.title("📊 Clean and Analyze Your Dataset")

    # Data Lottie Animation
    data_html = """
    <script src="https://unpkg.com/@dotlottie/player-component@2.7.12/dist/dotlottie-player.mjs" type="module"></script>
    <dotlottie-player 
        src="https://lottie.host/df67ee5f-a9b6-48b3-9bc5-6d35a68bdd09/giCnu4SoMb.lottie" 
        background="transparent" 
        speed="1" 
        style="width: 300px; height: 300px" 
        loop 
        autoplay>
    </dotlottie-player>
    """
    components.html(data_html, height=350)

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

elif choice == "🚧 Coming Soon":
    st.title("🚧 Coming Soon")

    # Coming Soon Lottie Animation
    coming_soon_html = """
    <script src="https://unpkg.com/@dotlottie/player-component@2.7.12/dist/dotlottie-player.mjs" type="module"></script>
    <dotlottie-player 
        src="https://lottie.host/e1741d97-a60c-4df6-b30f-0c26dbbc6a64/9fNaqT8Bfc.lottie" 
        background="transparent" 
        speed="1" 
        style="width: 300px; height: 300px" 
        loop 
        autoplay>
    </dotlottie-player>
    """
    components.html(coming_soon_html, height=350)

    # Placeholder for future features
    st.write("""
    We're working hard to bring you new features, including:
    - Advanced data visualization tools.
    - Automated exploratory data analysis (EDA).
    - Predictive modeling options.

    **Stay tuned! 🔔**
    """)

# Footer
st.write("---")
st.write("💻 **Developed with DataCure** | 🚀 Optimized for user-friendly cleaning and analysis.")
