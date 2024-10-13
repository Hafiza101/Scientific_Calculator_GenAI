# Scientific_Calculator_GenAI

# Simple Calculator App using Streamlit

This is a simple calculator application built using the **Streamlit** framework. The app allows users to perform basic arithmetic operations: addition, subtraction, multiplication, and division.

## Features

- Addition of two numbers
- Subtraction of two numbers
- Multiplication of two numbers
- Division of two numbers (with division by zero handling)

## Installation

To run this application, you need to have Python and Streamlit installed.

1. **Clone this repository or download the `calculator.py` file**.
2. Open your terminal and navigate to the project directory.
3. Install the required dependency (**Streamlit**) by running the following command:

    ```bash
    pip install streamlit
    ```

## How to Run

1. After installing the required dependencies, run the Streamlit app with the following command:

    ```bash
    streamlit run calculator.py
    ```

2. This will start a local web server, and you'll see an output like this:

    ```bash
    Local URL: http://localhost:8501
    Network URL: http://<your-network-ip>:8501
    ```

3. Open your browser and navigate to `http://localhost:8501`. You will now be able to use the calculator app.

## Usage

1. Enter the first number in the **"Enter the first number"** field.
2. Enter the second number in the **"Enter the second number"** field.
3. Select the operation (Add, Subtract, Multiply, or Divide) from the dropdown.
4. Click the **Calculate** button.
5. The result will be displayed below the button.

## Error Handling

- The app prevents division by zero by showing an error message when attempting to divide by zero.

## Technologies Used

- **Python**
- **Streamlit**

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to submit issues or pull requests if you'd like to contribute.

