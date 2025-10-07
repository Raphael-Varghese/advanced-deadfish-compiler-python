# 🐟 Deadfish++ Compiler

Deadfish++ is an advanced interpreter for the esoteric programming language **Deadfish**, extended with new instructions, debugging tools, and loop support. This project is designed for educational and experimental use.

---

## 🚀 Features

- ✅ Supports standard Deadfish instructions: `i`, `d`, `s`, `o`
- ✨ Extended commands:
  - `*` → Output ASCII character  
  - `\` → Clear accumulator  
  - `b` → Double accumulator  
  - `!` → Negate accumulator  
  - `m` → Modulo 10  
  - `r` → Randomize (0–255)  
  - `:` → Newline  
  - `[` `]` → Loop (repeat enclosed instructions N times)
- 🐞 Debug mode with step-by-step tracing
- 📂 File-based execution
- 🔒 Overflow protection (resets at 256 or -1)

---

## 📦 Installation

1. Make sure you have **Python 3.6+** installed.
2. Clone this repository by running:  
   `git clone https://github.com/Raphael-Varghese/advanced-deadfish-compiler-pythondeadfish-compiler.git && cd deadfish-compiler`
3. Run the compiler:  
   `python advanced_deadfish.py <your_program.dfish> [--debug]`

---

## 🧠 Language Reference

| Command | Description                     |
|---------|---------------------------------|
| `i`     | Increment accumulator           |
| `d`     | Decrement accumulator           |
| `s`     | Square accumulator              |
| `o`     | Output numeric value            |
| `*`     | Output ASCII character          |
| `\`     | Clear accumulator               |
| `b`     | Double accumulator              |
| `!`     | Negate accumulator              |
| `m`     | Modulo 10                       |
| `r`     | Randomize (0–255)               |
| `:`     | Print newline                   |
| `[` `]` | Loop N times (N = accumulator)  |

---

## 🧪 Example Program

Example Deadfish++ code:  
`iiiiib*:[io]`

- Sets accumulator to 10  
- Prints newline  
- Loops: prints numbers 0–9

---

## 📄 License

This project is licensed under the Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License.

You may use this software for personal and educational purposes only. Redistribution, modification, or commercial use is prohibited without written permission.

To view a copy of this license, visit [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/)
