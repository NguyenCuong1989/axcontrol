class CtrlState:
    def __init__(
        self,
        last_action,
        last_result,
        focus_history_signature,
        action_count_bucket,
    ):
        self.last_action = last_action
        self.last_result = last_result
        self.focus_history_signature = focus_history_signature
        self.action_count_bucket = action_count_bucket
