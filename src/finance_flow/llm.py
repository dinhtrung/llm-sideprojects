from langchain_core.tracers import ConsoleCallbackHandler
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    base_url="http://localhost:8080/v1",
    model="unsloth/gemma-4-E4B-it-GGUF:Q4_K_M",
    temperature=0.5,
    api_key="not-needed-for-local-inference",
    callbacks=[ConsoleCallbackHandler()] # for debugging purpose
)
