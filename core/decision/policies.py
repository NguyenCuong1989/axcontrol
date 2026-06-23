# core/decision/policies.py

"""
Deterministic policy layer.
Each policy returns:
- None            → not applicable
- intent (str)    → mapped later
- action (KEY_*)  → direct action
"""

def policy_P0(decision_input):
    # HARD STOP conditions
    ui_state, ctrl_state = decision_input

    if ctrl_state.action_count_bucket is not None and ctrl_state.action_count_bucket >= 50:
        return "STOP"

    if ctrl_state.last_result == "TIMEOUT":
        return "STOP"

    return None


def policy_P1(decision_input):
    # Direct select when focused element is clearly selectable
    ui_state, _ = decision_input

    if ui_state.focused_role in {"AXButton", "AXMenuItem", "AXListItem"}:
        if ui_state.focused_label:
            return "SELECT"

    return None


def policy_P2(decision_input):
    # Default forward navigation
    return "NAVIGATE_NEXT"


def policy_P3(decision_input):
    # Backward navigation fallback (handled after NO-OP)
    ui_state, ctrl_state = decision_input

    if ctrl_state.last_action == "KEY_TAB" and ctrl_state.last_result == "NO_OP":
        return "NAVIGATE_PREV"

    return None


def policy_P4(decision_input):
    # Ambiguity → defer to higher-level strategy (LLM later)
    ui_state, _ = decision_input

    if ui_state.focused_label in {"ok", "yes", "submit"}:
        return "SELECT"

    return None


def policy_P5(decision_input):
    # Final fallback: STOP deterministically
    return None
