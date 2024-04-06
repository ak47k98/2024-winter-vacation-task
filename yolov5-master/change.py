import torch
from models.yolo import Model  # 确保这个导入语句反映了您的 YOLOv5 目录结构

# 模型配置文件的相对路径
cfg = './models/yolov5s.yaml'  # 请根据您的 YOLOv5 版本更新路径

# 权重文件路径（根据您的设置可能需要修改）
weights = './yolov5s.pt'

# 类别数，根据您的模型进行调整
nc = 80

# 加载模型权重
if weights.endswith('.pt'):  # pytorch format
    # 这里假设模型权重是以.pth或.pt后缀名保存的PyTorch模型
    checkpoint = torch.load(weights, map_location=torch.device('cpu'))
    model_state_dict = checkpoint['model'].state_dict()
else:
    raise ValueError(f"Unsupported weights format '{weights.split('.')[-1]}'")

# 初始化模型
model = Model(cfg, ch=3, nc=nc)  # 为模型配置路径及其他参数创建 Model 实例
model.load_state_dict(model_state_dict)  # 加载模型状态字典
model.eval()  # 打开模型的 eval 模式

# 创建一个伪输入。维度 [1, 3, 640, 640] 代表 [批处理大小, 颜色通道数, 高度, 宽度]
dummy_input = torch.randn(1, 3, 640, 640)

# 定义要导出的 ONNX 文件的路径
onnx_file_path = './yolov5s.onnx'

# 导出模型到 ONNX 格式
print('Exporting model to ONNX format...')
torch.onnx.export(model,  # 模型实例
                  dummy_input,  # 伪输入张量
                  onnx_file_path,  # 输出 ONNX 文件的路径
                  export_params=True,  # 包括训练好的参数
                  opset_version=12,  # ONNX版本
                  do_constant_folding=True,  # 是否应用常数折叠优化
                  input_names=['images'],  # 输入层命名
                  output_names=['output'],  # 输出层命名
                  dynamic_axes={'images': {0: 'batch'}, 'output': {0: 'batch'}}  # 批处理大小使用动态轴
                  )

print(f'Model has been converted to ONNX: {onnx_file_path}')


