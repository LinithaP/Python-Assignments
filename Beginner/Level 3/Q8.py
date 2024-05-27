'''
8. You need to write a function that accepts an encoded string as a parameter.
This string will contain a first name, last name, and an id. Values in the string can be separated by any number of zeros.
The id is a numeric value but will contain no zeros.
The function should parse the string and return a Python dictionary that contains the first name, last name, and id values.
For example: Input : “Robert000Smith000123” Output: { “first_name”: “Robert”, “last_name”: “Smith”, “id”: “123” }
'''


def decode_string(st):
    parts = st.split("0")
    result = [i.strip() for i in parts if i.strip()]

    # print(result)
    first_name = result[0]
    last_name = result[1]
    id_number = result[2]

    decoded_dict = {
        "first_name": first_name,
        "last_name": last_name,
        "id": id_number
    }
    return decoded_dict


print(decode_string("Robert000Smith000123"))