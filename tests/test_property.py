from hypothesis import given
import hypothesis.strategies as st
import pytest
from src.tasks import search_tasks

@given(st.lists(st.dictionaries(keys=st.text(), values=st.text())))
def test_search_function_stability(random_tasks):
    try:
        search_tasks(random_tasks, "test")
    except Exception:
        pytest.fail("Search raised an exception unexpectedly")
