import os
os.mkdir("data")
for i in range(1, 100):
    os.mkdir(f"data/Day{i+1}")

folders = os.listdir("data")
print(folders)

for folder in folders:
    print(folder)