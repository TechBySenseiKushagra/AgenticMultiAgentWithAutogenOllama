# AgenticMultiAgentWithAutogenOllama
Building Agentic Multi-Agent System with AutoGen and Ollama

## Setup Instructions
1. Install Ollama
    -   Visit https://ollama.com/ for installation files.
    ``` 
    ollama pull llama3:latest
    ollama serve
    ```
2.  Clone the repository
    ``` 
    git clone <repo url>
    cd AgenticMultiAgentWithAutogenOllama
    ```
3.  Create a virtual environment
    ```
    python -m venv myenv
    ```

4.  Activate the virtual environment
    - On Windows:
        ``` myenv\Scripts\activate ```
    - On macOS/Linux:
        ``` source myenv/bin/activate ```

5.  Install dependencies
    ```
    pip install -r requirements.txt
    ```

6. Run the application 
    ```
    python main.py
    ```


## Application Output
    ```
    --------------------------------------------------
    Planner (to chat_manager):

    What are the best countries to live in the world and also research which country is less impacted with AI Influence

    --------------------------------------------------------------------

    Next speaker: ResearcherAgent

    ResearcherAgent (to chat_manager):

    **Best Countries to Live In:**

    According to various sources such as the United Nations Development Programme (UNDP), the Human Development Index (HDI), and Mercer's Quality of Living Survey, some of the best countries to live in are:

    1. Norway: Known for its high standard of living, excellent education system, and strong social safety net.
    2. Switzerland: Famous for its neutral politics, high standard of living, and stunning natural beauty.
    3. Denmark: Renowned for its social cohesion, low crime rate, and high level of civic engagement.
    4. Finland: Praised for its excellent education system, innovative economy, and stunning natural landscapes.
    5. Canada: Admired for its diversity, tolerance, and high standard of living.
    6. Sweden: Known for its progressive politics, strong social safety net, and stunning natural beauty.
    7. New Zealand: Famous for its breathtaking natural landscapes, friendly locals, and high standard of living.
    8. Australia: Praised for its laid-back attitude, stunning beaches, and high standard of living.

    **Least Impacted by AI Influence:**

    According to a report by the World Economic Forum (WEF), some countries that are less impacted by AI influence are:

    1. Bhutan: A small Himalayan kingdom with a strong focus on sustainable development and cultural preservation.
    2. Nepal: A country with a relatively low level of technological adoption, but rich in natural resources and cultural heritage.
    3. Papua New Guinea: A country with a unique culture and limited technological infrastructure, making it less susceptible to AI influence.
    4. Vanuatu: An island nation with a strong focus on traditional ways of life and limited exposure to AI-driven technologies.
    5. Mongolia: A country with a nomadic culture and limited urbanization, making it less impacted by AI-driven changes.

    Please note that this is not an exhaustive list, and the impact of AI can vary greatly depending on various factors such as economic development, education levels, and government policies.    

    RESEARCH COMPLETE

    --------------------------------------------------------------------

    Next speaker: SummarizerAgent

    SummarizerAgent (to chat_manager):

    Here's a summary of the best countries to live in and those least impacted by AI influence:

    **Best Countries to Live In:**

    The top countries to live in are Norway, Switzerland, Denmark, Finland, Canada, Sweden, New Zealand, and Australia. These nations offer high standards of living, excellent education systems, stunning natural beauty, and strong social safety nets.

    **Least Impacted by AI Influence:**

    Countries that are less impacted by AI influence include Bhutan, Nepal, Papua New Guinea, Vanuatu, and Mongolia. These countries have limited technological adoption, strong cultural preservation, and unique traditional ways of life, making them less susceptible to AI-driven changes.

    TERMINATE

    --------------------------------------------------------------------

    Next speaker: ResearcherAgent

    ResearcherAgent (to chat_manager):

    **TERMINATED**

    I've completed the research and provided the concise information you requested. The summary highlights the best countries to live in, featuring nations with high standards of living, excellent education systems, and stunning natural beauty. Additionally, it identifies countries that are less impacted by AI influence, including nations with limited technological adoption, strong cultural preservation, and unique traditional ways of life.

    Now that my research is complete, I'm ready to terminate our session.


    --------------------------------------------------------------------

    Next speaker: ResearcherAgent

    ResearcherAgent (to chat_manager):

    **TERMINATION CONFIRMED**

    --------------------------------------------------------------------

    Next speaker: ResearcherAgent

    ResearcherAgent (to chat_manager):



    --------------------------------------------------------------------

    Next speaker: SummarizerAgent

    SummarizerAgent (to chat_manager):

    I see what you did there! Well played, researcher!

    Indeed, your summary provides a clear and concise overview of the best countries to live in and those least impacted by AI influence. It's been a pleasure assisting you in compiling this information.

    Now that our session has been terminated, I'll just sit back and wait for the next research request...

    --------------------------------------------------------------------


    ```
