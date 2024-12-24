from datetime import datetime
from typing import List, Optional

class DateFormatDetector:
    # Common date format patterns to check against
    COMMON_PATTERNS = [
        "%Y-%m-%d",
        "%d/%m/%Y",
        "%m/%d/%Y",
        "%Y/%m/%d",
        "%d-%m-%Y",
        "%m-%d-%Y",
        "%d.%m.%Y",
        "%Y.%m.%d",
        "%d %b %Y",
        "%b %d %Y",
        "%Y %b %d",
        "%d %B %Y",
        "%B %d %Y",
        "%Y-%m-%d %H:%M:%S",
        "%d/%m/%Y %H:%M:%S",
        "%Y/%m/%d %H:%M:%S"
    ]

    @staticmethod
    def detect_format(date_input: str | List[str]) -> Optional[str]:
        """
        Detects the date format pattern from either a single date string or a list of date strings.
        
        Args:
            date_input: A string or list of strings containing date samples
            
        Returns:
            The matching date format pattern, or None if no match is found
        """
        if isinstance(date_input, str):
            return DateFormatDetector._detect_single_format(date_input)
        elif isinstance(date_input, list):
            return DateFormatDetector._detect_multiple_formats(date_input)
        return None

    @staticmethod
    def _detect_single_format(date_str: str) -> Optional[str]:
        """
        Detects the date format pattern from a single date string.
        """
        if not date_str or not isinstance(date_str, str):
            return None

        date_str = date_str.strip()
        
        for pattern in DateFormatDetector.COMMON_PATTERNS:
            try:
                datetime.strptime(date_str, pattern)
                return pattern
            except ValueError:
                continue
        return None

    @staticmethod
    def _detect_multiple_formats(date_samples: List[str]) -> Optional[str]:
        """
        Detects the most common date format pattern from a list of sample dates.
        """
        if not date_samples:
            return None

        valid_formats = []
        
        # Find formats that work for all samples
        for pattern in DateFormatDetector.COMMON_PATTERNS:
            valid_for_all = True
            for date in date_samples:
                try:
                    datetime.strptime(date.strip(), pattern)
                except (ValueError, AttributeError):
                    valid_for_all = False
                    break
            
            if valid_for_all:
                valid_formats.append(pattern)

        # Return the most specific format if multiple matches found
        return max(valid_formats, key=len) if valid_formats else None