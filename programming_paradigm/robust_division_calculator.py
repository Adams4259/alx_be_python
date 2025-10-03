def safe_divide(numerator, denominator):
    """Perform safe division with error handling for zero and non-numeric inputs."""

    try:
        # Attempt to convert inputs to float
        num = float(numerator)
        den = float(denominator)

        # Check for division by zero
        try:
            result = num / den
            return f"The result of the division is {result}"
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."

    except ValueError:
        return "Error: Please enter numeric values only."
