# alternate_universe_gemini.py
from dotenv import load_dotenv
import os
from google import genai
import json
import random

# -------- Load API key from .env --------
# Try loading from project root first, then current directory
env_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
if os.path.exists(env_path):
    load_dotenv(env_path)
else:
    load_dotenv()  # Try current directory

GENAI_API_KEY = os.getenv("GENAI_API_KEY")
if not GENAI_API_KEY:
    raise ValueError("GENAI_API_KEY not found in .env file. Add GENAI_API_KEY=your_key_here")

# -------- Initialize Gemini client --------
client = genai.Client(api_key=GENAI_API_KEY)

# -------- Define universe styles --------
UNIVERSE_STYLES = {
    "wizard": "Speak like a mystical medieval wizard, using thee, thou, and magical words.",
    "robot": "Speak like a futuristic robot, monotone and precise.",
    "medieval knight": "Speak like a brave knight in medieval times, formal and chivalrous.",
    "king": "Speak like a royal king giving a speech.",
    "sci-fi": "Speak like a futuristic sci-fi character, imaginative and advanced."
}

# -------- AI transformation function using Gemini --------
def transform_text(text: str, universe: str) -> str:
    prompt = (
        f"You are a {universe}.\n"
        f"Answer or respond to the user text below in your universe style.\n\n"
        f"User text: {text}"
    )
    
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text  # Gemini returns .text with the generated content
    except Exception as e:
        return json.dumps({"error": str(e)})

# -------- Main Interactive Loop --------
if __name__ == "__main__":
    print("="*60)
    print("🪄 Alternate Universe AI Chatbot (Gemini)")
    print("="*60)

    while True:
        text = input("\nEnter your message (or 'exit' to quit): ").strip()
        if text.lower() == "exit":
            break

        universe = input(f"Choose a universe {list(UNIVERSE_STYLES.keys())} or leave blank for random: ").strip().lower()
        if not universe or universe not in UNIVERSE_STYLES:
            universe = random.choice(list(UNIVERSE_STYLES.keys()))
            print(f"🌟 AI chose the universe: {universe}")

        print("\nGenerating response...\n")
        response_text = transform_text(text, universe)
        print(f"[{universe.upper()} STYLE]: {response_text}")

        # Optional: save chat history
        chat_data = {
            "original": text,
            "universe": universe,
            "response": response_text
        }
        with open("chat_history.json", "a", encoding="utf-8") as f:
            f.write(json.dumps(chat_data, ensure_ascii=False) + "\n")
            
