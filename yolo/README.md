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
For thresh = 0.25, precision = 0.62, recall = 0.67, mAP@0.50 = 0.54

| Category | ap | Category | ap |
| ----------- | ----------- | ----------- | ----------- |
| Walk Stand | 67.99% | Car | 67.99% |
| Van | 59.22% | Bus | 82.32% |
| Motorcycle | 73.56% | Riding bike | 65.18% |
| Children | 2.97% | Skateboarder | 62.71% |
| Queuing | 14.4% | Sit | 46.67% |
| Truck | 37.94% | Riding scooter | 66.57% |

## YOLO V4 tiny:
### Train:
`./darknet detector train data/curb.data cfg/yolov4-tiny-curb.cfg weights/yolov4-tiny.conv.29 -gpus 0,1 -dont_show -mjpeg_port 8894 -map`

### Validate:
`./darknet detector map data/curb.data cfg/yolov4-tiny-curb.cfg backup/yolov4-tiny-curb_best.weights`

### Inference:

### Performance:
For thresh = 0.25, precision = 0.57, recall = 0.48, mAP@0.50 = 0.38

| Category | ap | Category | ap |
| ----------- | ----------- | ----------- | ----------- |
| Walk Stand | 47.6% | Car | 51% |
| Van | 39.66% | Bus | 61.50% |
| Motorcycle | 56.83% | Riding bike | 48.69% |
| Children | 2.97% | Skateboarder | 43.44% |
| Queuing | 5.54% | Sit | 20.69% |
| Truck | 17.42% | Riding scooter | 59.41% |

