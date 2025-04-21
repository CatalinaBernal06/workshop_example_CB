import pandas as pd

def main():
    # 1. Creating a DataFrame from a dictionary
    data = {
        "Name": ["Alice", "Bob", "Charlie"],
        "Age": [25, 30, 35],
        "City": ["New York", "Los Angeles", "Chicago"]
    }
    df = pd.DataFrame(data)
    print("DataFrame created from a dictionary:")
    print(df)
    print("\n")

    # 2. Reading a CSV file
    # Uncomment the following lines if you have a CSV file to read
    # df_csv = pd.read_csv("example.csv")
    # print("DataFrame read from a CSV file:")
    # print(df_csv)
    # print("\n")

    # 3. Writing a DataFrame to a CSV file
    df.to_csv("output.csv", index=False)
    print("DataFrame written to 'output.csv'.\n")

    # 4. Basic operations
    print("Basic operations on the DataFrame:")
    print("Column 'Age' statistics:")
    print(df["Age"].describe())
    print("\n")

    print("Filtering rows where Age > 28:")
    print(df[df["Age"] > 28])
    print("\n")

    # 5. Adding a new column
    df["Is_Adult"] = df["Age"] >= 18
    print("DataFrame after adding a new column 'Is_Adult':")
    print(df)
    print("\n")

    # 6. Grouping and aggregating data
    grouped = df.groupby("City").agg({"Age": "mean"})
    print("Average age by city:")
    print(grouped)
    print("\n")

if __name__ == "__main__":
    main()