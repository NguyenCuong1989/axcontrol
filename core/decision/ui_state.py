class UIState:
    def __init__(
        self,
        app_id,
        window_id,
        focused_id,
        focused_role,
        focused_label,
        focused_bbox,
        siblings_signature,
    ):
        self.app_id = app_id
        self.window_id = window_id
        self.focused_id = focused_id
        self.focused_role = focused_role
        self.focused_label = focused_label
        self.focused_bbox = focused_bbox
        self.siblings_signature = siblings_signature
