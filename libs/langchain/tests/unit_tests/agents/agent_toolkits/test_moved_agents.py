"""Tests for agents moved from `agent_toolkits` to `langchain_experimental`."""

import pytest

from langchain_classic.agents import agent_toolkits


@pytest.mark.parametrize(
    "name",
    [
        "create_csv_agent",
        "create_pandas_dataframe_agent",
        "create_xorbits_agent",
    ],
)
def test_moved_agent_raises_import_error_with_new_path(name: str) -> None:
    with pytest.raises(ImportError) as exc_info:
        getattr(agent_toolkits, name)

    message = str(exc_info.value)
    assert f"`langchain_classic.agents.agent_toolkits.{name}`" in message
    assert f"`langchain_experimental.agents.agent_toolkits.{name}`" in message
