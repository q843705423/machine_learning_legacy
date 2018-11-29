import os.path
import re

# we can use csv file to get all label name,and then
# we can auto to change some file to for our quickily start train
# o data/object-detection.pbtxt
# o ./generate_tfrecord.py
# o config/pipeline.config

def getlabels_by_filename(fatherPath,filename):
	#print(filename)
	file = open(fatherPath+"/"+filename,"r")
	lines = file.readlines()
	names = []
	for line in lines:
		if line.find("<name>")!=-1:
			#print(line)
			name = re.match(".*<name>(.*)</name>.*",line,0).group(1)
			#print("name="+name.strip())
			names.append(name.strip())
	return names
	
def images_train_foreach_and_get_labels(image_train_dir):
	files = os.listdir(image_train_dir)
	labels = [];
	for f in files:
		if f.find(".xml")!=-1:
			some_label = getlabels_by_filename(image_train_dir,f)
			labels.extend(some_label)
			labels = list(set(labels))
	#print(labels)
	return labels
	
def create_or_replace_object_detection_pbtxt(labels):
	count = 0
	file = open("data/object-detection.pbtxt","w")	
	for label in labels:
		count = count + 1
		file.writelines(
		["item {\n",
		"\tid : "+str(count)+"\n",		
		"\tname :\""+label+"\"\n",
		"}\n\n"])
	file.close()
			
def generate_tfrecord_get_message_for_deal(labels):
	file = open("generate_tfrecord.py","r")
	wFile = open("g.txt","w")
	lines = file.readlines()
	#print(lines)
	flag_can_remove = False
	for line in lines:
		if line.find("class_text_to_int")!=-1:
			flag_can_remove = True
			wFile.write(line)
			count = 0
			for label in labels:
				count = count + 1;	
				if count==1:
					wFile.write("\tif row_label == '"+label+"':\n")
				else:
					wFile.write("\telif row_label == '"+label+"':\n")
				
				wFile.write("\t\treturn "+str(count)+"\n")
		elif line.find("else")!=-1:
			flag_can_remove = False
		if flag_can_remove==False:
			wFile.write(line)
	wFile.close()
	file.close()

	
def copy_file(sourcePath,targetPath):
	source = open(sourcePath,"r")
	target = open(targetPath,"w")
	target.writelines(source.readlines())
	target.close()
	source.close()
	
	
labels = images_train_foreach_and_get_labels("images/train")
print(labels)
create_or_replace_object_detection_pbtxt(labels)
generate_tfrecord_get_message_for_deal(labels)
copy_file("g.txt","ge.txt")











