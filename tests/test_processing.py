import pytest

from src.processing import (
    filter_by_state,
    sort_by_date,
)


@pytest.fixture()
def get_list():
    return [
        {"id": 41428829, "state": "ИСПОЛНЕНО", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "ИСПОЛНЕНО", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "ОТМЕНЕНО", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "ОТМЕНЕНО", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.mark.parametrize(
    "state, expected",
    [
        (
            "ИСПОЛНЕНО",
            [
                {"id": 41428829, "state": "ИСПОЛНЕНО", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "ИСПОЛНЕНО", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            "ОТМЕНЕНО",
            [
                {"id": 594226727, "state": "ОТМЕНЕНО", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "ОТМЕНЕНО", "date": "2018-10-14T08:21:33.419441"},
            ],
        ),
        ("EXECUTED", []),
    ],
)
def test_filter_by_state(get_list, state, expected):
    assert filter_by_state(get_list, state) == expected


@pytest.fixture()
def get_operations():
    return [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    ]


@pytest.mark.parametrize(
    "order, expected",
    [
        (
            "asc",
            [
                {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
                {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            ],
        ),
        (
            "desc",
            [
                {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
                {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            ],
        ),
    ],
)
def test_sort_by_date(get_operations, order, expected):
    assert sort_by_date(get_operations, order) == expected


def test_sort_by_date_invalid_order(get_operations):
    with pytest.raises(ValueError):
        sort_by_date(get_operations, 1)
