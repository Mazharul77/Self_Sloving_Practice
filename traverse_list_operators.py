print("Accessing Required Values of List's Using Operators-Techniques:\n")
data = ["Akhirat-Jannat", "IELTS", 8, "USA-Canada", "UK", 3.97, "Govt. Jobs", 50000, "Research", "M.Sc."]

# Technique-1 with [:-1]
print("All Data-Values First to Last:", data[:-1])

# or Technique-2 with assigned var
print("All Data-Values First to Last:", data)

# Position finding of specific values
print("The Position Of IELTS Score 8(if any): ", end="")
search_value = 8
print([position for position in range(len(data)) if data[position] == search_value])

# Access/Get (Traverse List): Expected Data-Information:
print("last to First:", data[::-1])
print("First 5 Data-info:", data[0:5])
print("5th to End  Data-info:", data[4:-1])
print("Last 5 Data-info:", data[-5:-1])

print("Get All Data at Even-Position  only: ", data[0:-1:2])
print("Get All Data at Odd-Position  only: ", data[1:-1:2])
print("Get The Last Vlaue/Item within the Data_storage:", data[-1])
print("Get The First Vlaue/Item within the Data_storage:", data[0])