# 🎙️ Jarvis - Python Voice Assistant

A **Python-based Voice Assistant** inspired by Iron Man's J.A.R.V.I.S that can perform various tasks using voice commands such as searching Wikipedia, opening applications, playing music, reading news headlines, and more.

This project demonstrates the use of **Speech Recognition, Text-to-Speech, Web Automation, and Python scripting** to build a simple but powerful personal assistant.

---

## 🚀 Features

* 🎤 Voice command recognition

* 🔊 Text-to-speech responses

* 🌐 Search information from **Wikipedia**

* 📺 Open websites like:

  * YouTube
  * Google
  * StackOverflow
  * WhatsApp Web
  * CGTrader
  * TurboSquid

* 🎵 Play random music from your system

* 📰 Read latest news headlines

* 🧠 "How To Do" mode using WikiHow

* ⌚ Tell the current time

* 💻 Open system applications:

  * Notepad
  * Command Prompt
  * Visual Studio Code
  * Discord

* 🪟 Window switching automation

* 🧾 Fetch technology, politics, sports, and cricket news

---

## 🛠️ Tech Stack

### Language

* Python 3

### Libraries Used

* `pyttsx3` – Text to Speech
* `speech_recognition` – Voice command recognition
* `wikipedia` – Wikipedia API access
* `pyautogui` – Keyboard automation
* `GoogleNews` – Fetch news headlines
* `pywikihow` – How-to search functionality
* `webbrowser` – Open websites
* `datetime`
* `random`
* `os`
* `sys`

---

## 📦 Installation

Clone the repository

```bash
git clone https://github.com/your-username/jarvis-voice-assistant.git
cd jarvis-voice-assistant
```

Install required dependencies

```bash
pip install pyttsx3
pip install SpeechRecognition
pip install wikipedia
pip install pyautogui
pip install GoogleNews
pip install pywikihow
pip install pyaudio
```

---

## ▶️ Running the Project

Run the Python script:

```bash
python jarvis.py
```

After running, the assistant will greet you and start listening for commands.

### Example commands

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

## 📂 Project Structure

```
Jarvis-Voice-Assistant
│
├── jarvis.py
├── NewsRead.py
├── README.md
```

---

## 🧠 How It Works

1. The program uses **SpeechRecognition** to capture voice input from the microphone.
2. The speech is converted into text using **Google Speech API**.
3. Based on the detected command, different Python functions are triggered.
4. Responses are spoken back using **pyttsx3 text-to-speech engine**.

---

## ⚠️ Notes

* This project currently works best on **Windows** because it uses the **SAPI5 speech engine**.
* Some application paths may need to be changed depending on your system.
* A working **microphone** is required.

---

## 👨‍💻 Author

**Debayan Ghosh**

Aspiring developer interested in:

* Artificial Intelligence
* Automation
* Game Development
* Financial Technology

GitHub: https://github.com/Debayan-G

---

## ⭐ Support

If you found this project useful, consider **starring ⭐ the repository** to support the project.
