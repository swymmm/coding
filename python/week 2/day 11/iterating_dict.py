student={"name":"swayam", "age":21, "city":"nipani"}

#iterating over key(default)
for key in student:
    print(key)

#iterating over values
for value in student.values():
    print(value)

#iterating over key:value pairs   most useful
for key, value in student.items():
    print(f"{key} : {value}")