def calculate_flight_time(weight_grams):
    """Calculate active flight time based on payload weight in grams.
    Args:
        weight_grams (float): The payload weight in grams.  
        Returns:
            float: The calculated flight time in minutes.
    """
    if weight_grams < 0:
        raise ValueError("Weight cannot be negative.")
    flight_time = 180 - 0.1 * weight_grams
    return max(0, flight_time)

def flight_time_table(max_weight_grams, step_grams):
    """Generate a table of flight times for different payload weights.
    Args:
        max_weight_grams (float): The maximum payload weight in grams.
        step_grams (float): The increment step for payload weight in grams.
    Returns:
        list of tuples: Each tuple contains (weight_grams, flight_time_minutes).
    """
    if max_weight_grams < 0 or step_grams <= 0:
        raise ValueError("Max weight must be non-negative and step must be positive.")
    
    table = []
    for weight in range(0, max_weight_grams + 1, step_grams):
        flight_time = calculate_flight_time(weight)
        table.append((weight, flight_time))
    
    return table