# 打开输入文件
with open("file/fruitcount.txt", "r") as input_file:
    # 创建一个字典来存储水果和数量
    fruit_counts = {}

    # 逐行读取文件
    for line in input_file:
        # 按空格分割每行，并将水果名称和数量存储到字典中
        parts = line.strip().split(" ")
        fruit = parts[0]
        count = int(parts[1])
        if fruit in fruit_counts:
            fruit_counts[fruit] += count
        else:
            fruit_counts[fruit] = count

# 打开输出文件
with open("file/fruit-countOut.txt", "w") as output_file:
    # 将每个水果的总数写入输出文件
    for fruit, count in fruit_counts.items():
        output_file.write("{} {}\n".format(fruit, count))
