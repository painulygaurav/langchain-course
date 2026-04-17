from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from tavily import TavilyClient
from langchain_tavily import TavilySearch

load_dotenv()

tavily = TavilyClient() #This will look for Tavily API key in environment variable

# below is a custom search tool, but tavily has a langchain implementation that we can use
@tool
def search(query: str) -> str:
    """
    Tool that searches over the internet
    Args:
        query: the query to search for
    Returns:
        The search result
    """
    print(f"Searching for {query}")
    return tavily.search(query=query)

llm = ChatOpenAI(model="gpt-5")
# tools = [TavilySearch()]
tools = [search]
agent = create_agent(model=llm,tools=tools)

def main():
    print("Hello from langchain-course!")
    result = agent.invoke({"messages": HumanMessage(content="search for 3 job postings for an AI engineer in langchain in Hyderabad on linkedin and list their details.")})
    print(result)


if __name__ == "__main__":
    main()
