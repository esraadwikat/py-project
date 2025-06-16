

# إدخال المصفوفة من المستخدم
user_input = input("Enter the array separated by space: ")
arr = list(map(int, user_input.strip().split()))
print("You entered Array :", arr)



def find_and_fill_missing_numbers(arr):
    start = min(arr)
    end = max(arr)

    expected_set = set(range(start, end + 1))
    arr_set = set(arr)

    missing_numbers = list(expected_set - arr_set)
    completed_array = arr + missing_numbers
    completed_array.sort()
    unique_sorted_array = sorted(set(completed_array))
    print("The range", start, "to", end)
    print("MissingNum:", sorted(missing_numbers))
    print("FullArray", unique_sorted_array)



   
   
find_and_fill_missing_numbers(arr)
