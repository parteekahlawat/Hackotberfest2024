import random

# Function to generate a random number between a specified range
def generate_random_number(start, end):
    return random.randint(start, end)

# Example usage
start_range = 1
end_range = 100
random_number = generate_random_number(start_range, end_range)

print(f"Random number between {start_range} and {end_range}: {random_number}")
