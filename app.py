import speech_recognition as sr

def transcribe_audio_file(file_path):
    """
    Transcribes an audio file (WAV format) to text.
    
    Parameters:
        file_path (str): The path to the audio file (e.g., "C:\\audio\\sample.wav")
        
    Returns:
        str: The recognized text or an error message.
    """
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(file_path) as source:
            # Read the entire audio file
            audio_data = recognizer.record(source)
        # Recognize speech using Google's speech recognition service (English language)
        text = recognizer.recognize_google(audio_data, language="en-US")
        return text
    except Exception as e:
        return f"Error processing file: {e}"

def transcribe_from_microphone():
    """
    Transcribes spoken words from the microphone to text.
    
    Returns:
        str: The recognized text or an error message.
    """
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Please start speaking... (listening from microphone)")
            # Adjust for ambient noise for a short duration (1 second)
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio_data = recognizer.listen(source)
            print("Recording finished. Transcribing now...")
        # Recognize speech using Google's speech recognition service (English language)
        text = recognizer.recognize_google(audio_data, language="en-US")
        return text
    except Exception as e:
        return f"Error during recording: {e}"

def main():
    print("Select the transcription mode:")
    print("   (m) Microphone input")
    print("   (f) Audio file input (WAV file)")
    
    mode = input("Please choose 'm' or 'f': ").strip().lower()
    
    if mode == 'm':
        transcription = transcribe_from_microphone()
        print("Transcription:", transcription)
    elif mode == 'f':
        file_path = input("Enter the full path to the audio file (e.g., C:\\audio\\sample.wav): ").strip()
        transcription = transcribe_audio_file(file_path)
        print("Transcription:", transcription)
    else:
        print("Invalid option selected. Please choose 'm' for microphone or 'f' for file input.")

if __name__ == "__main__":
    main()
