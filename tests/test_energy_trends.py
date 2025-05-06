import pytest

from energy_data import (
    DataGeneratorFactory,
    DailyDataGenerator,
    WeeklyDataGenerator,
    MonthlyDataGenerator,
)

@pytest.fixture
def factory():
    return DataGeneratorFactory()

@pytest.mark.parametrize(
    "period, cls, expected_len, min_val, max_val",
    [
        ("daily",   DailyDataGenerator,   24,  100,  300),
        ("weekly",  WeeklyDataGenerator,   7,   800, 1500),
        ("monthly", MonthlyDataGenerator, 30, 1000, 3000),
    ]
)
def test_factory_and_generator(period, cls, expected_len, min_val, max_val, factory):
    gen = factory.create(period)
    assert isinstance(gen, cls)
    data = gen.generate()
    assert isinstance(data, list)
    assert len(data) == expected_len
    assert all(isinstance(v, int) for v in data)
    assert all(min_val <= v <= max_val for v in data)

def test_factory_invalid_period_raises(factory):
    with pytest.raises(ValueError) as excinfo:
        factory.create("yearly")
    assert "Invalid period" in str(excinfo.value)