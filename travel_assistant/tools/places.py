import os
from typing import Any, Dict, List

import requests
from google.adk.tools import ToolContext

GOOGLE_PLACES_API_KEY = os.getenv("GOOGLE_PLACES_API_KEY")


def find_place_from_text(query: str) -> Dict[str, str]:
    """Fetches place details using a text query."""
    places_url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
    params = {
        "input": query,
        "inputtype": "textquery",
        "fields": "place_id,formatted_address,name",
        "key": GOOGLE_PLACES_API_KEY,
    }

    try:
        response = requests.get(places_url, params=params)
        response.raise_for_status()
        place_data = response.json()

        if not place_data.get("candidates"):
            return {"error": "No places found."}

        # Extract data for the first candidate
        place_details = place_data["candidates"][0]
        place_id = place_details["place_id"]
        place_name = place_details["name"]
        place_address = place_details["formatted_address"]

        return {
            "place_id": place_id,
            "place_name": place_name,
            "place_address": place_address,
        }

    except requests.exceptions.RequestException as e:
        return {"error": f"Error fetching place data: {e}"}


def find_place_tool(key: str, tool_context: ToolContext):
    """
    This is going to inspect the pois stored under the specified key in the state.
    One by one it will retrieve the accurate Lat/Lon from the Map API, if the Map API is available for use.

    Args:
        key: The key under which the POIs are stored.
        tool_context: The ADK tool context.

    Returns:
        The updated state with the full JSON object under the key.
    """
    if key not in tool_context.state:
        tool_context.state[key] = {}

    # The pydantic object types.POISuggestions
    if "places" not in tool_context.state[key]:
        tool_context.state[key]["places"] = []

    pois = tool_context.state[key]["places"]
    for poi in pois:  # The pydantic object types.POI
        location = poi["place_name"] + ", " + poi["address"]
        result = find_place_from_text(location)
        poi["place_id"] = result["place_id"] if "place_id" in result else None

    return {"places": pois}  # Return the updated pois
