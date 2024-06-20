import re
import random
from collections import defaultdict, Counter

# List of file paths
file_paths = ['./alice_in_wonderland.txt', './shakespeare.txt', './test.txt']  # Update this to your file paths

sequence = ["a", "person", "who"]  # sequence to complete (MAKE SURE IT IS non-null)
n_limit = 5  # limit

# Function to read and tokenize text from multiple files
def read_and_tokenize_files(file_paths):
    tokens = []
    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            tokens.extend(tokenize(text))
    return tokens

# Tokenize the text
def tokenize(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    tokens = text.split()
    return tokens

# Read and tokenize all files
tokens = read_and_tokenize_files(file_paths)

# Build the n-gram model
def build_ngram_model(tokens, n):
    ngrams = defaultdict(Counter)
    for i in range(len(tokens) - n):
        gram = tuple(tokens[i:i+n])
        next_word = tokens[i+n]
        ngrams[gram][next_word] += 1
    return ngrams

# Predict the next word
def predict_next_word(ngram_model, sequence, n):
    if isinstance(sequence, list):
        sequence = tuple(sequence)
    elif isinstance(sequence, str):
        sequence = tuple(sequence.split())
    
    sequence = sequence[-n:]  # get last n elements only
    
    if sequence in ngram_model:
        next_words = ngram_model[sequence]
        next_word = random.choices(list(next_words.keys()), weights=next_words.values())[0]
        return next_word
    else:
        return None

# Initial build of the n-gram model
ngram_model = build_ngram_model(tokens, n_limit)

last_build = False

# Test the prediction
for i in range(24):  # just 24 iterations for test
    current_n = min(len(sequence), n_limit)  # dynamically adjust n
    ngram_model = build_ngram_model(tokens, current_n)  # rebuild n-gram model with current n

    next_word = predict_next_word(ngram_model, sequence, current_n)  # predict next word
    
    if next_word:
        sequence.append(next_word)  # add next word to existing sequence
        print(sequence)  # print sequence
        print(f'n: {current_n}\n')  # print current n value
    else:
        print("No valid next word found.")
        break
