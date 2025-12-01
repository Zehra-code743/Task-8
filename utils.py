def validate_numeric_input(value,  input_name):
    try:
        return float(value)
    except ValueError:
        raise ValueError(f"Invalid input for {input_name}. Please enter numbers only.")