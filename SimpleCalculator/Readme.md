# 🧮 Simple Calculator

A beginner-friendly command-line calculator written in Python. It performs basic arithmetic operations, validates user input, and gracefully handles errors like division by zero.


---

## ✨ Features

- Perform **addition, subtraction, multiplication, and division**
- Clean, guided prompts for user input
- Input validation — rejects non-numeric values instead of crashing
- Handles **division by zero** using `try/except`
- Loop support — perform multiple calculations in one session
- Quit anytime by typing `q`
- Well-commented, beginner-readable code

---

## 🧰 Technologies Used

- **Language:** Python 3
- **Standard Library modules:** `built-in input()/print()` (no external dependencies)
- **Tools:** Git & GitHub for version control

---

## 📸 Demo

```
=== Simple Calculator ===
Type 'q' at any time during number entry to quit.

Enter first number (or 'q' to quit): 10
Choose an operation (+, -, *, /): +
Enter second number: 5
Result: 10.0 + 5.0 = 15.0

Perform another calculation? (y/n): y
Enter first number (or 'q' to quit): 20
Choose an operation (+, -, *, /): /
Enter second number: 0
Error: Division by zero is not allowed.

Perform another calculation? (y/n): n
Thank you for using the Simple Calculator. Goodbye!
```

---

## 🛠 Requirements

- Python 3.6 or higher (no external libraries needed)

---

## 🚀 How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/<your-username>/<your-repo-name>.git
   cd <your-repo-name>
   ```

2. Run the script:
   ```bash
   python3 calculator.py
   ```
   *(On Windows, you can use `python calculator.py`)*

---

## 🔗 GitHub Repository Link

[https://github.com/harshikadarda/CodeOrbit-Intenship](https://github.com/harshikadarda/CodeOrbit-Intenship)

*(Replace `<your-username>` and `<your-repo-name>` with your actual GitHub username and repository name once pushed.)*

---

## 📂 Project Structure

```
.
├── calculator.py   # Main calculator script
└── README.md        # Project documentation
```

---

## 🧩 How It Works

| Function        | Purpose                                             |
|------------------|------------------------------------------------------|
| `add()`          | Returns the sum of two numbers                      |
| `subtract()`     | Returns the difference of two numbers                |
| `multiply()`     | Returns the product of two numbers                   |
| `divide()`       | Returns the quotient of two numbers                   |
| `get_number()`   | Prompts the user until a valid number is entered     |
| `get_operation()`| Prompts the user until a valid operator is entered    |
| `calculate()`    | Runs the correct operation and handles divide-by-zero |
| `main()`         | Runs the overall program loop                        |

---

## 🔮 Possible Improvements

- Add support for more operations (exponents, modulus, square root)
- Add a GUI version using Tkinter or a web frontend
- Add unit tests using `unittest` or `pytest`

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙋 Author

Built as part of a daily Python practice challenge — one task, one day.
