from .health import *
import pytest


class TestHealth:
    @pytest.mark.asyncio
    async def test_health(self):
        response = await health()
        assert response == {"status": "OK"}
