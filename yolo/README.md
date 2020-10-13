# Yolo

This part records the process of training curb model on YOLO. We tried yolo v4 and yolo v4 tiny.

## YOLO V4:
### Train:
`./darknet detector train data/curb.data cfg/yolov4-curb.cfg weights/yolov4.conv.137 -gpus 0,1 -dont_show -mjpeg_port 8894 -map`

### Validate:
`./darknet detector map data/curb.data cfg/yolov4-curb.cfg backup/yolov4-curb_6000.weights`

### Inference:
`./darknet test data/curb.data cfg/yolov4-curb.cfg backup/yolov4-curb_6000.weights data/curb/val_0.jpg`

`./darknet detector test data/curb.data cfg/yolov4-curb.cfg backup/yolov4-curb_6000.weights -dont_show -ext_output < data/val.txt > result.txt`

### Performance:
For thresh = 0.25, precision = 0.62, recall = 0.67

| Category | ap |
| ----------- | ----------- |
| Walk Stand | 67.99% |
| Walk Stand | 67.99% |
| Walk Stand | 67.99% |

## YOLO V4 tiny:
### Train:
`./darknet detector train data/curb.data cfg/yolov4-tiny-curb.cfg weights/yolov4-tiny.conv.29 -gpus 0,1 -dont_show -mjpeg_port 8894 -map`

### Validate:
`./darknet detector map data/curb.data cfg/yolov4-tiny-curb.cfg backup/yolov4-tiny-curb_best.weights`

### Inference:

