from __future__ import annotations
from langgraph.graph import StateGraph, END

from state import GraphState
from nodes import planner_node, reviewer_node
from router import router_logic


def build_workflow():
    g = StateGraph(GraphState)

    g.add_node("planner", planner_node)
    g.add_node("reviewer", reviewer_node)

    g.set_entry_point("planner")

    # After planner, go to router decision
    g.add_conditional_edges(
        "planner",
        router_logic,
        {
            "run_planner": "planner",
            "run_reviewer": "reviewer",
            "END": END,
        },
    )

    # After reviewer, increment attempts and route again
    def bump_attempts(state: GraphState):
        return {"attempts": state.get("attempts", 0) + 1, "reviewer_feedback": state.get("reviewer_feedback", {})}

    g.add_node("attempt_counter", bump_attempts)

    g.add_edge("reviewer", "attempt_counter")

    g.add_conditional_edges(
        "attempt_counter",
        router_logic,
        {
            "run_planner": "planner",
            "run_reviewer": "reviewer",
            "END": END,
        },
    )

    return g.compile()
