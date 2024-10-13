import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import logging
import sys

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(_name_)

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
    try:
        x = np.linspace(x_range[0], x_range[1], 100)
        y = func(x)
        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.set_title(f'Graph of {func._name_}(x)')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        return fig
    except Exception as e:
        logger.error(f"Error in plot_function: {str(e)}")
        return None

# Streamlit app
def calculator():
    try:
        st.title("Enhanced Calculator with Graphs")

        # Sidebar for basic calculations
        st.sidebar.header("Basic Calculations")
        num1 = st.sidebar.number_input("Enter the first number:", value=0.0, step=1.0)
        num2 = st.sidebar.number_input("Enter the second number:", value=0.0, step=1.0)
        operation = st.sidebar.selectbox("Choose an operation", 
                                         ["Add", "Subtract", "Multiply", "Divide", "Power"])

        if st.sidebar.button("Calculate"):
            try:
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
            except Exception as e:
                logger.error(f"Error in basic calculation: {str(e)}")
                st.sidebar.error(f"An error occurred: {str(e)}")

        # Main area for advanced functions and graphing
        st.header("Advanced Functions")
        func_choice = st.selectbox("Choose a function to graph", 
                                   ["Sin", "Cos", "Tan", "Square Root", "Logarithm"])
        
        x_min = st.number_input("Enter the minimum x value:", value=-10.0, step=1.0)
        x_max = st.number_input("Enter the maximum x value:", value=10.0, step=1.0)

        if st.button("Generate Graph"):
            try:
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

                if fig:
                    st.pyplot(fig)
                else:
                    st.error("An error occurred while generating the graph.")
            except Exception as e:
                logger.error(f"Error in generating graph: {str(e)}")
                st.error(f"An error occurred while generating the graph: {str(e)}")

        # Additional calculations
        st.header("Additional Calculations")
        extra_num = st.number_input("Enter a number for additional calculations:", value=1.0, step=1.0)
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Calculate Square Root"):
                try:
                    result = square_root(extra_num)
                    st.write(f"Square root of {extra_num} is: {result}")
                except Exception as e:
                    logger.error(f"Error in square root calculation: {str(e)}")
                    st.error(f"An error occurred: {str(e)}")
        
        with col2:
            if st.button("Calculate Natural Logarithm"):
                try:
                    result = logarithm(extra_num, base=np.e)
                    st.write(f"Natural logarithm of {extra_num} is: {result}")
                except Exception as e:
                    logger.error(f"Error in logarithm calculation: {str(e)}")
                    st.error(f"An error occurred: {str(e)}")

    except Exception as e:
        logger.error(f"Unhandled exception in calculator: {str(e)}")
        st.error(f"An unexpected error occurred: {str(e)}")

# Run the calculator app
if _name_ == '_main_':
    try:
        calculator()
    except Exception as e:
        logger.error(f"Fatal error: {str(e)}")
        print(f"Fatal error: {str(e)}", file=sys.stderr)
