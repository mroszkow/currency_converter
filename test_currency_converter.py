import pytest
from unittest import mock


from currency_converter import get_rate, convert


def test_get_rate_success(mock_requests_get):
    mock_response = mock.MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {'rates': [{'mid': 1.23}]}
    mock_requests_get.return_value = mock_response

    rate = get_rate('USD')

    assert rate == 1.23


def test_get_rate_invalid_code(mock_requests_get):
    mock_response = mock.MagicMock()
    mock_response.status_code = 404
    mock_requests_get.return_value = mock_response

    with pytest.raises(ValueError):
        get_rate('XYZ')


def test_convert(mock_get_rate):
    mock_get_rate.return_value = 1.23

    result = convert(10.0, 'USD')

    assert result == 12.30


@pytest.fixture
def mock_requests_get():
    with mock.patch('currency_converter.requests.get') as mock_get:
        yield mock_get


@pytest.fixture
def mock_get_rate():
    with mock.patch('currency_converter.get_rate') as mock_rate:
        yield mock_rate