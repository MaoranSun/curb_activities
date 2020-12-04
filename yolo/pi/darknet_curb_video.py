import argparse
import os
import glob
import random
import darknet
import time
import cv2
import numpy as np
import datetime
import sqlite3
import paho.mqtt.client as mqtt
import json


def parser():
    parser = argparse.ArgumentParser(description="YOLO Object Detection")
    parser.add_argument("--input", type=str, default=0,
                        help="video source. If empty, uses webcam 0 stream")
    parser.add_argument("--out_filename", type=str,
                        help="inference video name. Not saved if empty")
    parser.add_argument("--out_img", type=str,
                        help="inference image folder. Not saved if empty")
    parser.add_argument("--save_infer", action='store_true',
                        help="save inferenced video or raw video")
    parser.add_argument("--out_db", type=str,
                        help="inference result database name. Not saved if empty")
    parser.add_argument("--vflip", action='store_true',
                        help="vertical flip the video")
    parser.add_argument("--weights", default="yolov4.weights",
                        help="yolo weights path")
    parser.add_argument("--dont_show", action='store_true',
                        help="windown inference display. For headless systems")
    parser.add_argument("--ext_output", action='store_true',
                        help="display bbox coordinates of detected objects")
    parser.add_argument("--save_labels", action='store_true',
                        help="save detections bbox for each image in yolo format")
    parser.add_argument("--config_file", default="./cfg/yolov4.cfg",
                        help="path to config file")
    parser.add_argument("--data_file", default="./cfg/coco.data",
                        help="path to data file")
    parser.add_argument("--thresh", type=float, default=.25,
                        help="remove detections with confidence below this value")
    parser.add_argument("--topic", type=str, default="RATP/Entries",
                        help="topic to publish MQTT message")
    return parser.parse_args()

def str2int(video_path):
    """
    argparse returns and string althout webcam uses int (0, 1 ...)
    Cast to int if needed
    """
    try:
        return int(video_path)
    except ValueError:
        return video_path
    
def set_saved_video(input_video, output_video, size, fps):
    """
    """
    fourcc = cv2.VideoWriter_fourcc(*"MJPG")
    #fps = input_video.get(cv2.CAP_PROP_FPS)
    #fps = int(input_video.get(cv2.CAP_PROP_FPS))
    video = cv2.VideoWriter(output_video.replace('.', datetime.datetime.now(datetime.timezone.utc).astimezone().isoformat("T", "seconds")+'.').replace(':', '_'), fourcc, fps, size)
    return video
    
def image_detection(frame, network, class_names, class_colors, thresh):
    # Darknet doesn't accept numpy images.
    # Create one with image we reuse for each detect
    width = darknet.network_width(network)
    height = darknet.network_height(network)
    darknet_image = darknet.make_image(width, height, 3)

    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image_resized = cv2.resize(image_rgb, (width, height),
                               interpolation=cv2.INTER_LINEAR)

    darknet.copy_image_from_bytes(darknet_image, image_resized.tobytes())
    detections = darknet.detect_image(network, class_names, darknet_image, thresh=thresh)
    darknet.free_image(darknet_image)
    image = darknet.draw_boxes(detections, image_resized, class_colors)
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB), detections

def count_result(detections, class_names):
    count_dict = {}
    return_dict = {'sampleTime': datetime.datetime.now(datetime.timezone.utc).astimezone().isoformat("T", "seconds")}
    
    for cls in class_names:
        count_dict[cls] = 0
    for detection in detections:
        count_dict[detection[0]] += 1
    for key in count_dict:
        return_dict["count" + key.title().replace(" ", "")] = count_dict[key]

    return return_dict
    
def main():
    # read user's input
    args = parser()
    print("publish to ", args.topic)
    # initialize darknet
    network, class_names, class_colors = darknet.load_network(
            args.config_file,
            args.data_file,
            args.weights,
            batch_size=1
        )
    # initialize mqtt client and connect to broker
    client = mqtt.Client()
    client.connect("localhost")
    
    # read input, webcam or video file
    input_path = str2int(args.input)
    cap = cv2.VideoCapture(input_path)
    
    # if using webcam, set video fps, width and height
    if type(input_path) == int:
        cap.set(cv2.CAP_PROP_FPS, 1)
        cap.set(3, 416)
        cap.set(4, 416)
    
    # get video properties
    fps = cap.get(cv2.CAP_PROP_FPS)
    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # record when to take photo
    # take a shot every # seconds
    seconds = 3
    multiplier = int(fps * seconds)
    
    # set saved video format and properties
    if args.out_filename is not None:
        video = set_saved_video(cap, args.out_filename, (w, h), 1 / seconds)
    if args.out_img is not None:
        image_folder = args.out_img + "/" + datetime.datetime.now(datetime.timezone.utc).astimezone().isoformat("T", "seconds").replace(':', '_')
        if not os.path.exists(image_folder):
            os.makedirs(image_folder)
    
    # Init sql
    if args.out_db is not None:
        conn = sqlite3.connect(args.out_db + datetime.datetime.now(datetime.timezone.utc).astimezone().isoformat("T", "seconds").replace(':', '_') + '.sqlite')
        cur = conn.cursor()
        cur.execute('CREATE TABLE inference_result (frameID INTEGER, time TEXT, Walk_stand INTEGER, Car INTEGER, Van INTEGER, Bus INTEGER, Motorcycle INTEGER, Riding_bike INTEGER, Children INTEGER, Skateboarder INTEGER, Queuing INTEGER, Sit INTEGER, Truck INTEGER, Riding_scooter INTEGER)')
        conn.commit()
        
    count = 0
    while cap.isOpened():
        count += 1
        ret, frame = cap.read()
        
        if not ret:
            break
        frameID = count
        if frameID % multiplier == 0:
            if args.vflip:
                frame = cv2.flip(frame, 0)
            anno_image, detections = image_detection(frame, network, class_names, class_colors, .25)
            darknet.print_detections(detections, args.ext_output)
            
            # format result
            re = count_result(detections, class_names)
            # send result to mqtt
            client.publish(args.topic, json.dumps(re))
            
            # Store result to database
            if args.out_db is not None:
                # save result to database
                cur.execute('INSERT INTO inference_result (frameID, time, Walk_stand, Car, Van, Bus, Motorcycle, Riding_bike, Children, Skateboarder, Queuing, Sit, Truck, Riding_scooter) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?)', [frameID, re['sampleTime'], re["count" + class_names[0].title().replace(" ", "")], re["count" + class_names[1].title().replace(" ", "")], re["count" + class_names[2].title().replace(" ", "")], re["count" + class_names[3].title().replace(" ", "")], re["count" + class_names[4].title().replace(" ", "")], re["count" + class_names[5].title().replace(" ", "")], re["count" + class_names[6].title().replace(" ", "")], re["count" + class_names[7].title().replace(" ", "")], re["count" + class_names[8].title().replace(" ", "")], re["count" + class_names[9].title().replace(" ", "")], re["count" + class_names[10].title().replace(" ", "")], re["count" + class_names[11].title().replace(" ", "")]])
                conn.commit()
            
            # show image
            if not args.dont_show:
                cv2.imshow('Inference', frame)
            
            # write video to file
            if args.out_filename is not None:
                if args.save_infer:
                    anno_image = cv2.resize(anno_image, (w, h),
                        interpolation=cv2.INTER_LINEAR)
                    video.write(anno_image)
                else:
                    video.write(frame)
            
            # write images to folder
            if args.out_img is not None:
                cv2.imwrite(image_folder + "/" + datetime.datetime.now(datetime.timezone.utc).astimezone().isoformat("T", "seconds").replace(':', '_') + ".jpg", frame)
                    
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    video.release()
    cv2.destroyAllWindows()
    
if __name__ == '__main__':
    main()


