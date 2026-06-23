"""
Mapping layer: converts intents to concrete actions.
"""
from typing import Any, Dict


def map_intent_to_action(intent: str, snapshot: Any, state: Any) -> Dict[str, Any]:
    """
    Map a high-level intent to a concrete action.
    
    Args:
        intent: The high-level intent (e.g., "SELECT", "NAVIGATE_NEXT")
        snapshot: Current UI state snapshot
        state: Current control state
        
    Returns:
        Dictionary representing the action to execute
    """
    action_map = {
        "SELECT": {"type": "click", "target": "focused"},
        "NAVIGATE_NEXT": {"type": "key", "key": "TAB"},
        "NAVIGATE_PREV": {"type": "key", "key": "TAB", "modifiers": ["SHIFT"]},
        "STOP": {"type": "stop"},
    }
    
    return action_map.get(intent, {"type": "noop"})
