from openai import OpenAI

class OpenAiHelper:
    def __init__(self, api_key, model='gpt-3.5-turbo-1106'):
        self.client = OpenAI()
        self.api_key = api_key
        self.model = model

    def get_response(self, prompt):
        try:
            response = self.client.chat.completions.create(
                model = self.model,
                messages = [{"role" : "user", "content" : prompt}]
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error getting response from OpenAI: {e}")
            return ""

    # Prompt Generation Functions    
    def generate_prompt_for_summary(self, userid, chat_messages):
        prompt = "Summarize the following chat messages relevant to" + str(userid) + ": \n"
        prompt += "\n".join(chat_messages)
        return prompt
    
    def generate_prompt_for_task(self, userid, chat_messages):
        prompt = "Extract tasks from the following chat messages relevant to" + str(userid) + ": \n"
        prompt += "\n".join(chat_messages)
        return prompt
    
    def generate_prompt_for_event(self, userid, chat_messages):
        prompt = "Extract events from the following chat messages relevant to" + str(userid) + ": \n"
        prompt += "\n".join(chat_messages)
        return prompt
    
    # Summarize, task and event functions
    def get_chat_summary(self, userid, chat_messages):
        prompt = self.generate_prompt_for_summary(userid, chat_messages)
        return self.get_response(prompt)
    
    def get_tasks(self, userid, chat_messages):
        prompt = self.generate_prompt_for_task(userid, chat_messages)
        return self.get_response(prompt)
    
    def get_events(self, userid, chat_messages):
        prompt = self.generate_prompt_for_event(userid, chat_messages)
        return self.get_response(prompt)