# hello
'''python
    User Image
   ↓
Landmark Vision Agent
   ↓
Geo Intelligence Agent
   ↓
Context Enrichment Layer
   ├── Weather Agent
   ├── Culture & Etiquette Agent
   ├── Safety & Advisory Agent
   ├── Connectivity Agent
   ↓
Preference-Aware Planning Layer
   ├── Accommodation Agent
   ├── Food & Lifestyle Agent
   ├── Transport Agent
   ↓
Route & Optimization Agent
   ↓
Experience Roadmap Agent
   ↓
Interactive Map + Travel Dossier

# 🧬 LangGraph State (Clean & Scalable)

    class TravelState(TypedDict):
    image: str
    landmark: dict
    geo: dict
    weather: dict
    culture: dict
    connectivity: dict
    preferences: dict
    accommodations: list
    attractions: list
    routes: dict
    roadmap: str
    map_data: dict


# 🔁 LangGraph Control Flow

 Vision
  ↓
Geo
  ↓
 ┌───────────────┬───────────────┬───────────────┐
Weather        Culture        Connectivity
 └───────────────┴───────────────┴───────────────┘
          ↓
Preference-Based Filtering
          ↓
Routes & Optimization
          ↓
Roadmap Synthesis



# 🌍 AI Landmark Intelligence & Travel Planner

## Overview
An agentic AI system that transforms a single image into a complete,
context-aware, preference-driven travel guide.

## Key Capabilities
- Landmark recognition from images
- Weather-aware planning
- Cultural intelligence
- Preference-based accommodation
- Optimized routing
- Interactive travel roadmap

## Architecture
Multi-agent orchestration using LangGraph with tool-augmented reasoning.

## Agent Pipeline
Vision → Geo → Context → Preferences → Optimization → Roadmap

## Sample Output
- Landmark: Eiffel Tower
- Best Time to Visit: Morning (low crowd)
- Weather Advisory: Light rain expected
- Culture Tip: Greet before interaction
- Connectivity: Excellent public transport

## Interactive Map
Generated as `map.html`

## Tech Stack
- Python
- LangGraph
- LangChain
- Vision LLM
- Mapping APIs
- Folium

## How to Run
```bash
pip install -r requirements.txt
python main.py --image sample.jpg
