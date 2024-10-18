from extractors import CompanyNameExtractor, DateExtractor
from validators import CompanyNameValidator, DateValidator
import logging


class ValidationPipeline:
    """
    Pipeline for running the validation process on extracted data.
    """

    def __init__(self, pdf_path: str, company_name: str, date: str, config: dict):
        """
        Initializes the validation pipeline.

        :param pdf_path: Path to the PDF file.
        :param company_name: Expected company name.
        :param date: Expected date in ISO format.
        :param config: Configuration dictionary.
        """
        self.pdf_path = pdf_path
        self.company_name = company_name
        self.date = date
        self.config = config

    def run(self):
        """
        Executes the validation pipeline.
        """
        company_extractor = CompanyNameExtractor(self.config['company_keyword'])
        date_extractor = DateExtractor()

        extracted_name = company_extractor.extract(self.pdf_path)
        extracted_date = date_extractor.extract(self.pdf_path)

        name_validator = CompanyNameValidator()
        date_validator = DateValidator()

        name_valid = name_validator.validate(extracted_name, self.company_name)
        date_valid = date_validator.validate(extracted_date, self.date)

        if name_valid and date_valid:
            logging.info("All validations passed successfully.")
        else:
            logging.error("Validation failed.")