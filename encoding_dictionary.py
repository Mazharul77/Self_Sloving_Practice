"""
Dictinary Encoding: as a partial compression technique of lossless compression
part-1 : made by Bhuiyan
"""

def dictionary_encoding(passed_data):
    compressed_data = []
    dict_data = {}
    reverse_dict_data = {}

    for index, val in enumerate(passed_data):
        # print(f"index: {index}, val:{ val}, key(val[0]): {val[0]}\n")
        if val not in reverse_dict_data:
            dict_data[val[0]] = val  # {'Y': 'Yellow'}
            reverse_dict_data[val] = val[0]  # {'Yellow': 'Y'}

            compressed_data.append(val[0])
        else:
            compressed_data.append(reverse_dict_data[val])

        print("reverse_dict_data[val]: ", reverse_dict_data)

        print("compressed_data: ", compressed_data)
        print("dict_data: ", dict_data)

    return compressed_data, dict_data

given_data = ["Yellow", "Yellow", "Yellow", "Red", "Red", "Blue", "Blue", "Blue", "Green", "Red"]
print("Before compressing Given Original Data:")
print(given_data)
print("After Encoding the data:")
compressd_data, dictionary = dictionary_encoding(given_data)
print("compressd_data:", compressd_data, "and dictionary: ", dictionary)