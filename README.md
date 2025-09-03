# Travel Assistant AI Agent

A sophisticated multi-agent travel planning system built with Google's ADK (Agent Development Kit) that helps users discover, plan, and book their dream vacations through intelligent conversation.

## Overview

The Travel Assistant is an AI-powered system that orchestrates multiple specialized agents to provide comprehensive travel services:

- **Inspiration**: Discover destinations and activities based on preferences
- **Planning**: Create detailed itineraries with flight and hotel searches
- **Booking**: Handle reservations and payment processing

## Architecture

The system follows a hierarchical multi-agent architecture:

```
Root Agent (Travel Assistant)
├── Inspiration Agent
│   ├── Place Agent (destination suggestions)
│   └── POI Agent (points of interest)
├── Planning Agent
│   ├── Itinerary Agent
│   ├── Flight Search Agent
│   ├── Flight Seat Selection Agent
│   ├── Hotel Search Agent
│   └── Hotel Room Selection Agent
└── Booking Agent
    ├── Create Reservation Agent
    ├── Payment Choice Agent
    └── Process Payment Agent
```

## Features

### 🌍 Travel Inspiration
- Personalized destination recommendations
- Activity and point-of-interest suggestions
- Integration with Google Places API for accurate location data

### 📅 Trip Planning
- Comprehensive itinerary creation
- Flight search and seat selection
- Hotel search and room selection
- Memory system to track preferences and decisions

### 💳 Booking & Payment
- Reservation creation and management
- Multiple payment options
- Secure payment processing simulation

### 🧠 Smart State Management
- Persistent user preferences and profiles
- Session state tracking
- Contextual information retention across conversations

## Project Structure

```
travel_assistant/
├── agent.py                 # Root agent configuration
├── prompt.py               # Root agent instructions
├── requirements.txt        # Python dependencies
├── common/
│   ├── constant.py        # Application constants
│   └── state.py           # State management utilities
├── sub_agents/
│   ├── inspiration/       # Travel inspiration agents
│   ├── planning/          # Trip planning agents
│   └── booking/           # Booking and payment agents
├── tools/
│   ├── memory.py          # Memory management tools
│   └── places.py          # Google Places API integration
└── resources/
    └── state.json         # Initial state configuration
```

### Example Conversations

**Inspiration Phase**:
```
User: "I love beaches and want somewhere tropical but not too touristy"
Assistant: "I'd love to help you find the perfect tropical getaway! Let me suggest some beautiful, less crowded beach destinations..."
```

**Planning Phase**:
```
User: "I want to visit Bali from Jakarta, leaving March 15th for 5 days"
Assistant: "Perfect! Let me help you plan your Bali trip. I'll search for flights and hotels..."
```

**Booking Phase**:
```
User: "I'm ready to book the hotel and flights we discussed"
Assistant: "Great! Let me help you complete your booking. I'll show you the payment options..."
```

---

*Built with Google ADK - Enabling intelligent conversational AI agents*
