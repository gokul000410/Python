import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 22],
    "City": ["New York", "Los Angeles", "Chicago"]
}

df = pd.DataFrame(data)

# Make sure this folder exists on your PC
df.to_csv(r"D:\project\demo.csv", index=False)

print("CSV saved successfully!")

