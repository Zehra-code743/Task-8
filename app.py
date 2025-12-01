import streamlit as st
from calculator import calculate
from utils import validate_numeric_input

# Page configuration
st.set_page_config(page_title="🧮 Simple Calculator", page_icon="🧮", layout="centered")

# Custom CSS for styling
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(to right, #f5f7fa, #c3cfe2);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        padding: 10px 20px;
        border-radius: 8px;
        border: none;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #45a049;
        cursor: pointer;
    }
    .stTextInput>div>div>input {
        border-radius: 8px;
        padding: 8px;
        border: 1px solid #ccc;
        font-size: 16px;
    }
    .stSelectbox>div>div>div>select {
        border-radius: 8px;
        padding: 8px;
        font-size: 16px;
    }
</style>
""", unsafe_allow_html=True)

# Title with emoji
st.markdown("## 🧮 Simple Calculator")

# Layout with two columns for input
col1, col2 = st.columns(2)
with col1:
    num1_input = st.text_input("Enter first number", value="0.0")
with col2:
    num2_input = st.text_input("Enter second number", value="0.0")

# Operation selector
operation = st.selectbox("Select operation", ("add", "subtract", "multiply", "divide"))

# Calculate button with spacing
st.markdown("<br>", unsafe_allow_html=True)
if st.button("Calculate"):
    result = None
    error_message = None
    try:
        num1 = validate_numeric_input(num1_input, "first number")
        num2 = validate_numeric_input(num2_input, "second number")
        result = calculate(num1, num2, operation)
    except ValueError as e:
        error_message = str(e)
    except Exception as e:
        error_message = f"An unexpected error occurred: {e}"

    if error_message:
        st.error(f"❌ {error_message}")
    elif result is not None:
        st.success(f"✅ Result: {result}")

# Footer
st.markdown("<br><hr><center>Made with ❤️ using SHAN-E-ZEHRA", unsafe_allow_html=True)
