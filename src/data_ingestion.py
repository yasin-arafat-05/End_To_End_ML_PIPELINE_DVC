
import logging

logger = logging.getLogger("data_injection")
logger.setLevel("DEBUG")
formater = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

console_handeler = logging.StreamHandler()
console_handeler.setLevel("DEBUG")
console_handeler.setFormatter(formater)

file_handeler = logging.FileHandler()
file_handeler.setLevel("DEBUG")
file_handeler.setFormatter(formater)


