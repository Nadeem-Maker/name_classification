from names_dataset import NameDataset

# Initialize the NameDataset
nd = NameDataset()

# Custom dictionary for additional names
# custom_data = {
#     'Nazam': 'Male',
#     'Fazeelat': 'Female'
# }

# Function to classify gender based on name
def classify_gender(name):
    # Check in custom data first
    if name in custom_data:
        return custom_data[name]
    
    # Fallback to names-dataset
    result = nd.search(name)
    if result and 'gender' in result:
        gender = result['gender']
        if gender == 'Male':
            return 'Male'
        elif gender == 'Female':
            return 'Female'
    
    return 'Unknown'

# Take user input for names
user_input = input("Enter names separated by commas: ")
names = [name.strip() for name in user_input.split(',')]

# Classify and display results
for name in names:
    gender = classify_gender(name)
    print(f"Name: {name}, Gender: {gender}")
