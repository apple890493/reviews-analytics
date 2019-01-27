data = []
count = 0
with open("reviews.txt", "r") as f:
	for line in f:
		data.append(line)
		count += 1#count = count +1
		if count % 1000 == 0:#%是用來求餘數1001/1000==1 ; 1007/1000==7
			print(len(data))
print(len(data)) #讀取總共有幾則
print(data[0])#索引標籤第一筆由0開始
print("---------------------")
print(data[1])


