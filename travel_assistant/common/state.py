import json
from datetime import datetime
from typing import Any, Dict

from google.adk.agents.callback_context import CallbackContext
from google.adk.sessions.state import State

from ..common.constant import Constants


def _set_initial_states(source: Dict[str, Any], target: State | dict[str, Any]):
    """
    Setting the initial session state given a JSON object of states.

    Args:
        source: A JSON object of states.
        target: The session state object to insert into.
    """
    if not target.get("system_time", None):
        target["system_time"] = str(datetime.now())

    if not target.get("itin_initialized", False):
        target["itin_initialized"] = True

        target.update(source)

        itinerary = source.get(Constants.ITIN_KEY, {})
        if itinerary:
            target[Constants.ITIN_START_DATE] = itinerary["start_date"]
            target[Constants.ITIN_END_DATE] = itinerary["end_date"]
            target[Constants.ITIN_DATETIME] = itinerary["start_date"]


def _state_intializer(callback_context: CallbackContext):
    """
    Sets up the initial state.
    Set this as a callback as before_agent_call of the root_agent.
    This gets called before the system instruction is contructed.

    Args:
        callback_context: The callback context.
    """
    data = {}
    with open(Constants.STATE_PATH, "r") as file:
        data = json.load(file)
        print(f"\nLoading Initial State: {data}\n")

    _set_initial_states(data["state"], callback_context.state)
