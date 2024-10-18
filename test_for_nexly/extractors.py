import fitz
import re
import os
import logging
from abc import ABC, abstractmethod
from typing import Optional
from datetime import datetime


class BaseExtractor(ABC):
    """
    Abstract base class for extracting data from a PDF file.
    """

    @abstractmethod
    def extract(self, pdf_path: str) -> Optional[str]:
        """
        Extracts specific data from the given PDF file.

        :param pdf_path: Path to the PDF file.
        :return: Extracted data as a string, or None if extraction failed.
        """
        pass


class CompanyNameExtractor(BaseExtractor):
    """
    Extractor for retrieving the company name based on a given keyword.
    """

    def __init__(self, keyword: str):
        """
        Initializes the extractor with the keyword used for matching the company name.

        :param keyword: Keyword to search for in the PDF.
        """
        self.keyword = keyword

    def extract(self, pdf_path: str) -> Optional[str]:
        if not os.path.exists(pdf_path):
            logging.error(f"File {pdf_path} not found.")
            return None
        try:
            with fitz.open(pdf_path) as doc:
                text = doc[0].get_text()
                for line in text.splitlines():
                    if re.search(self.keyword, line, re.IGNORECASE):
                        return line.strip()
            return None
        except Exception as e:
            logging.exception(f"Error extracting company name: {e}")
            return None


class DateExtractor(BaseExtractor):
    """
    Extractor for retrieving and formatting a date from a PDF file.
    """

    def extract(self, pdf_path: str) -> Optional[str]:
        if not os.path.exists(pdf_path):
            logging.error(f"File {pdf_path} not found.")
            return None
        try:
            with fitz.open(pdf_path) as doc:
                text = doc[0].get_text()
                match = re.search(r'(\w+ \d{1,2}, \d{4})', text)
                if match:
                    return self.convert_date_to_iso(match.group(1))
            return None
        except Exception as e:
            logging.exception(f"Error extracting date: {e}")
            return None

    @staticmethod
    def convert_date_to_iso(date_str: str) -> str:
        """
        Converts a date string to ISO format (YYYY-MM-DD).

        :param date_str: Date string in the format 'Month DD, YYYY'.
        :return: Date in ISO format, or an empty string if conversion fails.
        """
        try:
            date_obj = datetime.strptime(date_str, "%B %d, %Y")
            return date_obj.strftime("%Y-%m-%d")
        except ValueError as e:
            logging.error(f"Error converting date: {e}")
            return ""
