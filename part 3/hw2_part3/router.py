from __future__ import annotations
from typing import Literal
from state import GraphState


def router_logic(state: GraphState) -> Literal["run_planner", "run_reviewer", "END"]:
    # increment attempts each cycle once reviewer has run
    attempts = state.get("attempts", 0)

    if state.get("approved"):
        return "END"

    # stop after 3 tries to avoid infinite loops
    if attempts >= 3:
        return "END"

    # if no planner output, run planner
    if not state.get("planner_output"):
        return "run_planner"

    # if we have planner output but not approved, run reviewer
    if state.get("planner_output") and not state.get("reviewer_feedback"):
        return "run_reviewer"

    # if reviewer rejected, reset reviewer_feedback and loop planner again
    return "run_planner"
