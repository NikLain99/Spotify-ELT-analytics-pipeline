from config.logging_config import setup_logging
import uuid
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

batch_id = str(uuid.uuid4())
logger = setup_logging(batch_id=batch_id)

logger.info("Test INFO")
logger.warning("Test WARNING ")
logger.error("Test ERROR")