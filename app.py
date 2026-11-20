
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Simple Calculator",
    page_icon="🧮",
    layout="centered"
)

# App heading
st.title("🧮 Simple Calculator")
st.write("Perform basic mathematical operations.")

# Input numbers
num1 = st.number_input(
    "Enter First Number",
    value=0.0
)

num2 = st.number_input(
    "Enter Second Number",
    value=0.0
)

# Select operation
operation = st.selectbox(
    "Select Operation",
    ["Addition (+)", "Subtraction (-)",
     "Multiplication (*)", "Division (/)", "Modulus (%)"]
)

# Calculate button
if st.button("Calculate", type="primary"):

    if operation == "Addition (+)":
        result = num1 + num2

    elif operation == "Subtraction (-)":
        result = num1 - num2

    elif operation == "Multiplication (*)":
        result = num1 * num2

    elif operation == "Division (/)":
        if num2 == 0:
            st.error("Cannot divide by zero!")
            result = None
        else:
            result = num1 / num2

    elif operation == "Modulus (%)":
        if num2 == 0:
            st.error("Cannot calculate modulus by zero!")
            result = None
        else:
            result = num1 % num2

    # Display result
    if result is not None:
        st.success(f"Result: {result}")

# Footer
st.divider()
st.caption("Developed using Python and Streamlit")
