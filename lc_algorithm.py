"""
............... Step by step Full Algorithm for Lossless Compression Data: ...............

Dictinary Encoding: as a partial compression technique of lossless compression
part-1 : made by Bhuiyan

"""

# Dictionary Encoding
def dictionary_encoding(passed_data):
    compressed_data = []
    dict_data = {}
    reverse_dict_data = {}

    for index, val in enumerate(passed_data):
        # print(f"index: {index}, val:{ val}, key(val[0]): {val[0]}\n")
        if val not in reverse_dict_data:
            dict_data[val[0]] = val  # {'A': 'AI'}
            reverse_dict_data[val] = val[0]  # {'AI': 'A'}

            compressed_data.append(val[0])
        else:
            compressed_data.append(reverse_dict_data[val])

    print("reverse_dict_data[val]: ", reverse_dict_data)

    print("compressed_data: ", compressed_data)
    print("dict_data: ", dict_data)

    return compressed_data, dict_data

"""
part-2(Run Length Encoding): for compression without losing data: made by Bhuiyan
"""

# Run Length Encoding
def run_length_encoding_dict(passed_data):
    compression_data = []
    counter = 1
    current_list_key = passed_data[0]

    for num in range(1, len(passed_data)):
        if passed_data[num] == current_list_key:
            counter += 1
        else:
            compression_data.append((current_list_key, counter))
            counter = 1
            current_list_key = passed_data[num]
    compression_data.append((current_list_key, counter))
    return compression_data


# Final Part of Full Lossless Compression Algorithm: made with Bhuiyan (Dict Enc + RLE)
def lossless_compression(passed_data):
    print("After Encoding the data:")
    compressd_data, dictionary = dictionary_encoding(passed_data)
    print("compressd_data:", compressd_data, "and dictionary: ", dictionary)

    rle = run_length_encoding_dict(compressd_data)
    print("\n\t Finally After RLE the compression Data:", rle)

career_path = ["AI", "Django", "Django", "Odoo", "Django", "Research", "Research", "React JS", "Python", "Odoo", "Ai"]

print("Before compressing Given Original Data:")
print(career_path)

print("............  Combined Lossless Compression Algorithms with Dict Enc & RLE ............")
lossless_compression(career_path)
