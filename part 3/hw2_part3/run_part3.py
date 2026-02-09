import json
from workflow import build_workflow
from state import initialize_state

def pretty(obj):
    print(json.dumps(obj, indent=2))

if __name__ == "__main__":
    app = build_workflow()

    task_text = "Write a short solution plan for HW2 Part 3 (stateful agent graph)."
    state = initialize_state(task_text)

    final_state = app.invoke(state)

    print("\n==================== FINAL RESULT ====================")
    print("Task:", final_state.get("task"))
    print("Approved:", final_state.get("approved"))
    print("Attempts:", final_state.get("attempts"))

    print("\n--- Planner Output ---")
    pretty(final_state.get("planner_output", {}))

    print("\n--- Reviewer Feedback ---")
    pretty(final_state.get("reviewer_feedback", {}))

    print("\n--- Interaction Log ---")
    for i, line in enumerate(final_state.get("interaction_log", []), start=1):
        print(f"{i}. {line}")

    print("======================================================\n")
