from core.decision.ui_state import UIState
from core.decision.ctrl_state import CtrlState


def _normalize_label(label):
    if label is None:
        return None
    return label.strip().lower()


def _normalize_bbox(bbox):
    if bbox is None:
        return None
    x, y, w, h = bbox
    return (
        int(x),
        int(y),
        int(w),
        int(h),
    )


def normalize_ui(ui_state: UIState) -> UIState:
    return UIState(
        app_id=ui_state.app_id,
        window_id=ui_state.window_id,
        focused_id=ui_state.focused_id,
        focused_role=ui_state.focused_role,
        focused_label=_normalize_label(ui_state.focused_label),
        focused_bbox=_normalize_bbox(ui_state.focused_bbox),
        siblings_signature=ui_state.siblings_signature,
    )


def normalize_ctrl(ctrl_state: CtrlState) -> CtrlState:
    return CtrlState(
        last_action=ctrl_state.last_action,
        last_result=ctrl_state.last_result,
        focus_history_signature=ctrl_state.focus_history_signature,
        action_count_bucket=ctrl_state.action_count_bucket,
    )
