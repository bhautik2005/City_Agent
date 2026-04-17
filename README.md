# 🌆 City AI Agent  
> AI-powered smart city assistant with real-time weather & news using LangChain

---

## 🚀 Overview

**City AI Agent** is a full-stack AI application that provides real-time information about cities such as weather updates and latest news. It leverages **LangChain tool-calling agents**, integrates external APIs, and delivers responses through a modern chat-based UI.

---

## ✨ Features

- 🌤️ Real-Time Weather Data  
- 📰 Latest City News Integration  
- 🤖 Agentic AI (Tool Calling with LangChain)  
- 💬 Interactive Chat Interface (React UI)  
- ⚡ Loading State & Smooth UX  
- 🔗 Clickable News Links  
- 🛡️ Error Handling & API Failures Managed  
- 🌐 Full Stack Architecture (Flask + React)  

---

## 🧠 How It Works
User → React Frontend → Flask API → LangChain Agent → Tools (Weather + News APIs) → Response


- The AI agent decides when to use tools  
- Fetches real-time data  
- Returns structured responses to UI  

---

## 🛠️ Tech Stack

### Frontend
- React.js  
- JavaScript  
- CSS  

### Backend
- Flask  
- LangChain  
- Mistral AI (LLM)  
- Tavily API (News)  
- OpenWeather API  

---

## 📸 Screenshots

### 💬 Chat Interface
![Chat UI](https://github.com/bhautik2005/City_Agent/blob/f70c40421cb189c1d5a5df576debe3d713affbc5/Screenshot%202026-04-17%20093526.png)

---

### 🌤️ Weather Response
![Weather](https://github.com/bhautik2005/City_Agent/blob/f70c40421cb189c1d5a5df576debe3d713affbc5/Screenshot%202026-04-17%20093403.png)

---

### 📰 News Output
![News](https://github.com/bhautik2005/City_Agent/blob/f70c40421cb189c1d5a5df576debe3d713affbc5/Screenshot%202026-04-17%20093430.png)

---

### ⚡ Loading State
![Loading](https://github.com/bhautik2005/City_Agent/blob/f70c40421cb189c1d5a5df576debe3d713affbc5/Screenshot%202026-04-17%20093554.png)

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/bhautik2005/City_Agent.git
cd City_Agent
```
2️⃣ Backend Setup
cd backend
python -m venv enve
enve\Scripts\activate
pip install -r requirements.txt
3️⃣ Environment Variables

Create .env file:

OPENWEATHER_API_KEY=your_key
TAVILY_API_KEY=your_key
4️⃣ Run Backend
python app.py
5️⃣ Frontend Setup
cd frontend
npm install
npm start
🔌 API Endpoint
POST /chat
{
  "message": "What is weather of Rajkot?"
}
Response:
{
  "status": "success",
  "response": "Weather in Rajkot..."
}
💡 Key Learnings
Implemented Agentic AI with tool calling
Integrated multiple real-time APIs
Built full-stack AI system
Managed CORS, async calls, and UI states
Designed user-friendly chat interface
🚀 Future Improvements
🔄 Streaming responses (real-time typing)
🧠 Memory-based conversations
📊 Structured UI (cards for news/weather)
🌍 Deployment (Render + Vercel)
🧩 Multi-agent architecture (planner + executor)

👨‍💻 Author

Bhautik Gondaliya
