""" Main application entry point.

    python -m notebook_adventure  ...

"""
from . import cli
from .core.logger import logger

def main():
    """ Execute the application.

    """
    #raise NotImplementedError
    try: 
      cli.main()
    except RuntimeError as e:
      logger.critical(e)
      return 1


# Make the script executable.

if __name__ == "__main__":
    raise SystemExit(main())
