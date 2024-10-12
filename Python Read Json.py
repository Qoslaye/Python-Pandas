import pandas as pd

# file_path = 'sample.json'
# df = pd.read_json(file_path)

# print("data frame from json : ")
# print(df)

data = {
    "Duration": {
        "0": 60,
        "1": 59,
        "2": 60,
        "3": 45
    },
    "Pulse": {
        "0": 110,
        "1": 117,
        "2": 103,
        "3": 109
    },
    "MaxPulse": {
        "0": 130,
        "1": 145,
        "2": 135,
        "3": 174
    },
    "Calories": {
        "0": 409,
        "1": 479,
        "2": 340,
        "3": 282
    }
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

# Print the DataFrame
print(df)
