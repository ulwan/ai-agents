from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
from google.genai.types import GenerateContentConfig

from ...common.constant import Constants
from ...tools.memory import memorize
from .entity import (
    FlightsSelection,
    HotelsSelection,
    Itinerary,
    RoomsSelection,
    SeatsSelection,
    json_response_config,
)
from .prompt import (
    FLIGHT_SEARCH,
    FLIGHT_SEAT_SELECTION,
    HOTEL_ROOM_SELECTION,
    HOTEL_SEARCH,
    ITINERARY_AGENT,
    PLANNING_AGENT,
)

itinerary_agent = Agent(
    model=Constants.LLM_MODEL,
    name="itinerary_agent",
    description="Create and persist a structured JSON representation of the itinerary",
    instruction=ITINERARY_AGENT,
    disallow_transfer_to_parent=True,
    disallow_transfer_to_peers=True,
    output_schema=Itinerary,
    output_key="itinerary",
    generate_content_config=json_response_config,
)


hotel_room_selection_agent = Agent(
    model=Constants.LLM_MODEL,
    name="hotel_room_selection_agent",
    description="Help users with the room choices for a hotel",
    instruction=HOTEL_ROOM_SELECTION,
    disallow_transfer_to_parent=True,
    disallow_transfer_to_peers=True,
    output_schema=RoomsSelection,
    output_key="room",
    generate_content_config=json_response_config,
)

hotel_search_agent = Agent(
    model=Constants.LLM_MODEL,
    name="hotel_search_agent",
    description="Help users find hotel around a specific geographic area",
    instruction=HOTEL_SEARCH,
    disallow_transfer_to_parent=True,
    disallow_transfer_to_peers=True,
    output_schema=HotelsSelection,
    output_key="hotel",
    generate_content_config=json_response_config,
)


flight_seat_selection_agent = Agent(
    model=Constants.LLM_MODEL,
    name="flight_seat_selection_agent",
    description="Help users with the seat choices",
    instruction=FLIGHT_SEAT_SELECTION,
    disallow_transfer_to_parent=True,
    disallow_transfer_to_peers=True,
    output_schema=SeatsSelection,
    output_key="seat",
    generate_content_config=json_response_config,
)

flight_search_agent = Agent(
    model=Constants.LLM_MODEL,
    name="flight_search_agent",
    description="Help users find best flight deals",
    instruction=FLIGHT_SEARCH,
    disallow_transfer_to_parent=True,
    disallow_transfer_to_peers=True,
    output_schema=FlightsSelection,
    output_key="flight",
    generate_content_config=json_response_config,
)


planning_agent = Agent(
    model=Constants.LLM_MODEL,
    description="""Helps users with travel planning, complete a full itinerary for their vacation, finding best deals for flights and hotels.""",
    name="planning_agent",
    instruction=PLANNING_AGENT,
    tools=[
        AgentTool(agent=flight_search_agent),
        AgentTool(agent=flight_seat_selection_agent),
        AgentTool(agent=hotel_search_agent),
        AgentTool(agent=hotel_room_selection_agent),
        AgentTool(agent=itinerary_agent),
        memorize,
    ],
    generate_content_config=GenerateContentConfig(temperature=0.1, top_p=0.5),
)
