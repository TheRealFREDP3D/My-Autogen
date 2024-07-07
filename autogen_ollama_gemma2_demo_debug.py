""" 
┌──────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ autogen_ollama_gemma2_demo_debug.py                                                                              │
│-================================================================================================================-│
│                                                                                                                  │
│ Python 3.x.x                                                                                                     │ 
│ Author: Frederick Pellerin                                                                                       │ 
│ Email: fredp3d@proton.me                                                                                         │ 
│ X/Github/Medium: @TheRealFredP3D                                                                                 │ 
│                                                                                                                  │
│-================================================================================================================-│
│                                                                                                                  │   
│ This script demonstrate how to make Autogen agent works using open-source LLM models with local Ollama server.   │
│                                                                                                                  │
│-================================================================================================================-│
│                                                                                                                  │
│ In this case, the model is Gemma2 served by a local Ollama server.                                               │
│ The test is successful and here is the code to make it run.                                                      │
│ I added error handling and logging for debugging.                                                                │
│                                                                                                                  │
│-================================================================================================================-│
│                                                                                                                  │
│ Workflow                                                                                                         │
│                                                                                                                  │
│ Agent #1 - Assistant: Create a script to fetch the data and plot a chart of NVDA and TESLA price change YTD.     │
│ Agent #2 - User Proxy: Write the script in the ./coding directory and execute it.                                │
│                                                                                                                  │
│-================================================================================================================-│
│                                                                                                                  │
│ WARNING: When asked, be sure to check the generated code before continuing to ensure it is safe to run.          │
│                                                                                                                  │
└──────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
"""


import os
import autogen
from autogen import AssistantAgent, UserProxyAgent
import logging

# Configure logging
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

# LLM model config
config_list = [
    {
        "model": "gemma2:latest",
        "base_url": "http://127.0.0.1:11434/v1",
        "api_key": "ollama",
    }
]
# AssistantAgent config 
try:
    assistant = AssistantAgent("assistant", llm_config={"config_list": config_list})
except Exception as e:
    print(f"Error creating AssistantAgent: {e}")

# UserProxyAgent config
try:
    user_proxy = UserProxyAgent(
        "user_proxy", code_execution_config={"executor": autogen.coding.LocalCommandLineCodeExecutor(work_dir="coding")}
    )
except Exception as e:
    print(f"Error creating UserProxyAgent: {e}")

# Start the chat
try:
    user_proxy.initiate_chat(
        assistant,
        message="Plot a chart of NVDA and TESLA stock price change YTD.",
    )
except Exception as e:
    print(f"Error initiating chat: {e}")
""" 
┌──────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                                                                                                  │
│                        ┌──────────────────────────────────────────────────────────────────────────┐              │
│                        │                  ORIGINAL CODE FROM AUTOGEN DOCUMENTATION                │              │
│                        └──────────────────────────────────────────────────────────────────────────┘              │
│                                                                                                                  │
│-================================================================================================================-│
│                                                                                                                  │
│ from autogen import AssistantAgent, UserProxyAgent                                                               │
│ config_list = [                                                                                                  │
│     {                                                                                                            │                                                                            │
│         "model": "codellama",                                                                                    │
│         "base_url": "http://localhost:11434/v1",                                                                 │
│         "api_key": "ollama",                                                                                     │
│     }                                                                                                            │
│ ]                                                                                                                │
│                                                                                                                  │
│ assistant = AssistantAgent("assistant", llm_config={"config_list": config_list})                                 │
│                                                                                                                  │
│ user_proxy = UserProxyAgent("user_proxy", code_execution_config={"work_dir": "coding", "use_docker": False})     │
│ user_proxy.initiate_chat(assistant, message="Plot a chart of NVDA and TESLA stock price change YTD.")            │
│                                                                                                                  │
└──────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
"""