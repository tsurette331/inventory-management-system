def get_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        else: 
            print("Input cannot be empty.")

def get_int(prompt):
    while True:
        value = input(prompt)
        try:
            return int(value)
        except ValueError:
            print("Please enter a valid number.")