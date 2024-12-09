def generate_numbers():
    with open("pass.txt", "w") as file:
        for length in range(8, 11):
            start = 10**(length - 1)
            end = 10**length
            for num in range(start, end):
                file.write(str(num) + "\n")

if __name__ == "__main__":
    generate_numbers()
