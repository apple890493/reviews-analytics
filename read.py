data = []
count = 0
with open("reviews.txt", "r") as f:
	for line in f:
		data.append(line)
		count += 1#count = count +1
		if count % 1000 == 0:#%是用來求餘數1001/1000==1 ; 1007/1000==7
			print(len(data))
print("檔案讀取完了,總共有", len(data), "筆資料")

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)

print("留言的平均長度為", sum_len/len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)#裝進去
print("一共有", len(new), "筆留言長度小於100")
print(new[0])
print(new[1])

good = []
for d in data:
	if "good" in d:
		good.append(d)
print("一共有", len(good), "筆留言有提及good")
print(good[0])

word_count = {}
for d in data:
	words = d.split()#為預設空白建,並會跳過不切割
	for word in words:
		if word in word_count:
			word_count[word] += 1 #累加
		else:
			word_count[word] = 1 #新增新的key進w_c字典
for word in word_count:
	if word_count[word] > 1000:
		print(word, word_count[word])

print(len(word_count))
print(word_count["good"])

while True:
	word = input("請問想查什麼字: ")
	if word == "q" or word == "Q":
		break
	if word in word_count:
		print(word, "出現過的次數為", word_count[word])
	else:
		print("沒有出現過喔!")
print("謝謝您的使用!")