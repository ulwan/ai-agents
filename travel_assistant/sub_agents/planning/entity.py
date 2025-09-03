from typing import Optional, Union

from google.genai import types
from pydantic import BaseModel, Field

json_response_config = types.GenerateContentConfig(response_mime_type="application/json")


class AttractionEvent(BaseModel):
    """An Attraction."""

    event_type: str = Field(default="visit")
    description: str = Field(
        description="A title or description of the activity or the attraction visit"
    )
    address: str = Field(description="Full address of the attraction")
    start_time: str = Field(description="Time in HH:MM format, e.g. 16:00")
    end_time: str = Field(description="Time in HH:MM format, e.g. 16:00")
    booking_required: bool = Field(default=False)
    price: Optional[str] = Field(
        description="Some events may cost money in indonesian rupiah (IDR)"
    )


class FlightEvent(BaseModel):
    """A Flight Segment in the itinerary."""

    event_type: str = Field(default="flight")
    description: str = Field(description="A title or description of the Flight")
    booking_required: bool = Field(default=True)
    departure_airport: str = Field(description="Airport code, i.e. SEA")
    arrival_airport: str = Field(description="Airport code, i.e. SAN")
    flight_number: str = Field(description="Flight number, e.g. UA5678")
    boarding_time: str = Field(description="Time in HH:MM format, e.g. 15:30")
    seat_number: str = Field(description="Seat Row and Position, e.g. 32A")
    departure_time: str = Field(description="Time in HH:MM format, e.g. 16:00")
    arrival_time: str = Field(description="Time in HH:MM format, e.g. 20:00")
    price: Optional[str] = Field(description="Total air fare in indonesian rupiah (IDR)")
    booking_id: Optional[str] = Field(description="Booking Reference ID, e.g LMN-012-STU")


class HotelEvent(BaseModel):
    """A Hotel Booking in the itinerary."""

    event_type: str = Field(default="hotel")
    description: str = Field(description="A name, title or a description of the hotel")
    address: str = Field(description="Full address of the attraction")
    check_in_time: str = Field(description="Time in HH:MM format, e.g. 16:00")
    check_out_time: str = Field(description="Time in HH:MM format, e.g. 15:30")
    room_selection: str = Field()
    booking_required: bool = Field(default=True)
    price: Optional[str] = Field(
        description="Total hotel price including all nights in indonesian rupiah (IDR)"
    )
    booking_id: Optional[str] = Field(description="Booking Reference ID, e.g ABCD12345678")


class ItineraryDay(BaseModel):
    """A single day of events in the itinerary."""

    day_number: int = Field(
        description="Identify which day of the trip this represents, e.g. 1, 2, 3... etc."
    )
    date: str = Field(description="The Date this day YYYY-MM-DD format")
    events: list[Union[FlightEvent, HotelEvent, AttractionEvent]] = Field(
        default=[], description="The list of events for the day"
    )


class Itinerary(BaseModel):
    """A multi-day itinerary."""

    trip_name: str = Field(
        description="Simple one liner to describe the trip. e.g. 'San Diego to Seattle Getaway'"
    )
    start_date: str = Field(description="Trip Start Date in YYYY-MM-DD format")
    end_date: str = Field(description="Trip End Date in YYYY-MM-DD format")
    origin: str = Field(description="Trip Origin, e.g. San Diego")
    destination: str = Field(description="Trip Destination, e.g. Seattle")
    days: list[ItineraryDay] = Field(default_factory=list, description="The multi-days itinerary")


class Room(BaseModel):
    """A room for selection."""

    is_available: bool = Field(description="Whether the room type is available for selection.")
    price_in_rp: int = Field(
        description="The cost of the room selection in indonesian rupiah (IDR)."
    )
    room_type: str = Field(
        description="Type of room, e.g. Twin with Balcon, King with Ocean View... etc."
    )


class RoomsSelection(BaseModel):
    """A list of rooms for selection."""

    rooms: list[Room]


class Hotel(BaseModel):
    """A hotel from the search."""

    name: str = Field(description="Name of the hotel")
    address: str = Field(description="Full address of the Hotel")
    check_in_time: str = Field(description="Time in HH:MM format, e.g. 16:00")
    check_out_time: str = Field(description="Time in HH:MM format, e.g. 15:30")
    price: int = Field(description="Price of the room per night in indonesian rupiah (IDR)")


class HotelsSelection(BaseModel):
    """A list of hotels from the search."""

    hotels: list[Hotel]


class Seat(BaseModel):
    """A Seat from the search."""

    is_available: bool = Field(description="Whether the seat is available for selection.")
    price_in_rp: int = Field(
        description="The cost of the seat selection in indonesian rupiah (IDR)."
    )
    seat_number: str = Field(description="Seat number, e.g. 22A, 34F... etc.")


class SeatsSelection(BaseModel):
    """A list of seats from the search."""

    seats: list[list[Seat]]


class AirportEvent(BaseModel):
    """An Airport event."""

    city_name: str = Field(description="Name of the departure city")
    airport_code: str = Field(description="IATA code of the departure airport")
    timestamp: str = Field(description="ISO 8601 departure or arrival date and time")


class Flight(BaseModel):
    """A Flight search result."""

    flight_number: str = Field(
        description="Unique identifier for the flight, like BA123, AA31, etc."
    )
    departure: AirportEvent
    arrival: AirportEvent
    airlines: list[str] = Field(description="Airline names, e.g., American Airlines, Emirates")
    price_in_rp: int = Field(description="Flight price in indonesian rupiah (IDR)")
    number_of_stops: int = Field(description="Number of stops during the flight")


class FlightsSelection(BaseModel):
    """A list of flights from the search."""

    flights: list[Flight]
