from dotenv import load_dotenv
from langchain.callbacks.streaming_aiter import AsyncIteratorCallbackHandler
from langchain.schema import HumanMessage
from langchain.llms import HuggingFaceHub
import asyncio
import sys

load_dotenv()

handler = AsyncIteratorCallbackHandler()
llm = HuggingFaceHub(
    repo_id="google/flan-t5-large",
    model_kwargs={"temperature": 0},
    streaming=True,
    callbacks=[handler],
)


async def consumer():
    iterator = handler.aiter()
    async for item in iterator:
        sys.stdout.write(item)
        sys.stdout.flush()

if __name__ == '__main__':
    message = "What is AI?"
    loop = asyncio.get_event_loop()
    loop.create_task(llm.agenerate(message=[
        [
            HumanMessage(content=message)
        ]
    ]))
    loop.create_task(consumer())
    loop.run_forever()
    loop.close()
