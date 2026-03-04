"""
Clara Answers - Onboarding Automation Pipeline
Usage: python pipeline.py
Requires: pip install groq
Set env var: GROQ_API_KEY=your_key
"""
import os, json, re, time
from datetime import datetime
from pathlib import Path
from groq import Groq

GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "")
client = Groq(api_key=GROQ_API_KEY)

def call_llm(prompt):
    for attempt in range(3):
        try:
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.1
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            if "429" in str(e):
                time.sleep(30 * (attempt + 1))
            else:
                raise
    raise Exception("LLM failed after 3 retries")

# Full pipeline code lives here - see Colab notebook for complete implementation
if __name__ == "__main__":
    print("Run via Colab notebook or import functions directly.")
    print("See README.md for full usage instructions.")
