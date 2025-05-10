"""
part-2(Run Length Encoding): for compression without losing data:
"""


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


career_path = ["AI", "Django", "Django", "Odoo", "Django", "Research", "Research", "React JS", "Python", "Odoo", "Ai"]
print("The Given Origin Data:", career_path)

rle = run_length_encoding_dict(career_path)
print("After RLE the compression Data:", rle)