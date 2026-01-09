import logging


logging.basicConfig(
    level=logging.DEBUG,
    filename="logs/pytest_session.log",
    filemode="w",
    format="%(asctime)s | %(levelname)8s | (%(name)s) %(message)s"
)

logging.getLogger("urllib3").setLevel(logging.WARNING)
