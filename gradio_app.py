import gradio as gr
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

# Load the model and tokenizer
model_name = "facebook/blenderbot-400M-distill"
print("Loading model...")
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
print("Model loaded successfully!")

# Store conversation history
conversation_history = []

def chat(message, history):
    """
    Chat function that processes user messages and returns bot responses.
    
    Args:
        message: Current user message
        history: Chat history from Gradio (list of message dicts with 'role' and 'content')
    
    Returns:
        Bot response as a string
    """
    global conversation_history
    
    # Build history string from conversation_history
    history_string = "\n".join(conversation_history)
    
    # Tokenize the input text along with the conversation history
    inputs = tokenizer(
        history_string + message, 
        return_tensors="pt", 
        max_length=128, 
        truncation=True
    )
    
    # Generate a response from the model
    outputs = model.generate(**inputs, max_length=128)
    
    # Decode the response
    response = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()
    
    # Update conversation history
    conversation_history.append(message)
    conversation_history.append(response)
    
    # Keep only last 12 messages (6 exchanges)
    if len(conversation_history) > 12:
        conversation_history = conversation_history[-12:]
    
    return response

# Create Gradio interface using ChatInterface for simpler setup
demo = gr.ChatInterface(
    fn=chat,
    title="🤖 BlenderBot Chatbot",
    description="Chat with Facebook's BlenderBot! The bot remembers your conversation context.",
    chatbot=gr.Chatbot(height=500),
    textbox=gr.Textbox(placeholder="Type your message here...", container=False, scale=7),
    theme=gr.themes.Soft(),
    examples=["Hello! How are you?", "Tell me a joke", "What's your favorite hobby?"]
)

if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",  # Makes it accessible from other devices on the network
        server_port=7860,       # Default Gradio port
        share=False             # Set to True to create a public link
    )
