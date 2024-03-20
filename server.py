from openai_helper import OpenAiHelper
import chatstodo_ml_service_pb2
import chatstodo_ml_service_pb2_grpc
import grpc
from concurrent import futures
# import os
# from dotenv import load_dotenv
# load_dotenv()

openai_key = os.getenv('OPENAI_API_KEY')

class ChatAnalysisServiceImpl(chatstodo_ml_service_pb2_grpc.ChatAnalysisServiceServicer):
    def __init__(self, api_key):
        self.openai_helper = OpenAiHelper(api_key)

    def AnalyzeChat(self, request, context):

        # Extract chat messages from request
        chat_messages = request.chatMessages
        user_id = request.user_id

        # Process the messages
        summary = self.openai_helper.get_chat_summary(user_id, chat_messages)
        tasks = self.openai_helper.get_tasks(user_id, chat_messages)
        events = self.openai_helper.get_events(user_id, chat_messages)

        # Create and return a response
        response = chatstodo_ml_service_pb2.ChatAnalysisResponse(
            userID = user_id,
            summary = [summary],
            tasks = [tasks],
            events = [events]
        )

        return response
    
def serve():
    # Have a threadpool of 10 
    server = grpc.server(futures.ThreadPoolExecutor(max_workers = 10))
    chatstodo_ml_service_pb2_grpc.add_ChatAnalysisServiceServicer_to_server(ChatAnalysisServiceImpl(openai_key), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
