# PDF Data Validation Pipeline

## Description:

This project provides a pipeline for validating data extracted from PDFs, specifically targeting the company name and date from the first (cover) page. 

It compares the extracted information against expected values specified by the user. 

The pipeline is designed to be easily extendable, allowing new extractors and validators to be added with minimal changes.

## Installation:

*1) Clone the repository:*

git clone https://github.com/StanislavKropotin/nexly_task

*2) Navigate to the project directory:*

cd test_for_nexly

*3) Install the required dependencies:*

pip install -r requirements.txt

## Usage:

*To run the script, use the following command:*

**Successful Validation:**

```bash

python pipeline.py report.pdf --config config.yaml --company_name "Bluegem III GP SARL" --date "2023-12-31"

```

Output:

2023-10-18 12:00:00 - INFO - Company name validation passed.

2023-10-18 12:00:00 - INFO - Date validation passed.

2023-10-18 12:00:00 - INFO - All validations passed successfully.

**Unsuccessful Validation:**

```bash

python pipeline.py report.pdf --config config.yaml  --company_name "no name" --date "2025-12-31"

```

Output:

2023-10-18 12:05:00 - WARNING - Company name validation failed: expected 'No Name', found 'Bluegem III GP SARL'.

2023-10-18 12:05:00 - WARNING - Date validation failed: expected '2025-12-31', found '2023-12-31'.

2023-10-18 12:05:00 - ERROR - Validation failed.

**The --config flag was added to make the pipeline more flexible and easier to configure.**

**By using a configuration file (config.yaml), users can specify parameters (such as keywords for extracting the company name) without modifying the script itself.**

**This allows for easier adjustments, such as changing search criteria, and makes the pipeline more adaptable for different use cases.**

## Adding New Extractors and Validators:

The pipeline is designed to allow easy integration of new extractors and validators. 

To add new components, create new classes that inherit from BaseExtractor or BaseValidator.

## Logging:

Logging was added to the pipeline to provide clear and detailed feedback during the extraction and validation process. 

It records information about successful operations and warnings or errors when issues occur. 

This helps users understand what happened during the execution, making troubleshooting and monitoring easier. 

Logs are saved to a file and also displayed on the console for real-time updates.
