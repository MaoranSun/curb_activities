# Curb Dataset

This curb activity dataset contains four format: VIA JSON format, VOC format, tfrecords and YOLO format.
Latest dataset contains 15 classes: Walk Stand, Car, Van, Bus, Motorcycle, Babysitting, Riding bike, Children, Skateboarder, Taxi, Queuing, Sit, Truck, Performance, Riding scooter

## Conversion between formats:
**VIA to VOC:**
path: /home/maoransu/mrcnn/Mask_RCNN/samples/scooter_mask/VIA-2-VOC.ipynb
**VOC to tfrecords:**
path: /home/maoransu/SSD_Mobile/models/research/object_detection/dataset_tools/create_pascal_tf_record.py
example usage:
`python dataset_tools/create_pascal_tf_record.py \
        --data_dir=/home/maoransu/SSD_Mobile/models/research/object_detection/datasets/CURB_DATASET \
        --year=VOC2012 \
        --output_path=/home/maoransu/SSD_Mobile/models/research/object_detection/datasets/CURB_TF/curb_train.record \
        --set=train \
        --label_map_path=/home/maoransu/SSD_Mobile/models/research/object_detection/data/curb_label_map.pbtxt`
**tfrecords to YOLO**
path: /home/maoransu/curb_activities/datasets/tf_to_yolo.ipynb


## VIA JSON
**Training and validation data are stored in seperate folder.**
Path: /home/maoransu/mrcnn/Mask_RCNN/samples/scooter_mask/dataset1700_combine03/Training_data
Training data label path: /home/maoransu/mrcnn/Mask_RCNN/samples/scooter_mask/dataset1700_combine03/Training_data/train/annotations.json
Training data image path: /home/maoransu/mrcnn/Mask_RCNN/samples/scooter_mask/dataset1700_combine03/Training_data/train/
Validation data label path: /home/maoransu/mrcnn/Mask_RCNN/samples/scooter_mask/dataset1700_combine03/Training_data/val/annotations.json
Validation data image path: /home/maoransu/mrcnn/Mask_RCNN/samples/scooter_mask/dataset1700_combine03/Training_data/val/

## VOC format
**Training and validation data are stored in seperate folder.**
Path: /home/maoransu/SSD_Mobile/models/research/object_detection/datasets/CURB_DATASET/
Training data label path: /home/maoransu/mrcnn/Mask_RCNN/samples/scooter_mask/dataset1700_combine03/Training_data/train/annotations.json
Training data image path: /home/maoransu/mrcnn/Mask_RCNN/samples/scooter_mask/dataset1700_combine03/Training_data/train/
Validation data label path: /home/maoransu/mrcnn/Mask_RCNN/samples/scooter_mask/dataset1700_combine03/Training_data/val/annotations.json
Validation data image path: /home/maoransu/mrcnn/Mask_RCNN/samples/scooter_mask/dataset1700_combine03/Training_data/val/
