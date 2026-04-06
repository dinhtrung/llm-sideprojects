from langgraph.pregel import Pregel

from finance_flow.graph import flow


def test_graph_compiles() -> None:
    assert isinstance(flow, Pregel)

