from langdetect import detect, DetectorFactory

# Ensure consistent results
DetectorFactory.seed = 0

def detect_language(text):
    """Detects the language of the provided text."""
    return detect(text)

if __name__ == '__main__':
    text = input("Enter text: ")
    language = detect_language(text)
    print("Detected Language:", language)
