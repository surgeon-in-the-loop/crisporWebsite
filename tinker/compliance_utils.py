import re
import os
import logging
from cryptography.fernet import Fernet

# Generate a static key for testing purposes (in production, manage keys securely)
key = Fernet.generate_key()
cipher_suite = Fernet(key)

def deidentify_data(text):
    """
    Naively removes specific identifiers from a text.
    """
    text = re.sub(r'\bJohn Doe\b', 'Patient', text)
    text = re.sub(r'\b\d{3}-\d{2}-\d{4}\b', '', text)
    text = re.sub(r'\b\d+ Main St\b', '', text)
    return text

def check_access(user_role, required_role):
    """
    Simulates an access control check. Raises PermissionError if roles do not match.
    """
    if user_role != required_role:
        raise PermissionError("Unauthorized access")
    return True

def encrypt_data(message):
    """
    Encrypts a message using Fernet symmetric encryption.
    """
    return cipher_suite.encrypt(message.encode()).decode()

def decrypt_data(token):
    """
    Decrypts a previously encrypted message.
    """
    return cipher_suite.decrypt(token.encode()).decode()

def log_event(message, log_file='audit.log'):
    """
    Logs an event to the specified audit log file.
    """
    logger = logging.getLogger("ComplianceLogger")
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        fh = logging.FileHandler(log_file)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        logger.addHandler(fh)
    logger.info(message)

def get_last_log_entry(log_file='audit.log'):
    """
    Retrieves the last entry from the audit log.
    """
    if not os.path.exists(log_file):
        return ""
    with open(log_file, "r") as f:
        lines = f.readlines()
    return lines[-1] if lines else ""

# For demonstration purposes, we add a main function
def main():
    sample_text = "John Doe lives at 123 Main St. His SSN is 123-45-6789."
    deid_text = deidentify_data(sample_text)
    print("De-identified text:", deid_text)
    
    try:
        # This should fail if the roles don't match.
        check_access("nurse", "doctor")
    except PermissionError as e:
        print("Access check failed:", e)
    
    message = "This is a confidential message."
    encrypted = encrypt_data(message)
    decrypted = decrypt_data(encrypted)
    print("Encrypted message:", encrypted)
    print("Decrypted message:", decrypted)
    
    log_event("Test compliance event.")
    last_entry = get_last_log_entry()
    print("Last log entry:", last_entry)

if __name__ == "__main__":
    main()
