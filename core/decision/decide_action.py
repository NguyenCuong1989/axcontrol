# core/decision/decide_action.py

from typing import Tuple, Any

from core.decision.policies import (
    policy_P0,
    policy_P1,
    policy_P2,
    policy_P3,
    policy_P4,
    policy_P5,
)
from core.decision.mapping import map_intent_to_action

DecisionInput = Tuple[Any, Any]  # (UIState_n, CtrlState_n)

def decide_action(decision_input: DecisionInput):
    """
    Deterministic decision entrypoint.
    """
    ui_state, ctrl_state = decision_input

    policies = [
        policy_P0,
        policy_P1,
        policy_P2,
        policy_P3,
        policy_P4,
        policy_P5,
    ]

    for policy in policies:
        result = policy(decision_input)
        if result is None:
            continue

        if isinstance(result, str) and result.startswith("KEY_"):
            return result

        return map_intent_to_action(
            intent=result,
            snapshot=ui_state,
            state=ctrl_state,
        )

    return None
