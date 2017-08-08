# -*- coding: utf8 -*-
# coding: utf8

import os

DATA_DIR = "ir_hw/wrd/"
file_data = []
for filename in os.listdir(DATA_DIR):
	print "Loading: %s" % filename
	loadFile = open(os.path.join(DATA_DIR, filename), 'rb')
	file_data.append(loadFile.read())
	k = 0
	file_allwords = open("wrd/"+filename)#"wrd/"+filename
	arr_words=[]
	i = 0
	for line in file_allwords:	     
		i+=1#總行數=總字詞數
		arr_words.append(line)
		print i,"th word is:"+line
		print "i is:",i
		st = arr_words[0]
		total = 0
		k+=1
		tffile = open('tf_result/'+filename+'_tf.txt','w')
		tffile.write('word,tf\n')
		n = 0
		total = 0
		while n <= (i-1) :
			firw = str((arr_words[n].split(' ')[0])).decode('string_escape')
			print (n+1),"th firw is:",firw
			secw = str((arr_words[n].split(' ')[1])).decode('string_escape')
			total += int(secw)
			print (n+1),"th secw is:",secw
			print "total =",total# float only with float can caculate
			n += 1
		n2 = 0
		total2 = float(total)
		print "file Name:"+filename
		while n2 <= (i-1) :
			firw2 = str((arr_words[n2].split(' ')[0])).decode('string_escape')
			print (n2+1),"th word write to file:"+firw2
			tffile.write(firw2) #file format
			tffile.write(',') #file format
			secw2 = str((arr_words[n2].split(' ')[1])).decode('string_escape')
			t = float(secw2) #converet to float type
			tf =  round((t/total2),3) #catch .001
			tffile.write(str(tf)) #file format
			tffile.write('\n') #file format
			print "what I writed in file:"+firw2+","+str(tf)
			print "(total is:"+str(total2)+"; t is:"+str(t)+"; tf is:"+str(tf)+")"
			n2+=1
	tffile.close()

	loadFile.close()