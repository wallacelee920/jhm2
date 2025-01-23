# 1.比較兩個價錢的大小 
價錢1 = float(input("Enter a price: "))
價錢2 = float(input("Enter another price: "))
if 價錢1 > 價錢2:
    print("The first price is larger than the second one.")
elif 價錢1 < 價錢2:
    print("The first price is smaller than the second one.")
else:
    print("The prices are the same.")


    #2.你想吃點零食嗎？
snack_preference = input("Do you want some snacks? (yes/no): ").lower()
if snack_preference == "no":
    print("Good! Let’s play games instead.")
elif snack_preference == "yes":
    snack_choice = input("Enter your choice (ice-cream / cookies / candies): ").lower()
    if snack_choice == "ice-cream":
        print("Remember to wash your hands.")
    elif snack_choice == "cookies":
        print("Can you share with your friends?")
    elif snack_choice == "candies":
        print("Don’t eat too much.")
    else:
        print("Invalid choice.")
else:
    print("Invalid input.")


# 3.加法口訣表
size = int(input("Input Addition Table Size smaller 10: "))
print("Addition Table")
print("-------------------------------------------------------")
for i in range(1, size + 1):
    for j in range(1, size + 1):
        result = i + j
        # 格式化輸出
        if result < 10:
            print(f"{i} + {j} = {result}  ", end=" ")
        else:
            print(f"{i} + {j} = {result} ", end=" ")
    print()  
print("-------------------------------------------------------")

# 4.來統計同學的身高
heights = []
count = 0
while count < 4:
    height = float(input(f"Input the height of student {count + 1} in cm: "))
    if height < 0:
        print("Height must be positive.")
    elif height > 200:
        print("Height is greater than 200cm.")
    else:
        heights.append(height)
        count += 1
print("End of input.")
average_height = sum(heights) / len(heights)
max_height = max(heights)
print(f"The average height of these students is {average_height:.2f} cm.")
print(f"The maximum height of these students is {max_height:.2f} cm.")

# 5.數據可視化
import pandas as pd
import matplotlib.pyplot as plt
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Sales': [380, 400, 660, 800, 900, 1200, 1600, 2200, 1500, 1100, 600, 250]
}
df = pd.DataFrame(data)

plt.figure(figsize=(10, 6))
plt.bar(df['Month'], df['Sales'], color='green', width=0.5)
plt.title('Bar Chart of Ice-cream Sales')
plt.xlabel('Month')
plt.ylabel('Sales (in thousand dollars)')
plt.show()44