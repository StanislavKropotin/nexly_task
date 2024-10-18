import logging
from abc import ABC, abstractmethod
from fuzzywuzzy import fuzz


class BaseValidator(ABC):
    """
    Abstract base class for validating extracted data.
    """

    @abstractmethod
    def validate(self, extracted: str, expected: str) -> bool:
        """
        Validates the extracted data against the expected value.

        :param extracted: Extracted data.
        :param expected: Expected value for comparison.
        :return: True if validation passes, otherwise False.
        """
        pass


class CompanyNameValidator(BaseValidator):
    """
    Validator for checking the extracted company name against the expected name.
    """

    def validate(self, extracted: str, expected: str) -> bool:
        if extracted and fuzz.partial_ratio(extracted.lower(), expected.lower()) >= 80:
            logging.info("Company name validation passed.")
            return True
        else:
            logging.warning(f"Company name validation failed: expected '{expected}', found '{extracted}'.")
            return False


class DateValidator(BaseValidator):
    """
    Validator for checking the extracted date against the expected date.
    """

    def validate(self, extracted: str, expected: str) -> bool:
        if extracted == expected:
            logging.info("Date validation passed.")
            return True
        else:
            logging.warning(f"Date validation failed: expected '{expected}', found '{extracted}'.")
            return False
