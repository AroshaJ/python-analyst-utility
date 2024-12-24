import pytest
from python_analyst_utils.date_management.date_manager import DateFormatDetector


@pytest.mark.parametrize(
    "date_input, expected_format",
    [
        ("2024-12-25", "%Y-%m-%d"),  # ISO format
        ("25/12/2024", "%d/%m/%Y"),  # European format
        ("12/25/2024", "%m/%d/%Y"),  # US format
        ("2024/12/25", "%Y/%m/%d"),  # Slash-separated ISO
        ("25-12-2024", "%d-%m-%Y"),  # Dash-separated European
        ("12-25-2024", "%m-%d-%Y"),  # Dash-separated US
        ("25.12.2024", "%d.%m.%Y"),  # Dot-separated European
        ("2024.12.25", "%Y.%m.%d"),  # Dot-separated ISO
        ("25 Dec 2024", "%d %b %Y"),  # Day Month Year short
        ("Dec 25 2024", "%b %d %Y"),  # Month Day Year short
        ("2024 Dec 25", "%Y %b %d"),  # Year Month Day short
        ("25 December 2024", "%d %B %Y"),  # Day Month Year long
        ("December 25 2024", "%B %d %Y"),  # Month Day Year long
        ("2024-12-25 14:30:00", "%Y-%m-%d %H:%M:%S"),  # ISO with time
        ("25/12/2024 14:30:00", "%d/%m/%Y %H:%M:%S"),  # European with time
        ("2024/12/25 14:30:00", "%Y/%m/%d %H:%M:%S"),  # Slash-separated ISO with time
        ("", None),  # Empty string
        (None, None),  # None input
    ],
)
def test_detect_single_format(date_input, expected_format):
    """Test detecting the format for single date strings."""
    assert DateFormatDetector.detect_format(date_input) == expected_format


@pytest.mark.parametrize(
    "date_samples, expected_format",
    [
        (["2024-12-25", "2023-11-15", "2022-01-01"], "%Y-%m-%d"),  # All ISO format
        (["25/12/2024", "15/11/2023", "01/01/2022"], "%d/%m/%Y"),  # All European format
        (["12/25/2024", "11/15/2023", "01/01/2022"], "%m/%d/%Y"),  # All US format
        (["2024-12-25", "2023/11/15", "2022.01.01"], None),  # Mixed formats
        ([], None),  # Empty list
    ],
)
def test_detect_multiple_formats(date_samples, expected_format):
    """Test detecting the format for multiple date samples."""
    assert DateFormatDetector.detect_format(date_samples) == expected_format


def test_invalid_inputs():
    """Test invalid inputs."""
    assert DateFormatDetector.detect_format(12345) is None  # Non-string input
    assert DateFormatDetector.detect_format([12345, "2024-12-25"]) is None  # Mixed input types
    assert DateFormatDetector.detect_format(["Invalid Date", "2024-12-25"]) is None  # Partially valid list
