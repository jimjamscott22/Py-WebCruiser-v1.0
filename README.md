# Py-WebCruiser-v1.0
A simple, web browser w/Python, designed as a foundational learning project to explore GUI application development and the integration of third-party rendering engines.

## 🎯 Project Overview
This project is a lightweight, fully functional web browser. Rather than building a DOM parser and JavaScript engine from scratch, Py-WebCruiser leverages a Chromium-based wrapper to render modern web content. The primary focus of this project is understanding how to structure an application shell, manage an event loop, and handle user interactions through the Observer pattern.

## 🧠 Core Concepts Explored
Building this browser provided hands-on experience with several fundamental software engineering concepts:
* **Event-Driven Programming:** Managing the infinite application loop (`QApplication`) that waits for and processes user inputs without blocking the main execution thread.
* **The Observer Pattern (Signals & Slots):** Wiring UI elements (buttons, text fields) to backend functions. For example, connecting the "Enter" key press in the address bar to the engine's navigation method.
* **Component Integration:** Embedding a heavy, complex third-party widget (`QWebEngineView`) into a custom `QMainWindow` container and bridging the communication between the two.
* **State Synchronization:** Ensuring the application's UI (like the URL bar) accurately reflects the internal state of the rendering engine as the user navigates through links.

## 🛠️ Technology Stack
* **Language:** Python 3.x
* **GUI Framework:** PyQt6 (Python bindings for the Qt C++ framework)
* **Rendering Engine:** PyQt6-WebEngine (Chromium wrapper)

## 🚀 Installation & Setup
To run this project locally, you will need Python installed on your machine.

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/Py-WebCruiser-v1.0.git
   cd Py-WebCruiser-v1.0
   ```
2. **Install `uv`:**
   ```bash
   pip install uv
   ```
3. **Create the project environment and install dependencies:**
   ```bash
   uv sync
   ```
4. **Launch the browser:**
   ```bash
   uv run py-webcruiser
   ```

If you add new packages later, use:

```bash
uv add <package-name>
```

To run the test suite:

```bash
uv run pytest
```

## 🗺️ Roadmap for Future Learning
This project serves as a foundation. Future iterations to deepen understanding of data structures and application state management include:
* **Custom History Stack:** Implementing a Stack data structure to handle "Back" and "Forward" navigation manually.
* **Tabbed Browsing:** Managing multiple instances of the rendering engine using a List or Array-based data structure and dynamically swapping them in the UI.
* **Bookmark Management:** Using JSON or SQLite to persist user data (bookmarks) across sessions.
