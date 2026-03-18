<p align="center">
  <img src="banner.png" alt="Jarvis Python Voice Assistant Banner" width="100%">
</p>

# 🎙️ Jarvis - Python Voice Assistant

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Windows-green)
![Made With Python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)

A **Python-based Voice Assistant inspired by Iron Man's J.A.R.V.I.S** that performs tasks using voice commands such as searching Wikipedia, opening applications, playing music, and reading news headlines.

This project demonstrates **Speech Recognition, Text-to-Speech, Web Automation, and Python scripting** to create a simple but powerful desktop voice assistant.

---

# 🚀 Features

### 🎤 Voice Interaction

* Voice command recognition
* Natural text-to-speech responses

### 🌐 Web Automation

Open websites using voice commands:

* YouTube
* Google
* StackOverflow
* WhatsApp Web
* CGTrader
* TurboSquid

### 💻 System Automation

Control applications with voice:

* Notepad
* Command Prompt
* Visual Studio Code
* Discord
* Window switching

### 🎵 Entertainment

* Play random music from your computer
* Fetch latest news headlines

### 🧠 Knowledge Assistant

* Wikipedia search
* WikiHow "How To" mode

---

# 📰 News Module

The project includes a separate module **`NewsRead.py`** which fetches and reads the latest news headlines.

This module uses **NewsAPI** to retrieve real-time news updates and converts them into speech using `pyttsx3`.

### Supported Categories

* Technology
* Politics
* Sports
* Cricket

Example commands:

* "News"
* "Tech news"
* "Sports news"
* "Cricket news"

---

# 🛠 Tech Stack

### Language

* Python 3

### Libraries

* `pyttsx3` – Text-to-Speech engine
* `SpeechRecognition` – Voice recognition
* `wikipedia`
* `pyautogui`
* `GoogleNews`
* `pywikihow`
* `webbrowser`
* `datetime`
* `random`
* `os`
* `sys`

---

# 📦 Installation

Clone the repository

```bash
git clone https://github.com/your-username/jarvis-python-voice-assistant.git
cd jarvis-python-voice-assistant
```

---

# 🔑 NewsAPI Setup (Required for News Feature)

The news feature requires a **NewsAPI key**.

### Step 1 — Create an Account

Visit:

https://newsapi.org

Sign up for a free account.

### Step 2 — Get Your API Key

After signing in, you will find your **API key** in the dashboard.

Example:

```
123abc456def789
```

### Step 3 — Add the API Key

Open:

```
NewsRead.py
```

Replace the placeholder with your key:

```python
api_key = "YOUR_API_KEY"
```

---

# ▶ Running the Project

Start the assistant by running:

```bash
python jarvis.py
```

Jarvis will greet you and start listening for commands.

### Example Commands

* "Open YouTube"
* "Search Wikipedia for Artificial Intelligence"
* "Play music"
* "Open Google"
* "What is the time"
* "Activate how to do mode"
* "Open Notepad"
* "News"
* "Quit"

---

# 📂 Project Structure

```
jarvis-python-voice-assistant
│
├── banner.png
├── jarvis.py
├── NewsRead.py
├── requirements.txt
└── README.md
```

---

# 🧠 How It Works

1. The program listens to the microphone using **SpeechRecognition**.
2. The voice is converted to text using the **Google Speech API**.
3. Jarvis analyzes the command and selects the correct function.
4. The response is spoken using **pyttsx3 text-to-speech engine**.
5. Some commands trigger web automation, system applications, or the news module.

---

# ⚠️ Notes

* Works best on **Windows** because it uses the **SAPI5 speech engine**.
* Some application paths (music folder, programs) may need modification.
* Requires a **working microphone**.

---

# 👨‍💻 Author

**Debayan Ghosh**

Interests:

* Artificial Intelligence
* Automation
* Game Development
* Game Environment Design

GitHub: https://github.com/Debayan-G

---

# ⭐ Support

If You Found This Project Useful, Please Consider **Starring The Repository ⭐**.
