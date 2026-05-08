
## Ai chat bot 
This is a real-time AI chatbot built using Python, FastAPI, WebSockets, HTML, CSS, and JavaScript.
***
### Technologies Used

- Python
- FastAPI
- WebSocket
- HTML
- CSS
- JavaScript
- Groq API
***
### Features
- Real-time AI chatbot
- FastAPI backend
- WebSocket communication
- Responsive frontend
***
### Installation
***
1.**Clone the repository**

```
git clone <https://github.com/manishaaverma/ai-chatbot>
```

2.**Move inside the project directory**

```
cd ai-chatbot
```

3.**Create Virtual Environment**

```
python -m venv venv
```

```
venv\Scripts\activate
```

4.**Install Dependencies**

```
pip install -r requirements.txt
```

5.**Create .env File**

Create a .env file in the root folder.

```
GROQ_API_KEY=your_groq_api_key
```

6.**Get Free Groq API Key**

Open:

```
https://console.groq.com
```

Create account

Generate API key

Paste API key inside ``.env``


7.**Run Server**

```
uvicorn app.main:app --reload
```

8.**Open Browser**

Visit:

```
http://127.0.0.1:8000
```




