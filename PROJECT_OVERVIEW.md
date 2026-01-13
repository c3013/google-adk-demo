# Google ADK Python Demo - Project Overview

## 项目说明 (Project Description)

本项目实现了一个使用 Google ADK (Application Development Kit) 调用开源模型的 Python 演示程序。

This project implements a Python demo using Google ADK to call open-source models.

## 核心功能 (Core Features)

### ✅ 已实现的功能 (Implemented Features)

1. **支持自定义模型 (Custom Model Support)**
   - 可配置任意兼容 OpenAI API 的模型
   - 支持本地模型（Ollama、LM Studio 等）
   - 支持云端模型（OpenAI、Google Gemini 等）

2. **支持自定义 API Key (Custom API Key)**
   - 通过环境变量配置
   - 通过命令行参数配置
   - 支持任意 API 认证方式

3. **支持自定义 Base URL (Custom Base URL)**
   - 可连接任意兼容的 API 端点
   - 支持本地服务器 (localhost)
   - 支持云端服务

## 项目结构 (Project Structure)

```
google-adk-demo/
├── demo.py                  # 主演示程序 (Main demo script)
├── simple_example.py        # 简单示例 (Simple example)
├── advanced_example.py      # 高级示例 (Advanced example)
├── test_demo.py            # 测试脚本 (Test script)
├── requirements.txt        # 依赖项 (Dependencies)
├── .env.example           # 环境变量模板 (Env template)
├── config.yaml            # 配置文件示例 (Config example)
├── README.md              # 英文文档 (English docs)
├── QUICKSTART.md          # 快速开始指南 (Quick start)
├── PROJECT_OVERVIEW.md    # 项目概览 (This file)
└── examples/              # 示例目录 (Examples directory)
    ├── README.md
    └── ollama_example.py  # Ollama 集成示例
```

## 使用方法 (Usage)

### 方法 1: 使用环境变量 (Using Environment Variables)

```bash
# 复制配置模板
cp .env.example .env

# 编辑 .env 文件
API_KEY=your_api_key_here
BASE_URL=https://api.example.com/v1
MODEL=gpt-3.5-turbo

# 运行演示
python demo.py
```

### 方法 2: 使用命令行参数 (Using Command Line Arguments)

```bash
python demo.py <api_key> <base_url> <model>

# 示例 (Example)
python demo.py sk-xxx https://api.openai.com/v1 gpt-3.5-turbo
```

### 方法 3: 编程方式 (Programmatic Usage)

```python
from demo import OpenSourceModelDemo

# 创建实例 (Create instance)
demo = OpenSourceModelDemo(
    api_key="your_key",
    base_url="https://api.example.com/v1",
    model="gpt-3.5-turbo"
)

# 初始化客户端 (Initialize client)
demo.initialize_client()

# 生成文本 (Generate text)
result = demo.generate_text("你好，世界！", max_tokens=100)
```

## 配置示例 (Configuration Examples)

### OpenAI

```env
API_KEY=sk-proj-xxxxxxxxxxxxx
BASE_URL=https://api.openai.com/v1
MODEL=gpt-3.5-turbo
```

### 本地 Ollama (Local Ollama)

```env
API_KEY=dummy_key
BASE_URL=http://localhost:11434/v1
MODEL=llama2
```

### Google Gemini

```env
API_KEY=your_google_api_key
BASE_URL=https://generativelanguage.googleapis.com/v1beta
MODEL=gemini-2.0-flash-exp
```

## 功能特性 (Features)

1. **文本生成 (Text Generation)**
   - 支持自定义提示词
   - 可配置最大 token 数
   - 可配置温度参数

2. **交互式对话 (Interactive Chat)**
   - 实时对话功能
   - 历史记录保存
   - 支持多轮对话

3. **批量处理 (Batch Processing)**
   - 可处理多个提示词
   - 自动错误处理
   - 进度显示

4. **错误处理 (Error Handling)**
   - 完善的异常捕获
   - 友好的错误提示
   - 自动重试机制

## 测试验证 (Testing & Validation)

运行测试脚本：

```bash
python test_demo.py
```

所有测试应该通过：
- ✓ Python 语法验证
- ✓ 必需函数检查
- ✓ 配置参数验证
- ✓ 错误处理测试

## 依赖项 (Dependencies)

- Python 3.8+
- google-genai >= 0.2.0
- python-dotenv >= 1.0.0
- pyyaml >= 6.0

安装依赖：

```bash
pip install -r requirements.txt
```

## 支持的模型 (Supported Models)

### 云端模型 (Cloud Models)
- OpenAI: gpt-3.5-turbo, gpt-4, etc.
- Google Gemini: gemini-2.0-flash-exp, etc.
- Anthropic Claude (通过兼容层)

### 本地模型 (Local Models)
- Llama 2
- Mistral
- CodeLlama
- Vicuna
- 任何 Ollama 支持的模型

### 本地服务器 (Local Servers)
- Ollama
- LM Studio
- LocalAI
- Text Generation WebUI

## 常见问题 (FAQ)

### Q: 如何获取 API Key？
A: 取决于您使用的服务：
- OpenAI: https://platform.openai.com/api-keys
- Google: https://ai.google.dev/
- 本地模型：使用任意值（如 "dummy_key"）

### Q: 支持哪些模型？
A: 支持任何兼容 OpenAI API 格式的模型和服务。

### Q: 如何使用本地模型？
A: 参考 `examples/ollama_example.py` 获取详细说明。

## 贡献 (Contributing)

欢迎提交 Pull Request 和 Issue！

## 许可证 (License)

MIT License

## 联系方式 (Contact)

如有问题，请在 GitHub 上提交 Issue。
