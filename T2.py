# 打开文件并读取其中的内容
with open('file/test.txt', 'r') as f:
    text = f.read()
    print(text)

# 打开文件并将一些文本写入其中
with open('file/test1.txt', 'a') as c:
    text = '\nthis is a demo!\n'
    c.write(text)
