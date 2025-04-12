from src.processing.summarizer import summarize_text
from src.voice.azure_tts import generate_speech

def main():
    with open("examples/sample.txt", "r") as file:
        input_text = file.read()

    summary = summarize_text(input_text)
    print("\n=== Summary ===\n", summary)

    generate_speech(summary, output_path="examples/output.mp3")

if __name__ == "__main__":
    main()
