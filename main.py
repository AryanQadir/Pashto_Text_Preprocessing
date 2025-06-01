"""
main.py - Pashto Text Normalization Script
Author: Your Name
Date: 2025-05-27

This script loads Pashto text input (either from command line or file), applies normalization,
and outputs the normalized text.

Usage:
    python main.py --text "آيا كابل يوازې يو ښار دی؟"
    python main.py --input_file input.txt --output_file output.txt
"""

import argparse
import logging
from nlp_pashto.normalization import normalize_text

def normalize_pashto_text(text: str) -> str:
    """
    Normalize the input Pashto text using normalize_text function.

    Args:
        text (str): Raw Pashto text string.

    Returns:
        str: Normalized Pashto text.
    """
    try:
        normalized = normalize_text(text)
        return normalized.strip()
    except Exception as e:
        logging.error(f"Normalization error: {e}")
        return ""

def main():
    parser = argparse.ArgumentParser(description="Pashto Text Normalization")
    parser.add_argument("--text", type=str, help="Pashto text string to normalize")
    parser.add_argument("--input_file", type=str, help="Path to input text file")
    parser.add_argument("--output_file", type=str, help="Path to output normalized text file")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    if args.text:
        logging.info("Normalizing single input text...")
        result = normalize_pashto_text(args.text)
        print("Normalized Text:", result)

    elif args.input_file:
        logging.info(f"Reading input file: {args.input_file}")
        try:
            with open(args.input_file, "r", encoding="utf-8") as infile:
                lines = infile.readlines()
            normalized_lines = [normalize_pashto_text(line) for line in lines]

            if args.output_file:
                logging.info(f"Writing normalized text to: {args.output_file}")
                with open(args.output_file, "w", encoding="utf-8") as outfile:
                    outfile.write("\n".join(normalized_lines))
                logging.info("Normalization completed successfully.")
            else:
                for line in normalized_lines:
                    print(line)

        except FileNotFoundError:
            logging.error(f"Input file not found: {args.input_file}")
        except Exception as e:
            logging.error(f"Error processing file: {e}")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
