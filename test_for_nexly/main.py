import logging
from argparse import ArgumentParser
from pipeline import ValidationPipeline
from utils import load_config

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("validation_pipeline.log"),
        logging.StreamHandler()
    ]
)

if __name__ == "__main__":
    parser = ArgumentParser(description="PDF Data Validation.")
    parser.add_argument("pdf_path", type=str, help="Path to the PDF file.")
    parser.add_argument("--config", type=str, required=True, help="Path to the YAML configuration file.")
    parser.add_argument("--company_name", type=str, required=True, help="Expected company name.")
    parser.add_argument("--date", type=str, required=True, help="Expected date in ISO format (YYYY-MM-DD).")

    args = parser.parse_args()
    config = load_config(args.config)

    pipeline = ValidationPipeline(args.pdf_path, args.company_name, args.date, config)
    pipeline.run()
