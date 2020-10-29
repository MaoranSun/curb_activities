# Curb model for raspberry pi

This curb activities model is trained with custom dataset on [AlexeyAB's YOLO v4 implementation](https://github.com/AlexeyAB/darknet)

## Prerequisites

* Python version: 3.7.3
* on Linux **GCC or Clang**, on Windows **MSVC 2017/2019** https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=Community

#### Optional dependencies
* **CMake >= 3.12**: https://cmake.org/download/
* **CUDA >= 10.0**: https://developer.nvidia.com/cuda-toolkit-archive (on Linux do [Post-installation Actions](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#post-installation-actions))
* **OpenCV >= 2.4**: use your preferred package manager (brew, apt), build from source using [vcpkg](https://github.com/Microsoft/vcpkg) or download from [OpenCV official site](https://opencv.org/releases.html) (on Windows set system variable `OpenCV_DIR` = `C:\opencv\build` - where are the `include` and `x64` folders [image](https://user-images.githubusercontent.com/4096485/53249516-5130f480-36c9-11e9-8238-a6e82e48c6f2.png))
* **cuDNN >= 7.0** https://developer.nvidia.com/rdp/cudnn-archive (on **Linux** copy `cudnn.h`,`libcudnn.so`... as desribed here https://docs.nvidia.com/deeplearning/sdk/cudnn-install/index.html#installlinux-tar , on **Windows** copy `cudnn.h`,`cudnn64_7.dll`, `cudnn64_7.lib` as desribed here https://docs.nvidia.com/deeplearning/sdk/cudnn-install/index.html#installwindows )
* **GPU with CC >= 3.0**: https://en.wikipedia.org/wiki/CUDA#GPUs_supported


## Compilation

For Raspberry Pi, the default settings should work. For other environments, make changes to `Makefile` according to [this link](https://github.com/AlexeyAB/darknet#how-to-compile-on-linux-using-make)

* Do `make` in the darknet directory

* `pip install -r requirements.txt`

## Usage

#### run inference with webcam:

This will save annotated video file to `data/testvideo/curb.avi`, store results to `data/result/curb_{start time}.sqlite`. If you don't want saved video or sqlite file, just remove the flags.

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

#### run inference with a video file:

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
