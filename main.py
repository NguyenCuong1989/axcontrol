"""
Main entry point for AXCONTROL application.
"""
from typing import Dict, Any
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from config import settings
from core.decision import decide_action, DecisionInput, CtrlState
from core.decision.ui_state import UIState

# Create FastAPI app
app = FastAPI(
    title="AXCONTROL",
    description="Deterministic macOS UI Control via Accessibility (AX)",
    version="0.1.0",
)


class UIStateRequest(BaseModel):
    """Request model for UI state."""
    app_id: str
    window_id: str
    focused_id: str
    focused_role: str
    focused_label: str | None = None
    focused_bbox: tuple[int, int, int, int] | None = None
    siblings_signature: str | None = None


class CtrlStateRequest(BaseModel):
    """Request model for control state."""
    last_action: str | None = None
    last_result: str | None = None
    focus_history_signature: str | None = None
    action_count_bucket: int | None = None


class DecisionRequest(BaseModel):
    """Request model for decision engine."""
    ui_state: UIStateRequest
    ctrl_state: CtrlStateRequest


@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "name": "AXCONTROL",
        "version": "0.1.0",
        "status": "running"
    }


@app.get("/health")
async def health():
    """Health check endpoint."""
    return {"status": "healthy"}


@app.post("/api/v1/decide")
async def decide(request: DecisionRequest) -> Dict[str, Any]:
    """
    Decision engine endpoint.
    
    Takes UI state and control state, returns the next action to take.
    """
    ui_state = UIState(
        app_id=request.ui_state.app_id,
        window_id=request.ui_state.window_id,
        focused_id=request.ui_state.focused_id,
        focused_role=request.ui_state.focused_role,
        focused_label=request.ui_state.focused_label,
        focused_bbox=request.ui_state.focused_bbox,
        siblings_signature=request.ui_state.siblings_signature,
    )
    
    ctrl_state = CtrlState(
        last_action=request.ctrl_state.last_action,
        last_result=request.ctrl_state.last_result,
        focus_history_signature=request.ctrl_state.focus_history_signature,
        action_count_bucket=request.ctrl_state.action_count_bucket,
    )
    
    decision_input = (ui_state, ctrl_state)
    
    try:
        action = decide_action(decision_input)
        return {
            "status": "success",
            "action": action,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def main():
    """Launch the application."""
    uvicorn.run(
        "main:app",
        host=settings.api_host,
        port=settings.api_port,
        reload=settings.api_reload,
    )


if __name__ == "__main__":
    main()
