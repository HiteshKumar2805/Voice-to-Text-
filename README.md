# Voice to Text Converter

## Overview
This is a simple **Voice-to-Text Converter** built using **Python, Vosk Speech Recognition, PyQt6, and SoundDevice**. The application captures real-time speech through a microphone, converts it into text, and displays the transcription in a graphical user interface (GUI).

## Features
- **Start & Stop Recording**: Click the microphone button to begin or stop recording.
- **Real-time Speech-to-Text**: Uses Vosk API for offline speech recognition.
- **Minimal UI**: Simple and easy-to-use PyQt6-based interface.
- **Low Latency**: Processes and displays text in real-time.

## Installation
### Prerequisites
Ensure you have Python **3.8+** installed on your system. Then, install the required dependencies:

```bash
pip install vosk sounddevice pyqt6
```

### Download Vosk Model
You need a Vosk speech model for offline recognition. Download the English model:

```bash
wget https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip
unzip vosk-model-small-en-us-0.15.zip
```

Set the `MODEL_PATH` in the script to the extracted folder path.

## Usage
Run the application using:

```bash
python voice_to_text.py
```

## How It Works
1. The app initializes a **Vosk speech recognition model**.
2. When the **"Start Recording"** button is clicked, it starts capturing audio using `sounddevice`.
3. Audio is **processed in real-time** using a separate thread.
4. **Recognized text** is updated in the PyQt6 GUI.
5. Clicking **"Stop Recording"** stops capturing audio.

## File Structure
```
voice-to-text/
│-- voice_to_text.py  # Main application script
│-- vosk-model-small-en-us-0.15/  # Downloaded Vosk model directory
│-- README.md  # Project documentation
```

## Troubleshooting
- **No text appears?** Ensure your microphone is working and the correct input device is selected.
- **Module not found?** Reinstall dependencies using `pip install vosk sounddevice pyqt6`.
- **High latency?** Try a smaller Vosk model for faster processing.

## Future Enhancements
- Support for **multiple languages**.
- Option to **save transcriptions** as text files.
- Improved **noise filtering** for better accuracy.

## License
This project is licensed under the **MIT License**.

## Author
Developed by **Hitesh Kumar S**.
