name = input("Ievadi savu vārdu")
print(f"Sveiks, {name}!")

numbers = []
print(f"ievadi piecus skaitļus pa vienam")
for i in range(5):
    num = float(input("Ievadiet {i + 1} skaitli: "))
    numbers.append(num)

print("sākotnejais saraksts: ")
print(numbers)

sorted_numbers = sorted(numbers)
print("sākotnejais saraksts augošā secībā:")
print(sorted_numbers)

average = sum(numbers)/ len(numbers)
print("saraksta vidēja vērtība:")
print(average)

print("rezultātu kopsavilkums:")
print(f"sākotnējais saraksts: {numbers}")
print(f"sakārtotais saraksts: {sorted_numbers}")
print(f"vidēja vērtība: {average}")