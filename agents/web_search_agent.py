from langchain.agents import Tool 
from langchain.tools.ddg_search.tool import DuckDuckGoSearchResults

# 📡 Web Search Tool for Real-Time Financial Insights
web_search_tool = Tool(
    name="Web Search",
    func=DuckDuckGoSearchResults().run,
    description=(
        "Useful for performing live web searches using DuckDuckGo when the agent "
        "needs to fetch the most recent and relevant information, such as breaking news, "
        "financial market updates, company reports, or economic events not available in static data. "
        "Ideal when answering questions that require current context or trending developments."
    )
)
