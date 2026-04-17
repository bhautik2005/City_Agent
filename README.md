# 🌆 City AI Agent  
> **AI-powered smart city assistant with real-time weather & news using LangChain**

---

## 🚀 Overview

**City AI Agent** is a full-stack AI application designed to provide real-time, localized information for any city. By leveraging **LangChain tool-calling agents**, the system intelligently determines whether to fetch weather data or search for the latest news based on the user's natural language input. It features a modern, responsive chat interface built with React and a robust Flask backend.

---

## ✨ Features

- 🌤️ **Real-Time Weather Data:** Fetches live temperature, humidity, and atmospheric conditions.
- 📰 **Latest City News Integration:** Provides trending headlines with direct source links.
- 🤖 **Agentic AI:** Uses LangChain's tool-calling logic to select the right API dynamically.
- 💬 **Interactive Chat Interface:** Clean React-based UI with message bubbles and timestamps.
- ⚡ **Loading State & Smooth UX:** Visual feedback during AI processing.
- 🔗 **Clickable News Links:** Direct access to news articles from the chat.
- 🛡️ **Error Handling:** Graceful management of API failures and empty queries.
- 🌐 **Full Stack Architecture:** Seamless communication between Flask (Python) and React.

---

## 🧠 How It Works

The system follows a linear request-response flow powered by an intelligent "brain":

`User → React Frontend → Flask API → LangChain Agent → Tools (Weather + News APIs) → Response`

- The **Mistral AI** model acts as the controller.
- The agent analyzes the user prompt and decides which tool (Weather or News) to invoke.
- Real-time data is fetched, processed by the LLM, and returned as a human-like response.

---

## 🛠️ Tech Stack

### Frontend
- **Framework:** React.js
- **Styling:** CSS3 (Modern Flexbox/Grid)
- **State Management:** React Hooks (useState, useEffect)

### Backend
- **Framework:** Flask (Python)
- **Orchestration:** LangChain
- **LLM:** Mistral AI
- **Search Engine:** Tavily API (Optimized for LLMs)
- **Weather Data:** OpenWeather API

---

## 📸 Screenshots

| 💬 Chat UI | 🌤️ Weather Output |
|-----------|-----------|
| ![Chat UI](https://github.com/bhautik2005/City_Agent/blob/f70c40421cb189c1d5a5df576debe3d713affbc5/Screenshot%202026-04-17%20093526.png) | ![Weather](https://github.com/bhautik2005/City_Agent/blob/f70c40421cb189c1d5a5df576debe3d713affbc5/Screenshot%202026-04-17%20093403.png) |

| 📰 News Output | ⚡ Loading State |
|--------------|----------------|
| ![News](https://github.com/bhautik2005/City_Agent/blob/f70c40421cb189c1d5a5df576debe3d713affbc5/Screenshot%202026-04-17%20093430.png) | ![Loading](https://github.com/bhautik2005/City_Agent/blob/f70c40421cb189c1d5a5df576debe3d713affbc5/Screenshot%202026-04-17%20093554.png) |

---

## ⚙️ Setup Instructions

## 1️⃣ Clone Repository
```bash
git clone [https://github.com/bhautik2005/City_Agent.git](https://github.com/bhautik2005/City_Agent.git)
cd City_Agent
```

2️⃣ Backend Setup
```
Bash
cd backend
python -m venv enve

# Activate the environment
# Windows:
enve\Scripts\activate
# Mac/Linux:
source enve/bin/activate

pip install -r requirements.txt

```
3️⃣ Environment Variables
```
Create a .env file inside the backend/ directory:

Code snippet
OPENWEATHER_API_KEY=your_openweather_api_key
TAVILY_API_KEY=your_tavily_api_key
MISTRAL_API_KEY=your_mistral_api_key
```
4️⃣ Run Backend
```
Bash
python app.py
```
5️⃣ Frontend Setup
```
Bash
cd ../frontend
npm install
npm start
```
🔌 API Endpoint
POST /chat
Used to send a message to the AI agent.

Request:

JSON
{
  "message": "What is the weather in Rajkot?"
}
Response:

JSON
{
  "status": "success",
  "response": "The current temperature in Rajkot is 32°C with clear skies and 40% humidity."
}

 
### 🛠️ Tools & Core AI Logic
This project utilizes LangChain's tool-calling architecture, allowing the AI to interact with the real-world.

## 🌦️ Weather Tool
  - Source: OpenWeather API.

  - Functionality: Fetches temperature, weather conditions (rain, clear, clouds), and humidity.

  - Trigger: Keywords related to "weather", "temperature", or "climate".

## 📰 News Tool
  - Source: Tavily Search API.

  - Functionality: Fetches the most recent news headlines and verified links for a specific city.

  - Trigger: Keywords related to "news", "updates", or "what's happening".

## 🤖 Agent Logic
  - Powered by LangChain + Mistral AI, the agent handles:

  - Intention Analysis: Determining if a tool call is necessary based on the user's query.

  - Execution: Running the appropriate tool and gathering raw API data.

  - Synthesis: Combining raw data into a conversational, accurate, and human-friendly response.

## 💡 Key Learnings
 - Agentic Design: Implemented autonomous decision-making using LLM tool calling.

 - API Orchestration: Successfully integrated and managed multiple real-time data streams.

 - Full-Stack Development: Connected a Python-based AI backend with a modern React frontend seamlessly.

 - State Management: Handled asynchronous API states (loading, success, error) to maintain a smooth UI/UX.

## 🚀 Future Improvements
 - 🔄 Streaming Responses: Implement real-time token streaming for a more interactive "typing" chat experience.

 - 🧠 Persistent Memory: Enable the AI to remember previous context within a conversation session.

 - 📊 Structured UI: Render specialized cards/charts for weather forecasts and organized news grids.

 - 🌍 Cloud Deployment: Host the backend on Render/AWS and the frontend on Vercel.

## 🧩 Multi-Agent Architecture: Transition to a Planner-Executor model to handle complex, multi-step queries.

### 👨‍💻 Author
Bhautik Gondaliya Full Stack & AI/ML  Developer

© 2026 City AI Agent Project
