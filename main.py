from sys import argv
from os import getenv
from configparser import ConfigParser
from logging import getLogger, FileHandler, Formatter, StreamHandler

from praw.models import Submission
from praw import Reddit

LOG_LEVEL = getenv("LOG_LEVEL", "INFO")

log_formatter = Formatter(
    "%(asctime)s, %(levelname)s [%(filename)s:%(lineno)d] %(funcName)s(): %(message)s",
    datefmt="%d/%m/%Y %H:%M:%S",
)

logger = getLogger(__name__)
logger.setLevel(LOG_LEVEL)

# Add file handler to logger
file = FileHandler(filename="logs/access.log", mode="a")
file.setFormatter(log_formatter)
logger.addHandler(file)

# Add stream handler to logger
stream = StreamHandler()
stream.setFormatter(log_formatter)
logger.addHandler(stream)


def main():
    args = argv[1:]

    if len(args) > 1:
        print("Too many arguments. Missing 1 required positional argument")
        exit(-1)

    elif len(args) < 1:
        print("No URL argument provided")
        exit(-2)

    else:
        try:
            config = ConfigParser()
            config.read("praw.ini")

            for section in config.sections():
                logger.info(f"Will login as {section}")

                bot = Reddit(
                    site_name=section,
                    config_interpolation="basic",
                )

                logger.info(f"Logged in as {bot.user.me()}")

                submission: Submission = bot.submission(url=args[0])
                submission.upvote()

                logger.info(f"{bot.user.me()} voted up {submission.url}")
        except Exception as e:
            logger.error(f"{e}")


if __name__ == "__main__":
    main()
