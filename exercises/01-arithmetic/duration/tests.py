import pytest
import student


def if_function_exists(function_name):
    return pytest.mark.skipif(function_name not in dir(student), reason=f'{function_name} not found in student module')


@if_function_exists('hours')
@pytest.mark.parametrize("duration", [0, 1, 59, 3599, 3600, 7200, 7201, 50000])
def test_hours(duration):
    actual = student.hours(duration)

    assert actual * 3600 <= duration
    assert (actual + 1) * 3600 > duration


@if_function_exists('minutes')
@pytest.mark.parametrize("duration", [0, 59, 60, 61, 578, 1234, 78912, 493929])
def test_minutes(duration):
    actual = student.minutes(duration)
    expected = (duration % 3600) // 60

    assert expected == actual, f'minutes({duration}) should return {expected} but returned {actual} instead'


@if_function_exists('seconds')
@pytest.mark.parametrize("duration", [0, 1, 59, 60, 61, 458, 785, 1678])
def test_seconds(duration):
    actual = student.seconds(duration)
    expected = duration % 60

    assert expected == actual, f'seconds({duration}) should return {expected} but returned {actual} instead'
