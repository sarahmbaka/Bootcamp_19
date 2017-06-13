def data_type(value):
    if isinstance(value, str):
        return len(value)
    elif isinstance(value, bool):
        return value
    elif isinstance(value, int):
        if value < 100:
            return "less than 100"
        elif value == 100:
            return "equal to 100"
        return "more than 100"
    elif isinstance(value, list):
        return value[2] if len(value) > 2 else None
    if value is None:
        return 'no value'


