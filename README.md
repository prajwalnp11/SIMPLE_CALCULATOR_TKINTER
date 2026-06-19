Mini-Project Report: Simple GUI Calculator
1. Project Title
Simple GUI Calculator using Tkinter
2. Project Objective
To design and develop a functional desktop calculator application using Python's standard GUI library. The primary goal of this project is to implement a grid-based layout structure (mimicking a physical calculator) and securely evaluate mathematical expressions entered by the user.
3. Technologies Used
Language: Python 3
GUI Framework: tkinter (Python's standard UI library)
4. Key Features
Grid Layout Management: Unlike simpler top-to-bottom applications, this project utilizes Tkinter's .grid() method to arrange the number pad and operators into a precise 4-column matrix.
Dynamic Expression Building: As the user clicks buttons, the application concatenates the input into a single mathematical string displayed on the screen.
Robust Error Handling: The application includes a try-except block to gracefully handle mathematical impossibilities. If a user attempts to divide by zero or input an invalid sequence, it displays "Div by Zero Error" or "Error" instead of crashing the program.
Clear Function: A dedicated 'C' button allows users to instantly clear the display and start a new calculation.
5. Implementation Details
Data Structures: A list of tuples ('text', row, column) is used to store the properties of all 16 buttons. This allows the application to generate the entire UI iteratively using a for loop, keeping the code clean and DRY (Don't Repeat Yourself).
Functions:
button_click(item): Fetches the current text on the display, appends the newly clicked item, and updates the screen.
button_clear(): Deletes the contents of the Entry widget from index 0 to the end.
button_equal(): Retrieves the string from the display and evaluates it using Python's built-in eval() function, then replaces the display text with the computed result.
6. Challenges Faced & Resolved
The "Late Binding" Loop Issue: When creating buttons in a loop, assigning a command like command=lambda: button_click(text) results in every button printing the last item in the loop (in this case, +).
Solution: Used default arguments in the lambda function (command=lambda t=text: button_click(t)). This captures the value of text at the exact moment the button is created, ensuring each button inputs the correct number or operator.
7. Future Enhancements
Keyboard Binding: Modifying the code to listen for physical keystrokes, allowing users to type on their keyboard instead of clicking the on-screen buttons.
Scientific Features: Adding a toggle to expand the window and reveal advanced functions like square roots, exponents, and trigonometric functions (sin, cos, tan).
Calculation History: Implementing a side-panel or secondary window that keeps a running log of past calculations during the session.
