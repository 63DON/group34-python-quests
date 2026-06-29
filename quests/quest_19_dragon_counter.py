# Quest 19 - The Dragon Counter
total_dragons = 0
for i in range(1, 6):
    print("Counting dragon", i)
    total_dragons += 1
print("Total dragons spotted:", total_dragons)
print("\nEven-numbered dragons:")
for i in range(1, 11):
    if i % 2 == 0:
        print("Dragon", i)
