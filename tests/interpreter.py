def load_file(file_path):
    with open(file_path, 'r') as file:
        code = file.read()
    return code

if __name__ == "__main__":
    file_path = "test.pgen"
    code = load_file(file_path)
    print(code)
