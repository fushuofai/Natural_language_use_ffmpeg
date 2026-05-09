#视频操作封装
import subprocess
import os
import json
import sys
from core.ai_client import Ai_Client
from datetime import datetime

class VideoEngine:
    # JSON_FILE_NAME = "session.json"

    def __init__(self, input_file_1, input_file_2, output_file):
        # --- 1. 先处理路径  ---
        if getattr(sys, 'frozen', False):
            # 如果是打包后的 exe 运行，base_path 就是 exe 所在的文件夹
            base_path = os.path.dirname(sys.executable)
        else:
            # 如果是开发环境运行，base_path 就是项目根目录
            base_path = os.path.abspath(".")
        
        # 定义 core 文件夹路径
        core_dir = os.path.join(base_path, "core")
        
        #exe目录/core/session.json
        self.full_path = os.path.join(core_dir, "session.json")

        # --- 2. 检查并自动创建文件  ---
        if not os.path.exists(core_dir):
            os.makedirs(core_dir)
            print(f"已创建 core 文件夹: {core_dir}")

        if not os.path.exists(self.full_path): # 这里使用你熟悉的变量名
            default_data = {"status": "new", "user": "guest", "function_id": None, "params": {}}
            with open(self.full_path, 'w', encoding='utf-8') as f:
                json.dump(default_data, f, indent=4)
            print("检测到首次运行，已自动创建配置文件。")
        else:
            print("读取现有配置文件...")

        # --- 3. 保留你原来的输入输出路径逻辑 ---
        current_datetime = datetime.now()
        formatted_time = current_datetime.strftime('%Y-%m-%d_%H-%M-%S')
        self.input_file_1 = os.path.join(input_file_1)
        self.input_file_2 = os.path.join(input_file_2)
        self.output_file = os.path.join(output_file, f"output_{formatted_time}")

        # --- 4. 初始化 AI ---
        self.ai_client = Ai_Client()


    #1.视频格式转换
    def convert_video(self, fmt):

        if not os.path.exists(self.input_file_1):
            print(f"输入文件不存在: {os.path.abspath(self.input_file_1)}")
            return False, "文件不存在"

        cmd = [
            "ffmpeg", 
            "-i", self.input_file_1, 
            "-c", "copy", 
            f"{self.output_file}.{fmt}"]
        
        return self.video_run(cmd)
        
    #2.视频裁剪
    def trim_video(self, start_time, duration):

        if not os.path.exists(self.input_file_1):
            print(f"输入文件不存在: {os.path.abspath(self.input_file_1)}")
            return False, "文件不存在"

        cmd = [
            "ffmpeg",
            "-ss",f"{start_time}", 
            "-i", self.input_file_1, 
            "-t", f"{duration}", 
            "-c", "copy", 
            f"{self.output_file}.mp4"]
        return self.video_run(cmd)

    #3.提取音频
    def extract_audio(self):

        if not os.path.exists(self.input_file_1):
            print(f"输入文件不存在: {os.path.abspath(self.input_file_1)}")
            return False, "文件不存在"

        cmd = [
            "ffmpeg",
            "-i", self.input_file_1,
            "-vn", "-c:a",
            "copy", f"{self.output_file}.m4a"
            ]
        return self.video_run(cmd)

    #4.调整视频分辨率
    def adjust_resolution(self, fmt):

        if not os.path.exists(self.input_file_1):
            print(f"输入文件不存在: {os.path.abspath(self.input_file_1)}")
            return False, "文件不存在"

        width, height = fmt.split("x")
        cmd = [
            "ffmpeg",
            "-i", self.input_file_1,
            "-vf", f"scale={width}:{height}",
            "-c:a", "copy",
            f"{self.output_file}.mp4"
        ]
        return self.video_run(cmd)

    #5.降低视频码率
    def reduce_bitrate(self, fmt):

        if not os.path.exists(self.input_file_1):
            print(f"输入文件不存在: {os.path.abspath(self.input_file_1)}")
            return False, "文件不存在"

        cmd = [
            "ffmpeg",
            "-i", self.input_file_1,
            "-b:v", f"{fmt}",
            "-c:a", "copy",
            f"{self.output_file}.mp4"
        ]
        return self.video_run(cmd)

    #6.合并视频
    def merge_videos(self):

        #拼接路径
        video1_path = os.path.join(self.input_file_1) # 假设命名为input1
        video2_path = os.path.join(self.input_file_2) # 假设命名为input2

        #检查两个输入文件是否存在
        if not os.path.exists(video1_path):
            return False, "合并失败: input.mp4 不存在"
        if not os.path.exists(video2_path):
            return False, "合并失败: input2.mp4 不存在"

        cmd = [
        "ffmpeg",
        "-i", video1_path,
        "-i", video2_path,
        "-filter_complex",
        "[0:v][0:a][1:v][1:a]concat=n=2:v=1:a=1[v][a]",
        "-map", "[v]",
        "-map", "[a]",  
        "-c:a", "aac",  
        f"{self.output_file}.mp4"
        ]
        return self.video_run(cmd)

    #7.提取单帧图像
    def extract_frame(self, time):

        if not os.path.exists(self.input_file_1):
            print(f"输入文件不存在: {os.path.abspath(self.input_file_1)}")
            return False, "文件不存在"

        cmd = [
            "ffmpeg",
            "-i", self.input_file_1,
            "-ss", f"{time}",
            "-vframes", "1",
            "-q:v", "2",
            f"{self.output_file}.jpg"
        ]
        return self.video_run(cmd)

    #8.视频去除音频
    def remove_audio(self):

        if not os.path.exists(self.input_file_1):
            print(f"输入文件不存在: {os.path.abspath(self.input_file_1)}")
            return False, "文件不存在"

        cmd = [
            "ffmpeg",
            "-i", self.input_file_1,
            "-an",
            "-c:v", "copy",
            f"{self.output_file}.mp4"
        ]
        return self.video_run(cmd)

    def video_run(self, cmd):
        #判断开头
        if not cmd or cmd[0] != "ffmpeg":
            return False, "拒绝执行非 ffmpeg 命令"

        #异常捕获
        try:
            subprocess.run(cmd, check=True, capture_output=True) 
            print("转换完成")
            return True, "成功"
        except subprocess.CalledProcessError as e:
            return False, e.stderr.decode("utf-8", errors="ignore")
        
    def choice_function(self):
        try:
            with open(self.full_path, "r", encoding="utf-8") as f:
                    content = f.read()
                    data = json.loads(content)
                    print("读取成功V")

            #判断data内是否为空值
            if not data:
                print("无法读取session的参数")
                return
            
            params = data.get("params",{})

            function_id = data.get("function_id")
            if function_id is not None:
                print(f"打印出来的{function_id}")

                choice = function_id

                match choice:
                    #1.视频格式转换
                    case 1:
                        #导入参数
                        output_format = params.get("output_format","mp4")
                        print("开始转换1")

                        #错误返回值全部交由ai来写，个人还未涉及到
                        success, msg = self.convert_video(output_format) # <-- 接收返回值
                        if not success:
                            print(f"[错误] 转换失败: {msg}")
                        else:
                            print("[成功] 转换完成")
                    
                    #2.裁剪视频
                    case 2:
                        #导入参数
                        start_time = params.get("start_time")
                        duration = params.get("duration")
                        print("开始转换2")
                        
                        #错误返回值全部交由ai来写，个人还未涉及到
                        success, msg = self.trim_video(start_time, duration) # <-- 接收返回值
                        if not success:
                            print(f"[错误] 转换失败: {msg}")
                        else:
                            print("[成功] 转换完成")
                    
                    #3.提取音频
                    case 3:
                        print("开始转换3")

                        #错误返回值全部交由ai来写，个人还未涉及到
                        success, msg = self.extract_audio() # <-- 接收返回值
                        if not success:
                            print(f"[错误] 转换失败: {msg}")
                        else:
                            print("[成功] 转换完成")

                    #4.调整分辨率
                    case 4:
                        #导入参数
                        resolution = params.get("resolution", "1920x1080")
                        print("开始转换4")

                        #错误返回值全部交由ai来写，个人还未涉及到
                        success, msg = self.adjust_resolution(resolution) # <-- 接收返回值
                        if not success:
                            print(f"[错误] 转换失败: {msg}")
                        else:
                            print("[成功] 转换完成")

                    #5.降低视频码率
                    case 5:
                        #导入参数
                        bitrate = params.get("bitrate", "1m")
                        print("开始转换5")
                        
                        #错误返回值全部交由ai来写，个人还未涉及到
                        success, msg = self.reduce_bitrate(bitrate) # <-- 接收返回值
                        if not success:
                            print(f"[错误] 转换失败: {msg}")
                        else:
                            print("[成功] 转换完成")


                    #6.合并两个视频
                    case 6:
                        print("开始转换6")
                        
                        #错误返回值全部交由ai来写，个人还未涉及到
                        success, msg = self.merge_videos() # <-- 接收返回值
                        if not success:
                            print(f"[错误] 转换失败: {msg}")
                        else:
                            print("[成功] 转换完成")

                    #7.提取单帧图像
                    case 7:
                        #导入参数
                        time = params.get("time", "0")
                        print("开始转换7")
                        
                         #错误返回值全部交由ai来写，个人还未涉及到
                        success, msg = self.extract_frame(time) # <-- 接收返回值
                        if not success:
                            print(f"[错误] 转换失败: {msg}")
                        else:
                            print("[成功] 转换完成")

                    #8.去除音频
                    case 8:
                        print("开始转换8")
                        
                         #错误返回值全部交由ai来写，个人还未涉及到
                        success, msg = self.remove_audio() # <-- 接收返回值
                        if not success:
                            print(f"[错误] 转换失败: {msg}")
                        else:
                            print("[成功] 转换完成")

                    case _:
                        print("输入错误,请重新输入")
                        return
        
        #报错部分由ai来写的
        except FileNotFoundError:
            print(f"错误: 配置文件未找到: {self.full_path}")
        except json.JSONDecodeError as e:
            print(f"错误: session.json 格式无效: {e}")
        except Exception as e:
            print(f"未知错误: {e}")