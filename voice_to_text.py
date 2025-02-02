import sys
import vosk
import sounddevice as sd
import queue
import json
import threading
from PyQt6.QtWidgets import QApplication, QWidget, QTextEdit, QPushButton, QVBoxLayout

MODEL_PATH = "# path of vosk-model-small-en-us-0.15"
q = queue.Queue()
recording = False

class VoiceToTextApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.model = vosk.Model(MODEL_PATH)
        self.recognizer = vosk.KaldiRecognizer(self.model, 16000)
        self.audio_thread = None

    def initUI(self):
        self.setWindowTitle("Voice to Text")
        self.setGeometry(100, 100, 400, 300)
        
        self.text_edit = QTextEdit(self)
        self.text_edit.setReadOnly(True)
        
        self.record_button = QPushButton("🎤 Start Recording", self)
        self.record_button.clicked.connect(self.toggle_recording)
        
        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        layout.addWidget(self.record_button)
        self.setLayout(layout)

    def toggle_recording(self):
        global recording
        if recording:
            recording = False
            self.record_button.setText("🎤 Start Recording")
        else:
            recording = True
            self.record_button.setText("🛑 Stop Recording")
            self.audio_thread = threading.Thread(target=self.record_audio)
            self.audio_thread.start()

    def record_audio(self):
        with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                               channels=1, callback=self.callback):
            while recording:
                data = q.get()
                if self.recognizer.AcceptWaveform(data):
                    result = json.loads(self.recognizer.Result())
                    self.update_text(result.get("text", ""))

    def callback(self, indata, frames, time, status):
        if status:
            print(status, file=sys.stderr)
        q.put(bytes(indata))

    def update_text(self, text):
        self.text_edit.append(text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VoiceToTextApp()
    window.show()
    sys.exit(app.exec())
