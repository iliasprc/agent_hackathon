# ./adk_agent_samples/mcp_agent/agent.py
from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters
from pathlib import Path
from src.prompts import SYSTEM_PROMPT
from src.config import GEMINI_MODEL

root_agent = LlmAgent(
    model=GEMINI_MODEL,
    name="orchistrator_agent",
    instruction=SYSTEM_PROMPT,
    tools=[
    #     MCPToolset(
    #         connection_params=StdioServerParameters(
    #             command="uv",
    #             args=[
    #                 "--directory",
    #                 f"{Path({$tool_file_path}.__file__).parent}/",
    #                 "run",
    #                 f"{Path({$tool_file_path}.__file__).name}",
    #             ],
    #         ),
    #     ),
    ],
    sub_agents=[],
)
