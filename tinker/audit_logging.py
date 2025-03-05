# File: audit_logging.py

import logging
import os

def setup_logger(log_file='audit.log'):
    logger = logging.getLogger("AuditLogger")
    logger.setLevel(logging.INFO)
    # Create a file handler
    fh = logging.FileHandler(log_file)
    fh.setLevel(logging.INFO)
    # Create a formatter and add it to the handler
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    # Add the handler to the logger
    logger.addHandler(fh)
    return logger

# Example usage in a core module
if __name__ == "__main__":
    logger = setup_logger()
    logger.info("Audit log initiated.")
    
    # Simulate a critical action: generation of a candidate pegRNA
    pegRNA = "ACGTACGTACGT-ACGTACGTACG-CTGTACGTACGT-forward"
    logger.info(f"Candidate pegRNA generated: {pegRNA}")

    # Read and print log content (for demonstration)
    if os.path.exists("audit.log"):
        with open("audit.log", "r") as log_file:
            print(log_file.read())
