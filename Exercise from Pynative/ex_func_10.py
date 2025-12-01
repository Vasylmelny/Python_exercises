# Define a function describe_pet(animal_type, pet_name)
# that prints a description of a pet.
# Call this function using both positional and keyword arguments.

def describe_pet(animal_type, pet_name):
    print(f"I have {animal_type}, named {pet_name}")

describe_pet("dog", "Rex")
describe_pet("cat", "Cat")

describe_pet(animal_type = "cat", pet_name = "Murchyk")
