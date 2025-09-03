from google.adk.agents import Agent

from .common.constant import Constants
from .common.state import _state_intializer
from .prompt import ROOT_AGENT
from .sub_agents.booking.agent import booking_agent
from .sub_agents.inspiration.agent import inspiration_agent
from .sub_agents.planning.agent import planning_agent

root_agent = Agent(
    model=Constants.LLM_MODEL,
    name="root_agent",
    description="Travel Assistant Service for multiple sub-agents",
    instruction=ROOT_AGENT,
    sub_agents=[inspiration_agent, planning_agent, booking_agent],
    before_agent_callback=_state_intializer,
)
