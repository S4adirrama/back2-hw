from openai import OpenAI
from src.assistants.base import AssistantBase

client = OpenAI()

class OpenAIAssistant(AssistantBase):
    def explain(self, song):
        prompt = f"Explain why '{song.title}' by {song.artist} is on the Billboard Hot 100."
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
