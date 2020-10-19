# Mask RCNN models

This part records the process of training curb model on Mask RCNN.

## 44 class:
### Path:
home/maoransu/mrcnn/Mask_RCNN/samples/scooter_mask/dataset1700_combine01
### Train:
`./darknet detector train data/curb.data cfg/yolov4-curb.cfg weights/yolov4.conv.137 -gpus 0,1 -dont_show -mjpeg_port 8894 -map`

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

## 35 class:
### Train:
`./darknet detector train data/curb.data cfg/yolov4-tiny-curb.cfg weights/yolov4-tiny.conv.29 -gpus 0,1 -dont_show -mjpeg_port 8894 -map`

## 15 class:
### Train:
`./darknet detector train data/curb.data cfg/yolov4-tiny-curb.cfg weights/yolov4-tiny.conv.29 -gpus 0,1 -dont_show -mjpeg_port 8894 -map`

