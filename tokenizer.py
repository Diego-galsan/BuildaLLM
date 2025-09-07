with open("the-verdict.txt", "r") as f:
    raw_text = f.read()
print(f"Length of text: {len(raw_text)} characters")  # Print the length of the text
print(raw_text[:99])  # Print the first 1000 characters to verify content  

import re 
preprocessed_text = re.split(r'([,.:;?_!"()\']|\s)', raw_text)  # Replace multiple spaces/newlines with a single space
preprocessed_text = [item.strip() for item in preprocessed_text if item.strip()]  # Split by space and remove empty tokens
print(f"Number of tokens: {len(preprocessed_text)}")  # Print the number of tokens

print(preprocessed_text[:30])  # Print the first 30 tokens to verify tokenization

all_words = sorted(set(preprocessed_text))  # Get unique words
vocab_size = len(all_words)  # Get vocabulary size
print(f"Vocabulary size: {vocab_size}")  # Print vocabulary size

vocab = {token:integer for integer, token in enumerate(all_words)}  # Create a mapping from token to integer
for i, item in enumerate(vocab.items()):
    print(item)  # Print the first 20 tokens with their integer mapping
    if i>=50:
        break

class SimpleTokenizerV1:
    def __init__(self,vocab):
        self.str_to_int = vocab
        self.int_to_str = {i:s for s,i in vocab.items()}

    def encode(self,text):
        preprocessed = re.split(r'([,.:;?_!"()\']|\s)', text)  # Replace multiple spaces/newlines with a single space
        preprocessed = [item.strip() for item in preprocessed if item.strip()]  #

        ids = [self.str_to_int[token] for token in preprocessed]
        return ids
    
    def decode(self,ids):
        tokens = [self.int_to_str[id] for id in ids]
        text = " ".join(tokens)
        text = re.sub(r'\s([,.:;?_!"()\'])', r'\1', text)  # Remove space before punctuation
        return text
    
tokenizer = SimpleTokenizerV1(vocab)
text = """"It's the last he painted, you know," Mrs. Gisburn said with pardonable pride."""
ids = tokenizer.encode(text)
print(ids)  # Print the encoded token IDs
decoded_text = tokenizer.decode(ids)
print(decoded_text)  # Print the decoded text to verify it matches the original