from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
from google.genai.types import GenerateContentConfig

from ...common.constant import Constants
from .prompt import BOOKING_AGENT, CONFIRM_RESERVATION, PAYMENT_CHOICE, PROCESS_PAYMENT

create_reservation = Agent(
    model=Constants.LLM_MODEL,
    name="create_reservation",
    description="""Create a reservation for the selected item.""",
    instruction=CONFIRM_RESERVATION,
)


payment_choice = Agent(
    model=Constants.LLM_MODEL,
    name="payment_choice",
    description="""Show the users available payment choices.""",
    instruction=PAYMENT_CHOICE,
)

process_payment = Agent(
    model=Constants.LLM_MODEL,
    name="process_payment",
    description="""Given a selected payment choice, processes the payment, completing the transaction.""",
    instruction=PROCESS_PAYMENT,
)


booking_agent = Agent(
    model=Constants.LLM_MODEL,
    name="booking_agent",
    description="Given an itinerary, complete the bookings of items by handling payment choices and processing.",
    instruction=BOOKING_AGENT,
    tools=[
        AgentTool(agent=create_reservation),
        AgentTool(agent=payment_choice),
        AgentTool(agent=process_payment),
    ],
    generate_content_config=GenerateContentConfig(temperature=0.0, top_p=0.5),
)
