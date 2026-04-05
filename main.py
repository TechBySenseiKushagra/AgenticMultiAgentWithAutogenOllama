from autogen import AssistantAgent, UserProxyAgent
from autogen.agentchat.groupchat import GroupChat, GroupChatManager

# Define LLM configuration for Ollama
llm_config = {
    "config_list": [
        {
            "model": "llama3:latest",  # or any other model you have installed
            "base_url": "http://localhost:11434/v1",
            "api_key": "ollama",  # Ollama doesn't need a real API key, but AutoGen requires this field
            "price": [0, 0]
        }
    ],
    "temperature": 0.5,
}

# Define the Researcher Agent
researcher = AssistantAgent(
    name="ResearcherAgent",
    llm_config=llm_config,
    system_message="""You are a researcher. Provide concise information on the given topic. 
    Focus on finding relevant and accurate information about the subject matter.
    After providing your research, say 'RESEARCH COMPLETE' to indicate you're done."""
)

# Define the Summarizer Agent
summarizer = AssistantAgent(
    name="SummarizerAgent",
    llm_config=llm_config,
    system_message="""You are a summarizer. Take the information provided by the researcher 
    and create a clear, concise summary highlighting the key points.
    After completing your summary, end your message with 'TERMINATE' to end the conversation."""
)

# Define the Planner Agent (User Proxy)
planner = UserProxyAgent(
    name="Planner",
    human_input_mode="NEVER",
    llm_config=llm_config,
    system_message="""You are a planner. Coordinate the workflow between the researcher and summarizer.
    Once you receive the final summary, try to analyse the summary and if you are still not happy, try to reinitate the process, once you are happy, then, reply with 'TERMINATE' to end the conversation and return the response""",
    code_execution_config=False,
    is_termination_msg=lambda x: x.get("content", "").strip().endswith("TERMINATE")
)

# Create a group chat with the agents
groupchat = GroupChat(
    agents=[planner, researcher, summarizer],
    messages=[],
    max_round=20,
    speaker_selection_method="auto"
)

# Create a group chat manager
manager = GroupChatManager(
    groupchat=groupchat,
    llm_config=llm_config
)

# Start the conversation
if __name__ == "__main__":
    print("Starting AI Education Research with Ollama...")
    print("Make sure Ollama is running with: ollama serve")
    print("-" * 50)
    
    try:
        planner.initiate_chat(
            manager,
            message="What are the best countries to live in the world and also research which country is less impacted with AI Influence",
        )
    except Exception as e:
        print(f"Error: {e}")