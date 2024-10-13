import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Basic arithmetic functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y if y != 0 else "Error: Division by zero"

# Advanced mathematical functions
def power(x, y):
    return x ** y

def square_root(x):
    return np.sqrt(x) if x >= 0 else "Error: Cannot compute square root of negative number"

def logarithm(x, base=np.e):
    return np.log(x) / np.log(base) if x > 0 else "Error: Logarithm undefined for non-positive numbers"

# Trigonometric functions
def sin(x):
    return np.sin(x)

def cos(x):
    return np.cos(x)

def tan(x):
    return np.tan(x)

# Graphing function
def plot_function(func, x_range, title):
    x = np.linspace(x_range[0], x_range[1], 200)
    y = func(x)
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title(title)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.grid(True)
    return fig

def main():
    st.title("Enhanced Calculator")

    # Sidebar for basic calculations
    st.sidebar.header("Basic Calculations")
    num1 = st.sidebar.number_input("Enter first number:", value=0.0)
    num2 = st.sidebar.number_input("Enter second number:", value=0.0)
    operation = st.sidebar.selectbox("Choose operation:", 
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
        
        st.sidebar.write(f"Result: {result}")

    # Main area for advanced functions and graphing
    st.header("Advanced Functions and Graphing")
    
    func_choice = st.selectbox("Choose a function to graph:", 
                               ["Sine", "Cosine", "Tangent", "Square Root", "Logarithm", "Custom Power"])

    x_min = st.number_input("Minimum x value:", value=-10.0)
    x_max = st.number_input("Maximum x value:", value=10.0)

    if st.button("Generate Graph"):
        if func_choice == "Sine":
            fig = plot_function(sin, [x_min, x_max], "Sine Function")
        elif func_choice == "Cosine":
            fig = plot_function(cos, [x_min, x_max], "Cosine Function")
        elif func_choice == "Tangent":
            fig = plot_function(tan, [x_min, x_max], "Tangent Function")
        elif func_choice == "Square Root":
            fig = plot_function(square_root, [0, x_max], "Square Root Function")
        elif func_choice == "Logarithm":
            fig = plot_function(lambda x: logarithm(x, np.e), [0.1, x_max], "Natural Logarithm Function")
        elif func_choice == "Custom Power":
            power_val = st.number_input("Enter power value:", value=2.0)
            fig = plot_function(lambda x: power(x, power_val), [x_min, x_max], f"Power Function (x^{power_val})")

        st.pyplot(fig)

    # Additional calculations
    st.header("Additional Calculations")
    extra_num = st.number_input("Enter a number:", value=1.0)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Calculate Square Root"):
            result = square_root(extra_num)
            st.write(f"Square root of {extra_num} is: {result}")
    
    with col2:
        if st.button("Calculate Natural Logarithm"):
            result = logarithm(extra_num)
            st.write(f"Natural logarithm of {extra_num} is: {result}")

if __name__ == "__main__":
    main()
