import bisect


def closest_key_binary_search(data_dict, temperature):
    # Extract sorted keys from the dictionary
    sorted_keys = sorted(data_dict.keys())

    # Perform binary search to find the insertion point
    idx = bisect.bisect_left(sorted_keys, temperature)

    # If temperature is less than the smallest key
    if idx == 0:
        return sorted_keys[0]
    # If temperature is greater than the largest key
    elif idx == len(sorted_keys):
        return sorted_keys[-1]
    else:
        # Compare the closest two keys (before and after the insertion point)
        left = sorted_keys[idx - 1]
        right = sorted_keys[idx]

        # Return the key closest to the temperature
        return left if abs(left - temperature) <= abs(right - temperature) else right
