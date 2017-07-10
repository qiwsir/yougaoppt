#http://yocomedia.oss-cn-shanghai.aliyuncs.com/znkz2/12/1.JPG
pic_dict = {15:15, 16:14, 17:13, 18:12, 19:12, 20:12, 21:15, 22:27, 23:24, 24:22, 25:13 }

pic_head = "http://yocomedia.oss-cn-shanghai.aliyuncs.com/znkz2"

md_head = "znkz2_"

for k,v in pic_dict.items():
    pic_number = [i+1 for i in range(v)]
    pic_dir = pic_head + "/" + str(k)
    md_name = md_head + str(k) + ".md"
    f = open(md_name, "w")
    for i in pic_number:
        pic = pic_dir + "/" + str(i) + ".JPG"
        content = "[slide]\n![](" + pic + ")\n"
        f.write(content)
    f.close()

print("finished all")

