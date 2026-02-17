from flask import Flask
from flask_cors import CORS
from transformers import AutoModelForSeq2SeqLM
from transformers import AutoTokenizer
from flask import request
import json

app = Flask(__name__)
CORS(app)

model_name = "facebook/blenderbot-400M-distill"
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

conversation_history = []


@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/chat', methods=['POST'])
def handle_prompt():

    data = request.get_json()
    input_text = data.get('prompt', '')

    history_string = "\n".join(conversation_history)

    # Tokenize the input text along with the conversation history
    inputs = tokenizer(history_string + input_text, return_tensors="pt", max_length=128, truncation=True)
    
    # Generate a response from the model
    outputs = model.generate(**inputs)

    response = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()

    conversation_history.append(input_text)
    conversation_history.append(response)
    if len(conversation_history) > 12:
        conversation_history = conversation_history[-12:]

    return json.dumps({"response": response})

if __name__ == '__main__':
    app.run()