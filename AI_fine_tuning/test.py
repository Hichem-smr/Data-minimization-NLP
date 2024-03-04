import spacy

# Load the small English model with GPU support
nlp = spacy.load("en_core_web_sm")

# Check if GPU is being used
if nlp.pipe_names:
    print("GPU is being used")
else:
    print("GPU is not being used")