"""



python detect.py  --weights yolov5x.pt --source 'http://admin:admin@192.168.178.154:4747/video'
weight n s m l x

`source` 参数在 YOLOv5 检测功能中用来指定输入源。这个输入可以是多种不同的类型：

- **文件路径**：你可以传递一个图像文件（如 `.jpg`, `.png`）或视频文件（如 `.mp4`）的路径。
- **目录**：如果你想一次处理多个文件，可以传递一个存储多个图像或视频的目录路径。
- **URL**：你也可以通过网络URL来指定一个远程图片或视频资源。
- **文件模式（Glob）**：可以使用模式匹配来选择一个目录中符合特定规则的多个文件，如`images/*.jpg`。
- **屏幕捕获源** (`screen`)：在某些系统中，我们可以指定`screen`来从桌面捕获实时图像。
- **网络摄像头**：通常，传递数字`0`可以指定计算机上的默认网络摄像头作为实时视频输入源。如果你有多个摄像头，可以传递`1`, `2`, `3`等来选择其他摄像头。
'http://admin:admin@192.168.178.154:4747/video'

conf-thres 置信值
python detect.py --weights yolov5x.pt --conf-thres 0.8

iou-thres IOU阈值 越低框越少



"""