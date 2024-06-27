# modules_and_testing

## Modules and Testing Lab

This lab demonstrates the use of modules and testing in Python by implementing factorial calculations using both iterative and recursive methods, as well as a clumsy factorial function.

## Project Structure

The project is organized as follows:

## Implementation

1. **Factorial Module:**
    - Created a `factorial_module.py` file inside the `factorial_module` directory.
    - Implemented the following functions:
        - `factorial_iterative(n)`: Calculates the factorial of a positive integer `n` using an iterative approach.
        - `factorial_recursion(n)`: Calculates the factorial of a positive integer `n` using recursion.
        - `clumsy(n)`: Calculates the clumsy factorial of a positive integer `n`, following a specific sequence of arithmetic operations.

2. **Testing:**
    - Created a `test_factorial.py` file inside the `test` directory.
    - Added test cases for `factorial_iterative`, `factorial_recursion`, and `clumsy` functions to ensure they work correctly for various inputs, including edge cases.
    - Included a helper function `assert_raises_value_error` to test for exceptions when invalid inputs are provided.

3. **Dependencies:**
    - Created a `requirements.txt` file listing the required packages for the project. For this lab, it includes:
      ```txt
      pytest
      ```

4. **Version Control:**
    - Initialized a local git repository and created a remote repository on GitHub.
    - Linked the local and remote repositories and set up the project structure.
    - Created and worked on a separate branch called `factorial`.
    - After completing the implementation and testing, created a pull request from the `factorial` branch to the `main` branch and merged the code.

## Running the Tests

To run the tests, ensure you have `pytest` installed. If not, install it using the following command:

```bash
pip install -r requirements.txt


