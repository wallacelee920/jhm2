import pandas

print(dir(pandas))

#step1: Create a DateFerame
date={
     'Name': ['Alice', 'Bob', 'Chicago']
}

df = pd.DateFrame(date)

#step2 Diplay the DataFrame
print("Original DataFrame")
print(df)

# Step 3: Access specific columns
print("\nAccess the 'Name' columns:")
print(df.iloc['Name'])

#step 4: Access specific row using iloc
print(\nAccess the second row using iloc:")
print(df.iloc[1])

#