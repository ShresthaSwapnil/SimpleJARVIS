# Jarvis AI

A Python-based virtual assistant named Jarvis with various functionalities such as sending emails, fetching weather updates, managing clipboard text, automating tasks, and much more. This project demonstrates the integration of multiple libraries and APIs for practical and interactive user experiences.

---

## Features

### General Features:

- **Voice Interaction**: Uses text-to-speech and speech-to-text for seamless interaction.
- **Greeting & Time Updates**: Offers personalized greetings and tells the current time and date.
- **Voice Switching**: Switch between two voice personas (Jarvis and Friday).

### Productivity Tools:

- **Email Sending**: Automates sending emails via Gmail.
- **Clipboard Text Reading**: Reads the current clipboard content aloud.
- **Task Automation**:
  - Opens Visual Studio Code, Edge browser, and other directories.
  - Takes screenshots and saves them.

### Information Retrieval:

- **Weather Updates**: Fetches weather information using OpenWeatherMap API.
- **Wikipedia Search**: Summarizes topics using Wikipedia.
- **News Updates**: Retrieves news articles using NewsAPI.
- **Google Search**: Automates Google search queries.
- **YouTube Search**: Plays requested videos on YouTube.

### Fun Features:

- **Jokes**: Tells a random joke using `pyjokes`.
- **Password Generator**: Generates strong, random passwords.
- **Coin Flipping & Dice Rolling**: Simulates these for quick decisions or games.

### System Monitoring:

- **CPU & Battery Status**: Reports current CPU usage and battery percentage.

### Memory Features:

- **Remember Things**: Remembers specific user-input data.
- **Retrieve Memory**: Reads back remembered information.

### Communication Tools:

- **WhatsApp Messaging**: Sends messages using WhatsApp Web.

---

## Installation

### Prerequisites

1. Python 3.8+
2. Required Python libraries:
   ```bash
   pip install pyttsx3 speechrecognition smtplib pyautogui webbrowser wikipedia pywhatkit requests newsapi clipboard psutil nltk google-generativeai pyjokes
   ```
3. Additional setups:
   - `credentials.py` file for storing your email credentials:
     ```python
     senderEmail = "your_email@gmail.com"
     ePWD = "your_email_password"
     ```
   - `geminiAPI.py` file for Gemini API key:
     ```python
     apiKey = "your_gemini_api_key"
     ```

### Running the Program

1. Clone this repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd JARVIS
   ```
3. Run the script:
   ```bash
   python jarvis.py
   ```

---

## Usage

1. Launch the program.
2. Use the wake word "Jarvis" to activate voice commands.
3. Interact using predefined commands such as:
   - "What's the time?"
   - "Send an email."
   - "Tell me the weather."
   - "Play a video on YouTube."
4. Say "quit" or "exit" to terminate the assistant.

---

## Technologies Used

- **Programming Language**: Python
- **APIs**:
  - OpenWeatherMap API
  - NewsAPI
  - Gemini API
- **Libraries**:
  - `pyttsx3` for text-to-speech
  - `speechrecognition` for voice recognition
  - `pywhatkit` for YouTube search
  - `psutil` for system monitoring
  - `nltk` for text processing

---

## Future Improvements

- Adding natural language processing for more conversational interactions.
- Expanding third-party integrations.
- Building a GUI for easier interaction.

---

## Contribution

Feel free to contribute by submitting issues or pull requests. All contributions are welcome!

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Acknowledgments

- **Libraries**: Open-source libraries and APIs that made this project possible.
- **Special Thanks**: Python and its vast ecosystem of tools and libraries.
