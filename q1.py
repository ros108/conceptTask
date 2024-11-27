steps = list(map(int, input("Enter the steps for each day in a month, separated by spaces: ").split(",")))
highest_steps = max(steps)
lowest_steps = min(steps)
average_steps = sum(steps) / len(steps)
sorted_steps = sorted(steps , reverse=True)

print(f"Highest steps: {highest_steps}")

print(f"Lowest steps: {lowest_steps}")
print(f"Average steps: {average_steps:.2f}")
print("Steps in descending order:", sorted_steps)