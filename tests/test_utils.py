import json
import os
from unittest.mock import Mock

from src.utils import get_operations_list


def test_get_operations_list():
    mock_loads = Mock(return_value=[{"id": 1, "test": 1}])
    json.loads = mock_loads
    assert get_operations_list(
        os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.json")
    ) == [{"id": 1, "test": 1}]
    mock_loads.assert_called_once()


def test_get_operation_list_error():
    assert get_operations_list("") == []
