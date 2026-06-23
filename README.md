# AXCONTROL

Deterministic macOS UI Control via Accessibility (AX)

## Contents
- RFC & Determinism Proof
- Public SDK Spec
- Threat Model (STRIDE)
- Mobile Control Plane Spec

Status: v1.0.0 (public)

## Quick Start

### Setup Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Configure Environment
```bash
cp .env.example .env
# Edit .env with your settings
```

### Launch Application
```bash
python main.py
```

The API will be available at http://127.0.0.1:8000
