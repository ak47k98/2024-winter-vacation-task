import torch
model = torch.hub.load("./","yolov5x",source="local")
img = "/home/ak47k98/class home for team/2024-winter-vacation-task/2024视觉寒假任务/图片/6-1.jpg"
results = model(img)
results.show()