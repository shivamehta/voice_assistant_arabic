# Standard library
from typing import Dict, List

# Third-party
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from langchain_community.tools import DuckDuckGoSearchRun
import httpx  # Or use `requests` if preferred

# LiveKit SDK & plugins
from livekit import agents
from livekit.agents import (
    Agent,
    AgentSession,
    JobContext,
    RoomInputOptions,
    RunContext,
    WorkerOptions,
    cli,
    function_tool,
)
from livekit.plugins import google, groq, silero
from livekit.plugins.turn_detector.multilingual import MultilingualModel

# Local imports
from prompts import SYSTEM_PROMPT, SYSTEM_PROMPT_OG
from tools import lookup_important_numbers


load_dotenv(".env.local")

class Assistant(Agent):
    """
    A custom voice assistant agent that uses a system prompt and specified tools.

    Inherits from:
        Agent (livekit.agents.Agent): Base class for LiveKit voice agents.

    Attributes:
        instructions (str): Initial prompt to guide the agent's behavior.
        tools (list): List of tools available for the agent to use during interaction.
    """
    def __init__(self) -> None:
        #super().__init__(instructions="You are a helpful voice AI assistant.")
        super().__init__(instructions=SYSTEM_PROMPT_OG,tools=[lookup_important_numbers])


async def entrypoint(ctx: agents.JobContext):
    """
    The main entry point for the LiveKit worker.

    Initializes the AgentSession with TTS, LLM, STT, and VAD components,
    and starts a conversation with the custom Assistant agent.

    Args:
        ctx (agents.JobContext): The job context provided by the LiveKit framework.
    """
    session = AgentSession(
        tts=groq.TTS(model="playai-tts-arabic",voice="Khalid-PlayAI"),

        #llm=groq.LLM(model="openai/gpt-oss-120b",temperature=0.9,max_completion_tokens=250),
        llm=google.beta.realtime.RealtimeModel(
        model="gemini-2.0-flash-exp",
        voice="Puck",
        temperature=0.8,
        max_output_tokens=500
    ),
        
        #stt=groq.STT(model="whisper-large-v3-turbo",language="en"), #For English
        stt = groq.STT(model="whisper-large-v3-turbo", language="ar"), #For Arabic
        vad=silero.VAD.load(),
         )

    await session.start(
        room=ctx.room,
        agent=Assistant(),
       
    )

    await session.generate_reply(
        instructions="""Begin by warmly and politely welcoming the user in the Omani dialect. Introduce yourself as a smart voice assistant specialized in mental health support, and explain that you're here to listen and help. Assure them that everything shared is respected and kept confidential. Gently ask: How can I assist you today?"""
    )


if __name__ == "__main__":
    """
    Runs the LiveKit voice assistant app using the provided entrypoint function.
    """
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))