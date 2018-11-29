"""
Usage:
  # From tensorflow/models/
  # Create train data:
  python generate_tfrecord.py --csv_input=data/train_labels.csv  --output_path=train.record

  # Create test data:
  python generate_tfrecord.py --csv_input=data/test_labels.csv  --output_path=test.record
"""
from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

import os
import io
import pandas as pd
import tensorflow as tf

from PIL import Image
from object_detection.utils import dataset_util
from collections import namedtuple, OrderedDict

flags = tf.app.flags
flags.DEFINE_string('csv_input', '', 'Path to the CSV input')
flags.DEFINE_string('output_path', '', 'Path to output TFRecord')
FLAGS = flags.FLAGS


# TO-DO replace this with label map
# TO-DO replace this with label map
def class_text_to_int(row_label):
	if row_label == 'japanese_1':
		return 1
	elif row_label == 'japanese_2':
		return 2
	elif row_label == 'japanese_3':
		return 3
	elif row_label == 'japanese_4':
		return 4
	elif row_label == 'japanese_5':
		return 5
	elif row_label == 'japanese_6':
		return 6
	elif row_label == 'japanese_7':
		return 7
	elif row_label == 'japanese_8':
		return 8
	elif row_label == 'japanese_9':
		return 9
	elif row_label == 'japanese_10':
		return 10
	elif row_label == 'japanese_11':
		return 11
	elif row_label == 'japanese_12':
		return 12
	elif row_label == 'japanese_13':
		return 13
	elif row_label == 'japanese_14':
		return 14
	elif row_label == 'japanese_15':
		return 15
	elif row_label == 'japanese_16':
		return 16
	elif row_label == 'japanese_17':
		return 17
	elif row_label == 'japanese_18':
		return 18
	elif row_label == 'japanese_19':
		return 19
	elif row_label == 'japanese_20':
		return 20
	elif row_label == 'japanese_21':
		return 21
	elif row_label == 'japanese_22':
		return 22
	elif row_label == 'japanese_23':
		return 23
	elif row_label == 'japanese_24':
		return 24
	elif row_label == 'japanese_25':
		return 25
	elif row_label == 'japanese_26':
		return 26
	elif row_label == 'japanese_27':
		return 27
	elif row_label == 'japanese_28':
		return 28
	elif row_label == 'japanese_29':
		return 29
	elif row_label == 'japanese_30':
		return 30
	elif row_label == 'japanese_31':
		return 31
	elif row_label == 'japanese_32':
		return 32
	elif row_label == 'japanese_33':
		return 33
	elif row_label == 'japanese_34':
		return 34
	elif row_label == 'japanese_35':
		return 35
	elif row_label == 'japanese_36':
		return 36
	elif row_label == 'japanese_37':
		return 37
	elif row_label == 'japanese_38':
		return 38
	elif row_label == 'japanese_39':
		return 39
	elif row_label == 'japanese_40':
		return 40
	elif row_label == 'japanese_41':
		return 41
	elif row_label == 'japanese_42':
		return 42
	elif row_label == 'japanese_43':
		return 43
	elif row_label == 'japanese_44':
		return 44
	elif row_label == 'japanese_45':
		return 45
	elif row_label == 'japanese_46':
		return 46
	elif row_label == 'japanese_47':
		return 47
	elif row_label == 'japanese_48':
		return 48
	elif row_label == 'japanese_49':
		return 49
	elif row_label == 'japanese_50':
		return 50
	elif row_label == 'japanese_51':
		return 51
	elif row_label == 'japanese_52':
		return 52
	elif row_label == 'japanese_53':
		return 53
	elif row_label == 'japanese_54':
		return 54
	elif row_label == 'japanese_55':
		return 55
	elif row_label == 'japanese_56':
		return 56
	elif row_label == 'japanese_57':
		return 57
	elif row_label == 'japanese_58':
		return 58
	elif row_label == 'japanese_59':
		return 59
	elif row_label == 'japanese_60':
		return 60
	elif row_label == 'japanese_61':
		return 61
	elif row_label == 'japanese_62':
		return 62
	elif row_label == 'japanese_63':
		return 63
	elif row_label == 'japanese_64':
		return 64
	elif row_label == 'japanese_65':
		return 65
	elif row_label == 'japanese_66':
		return 66
	elif row_label == 'japanese_67':
		return 67
	elif row_label == 'japanese_68':
		return 68
	elif row_label == 'japanese_69':
		return 69
	elif row_label == 'japanese_70':
		return 70
	elif row_label == 'japanese_71':
		return 71
	elif row_label == 'japanese_72':
		return 72
	elif row_label == 'japanese_73':
		return 73
	elif row_label == 'japanese_74':
		return 74
	elif row_label == 'japanese_75':
		return 75
	elif row_label == 'japanese_76':
		return 76
	elif row_label == 'japanese_77':
		return 77
	elif row_label == 'japanese_78':
		return 78
	elif row_label == 'japanese_79':
		return 79
	elif row_label == 'japanese_80':
		return 80
	elif row_label == 'japanese_81':
		return 81
	elif row_label == 'japanese_82':
		return 82
	elif row_label == 'japanese_83':
		return 83
	elif row_label == 'japanese_84':
		return 84
	elif row_label == 'japanese_85':
		return 85
	elif row_label == 'japanese_86':
		return 86
	elif row_label == 'japanese_87':
		return 87
	elif row_label == 'japanese_88':
		return 88
	elif row_label == 'japanese_89':
		return 89
	elif row_label == 'japanese_90':
		return 90
	elif row_label == 'japanese_91':
		return 91
	elif row_label == 'japanese_92':
		return 92
	elif row_label == 'japanese_93':
		return 93
	elif row_label == 'japanese_94':
		return 94
	elif row_label == 'japanese_95':
		return 95
	elif row_label == 'japanese_96':
		return 96
	elif row_label == 'japanese_97':
		return 97
	elif row_label == 'japanese_98':
		return 98
	elif row_label == 'japanese_99':
		return 99
	elif row_label == 'japanese_100':
		return 100
	elif row_label == 'japanese_101':
		return 101
	elif row_label == 'japanese_102':
		return 102
	elif row_label == 'japanese_103':
		return 103
	elif row_label == 'japanese_104':
		return 104
	elif row_label == 'japanese_105':
		return 105
	elif row_label == 'japanese_106':
		return 106
	elif row_label == 'japanese_107':
		return 107
	elif row_label == 'japanese_108':
		return 108
	elif row_label == 'japanese_109':
		return 109
	elif row_label == 'japanese_110':
		return 110
	elif row_label == 'japanese_111':
		return 111
	elif row_label == 'japanese_112':
		return 112
	elif row_label == 'japanese_113':
		return 113
	elif row_label == 'japanese_114':
		return 114
	elif row_label == 'japanese_115':
		return 115
	elif row_label == 'japanese_116':
		return 116
	elif row_label == 'japanese_117':
		return 117
	elif row_label == 'japanese_118':
		return 118
	elif row_label == 'japanese_119':
		return 119
	elif row_label == 'japanese_120':
		return 120
	elif row_label == 'japanese_121':
		return 121
	elif row_label == 'japanese_122':
		return 122
	elif row_label == 'japanese_123':
		return 123
	elif row_label == 'japanese_124':
		return 124
	elif row_label == 'japanese_125':
		return 125
	elif row_label == 'japanese_126':
		return 126
	elif row_label == 'japanese_127':
		return 127
	elif row_label == 'japanese_128':
		return 128
	elif row_label == 'japanese_129':
		return 129
	elif row_label == 'japanese_130':
		return 130
	elif row_label == 'japanese_131':
		return 131
	elif row_label == 'japanese_132':
		return 132
	elif row_label == 'japanese_133':
		return 133
	elif row_label == 'japanese_134':
		return 134
	elif row_label == 'japanese_135':
		return 135
	elif row_label == 'japanese_136':
		return 136
	elif row_label == 'japanese_137':
		return 137
	elif row_label == 'japanese_138':
		return 138
	elif row_label == 'japanese_139':
		return 139
	elif row_label == 'japanese_140':
		return 140


	else:
		None
def split(df, group):
    data = namedtuple('data', ['filename', 'object'])
    gb = df.groupby(group)
    return [data(filename, gb.get_group(x)) for filename, x in zip(gb.groups.keys(), gb.groups)]


def create_tf_example(group, path):
    with tf.gfile.GFile(os.path.join(path, '{}'.format(group.filename)), 'rb') as fid:
        encoded_jpg = fid.read()
    encoded_jpg_io = io.BytesIO(encoded_jpg)
    image = Image.open(encoded_jpg_io)
    width, height = image.size

    filename = group.filename.encode('utf8')
    image_format = b'jpg'
    xmins = []
    xmaxs = []
    ymins = []
    ymaxs = []
    classes_text = []
    classes = []

    for index, row in group.object.iterrows():
        xmins.append(row['xmin'] / width)
        xmaxs.append(row['xmax'] / width)
        ymins.append(row['ymin'] / height)
        ymaxs.append(row['ymax'] / height)
        classes_text.append(row['class'].encode('utf8'))
        classes.append(class_text_to_int(row['class']))

    tf_example = tf.train.Example(features=tf.train.Features(feature={
        'image/height': dataset_util.int64_feature(height),
        'image/width': dataset_util.int64_feature(width),
        'image/filename': dataset_util.bytes_feature(filename),
        'image/source_id': dataset_util.bytes_feature(filename),
        'image/encoded': dataset_util.bytes_feature(encoded_jpg),
        'image/format': dataset_util.bytes_feature(image_format),
        'image/object/bbox/xmin': dataset_util.float_list_feature(xmins),
        'image/object/bbox/xmax': dataset_util.float_list_feature(xmaxs),
        'image/object/bbox/ymin': dataset_util.float_list_feature(ymins),
        'image/object/bbox/ymax': dataset_util.float_list_feature(ymaxs),
        'image/object/class/text': dataset_util.bytes_list_feature(classes_text),
        'image/object/class/label': dataset_util.int64_list_feature(classes),
    }))
    return tf_example


def main(_):
    writer = tf.python_io.TFRecordWriter(FLAGS.output_path)
    path = os.path.join(os.getcwd(), 'images')
    examples = pd.read_csv(FLAGS.csv_input)
    grouped = split(examples, 'filename')
    for group in grouped:
        tf_example = create_tf_example(group, path)
        writer.write(tf_example.SerializeToString())

    writer.close()
    output_path = os.path.join(os.getcwd(), FLAGS.output_path)
    print('Successfully created the TFRecords: {}'.format(output_path))


if __name__ == '__main__':
    tf.app.run()