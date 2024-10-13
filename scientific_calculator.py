import streamlit as st
import plotly.graph_objs as go
import numpy as np

# Basic arithmetic functions
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

# Advanced mathematical functions
def power(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return "Error! Cannot calculate square root of a negative number."
    return x ** 0.5

def logarithm(x, base=10):
    if x <= 0:
        return "Error! Logarithm is undefined for non-positive numbers."
    return np.log(x) / np.log(base)

# Trigonometric functions
def sin(x):
    return np.sin(x)

def cos(x):
    return np.cos(x)

def tan(x):
    return np.tan(x)

# Graphing function
def plot_function(func, x_range):
    x = np.linspace(x_range[0], x_range[1], 100)
    y = func(x)
    fig = go.Figure(data=go.Scatter(x=x, y=y, mode='lines'))
    fig.update_layout(title=f'Graph of {func._name_}(x)', xaxis_title='x', yaxis_title='y')
    return fig

# Streamlit app
def calculator():
    st.title("Enhanced Calculator with Graphs")

    # Sidebar for basic calculations
    st.sidebar.header("Basic Calculations")
    num1 = st.sidebar.number_input("Enter the first number:", value=0.0, step=1.0)
    num2 = st.sidebar.number_input("Enter the second number:", value=0.0, step=1.0)
    operation = st.sidebar.selectbox("Choose an operation", 
                                     ["Add", "Subtract", "Multiply", "Divide", "Power"])

    if st.sidebar.button("Calculate"):
        if operation == "Add":
            result = add(num1, num2)
        elif operation == "Subtract":
            result = subtract(num1, num2)
        elif operation == "Multiply":
            result = multiply(num1, num2)
        elif operation == "Divide":
            result = divide(num1, num2)
        elif operation == "Power":
            result = power(num1, num2)
        
        st.sidebar.success(f"The result is: {result}")

    # Main area for advanced functions and graphing
    st.header("Advanced Functions")
    func_choice = st.selectbox("Choose a function to graph", 
                               ["Sin", "Cos", "Tan", "Square Root", "Logarithm"])
    
    x_min = st.number_input("Enter the minimum x value:", value=-10.0, step=1.0)
    x_max = st.number_input("Enter the maximum x value:", value=10.0, step=1.0)

    if st.button("Generate Graph"):
        if func_choice == "Sin":
            fig = plot_function(sin, [x_min, x_max])
        elif func_choice == "Cos":
            fig = plot_function(cos, [x_min, x_max])
        elif func_choice == "Tan":
            fig = plot_function(tan, [x_min, x_max])
        elif func_choice == "Square Root":
            fig = plot_function(square_root, [0, x_max])  # Adjust range for square root
        elif func_choice == "Logarithm":
            fig = plot_function(logarithm, [0.1, x_max])  # Adjust range for logarithm

        st.plotly_chart(fig)

    # Additional calculations
    st.header("Additional Calculations")
    extra_num = st.number_input("Enter a number for additional calculations:", value=1.0, step=1.0)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Calculate Square Root"):
            result = square_root(extra_num)
            st.write(f"Square root of {extra_num} is: {result}")
    
    with col2:
        if st.button("Calculate Natural Logarithm"):
            result = logarithm(extra_num, base=np.e)
            st.write(f"Natural logarithm of {extra_num} is: {result}")

# Run the calculator app
if _name_ == '_main_':
    calculator()
