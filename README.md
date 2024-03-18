# Chatstodo ML Functions

The Chat Analysis Service is a gRPC-based application designed to analyze chat messages using OpenAI's GPT-3.5 Turbo. It summarizes chat messages, extracts tasks, and identifies events, providing a comprehensive overview of the chat content.

## What's Completed

- **Protobuf Schema**: Defined for `UserChatRequest` and `ChatAnalysisResponse` to structure the request and response data.
- **gRPC Code Generation**: Generated the necessary `pb2` and `pb2_grpc` files from the protobuf schema.
- **OpenAI Helper**: Implemented `openai_helper.py` to interact with OpenAI's API for processing chat messages.
- **gRPC Server**: Created `server.py` to set up the gRPC server and handle incoming requests.
- **Dependencies**: Listed all necessary dependencies in `requirements.txt` for easy installation.

## Setup

### Cloning the Repository

To get started, clone this repository to your local machine:

```bash
git clone https://github.com/lucasodra/chatstodo-ml-functions.git
cd chat-analysis-service
```

### Virtual Environment Setup

Install virtualenv if you don't have it

```bash
pip install virtualenv
```

Create a virtual environment

```bash
virtualenv venv
```

Activate the virtual environment

```bash
# On Windows
venv\Scripts\activate

# On Unix or MacOS
source venv/bin/activate
```

### Dependencies

With the virtual environment activated, install the project dependencies.

```bash
pip install -r requirements.txt
```

### Environment Variables

Copy the `.env.example` file to `.env` and fill in your OPenAI API key.

```bash
cp .env.example .env
# Edit .env to add your OpenAI API key
```
