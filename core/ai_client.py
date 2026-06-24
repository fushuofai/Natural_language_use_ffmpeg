import os
import sys
import json
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI


# --- 加载 .env 配置 ---
def _get_base_path():
    """获取项目根目录（兼容开发环境和 PyInstaller 打包后的 exe）"""
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    return os.path.abspath(".")

BASE_PATH = _get_base_path()

# .env 查找优先级：exe 同目录 > PyInstaller 临时目录 > 默认搜索
env_path = Path(BASE_PATH) / ".env"
if env_path.exists():
    load_dotenv(dotenv_path=env_path)
else:
    # PyInstaller 打包后数据文件在 sys._MEIPASS
    meipass = getattr(sys, '_MEIPASS', None)
    if meipass:
        bundled_env = Path(meipass) / ".env"
        if bundled_env.exists():
            load_dotenv(dotenv_path=bundled_env)
        else:
            load_dotenv()
    else:
        load_dotenv()


class Ai_Client:
    JSON_FILE_NAME = "session.json"

    def __init__(self):
        base_path = BASE_PATH

        # 定义 core 文件夹路径
        self.core_dir = os.path.join(base_path, "core")

        #exe目录/core/session.json
        self.full_path = os.path.join(self.core_dir, "session.json")

        # --- 强制创建文件夹 ---
        if not os.path.exists(self.core_dir):
            os.makedirs(self.core_dir)
            print(f"已自动创建文件夹: {self.core_dir}")

        # --- 确保文件存在 ---
        if not os.path.exists(self.full_path):
            default_data = {"status": "new", "user": "guest", "function_id": None, "params": {}}
            with open(self.full_path, 'w', encoding='utf-8') as f:
                json.dump(default_data, f, indent=4)
            print(f"已自动创建初始文件: {self.full_path}")
        else:
            print(f"找到现有文件: {self.full_path}")

    #封装调用deepseek的函数
    def call_deepseek(self, input_lineEdit):
        api_key = os.getenv("DEEPSEEK_API_KEY")
        if not api_key or api_key == "your_api_key_here":
            raise ValueError(
                "未配置 DEEPSEEK_API_KEY，请在项目根目录的 .env 文件中填写你的 API Key。\n"
                "可从 https://platform.deepseek.com 获取。"
            )

        client = OpenAI(
            api_key=api_key,
            base_url=os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com"),
        )

        ai_model = os.getenv("AI_MODEL", "deepseek-v4-flash")

        #系统的提示词和用户的输入
        #提示词为ai生成
        system_prompt = """
你是一个安全的视频处理指令解析器。请严格遵守以下规则:

1. 用户希望对当前目录下的视频文件(统一命名为 input.mp4、input.mov 等)进行处理,并生成 output.xxx 文件。
2. 你只能从下方列出的【支持功能】中选择一个最匹配的操作。
3. 你的输出必须是**纯 JSON 格式**,且仅包含以下两个字段:
- "function_id": 整数,对应功能编号(若无法匹配,返回 0)
- "params": 对象,包含该功能所需的具体参数(若无参数,则为 {})
4. 禁止输出任何解释、注释、Markdown、代码块或额外文本。
5. 禁止生成任何涉及删除、写入系统路径(如 C:\\)、执行 shell 命令、网络操作等危险行为的内容。
6. 所有参数值必须来自用户输入,不得编造。时间格式可为秒数(如 30)或 HH:MM:SS(如 "00:01:30")。

【支持功能】
1. 视频格式转换:如 mp4 转 mkv。参数:{"output_format": "mkv"}(仅允许字母,如 mp4, mkv, avi, mov)
2. 裁剪视频:从指定时间开始,截取一段持续时间。参数:{"start_time": "...", "duration": "..."}
3. 提取音频:从视频中提取音频轨道。参数:{}
4. 调整分辨率:改变视频画面尺寸。参数:{"resolution": "1280x720"}(格式必须为 WxH,如 1920x1080)
5. 降低视频码率:压缩文件大小。参数:{"bitrate": "1M"}(单位可为 k 或 M,如 "500k", "2M")
6. 合并两个视频:将 input1.mp4 和 input2.mp4 拼接。参数:{}(程序会自动查找 input1 和 input2)
7. 提取单帧图像:在指定时间点保存一帧画面为图片。参数:{"time": "00:01:30"}(格式可为秒数或 HH:MM:SS)
8. 去除音频:移除视频中的声音轨道,保留画面。参数:{}

示例输出(正确):
{
"function_id": 1,
"params": {
    "output_format": "mkv"
}
}
{
"function_id": 2,
"params": {
    "start_time": "00:01:00",
    "duration": "10"
}
}
{
"function_id": 3,
"params": {}
}
{
"function_id": 4,
"params": {
    "resolution": "1280x720"
}
}
{
"function_id": 5,
"params": {
    "bitrate": "800k"
}
}
{
"function_id": 6,
"params": {}
}
{
"function_id": 7,
"params": {
    "time": "45"
}
}
{
"function_id": 8,
"params": {}
}
{
"function_id": 0,
"params": {}
}

现在,请解析用户的请求。
"""
        # print("功能: 1.视频格式转换 2.裁剪视频 3.提取音频 4.调整分辨率"
        #  "5.降低视频码率 6.合并两个视频 7.提取单帧图像 8.去除音频")
        
        user_prompt = input_lineEdit

        #提取出所需要的内容
        response = client.chat.completions.create(
            model = ai_model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            stream=False,
            reasoning_effort=os.getenv("REASONING_EFFORT", "high"),
            extra_body={"thinking": {"type": "enabled"}}
        )

        output_result = response.choices[0].message.content
        # print(output_result)
        return output_result

    #将ai输出的文字转入session.json文件里
    def incoming_file(self, _input):
        # ai_dict = input
        try:
            with open(self.full_path, "w", encoding="utf-8") as f:
                print(_input)
                f.write(_input)
                print("写入成功")
        except Exception as e:
            print(f"写入失败, {e}")
    #读取session.json的文件再转成字典
    # def export_file(self):
    #     try:
    #         with open(self.full_path, "r", encoding="utf-8") as f:
    #             content = f.read()
    #             data = json.loads(content)
    #             print("读取成功A")
    #             print(data)
    #             if data is not None:
    #                 return data
    #             else:
    #                 print("数据输出错误")
    #     except:
    #         print("读取失败")

        #读取function_id内的数
    # def function_judgment(self, data):
    #     if data:
    #         function_id = data.get('function_id')
    #         if function_id is not None:
    #             print(f"打印成功参数为:{function_id}")
    #             return function_id
    #         else:
    #             print("function_id内为空")

    # def ai_run(self):
    #     output_result = self.call_deepseek(user_output)
    #     self.incoming_file(output_result)
    #     data = self.export_file()
    #     self.function_judgment(data)

        
if __name__ == '__main__':
    ai = Ai_Client()
    # ai.ai_run()