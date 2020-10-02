# Curb Dataset

This curb activity dataset contains four format: [VIA JSON format](https://github.com/MaoranSun/curb_activities/tree/master/datasets#via-json), [VOC format](https://github.com/MaoranSun/curb_activities/tree/master/datasets#voc-format), [tfrecords](https://github.com/MaoranSun/curb_activities/tree/master/datasets#tfrecords) and [YOLO format](https://github.com/MaoranSun/curb_activities/tree/master/datasets#yolo).

Latest dataset contains 15 classes: **Walk Stand, Car, Van, Bus, Motorcycle, Babysitting, Riding bike, Children, Skateboarder, Taxi, Queuing, Sit, Truck, Performance, Riding scooter**

## Conversion between formats:
### VIA to VOC:

path: /home/maoransu/mrcnn/Mask_RCNN/samples/scooter_mask/VIA-2-VOC.ipynb

### VOC to tfrecords:
path: /home/maoransu/SSD_Mobile/models/research/object_detection/dataset_tools/create_pascal_tf_record.py

example usage:

`python dataset_tools/create_pascal_tf_record.py \
        --data_dir=/home/maoransu/SSD_Mobile/models/research/object_detection/datasets/CURB_DATASET \
        --year=VOC2012 \
        --output_path=/home/maoransu/SSD_Mobile/models/research/object_detection/datasets/CURB_TF/curb_train.record \
        --set=train \
        --label_map_path=/home/maoransu/SSD_Mobile/models/research/object_detection/data/curb_label_map.pbtxt`
        
### tfrecords to YOLO

path: /home/maoransu/curb_activities/datasets/tf_to_yolo.ipynb


## VIA JSON

**Training and validation data are stored in seperate folder.**

**Path:** /home/maoransu/mrcnn/Mask_RCNN/samples/scooter_mask/dataset1700_combine03/Training_data

## VOC format

**Path:** /home/maoransu/SSD_Mobile/models/research/object_detection/datasets/CURB_DATASET/

## tfrecords

**Path:** /home/maoransu/SSD_Mobile/models/research/object_detection/datasets/CURB_TF/

## YOLO

**Path:** /home/maoransu/yolo/darknet/data/curb
