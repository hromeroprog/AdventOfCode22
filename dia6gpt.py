def find_marker(s: str, n: int) -> int:
    # Create a set to keep track of the most recent characters seen
    seen = set()
    
    # Iterate through the input string, one character at a time
    for i, c in enumerate(s):
        # Add the current character to the set of seen characters
        seen.add(c)
        
        # If the length of the set is equal to the marker length, it means
        # we have found a marker
        if len(seen) == n:
            # Return the index where the marker starts
            return i - n + 1
        
        # If the length of the set is greater than the marker length, it means
        # we have seen a repeated character. In this case, we need to clear the
        # set and start over.
        if len(seen) > n:
            seen.clear()
    
    # If we reach the end of the input string without finding a marker,
    # return -1
    return -1

with open("input.txt") as file:
    s = [line[:-1] for line in file.readlines()][0]

# Find the start-of-packet marker
start_of_packet_marker = find_marker(s, 4)
print(start_of_packet_marker)  # Output: 7

# Find the start-of-message marker
start_of_message_marker = find_marker(s, 14)
print(start_of_message_marker)  # Output: 19