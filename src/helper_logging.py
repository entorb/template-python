"""Helper: Logging."""

import logging

LOGGER = logging.getLogger(__name__)


def init_logging() -> None:
    """Initialize logging."""
    logging.addLevelName(logging.DEBUG, "D")
    logging.addLevelName(logging.INFO, "I")
    logging.addLevelName(logging.WARNING, "W")
    logging.addLevelName(logging.ERROR, "E")
    logging.addLevelName(logging.CRITICAL, "C")
    logging.basicConfig(
        level=logging.INFO, format="%(levelname)s: %(name)s: %(message)s"
    )
    logging.getLogger("httpx").setLevel(logging.WARNING)
