# tests/test_chatbot_flow.py
import pytest
from app.services.chatbot import handle_chatbot_query

@pytest.mark.asyncio
async def test_sipitori_flow():
    result = await handle_chatbot_query("Ke nyaka go tseba gore ke safe ka condom.", source_lang="sipitori", target_lang="sipitori")
    assert "condom" in result.lower() or "clinic" in result.lower()
