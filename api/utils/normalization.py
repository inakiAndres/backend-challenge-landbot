def normalize_keys(data):
    """
    Normalize the keys in the request body.
    - Converts keys to lowercase
    """
    normalized_data = {}
    
    for key, value in data.items():
        normalized_key = key.lower()
        normalized_data[normalized_key] = value

    return normalized_data
