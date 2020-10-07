# Yolo

This part records the process of training curb model on YOLO. We tried yolo v4 and yolo v4 tiny.

## YOLO V4:
### Train:
'./darknet detector train data/curb.data cfg/yolov4-curb.cfg weights/yolov4.conv.137 -gpus 0,1 -dont_show -mjpeg_port 8894 -map'

### Validate:
'./darknet detector map data/curb.data cfg/yolov4-curb.cfg backup/yolov4-curb_6000.weights'

### Inference:
'./darknet test data/curb.data cfg/yolov4-curb.cfg backup/yolov4-curb_6000.weights data/curb/val_0.jpg'

'./darknet detector test data/curb.data cfg/yolov4-curb.cfg backup/yolov4-curb_6000.weights -dont_show -ext_output < data/val.txt > result.txt'

## YOLO V4 tiny:
### Train:
'./darknet detector train data/curb.data cfg/yolov4-tiny-curb.cfg weights/yolov4-tiny.conv.29 -gpus 0,1 -dont_show -mjpeg_port 8894 -map'

### Validate:


### Inference:
