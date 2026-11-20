import streamlit as st
from calculator import calculate

st.set_page_config(
    page_title="Simple Calculator",
    page_icon="🧮",
    layout="centered"
)

st.title("🧮 Simple Calculator")
st.write("Perform basic mathematical operations.")

num1 = st.number_input("Enter First Number", value=0.0)
num2 = st.number_input("Enter Second Number", value=0.0)

operation = st.selectbox(
    "Select Operation",
    [
        "Addition (+)",
        "Subtraction (-)",
        "Multiplication (*)",
        "Division (/)",
        "Modulus (%)"
    ]
)

if st.button("Calculate", type="primary"):

    try:
        result = calculate(num1, num2, operation)
        st.success(f"Result: {result}")

    except ValueError as error:
        st.error(str(error))

st.divider()
st.caption("Developed using Python and Streamlit")
