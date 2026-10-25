import importlib.util
from pathlib import Path

# Lightweight static test: ensure the app contains the key tasks and local Ollama endpoint.
APP = Path(__file__).resolve().parents[1] / "app.py"
source = APP.read_text(encoding="utf-8")

def test_local_ollama_endpoint_is_used():
    assert "/api/chat" in source
    assert "localhost:11434" in source

def test_all_four_workflows_are_present():
    for task in [
        "Create a study pack",
        "Make a quick summary",
        "Generate revision questions",
        "Create an action checklist",
    ]:
        assert task in source

def test_supported_upload_types_are_text_only():
    assert 'type=["txt", "md"]' in source
