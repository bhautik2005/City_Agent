from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

import os
import requests
from tavily import TavilyClient
from langchain_mistralai import ChatMistralAI
from langchain.tools import tool
from langchain.agents import create_agent

app = Flask(__name__)
CORS(app)  # ✅ allow all origins

# -------------------- TOOLS --------------------

@tool
def get_wather(CITY: str) -> str:
    """get current weather of city"""

    API_KEY = os.getenv("OPENWEATHER_API_KEY")

    if not API_KEY:
        return "❌ API key missing"

    URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(URL)

        if response.status_code != 200:
            return f"❌ API Error {response.status_code}: {response.text}"

        data = response.json()

        return {
            "city": CITY,
            "temperature": data['main']['temp'],
            "condition": data['weather'][0]['description'],
            "humidity": data['main']['humidity']
        }

    except Exception as e:
        return f"❌ Error: {str(e)}"


tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def get_news(city: str) -> str:
    """get latest news about city"""

    try:
        response = tavily_client.search(
            query=f"{city} news today india",
            search_depth="basic",
            max_results=3,
        )

        results = response.get("results", [])

        if not results:
            return "No news found"

        return results

    except Exception as e:
        return f"❌ Error: {str(e)}"


# -------------------- AGENT --------------------

llm = ChatMistralAI(model="mistral-small-2506")

agent = create_agent(
    llm,
    tools=[get_wather, get_news],
    system_prompt="""
        You are an AI city assistant with access to tools.

        STRICT RULES:
        - If user asks about weather → MUST call get_wather tool
        - If user asks about news → MUST call get_news tool
        - DO NOT answer from your own knowledge
        - ALWAYS use tools for real-time information
        - Do NOT give generic answers

        If unsure, still prefer using tools.
        """
)

# -------------------- ROUTE --------------------

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.json
        print("Incoming data:", data)  # ✅ DEBUG

        user_input = data.get("message")

        result = agent.invoke({
            "messages": [{"role": "user", "content": user_input}]
        })

        print("Agent result:", result)  # ✅ DEBUG

        ai_message = result["messages"][-1].content

        return jsonify({
            "status": "success",
            "response": ai_message
        })

    except Exception as e:
        print("ERROR:", str(e))  # ✅ IMPORTANT
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)