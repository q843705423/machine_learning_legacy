
ʹ��ǰ��:
--------------------------------------------------------------------------------------
python3.6 

models (https://github.com/tensorflow/models)
 
protoc (https://github.com/protocolbuffers/protobuf/releases)
--------------------------------------------------------------------------------------
���ܣ�
����Ŀ��tensorflow ����Ʒʶ��ģ���һ��������·��
�ֳɼ��飬
- config
- data
- graph
- images
- test_images
- training
- ....*.py
����ʹ�÷�ʽҲ�ǳ��򵥡�
����clone�����Ժ󣬰������� object_dection��legacyĿ¼�£��滻��ԭ���Ķ���.

ʹ�÷�ʽ��
1.��protoc��ѹ
2.��reacherĿ¼��������������
D:\code\python\protoc_3.4\bin\protoc object_detection/protos/*.proto --python_out=.
3.����slim���õ�����������

���������ǽ�images��train��testĿ¼���jpg��xml��Ϣת����csv�ļ�
python xml_to_csv.py 

���������ǽ�csv�ļ�ת����tfrecord��¼��
python generate_tfrecord.py --csv_input=data/test_labels.csv --output_path=data/test.record
python generate_tfrecord.py --csv_input=data/train_labels.csv --output_path=data/train.record