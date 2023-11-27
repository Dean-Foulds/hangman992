def get_user_input():
    """Prompt user for input and validate it."""
    user_input = input("Enter a single alphabetical character: ")
    return user_input

def validate_user_input(user_input):
    """Validate user input."""
    return len(user_input) == 1 and user_input.isalpha()

def provide_feedback(is_valid):
    """Provide feedback based on the validation result."""
    if is_valid:
        print("Good guess!")
    else:
        print("Oops! That is not a valid input.")


