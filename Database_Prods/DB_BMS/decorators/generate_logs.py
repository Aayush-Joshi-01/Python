import logging
import functools
import os
import inspect
from typing import Callable, Any


logger: logging.Logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler: logging.FileHandler = logging.FileHandler(
    os.path.join(os.path.dirname(__file__), '..', 'logs', 'logs.json'))
file_handler.setLevel(logging.DEBUG)
formatter: logging.Formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def logger_v(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    A decorator to log function calls with arguments and results.
    """
    logger.debug('logger_v')

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        # Log the function call with arguments
        logger.debug(f'Calling {func.__name__} with args {args} and kwargs {kwargs}')

        # Call the function and log any exceptions
        try:
            result: Any = func(*args, **kwargs)
            logger.debug(f'{func.__name__} returned {result}')
            return result
        except Exception as e:
            logger.exception(f'Error in {func.__name__}: {e}')
            raise

    return wrapper


def log_nested_calls(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    A decorator to log function calls with arguments, results, and nested function calls.
    """
    logger.debug('Nested function calls decorator')

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        # Log the function call with arguments
        logger.debug(f'Calling {func.__name__} with args {args} and kwargs {kwargs}')

        # Call the function and log any exceptions
        try:
            result: Any = func(*args, **kwargs)
            logger.debug(f'{func.__name__} returned {result}')
            return result
        except Exception as e:
            logger.exception(f'Error in {func.__name__}: {e}')
            raise

    # Get the current call stack
    call_stack: list[str] = []
    for frame in inspect.getouterframes(inspect.currentframe()):
        call_stack.append(frame.function)

    # Log the nested function calls
    logger.debug(f'Nested function calls: {call_stack}')

    return wrapper
