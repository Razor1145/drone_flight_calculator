import pytest

from flight_calculator import calculate_flight_time, flight_time_table


@pytest.mark.parametrize(
    ("weight_grams", "expected"),
    [
        (0, 180.0),
        (1, 179.9),
        (100, 170.0),
        (500, 130.0),
        (900, 90.0),
        (1800, 0.0),
        (2000, 0.0),
    ],
)
def test_calculate_flight_time_returns_expected_values(weight_grams, expected):
    assert calculate_flight_time(weight_grams) == pytest.approx(expected)


def test_calculate_flight_time_rejects_negative_weight():
    with pytest.raises(ValueError, match="Weight cannot be negative."):
        calculate_flight_time(-0.1)


@pytest.mark.parametrize("weight_grams", [0, 1000, 5000])
def test_calculate_flight_time_never_returns_negative(weight_grams):
    assert calculate_flight_time(weight_grams) >= 0


@pytest.mark.parametrize(
    ("max_weight_grams", "step_grams", "expected"),
    [
        (0, 1, [(0, 180.0)]),
        (10, 5, [(0, 180.0), (5, 179.5), (10, 179.0)]),
        (20, 10, [(0, 180.0), (10, 179.0), (20, 178.0)]),
    ],
)
def test_flight_time_table_returns_expected_values(max_weight_grams, step_grams, expected):
    assert flight_time_table(max_weight_grams, step_grams) == expected


def test_flight_time_table_with_positive_step_and_zero_max():
    assert flight_time_table(0, 1) == [(0, 180.0)]


@pytest.mark.parametrize(
    ("max_weight_grams", "step_grams"),
    [
        (-1, 1),
        (10, 0),
        (10, -2),
    ],
)
def test_flight_time_table_rejects_invalid_inputs(max_weight_grams, step_grams):
    with pytest.raises(ValueError, match="Max weight must be non-negative and step must be positive."):
        flight_time_table(max_weight_grams, step_grams)