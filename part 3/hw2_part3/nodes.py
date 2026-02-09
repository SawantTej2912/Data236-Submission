from __future__ import annotations
from typing import Any, Dict
from state import GraphState


def planner_node(state: GraphState) -> Dict[str, Any]:
    log = state.get("interaction_log", [])
    log.append("Planner: start")

    # Minimal planner output (can be LLM later)
    proposal = {
        "plan": f"Plan for task: {state.get('task', '')}",
        "steps": [
            "Identify requirements",
            "Propose a solution",
            "Validate constraints",
        ],
    }

    log.append("Planner: complete")
    return {"planner_output": proposal, "interaction_log": log}


def reviewer_node(state: GraphState) -> Dict[str, Any]:
    log = state.get("interaction_log", [])
    log.append("Reviewer: start")

    proposal = state.get("planner_output", {})
    plan_text = (proposal.get("plan") or "").lower()

    # Simple “validation rule” to demonstrate review + loop
    # (You can make this stricter based on HW prompt.)
    approved = "task" in plan_text and len(proposal.get("steps", [])) >= 3

    feedback = {
        "approved": approved,
        "notes": "Looks good." if approved else "Needs more detail (at least 3 steps + mention task).",
    }

    log.append("Reviewer: complete")
    return {"reviewer_feedback": feedback, "approved": approved, "interaction_log": log}
