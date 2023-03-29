# Define the dataset as a list of dictionaries
dataset = [
    {"Make": "Ford", "Model": "Mustang", "Year": 2015, "Price": 10000, "MPG": 20},
    {"Make": "Toyota", "Model": "Camry", "Year": 2018, "Price": 20000, "MPG": 30},
    {"Make": "Honda", "Model": "Civic", "Year": 2020, "Price": 30000, "MPG": 40},
]

# Print the dataset in the desired format
for row in dataset:
    print("{:<7} {:<7} {:<5} {:<6} {}".format(row["Make"], row["Model"], row["Year"], row["Price"], row["MPG"]))