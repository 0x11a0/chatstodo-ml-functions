import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai_key = os.getenv('OPENAI_API_KEY')

class OpenAiHelper:
    def __init__(self, api_key = openai_key, model='gpt-3.5-turbo-1106'):
        self.api_key = api_key
        openai.api_key = self.api_key
        self.model = model

    def get_response(self, prompt):
        try:
            response = openai.Completion.create(
                model = self.model,
                prompt = prompt,
            )
            return response.choices[0].text.strip()
        except Exception as e:
            print(f"Error getting response from OpenAI: {e}")
            return ""

    # Prompt Generation Functions    
    def generate_prompt_for_summary(self, chat_messages):
        prompt = " Summarize the following chat messages: \n"
        prompt += "\n".join(chat_messages)
        return prompt
    
    def generate_prompt_for_task(self, chat_messages):
        prompt = "Extract tasks from the following chat messages: \n"
        prompt += "\n".join(chat_messages)
        return prompt
    
    def generate_prompt_for_event(self, chat_messages):
        prompt = "Extract events from the following chat messages: \n"
        prompt += "\n".join(chat_messages)
        return prompt
    
    # Summarize, task and event functions
    def get_chat_summary(self, chat_messages):
        prompt = self.generate_prompt_for_summary(chat_messages)
        return self.get_response(prompt)
    
    def get_tasks(self, chat_messages):
        prompt = self.generate_prompt_for_task(chat_messages)
        return self.get_response(prompt)
    
    def get_events(self, chat_messages):
        prompt = self.generate_prompt_for_event(chat_messages)
        return self.get_response(prompt)