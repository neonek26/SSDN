import ssdn-1.1

#Open SSDN file
with open('data.ssdn', 'r') as file:
    # Load the data from the YAML file
    data = ssdn.safe_load(file)

# Print the data
print(data)