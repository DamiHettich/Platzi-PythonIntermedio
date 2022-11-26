def read():
    numbers = []
    with open("./numbers_file.txt", "r", encoding="utf-8") as f:
        for line in f:
            numbers.append(float(line))
    print(numbers)

def write():
    names = ['antonio','belen','cristina','dami','ernesto']
    with open('./names_file.txt', 'w', encoding='utf-8') as wf :
        for element in names:
            wf.write(element)
            wf.write("\n")

def run():
    read()

if __name__ == "__main__":
    run()