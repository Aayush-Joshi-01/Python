import logging
import functools
import os
import inspect

from typing import Callable, Any


logger: logging.Logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler: logging.FileHandler = logging.FileHandler(
    os.path.join(os.path.dirname(__file__), '..', 'Logs', 'Analysis_Logs''.json')
)
file_handler.setLevel(logging.DEBUG)
formatter: logging.Formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def logger_analysis(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    A decorator to log function calls with arguments, results, and nested function calls.
    """

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        logger.debug(f'Calling the {func.__name__} with args {args} and kwargs {kwargs}')
        try:
            result: Any = func(*args, **kwargs)
            logger.debug(f'{func.__name__} returned {result}')
            return result
        except Exception as e:
            logger.exception(f'Error in {func.__name__}: {e}')
            raise

    call_stack: list[str] = []
    for frame in inspect.getouterframes(inspect.currentframe()):
        call_stack.append(frame.function)
    logger.debug(f'function calls: {call_stack}')

    return wrapper


if __name__ == '__main__':
    @logger_analysis
    def add(a: int, b: int) -> int:
        return a + b

    add(3, 4)
