from langchain.agents import initialize_agent
from langchain.agents import load_tools
from pydantic import BaseModel, Field
from langchain.chains import LLMMathChain
from langchain.agents import Tool
from langchain_experimental.utilities import PythonREPL
from langchain_experimental.tools.python.tool import PythonAstREPLTool
from langchain.tools import WikipediaQueryRun
from langchain.memory import ConversationBufferMemory
from langchain.prompts import MessagesPlaceholder
from langchain.schema import SystemMessage
from langchain.llms.ai21 import AI21
from datetime import datetime
from langchain.utilities import WikipediaAPIWrapper, DuckDuckGoSearchAPIWrapper
llm = AI21(ai21_api_key='AJYixGyGITvBULVqagcBFqn0dsPfYmLY',temperature=0.1,verbose=False)

datetime_tool = Tool(
    name="Datetime",
    func=lambda x: datetime.now().isoformat(),
    description="Returns the current datetime",
)
tools=[datetime_tool]
llm_math_chain = LLMMathChain.from_llm(llm=llm, verbose=False)
tools.append(
    Tool.from_function(
        func=llm_math_chain.run,
        name="Calculator",
        description="Use this tool when you need to answer questions only about math and arithmetic",      
    )
)

python_repl = PythonREPL()
tools.append(
    Tool.from_function(
     name="python_repl",
     description="Use A Python shell. Use this to execute python commands. Input should be a valid python command. If you want to see the output of a value, you should print it out with `print(...)`.",
     func=python_repl.run,
    )
)

duck = DuckDuckGoSearchAPIWrapper(region="en-us", max_results=10)

tools.append(
    Tool.from_function(
     name="duckduckgo",
     description="Useful for finding information about a specific topic. Useful for when you need to search the internet for something another tool cannot find.",
     func=duck.run,
    )
) 
 

 