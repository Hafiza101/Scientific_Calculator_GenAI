pip install streamlit
# Save the calculator code to a Python file
with open("calculator.py", "w") as f:
    f.write('''
import streamlit as st

# Define the functions for the calculator
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# Streamlit app
def calculator():
    st.title("Simple Calculator")

    # User inputs for the two numbers
    num1 = st.number_input("Enter the first number:", value=0.0, step=1.0)
    num2 = st.number_input("Enter the second number:", value=0.0, step=1.0)

    # Dropdown menu to select the operation
    operation = st.selectbox("Choose an operation", ["Add", "Subtract", "Multiply", "Divide"])

    # Calculate and display the result
    if st.button("Calculate"):
        if operation == "Add":
            result = add(num1, num2)
        elif operation == "Subtract":
            result = subtract(num1, num2)
        elif operation == "Multiply":
            result = multiply(num1, num2)
        elif operation == "Divide":
            result = divide(num1, num2)
        
        st.success(f"The result is: {result}")

# Run the calculator app
if __name__ == '__main__':
    calculator()
    ''')
streamlit run calculator.py
!pip install pyngrok
# Install streamlit and ngrok
!pip install streamlit
!pip install pyngrok

# Run streamlit app with ngrok
from pyngrok import ngrok

# Start ngrok
public_url = ngrok.connect(port='8501')
print(f"Streamlit is accessible at {public_url}")

# Run streamlit in the background
!streamlit run calculator.py &>/dev/null&
pip install streamlit
streamlit run calculator.py
