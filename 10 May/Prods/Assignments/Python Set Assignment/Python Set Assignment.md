
# Python set assignment.
1: Write a Python program to check if a set a subset of another set

2: Write a Python program to remove all duplicates from a given list of strings and return a list of unique strings. Use the Python set data type.

3: Write a Python program to find the union, symmetric difference, and intersection of the two sets. Print the results of each operation.

4: Write a Python program to create a symmetric difference.

5: program to count number of vowels using sets in given string.

```commandline
class SubsetChecker:
    def is_subset(self, set1, set2):
        return set1.issubset(set2)

class DuplicateRemover:
    def remove_duplicates(self, string_list):
        return list(set(string_list))

class SetOperations:
    def union(self, set1, set2):
        return set1.union(set2)

    def symmetric_difference(self, set1, set2):
        return set1.symmetric_difference(set2)

    def intersection(self, set1, set2):
        return set1.intersection(set2)

class SymmetricDifference:
    def symmetric_diff(self, set1, set2):
        return set1.symmetric_difference(set2)

class VowelCounter:
    def count_vowels(self, string):
        vowels = set('aeiou')
        return len(set(string.lower()).intersection(vowels))

def main():
    subset_checker = SubsetChecker()
    duplicate_remover = DuplicateRemover()
    set_operations = SetOperations()
    symmetric_difference = SymmetricDifference()
    vowel_counter = VowelCounter()

    while True:
        print("Set Operations Menu:")
        print("1. Check if a set is a subset of another set")
        print("2. Remove duplicates from a list of strings")
        print("3. Find union, symmetric difference, and intersection of two sets")
        print("4. Create a symmetric difference")
        print("5. Count vowels in a given string")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            set1 = set(input("Enter set 1: ").split())
            set2 = set(input("Enter set 2: ").split())
            print("Is subset:", subset_checker.is_subset(set1, set2))

        elif choice == 2:
            string_list = input("Enter list of strings: ").split()
            print("Unique strings:", duplicate_remover.remove_duplicates(string_list))

        elif choice == 3:
            set1 = set(input("Enter set 1: ").split())
            set2 = set(input("Enter set 2: ").split())
            print("Union:", set_operations.union(set1, set2))
            print("Symmetric difference:", set_operations.symmetric_difference(set1, set2))
            print("Intersection:", set_operations.intersection(set1, set2))

        elif choice == 4:
            set1 = set(input("Enter set 1: ").split())
            set2 = set(input("Enter set 2: ").split())
            print("Symmetric difference:", symmetric_difference.symmetric_diff(set1, set2))

        elif choice == 5:
            string = input("Enter a string: ")
            print("Vowel count:", vowel_counter.count_vowels(string))

        elif choice == 6:
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```

```commandline
Set Operations Menu:
1. Check if a set is a subset of another set
2. Remove duplicates from a list of strings
3. Find union, symmetric difference, and intersection of two sets
4. Create a symmetric difference
5. Count vowels in a given string
6. Exit
Enter your choice: 1
Enter set 1: a b c
Enter set 2: a b c d e
Is subset: True
Set Operations Menu:
1. Check if a set is a subset of another set
2. Remove duplicates from a list of strings
3. Find union, symmetric difference, and intersection of two sets
4. Create a symmetric difference
5. Count vowels in a given string
6. Exit
Enter your choice: 1
Enter set 1: a b c
Enter set 2: d e f
Is subset: False
Set Operations Menu:
1. Check if a set is a subset of another set
2. Remove duplicates from a list of strings
3. Find union, symmetric difference, and intersection of two sets
4. Create a symmetric difference
5. Count vowels in a given string
6. Exit
Enter your choice: 2
Enter list of strings: apple banana apple orange banana
Unique strings: ['orange', 'apple', 'banana']
Set Operations Menu:
1. Check if a set is a subset of another set
2. Remove duplicates from a list of strings
3. Find union, symmetric difference, and intersection of two sets
4. Create a symmetric difference
5. Count vowels in a given string
6. Exit
Enter your choice: 2
Enter list of strings: hello world hello universe world
Unique strings: ['world', 'universe', 'hello']
Set Operations Menu:
1. Check if a set is a subset of another set
2. Remove duplicates from a list of strings
3. Find union, symmetric difference, and intersection of two sets
4. Create a symmetric difference
5. Count vowels in a given string
6. Exit
Enter your choice: 3
Enter set 1: a b c
Enter set 2: c d e
Union: {'d', 'c', 'a', 'b', 'e'}
Symmetric difference: {'e', 'a', 'd', 'b'}
Intersection: {'c'}
Set Operations Menu:
1. Check if a set is a subset of another set
2. Remove duplicates from a list of strings
3. Find union, symmetric difference, and intersection of two sets
4. Create a symmetric difference
5. Count vowels in a given string
6. Exit
Enter your choice: 3
Enter set 1: 1 2 3
Enter set 2: 3 4 5
Union: {'3', '5', '4', '1', '2'}
Symmetric difference: {'1', '5', '4', '2'}
Intersection: {'3'}
Set Operations Menu:
1. Check if a set is a subset of another set
2. Remove duplicates from a list of strings
3. Find union, symmetric difference, and intersection of two sets
4. Create a symmetric difference
5. Count vowels in a given string
6. Exit
Enter your choice: 4
Enter set 1: a b c
Enter set 2: c d e
Symmetric difference: {'e', 'a', 'd', 'b'}
Set Operations Menu:
1. Check if a set is a subset of another set
2. Remove duplicates from a list of strings
3. Find union, symmetric difference, and intersection of two sets
4. Create a symmetric difference
5. Count vowels in a given string
6. Exit
Enter your choice: 4
Enter set 1: 1 2 3
Enter set 2: 3 4 5
Symmetric difference: {'1', '5', '4', '2'}
Set Operations Menu:
1. Check if a set is a subset of another set
2. Remove duplicates from a list of strings
3. Find union, symmetric difference, and intersection of two sets
4. Create a symmetric difference
5. Count vowels in a given string
6. Exit
Enter your choice: 5
Enter a string: hello world
Vowel count: 2
Set Operations Menu:
1. Check if a set is a subset of another set
2. Remove duplicates from a list of strings
3. Find union, symmetric difference, and intersection of two sets
4. Create a symmetric difference
5. Count vowels in a given string
6. Exit
Enter your choice: 5
Enter a string: aeiou
Vowel count: 5
Set Operations Menu:
1. Check if a set is a subset of another set
2. Remove duplicates from a list of strings
3. Find union, symmetric difference, and intersection of two sets
4. Create a symmetric difference
5. Count vowels in a given string
6. Exit
Enter your choice: 6

Process finished with exit code 0
```