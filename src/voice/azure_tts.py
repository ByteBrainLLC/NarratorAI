import azure.cognitiveservices.speech as speechsdk
import os
from dotenv import load_dotenv

load_dotenv()

def generate_speech(text, output_path="output.mp3"):
    speech_config = speechsdk.SpeechConfig(
        subscription=os.getenv("AZURE_TTS_KEY"),
        region=os.getenv("AZURE_TTS_REGION")
    )
    audio_config = speechsdk.audio.AudioOutputConfig(filename=output_path)
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

    result = synthesizer.speak_text_async(text).get()
    
    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print(f"Speech synthesized and saved to {output_path}")
    else:
        print(f"Speech synthesis failed: {result.reason}")
