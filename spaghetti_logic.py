"""Module for processing and logging financial data."""

from typing import List

# Configuration constants
PRICE_MULTIPLIER = 1.15
LOG_FILE_PATH = "log.txt"
DECIMAL_PLACES = 2


def apply_price_multiplier(prices: List[float]) -> List[float]:
    """
    Apply a fixed multiplier to each price.
    
    Args:
        prices: List of numeric price values.
    
    Returns:
        List of prices with multiplier applied.
    """
    return [price * PRICE_MULTIPLIER for price in prices]


def format_price_output(total_price: float) -> str:
    """
    Format a price value for display.
    
    Args:
        total_price: The price amount to format.
    
    Returns:
        Formatted price string.
    """
    return f"Total: {total_price:.{DECIMAL_PLACES}f}"


def log_results(results: List[float], filepath: str = LOG_FILE_PATH) -> None:
    """
    Log processed results to a file.
    
    Args:
        results: List of computed values to log.
        filepath: Path to the log file.
    """
    with open(filepath, "a") as log_file:
        log_file.write(str(results) + "\n")


def display_results(results: List[float]) -> None:
    """
    Print formatted results to console.
    
    Args:
        results: List of computed values to display.
    """
    for result in results:
        formatted_output = format_price_output(result)
        print(formatted_output)


def process_data(prices: List[float]) -> List[float]:
    """
    Process price data through calculation, display, and logging.
    
    Orchestrates the workflow: applies multiplier, displays results,
    and logs the output.
    
    Args:
        prices: List of price values to process.
    
    Returns:
        List of processed prices with multiplier applied.
    """
    processed_prices = apply_price_multiplier(prices)
    display_results(processed_prices)
    log_results(processed_prices)
    return processed_prices
