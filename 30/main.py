# Day 30: manage exceptions

# File not found

# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key does {error_message} not exists.")
# else:
#     content = file.read()
#     print(content)
# finally:
    # file.close()
    # print("File was closed.")
    # raise KeyError("This is an error that I made up.")

# Raise own exceptions

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")

bmi = weight / height**2
print(bmi)
