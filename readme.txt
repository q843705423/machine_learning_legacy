
使用前提:
--------------------------------------------------------------------------------------
python3.6 

models (https://github.com/tensorflow/models)
 
protoc (https://github.com/protocolbuffers/protobuf/releases)
--------------------------------------------------------------------------------------
介绍：
本项目是tensorflow 的物品识别模块的一个基本套路。
分成几块，
- config
- data
- graph
- images
- test_images
- training
- ....*.py
其中使用方式也非常简单。
将其clone下来以后，把它放入 object_dection的legacy目录下，替换掉原来的东西.

使用方式：
1.把protoc解压
2.到reacher目录下运行以下命令
D:\code\python\protoc_3.4\bin\protoc object_detection/protos/*.proto --python_out=.
3.配置slim配置到环境变量中

以下命令是将images的train和test目录里的jpg及xml信息转换成csv文件
python xml_to_csv.py 

以下命令是将csv文件转换成tfrecord记录集
python generate_tfrecord.py --csv_input=data/test_labels.csv --output_path=data/test.record
python generate_tfrecord.py --csv_input=data/train_labels.csv --output_path=data/train.record