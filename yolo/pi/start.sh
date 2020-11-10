#!/bin/bash
python3 darknet_curb_video.py \
	--out_filename=data/testvideo/curb.avi \
	--out_db=data/result/curb \
  	--topic=RATP/Entries \
	--weights=weights/yolov4-tiny-curb_best.weights \
	--dont_show \
	--ext_output \
	--config_file=cfg/yolov4-tiny-curb.cfg \
	--data_file=data/curb.data
