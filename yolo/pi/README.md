# Curb model for raspberry pi

### Compile on pi: using make

Just do `make` in the darknet directory

required python package: numpy, cv2, sqlite3, paho

### run inference with webcam:

This will save annotated video file to `data/testvideo/curb.avi`, store results to `data/result/curb_{start time}.sqlite`. If you don't want saved video file or sqlite, just remove the flags.

```
python3 darknet_curb_video.py \
--out_filename=data/testvideo/curb.avi \
--out_db=data/result/curb \
--weights=weights/yolov4-tiny-curb_best.weights \
--dont_show \
--ext_output \
--config_file=cfg/yolov4-tiny-curb.cfg \
--data_file=data/curb.data
```

### run inference with a video file:

```
python3 darknet_curb_video.py \
--input=data/testvideo/test.mp4 \
--out_filename=data/result/res.avi \
--out_db=data/result/curb \
--weights=weights/yolov4-tiny-curb_best.weights \
--dont_show \
--ext_output \
--config_file=cfg/yolov4-tiny-curb.cfg \
--data_file=data/curb.data
```
