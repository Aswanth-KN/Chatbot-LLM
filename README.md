# ChatBot with LLM 🤖

An AI-powered conversational chatbot using Facebook's BlenderBot model with multiple implementation options.

## 📋 Overview

This project provides a sophisticated conversational AI chatbot that maintains context and provides human-like responses. Built using Facebook's BlenderBot-400M-distill model from Hugging Face Transformers.

## ✨ Features

- **Context-Aware Conversations**: Maintains last 6 exchanges for contextual responses
- **Multiple Interfaces**: Choose between CLI, REST API, or Web UI
- **Pre-trained Model**: Uses state-of-the-art BlenderBot transformer
- **Easy Deployment**: Simple setup and multiple deployment options
- **Conversation History**: Automatically manages conversation context

## 🗂️ Project Structure

```
ChatBotwithLLM/
├── chatbot.py          # Command-line interface
├── app.py              # Flask REST API server
├── gradio_app.py       # Gradio web interface
└── README.md           # This file
```

## 📦 Installation

### 1. Set Up Virtual Environment

```bash
# Navigate to project root
cd /home/aswanth.cp@knackforge.com/Public/ML/Projects

# Activate virtual environment
source env/bin/activate
```

### 2. Install Dependencies

```bash
cd ChatBotwithLLM
pip install flask flask-cors transformers torch gradio
```

### Required Packages
- `transformers` - Hugging Face transformers library
- `torch` - PyTorch deep learning framework
- `flask` - Web framework for REST API
- `flask-cors` - CORS support for API
- `gradio` - Web UI framework

## 🚀 Usage

### Option 1: Command Line Interface

Perfect for quick testing and terminal-based interactions.

```bash
python3 chatbot.py
```

**Interaction:**
```
You: Hello! How are you?
Bot: I'm doing great, thanks for asking! How are you today?
You: Tell me a joke
Bot: Why don't scientists trust atoms? Because they make up everything!
```

Press `Ctrl+C` to exit.

### Option 2: Flask REST API

Ideal for integrating the chatbot into other applications.

```bash
python3 app.py
```

**Server Details:**
- Default URL: `http://localhost:5000`
- Endpoint: `/chat`
- Method: `POST`

**API Usage:**

```bash
# Using curl
curl -X POST http://localhost:5000/chat \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Hello! How are you?"}'
```

**Request Format:**
```json
{
  "prompt": "Your message here"
}
```

**Response Format:**
```json
{
  "response": "Bot's response here"
}
```

**Example with Python:**
```python
import requests

response = requests.post(
    'http://localhost:5000/chat',
    json={'prompt': 'What is AI?'}
)
print(response.json()['response'])
```

### Option 3: Gradio Web UI (Recommended)

Best for interactive use with a beautiful interface.

```bash
python3 gradio_app.py
```

**Access:**
- Local: `http://localhost:7860`
- Network: `http://0.0.0.0:7860` (accessible from other devices)

**Features:**
- 💬 Chat-style interface
- 📝 Pre-loaded example prompts
- 🎨 Modern, responsive design
- 📊 Conversation history display
- 🔄 Real-time responses

**Configuration Options:**
```python
demo.launch(
    server_name="0.0.0.0",  # Network access
    server_port=7860,       # Custom port
    share=True              # Create public link (optional)
)
```

## 🔧 File Details

### chatbot.py
**Purpose:** Command-line chatbot interface  
**Best For:** Quick testing, terminal-based chat  
**Features:**
- Simple while loop for continuous conversation
- Direct terminal input/output
- Maintains conversation history
- Easy to modify and extend

### app.py
**Purpose:** Flask REST API server  
**Best For:** Integration with other apps, web/mobile frontends  
**Features:**
- RESTful API endpoint
- CORS enabled for cross-origin requests
- JSON request/response format
- Stateful conversation management
- Home route for health checks

### gradio_app.py
**Purpose:** Web-based UI using Gradio  
**Best For:** End-user interaction, demos, production use  
**Features:**
- ChatInterface for seamless chat experience
- Customizable theme (Soft theme)
- Example prompts for quick start
- Configurable height and styling
- Network accessibility options

## 🧠 How It Works

### Architecture

```
User Input → Tokenization → Model Processing → Response Generation → Output
                ↑                                                        ↓
                └──────────── Conversation History ─────────────────────┘
```

### Workflow

1. **Model Initialization**
   - Downloads BlenderBot-400M-distill (~1.6 GB) on first run
   - Loads model and tokenizer into memory

2. **Input Processing**
   - Combines conversation history with new input
   - Tokenizes text (max 128 tokens)
   - Truncates if necessary

3. **Response Generation**
   - Feeds tokens to the model
   - Generates response (max 128 tokens)
   - Decodes output to text

4. **History Management**
   - Appends user message to history
   - Appends bot response to history
   - Keeps only last 12 messages (6 exchanges)

### Model Details

**BlenderBot-400M-distill**
- **Developer:** Meta AI (Facebook)
- **Type:** Sequence-to-sequence transformer
- **Parameters:** 400 million (distilled version)
- **Training:** Trained on diverse conversational datasets
- **Strengths:** Context awareness, engaging responses, knowledge breadth

## ⚙️ Configuration

### Adjust Response Length

In any file, modify the `max_length` parameter:

```python
outputs = model.generate(**inputs, max_length=256)  # Longer responses
```

### Adjust History Length

Change the history limit:

```python
if len(conversation_history) > 20:  # Keep 10 exchanges instead of 6
    conversation_history = conversation_history[-20:]
```

### Change Port (Gradio)

```python
demo.launch(server_port=8080)  # Use port 8080 instead
```

### Change Port (Flask)

```python
if __name__ == '__main__':
    app.run(port=8000)  # Use port 8000 instead
```

## 🐛 Troubleshooting

### Port Already in Use

```bash
# For Flask (port 5000)
lsof -ti:5000 | xargs kill -9

# For Gradio (port 7860)
lsof -ti:7860 | xargs kill -9
```

### Module Not Found

```bash
# Ensure virtual environment is activated
source ../env/bin/activate

# Reinstall dependencies
pip install flask flask-cors transformers torch gradio
```

### CUDA/GPU Issues

```bash
# Install CPU-only PyTorch
pip install torch --index-url https://download.pytorch.org/whl/cpu
```

### Model Download Fails

- Check internet connection
- Model auto-downloads on first run
- Cached in `~/.cache/huggingface/`
- Try manually: `huggingface-cli download facebook/blenderbot-400M-distill`

### Slow Responses

**Solutions:**
- Use GPU if available (5-10x faster)
- Reduce `max_length` parameter
- Use smaller model variant
- Close other applications to free RAM

## 📊 Performance

### System Requirements

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| RAM | 4 GB | 8 GB+ |
| Storage | 2 GB | 5 GB+ |
| CPU | 2 cores | 4+ cores |
| GPU | Optional | CUDA-capable |

### Response Times

| Setup | Time per Response |
|-------|-------------------|
| CPU (4 cores) | 2-4 seconds |
| GPU (CUDA) | 0.3-0.5 seconds |
| High-end GPU | 0.1-0.3 seconds |

### Model Size

- Download size: ~1.6 GB
- Memory footprint: ~2-3 GB RAM
- Cached location: `~/.cache/huggingface/transformers/`

## 🔐 Security Notes

### For Production Deployment

1. **API Security:**
   ```python
   # Add authentication
   # Add rate limiting
   # Use HTTPS
   # Validate inputs
   ```

2. **Input Sanitization:**
   - Validate JSON payloads
   - Limit message length
   - Filter harmful content

3. **Network Security:**
   - Don't expose to public internet without protection
   - Use firewall rules
   - Implement API keys

## 🚀 Advanced Usage

### Custom Prompts

Add system prompts to guide behavior:

```python
conversation_history = ["System: You are a helpful assistant specialized in Python programming."]
```

### Temperature Control

Add temperature for more creative responses:

```python
outputs = model.generate(
    **inputs, 
    max_length=128,
    temperature=0.8,  # Higher = more creative
    top_p=0.9
)
```

### Multiple Conversations

Implement session management:

```python
sessions = {}  # Store conversations per user

@app.route('/chat', methods=['POST'])
def handle_prompt():
    user_id = data.get('user_id', 'default')
    if user_id not in sessions:
        sessions[user_id] = []
    # Use sessions[user_id] for conversation history
```

## 📚 Resources

- [BlenderBot Paper](https://arxiv.org/abs/2004.13637)
- [Hugging Face Model Card](https://huggingface.co/facebook/blenderbot-400M-distill)
- [Transformers Documentation](https://huggingface.co/docs/transformers/)
- [Gradio Documentation](https://gradio.app/docs/)
- [Flask Documentation](https://flask.palletsprojects.com/)

## 🎯 Example Use Cases

1. **Customer Support Bot** - Answer FAQs
2. **Learning Assistant** - Help with homework
3. **Companion Bot** - Casual conversation
4. **Virtual Assistant** - Task reminders and info
5. **Game NPC** - Interactive game characters

## 🔄 Future Enhancements

- [ ] Multi-user session support
- [ ] Conversation export (JSON/PDF)
- [ ] Fine-tuning on custom data
- [ ] Voice input/output
- [ ] Sentiment analysis
- [ ] Multi-language support
- [ ] Database integration for persistence

## 📝 License

Educational and research purposes.

## 🙏 Acknowledgments

- Meta AI for BlenderBot
- Hugging Face for Transformers
- Gradio team for the UI framework

---

**Happy Chatting! 💬**
