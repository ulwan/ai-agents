from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool

from ...common.constant import Constants
from ...tools.places import find_place_tool
from .entity import DestinationIdeas, POISuggestions, json_response_config
from .prompt import INSPIRATION_AGENT, PLACE_AGENT, POI_AGENT

place_agent = Agent(
    model=Constants.LLM_MODEL,
    name="place_agent",
    instruction=PLACE_AGENT,
    description="This agent suggests a few destination given some user preferences",
    disallow_transfer_to_parent=True,
    disallow_transfer_to_peers=True,
    output_schema=DestinationIdeas,
    output_key="place",
    generate_content_config=json_response_config,
)

poi_agent = Agent(
    model=Constants.LLM_MODEL,
    name="poi_agent",
    description="This agent suggests a few activities and points of interests given a destination",
    instruction=POI_AGENT,
    disallow_transfer_to_parent=True,
    disallow_transfer_to_peers=True,
    output_schema=POISuggestions,
    output_key="poi",
    generate_content_config=json_response_config,
)

inspiration_agent = Agent(
    model=Constants.LLM_MODEL,
    name="inspiration_agent",
    description="A travel inspiration agent who inspire users, and discover their next vacations; Provide information about places, activities, interests, etc",
    instruction=INSPIRATION_AGENT,
    tools=[AgentTool(agent=place_agent), AgentTool(agent=poi_agent), find_place_tool],
)
