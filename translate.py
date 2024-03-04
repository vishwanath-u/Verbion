import transformers
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

# Translation Module
# Load the mBART model and tokenizer
model_name = "facebook/mbart-large-50-many-to-many-mmt"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def translate(original_text, target):
    # Tokenize the original text with specified source and target languages
    input_text = f'en_XX: {original_text}'
    encoded_text = tokenizer(input_text, return_tensors="pt")

    # Generate translated tokens with the specified target language
    generated_tokens = model.generate(**encoded_text, forced_bos_token_id=tokenizer.lang_code_to_id[target])

    # Decode the translated text
    translated_text = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)[0]

    return translated_text
