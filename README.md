# 🚀 Mini VPS - Web Terminal for Python

A lightweight web-based terminal that allows users to run Python code directly from the browser.
Designed for beginners to practice basic programming in a simple and interactive environment.

---

## ✨ Features

* Run Python code in browser
* Terminal-like interface
* Instant output display
* Beginner-friendly (print, variables, base64, etc.)
* Lightweight and easy to deploy

---

## 🧠 How It Works

```text
User (Browser)
     ↓
Send code to server
     ↓
Server executes Python (sandbox)
     ↓
Return output
```

---

## 📦 Project Structure

```bash
mini-vps/
├── server/
│   ├── main.js          # Express server
│   ├── runner.js        # Execute Python code
│
├── client/
│   ├── index.html       # UI
│   ├── app.js
│   └── style.css
│
├── sandbox/
│   └── temp.py          # Temporary Python file
│
├── package.json
└── README.md
```

---

## ▶️ Getting Started

### 1. Clone repository

```bash
git clone https://github.com/yourusername/mini-vps.git
cd mini-vps
```

### 2. Install dependencies

```bash
npm install
```

### 3. Run server

```bash
node server/main.js
```

### 4. Open browser

```
http://localhost:3000
```

---

## 🧪 Example Code

### Python

```python
print("Hello World")

ten = "An"
print(ten)
```

### Base64 Example

```python
import base64

text = "hello"
encoded = base64.b64encode(text.encode())
print(encoded)
```

---

## ⚠️ Notes

* This project is for learning purposes only
* Not secure for production use
* Avoid running untrusted code in public environments

---

## 🔮 Future Improvements

* Add real terminal commands (ls, cd, etc.)
* Docker sandbox for better isolation
* Multi-user support
* Authentication system
* UI improvements

---

## 🧑‍💻 Tech Stack

* Node.js (Express)
* Python
* HTML / CSS / JavaScript

---

## 📄 License

MIT License

