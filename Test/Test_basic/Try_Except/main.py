#bai 3:
# while 1:
#     n = input()
#     if n == "q": break
#     try:
#         print(float(n))
#     except ValueError:
#         print("ValueError")

#bai 4:

def DemTu (file):
    try:
        with open (file) as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {file} doesn't exist")
    else:
        words = contents.split()
        print(f"{file}: {len(words)} words")

filenames = ['guest.txt', 'file_name.txt']
for file in filenames:
    DemTu(file)