from langgraph.graph import StateGraph
from app.planner_agent import create_slide_plan
from app.ppt_generator import generate_ppt
from app.validator import validate_plan
from app.chart_agent import create_chart_plan
from typing import TypedDict
import os,json


class State(TypedDict):
    prompt: str
    plan: dict

def plan_slides(state):

    plan = create_slide_plan(state["prompt"])

    state["plan"] = plan

    return state


def plan_charts(state):

    plan = create_chart_plan(state["plan"])

    os.makedirs("artifacts", exist_ok=True)

    with open("artifacts/slide_plan.json", "w") as f:
        json.dump(plan, f, indent=2)

    state["plan"] = plan

    return state


def validate(state):

    state["plan"] = validate_plan(state["plan"])

    return state


def generate(state):
    generate_ppt(state["plan"])
    return state

graph = StateGraph(State)

graph.add_node("slide_planner", plan_slides)
graph.add_node("chart_planner", plan_charts)
graph.add_node("validator", validate)
graph.add_node("generator", generate)

graph.set_entry_point("slide_planner")

graph.add_edge("slide_planner", "chart_planner")
graph.add_edge("chart_planner", "validator")
graph.add_edge("validator", "generator")

workflow = graph.compile()