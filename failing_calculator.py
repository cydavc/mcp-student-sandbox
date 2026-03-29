def average_ratios(numbers):
    """Calculate average of 100 divided by each number.
    
    Args:
        numbers: List of numbers to divide into 100.
        
    Returns:
        Average of ratios, excluding zero values.
        
    Raises:
        ValueError: If input list is empty or contains only zeros.
    """
    if not numbers:
        raise ValueError("Input list cannot be empty")
    
    ratios = []
    for num in numbers:
        if num == 0:
            continue  # Skip zero values to avoid division by zero
        ratios.append(100 / num)
    
    if not ratios:
        raise ValueError("All input values were zero, cannot calculate average")
    
    return sum(ratios) / len(ratios)

print(average_ratios([10, 5, 0]))
