from __future__ import annotations
from typing import TypedDict, Dict, Any, List


class GraphState(TypedDict, total=False):
    task: str
    planner_output: Dict[str, Any]
    reviewer_feedback: Dict[str, Any]
    approved: bool
    attempts: int
    interaction_log: List[str]


def initialize_state(task: str) -> GraphState:
    return GraphState(
        task=task,
        planner_output={},
        reviewer_feedback={},
        approved=False,
        attempts=0,
        interaction_log=[],
    )
