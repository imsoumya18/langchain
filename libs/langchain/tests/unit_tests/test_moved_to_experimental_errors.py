"""Tests for the `ImportError` messages of code moved to `langchain_experimental`."""

import importlib

import pytest

SECURITY_POLICY_URL = "https://docs.langchain.com/oss/python/security-policy"
REMOVED_LINKS = (
    "blob/master/SECURITY.md",
    "discussions/11680",
)


@pytest.mark.parametrize(
    ("module_name", "attribute"),
    [
        ("langchain_classic.tools", "PythonAstREPLTool"),
        ("langchain_classic.tools", "PythonREPLTool"),
        ("langchain_classic.tools.python", "PythonREPLTool"),
        ("langchain_classic.agents", "create_csv_agent"),
        ("langchain_classic.agents.agent_toolkits.csv", "create_csv_agent"),
        (
            "langchain_classic.agents.agent_toolkits.pandas",
            "create_pandas_dataframe_agent",
        ),
        (
            "langchain_classic.agents.agent_toolkits.spark",
            "create_spark_dataframe_agent",
        ),
        ("langchain_classic.agents.agent_toolkits.xorbits", "create_xorbits_agent"),
        ("langchain_classic.agents.agent_toolkits.python", "create_python_agent"),
    ],
)
def test_moved_to_experimental_error_has_no_dead_links(
    module_name: str, attribute: str
) -> None:
    module = importlib.import_module(module_name)
    with pytest.raises((ImportError, AttributeError)) as exc_info:
        getattr(module, attribute)

    message = str(exc_info.value)
    assert "langchain_experimental" in message
    for dead_link in REMOVED_LINKS:
        assert dead_link not in message
    # Any URL must stand alone so it stays clickable, and must be the docs link.
    urls = [word for word in message.split() if word.startswith("http")]
    assert all(url == SECURITY_POLICY_URL for url in urls)
