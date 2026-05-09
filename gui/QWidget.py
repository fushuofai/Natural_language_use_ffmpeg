from PySide6.QtWidgets import (
    QApplication, QWidget, QFileDialog,
    QMessageBox
    )
from gui.ui_demo import Ui_Widget

from PySide6.QtCore import Signal, QThread

from core.ai_client import Ai_Client
from core.video_ops import VideoEngine

import time
import sys

class WorkerThread(QThread):
    progress_updated = Signal(int) #进度信号
    task_finished = Signal()

    def __init__(self, text, input_file_1, input_file_2, output_file):
        super().__init__()
        self.text = text
        self.input_file_1 = input_file_1
        self.input_file_2 = input_file_2
        self.output_file = output_file

    def run (self):
        for i in range(31):
            self.progress_updated.emit(i)
            self.msleep(50)

        ai = Ai_Client() ##ai运行的主代码

        output_result = ai.call_deepseek(self.text) #提取用户的输出并交给ai

        ai.incoming_file(output_result) #将ai输出的文字转入session.json文件里

        for i in range(31, 100):
            self.progress_updated.emit(i)
            self.msleep(10)
        ve = VideoEngine(self.input_file_1, self.input_file_2, self.output_file)
        ve.choice_function() #视频处理的主代码
        self.progress_updated.emit(100)
        self.task_finished.emit()
        

class Widget(QWidget):

    def __init__(self):
        super(Widget, self).__init__()
        self.ui = Ui_Widget() #UI类的实例化()
        self.ui.setupUi(self)
        self.bind()
        # 在 __init__ 里加上这句，强制让它变成白色文字
        self.ui.in_open_toolButton1.setStyleSheet("color: white; border: 1px solid #444;")
        self.ui.in_open_toolButton2.setStyleSheet("color: white; border: 1px solid #444;")
        self.ui.out_open_toolButton.setStyleSheet("color: white; border: 1px solid #444;")
        # 假设你在 ui_demo.py 中给这个 QTextBrowser 起的名字叫 textBrowser
        # 如果没有改名，默认通常是 textBrowser
        self.ui.textBrowser.setHtml("""
            <style>
                body { color: #00FF00; background-color: #1E1E1E; font-family: 'Consolas', 'Courier New', monospace; }
                h3 { color: #FFFFFF; border-bottom: 1px solid #00FF00; padding-bottom: 5px; }
                li { margin-bottom: 5px; }
            </style>
            <body>
                <h3>___支持功能___</h3>
                <ol>
                    <li>视频格式转换</li>
                    <li>裁剪视频</li>
                    <li>提取音频</li>
                    <li>调整分辨率</li>
                    <li>降低视频码率</li>
                    <li>合并两个视频</li>
                    <li>提取单帧图像</li>
                    <li>去除音频</li>
                </ol>
            </body>
        """)

    #信号槽绑定
    def bind(self):
        self.ui.run_pushButton.clicked.connect(self.all_run) #槽绑定all_run函数
        self.ui.in_open_toolButton1.clicked.connect(self.open_video_file_1)  # 槽绑定open_input_folder1函数
        self.ui.in_open_toolButton2.clicked.connect(self.open_video_file_2)  # 槽绑定open_input_folder2函数
        self.ui.out_open_toolButton.clicked.connect(self.open_output_folder)  # 槽绑定open_output_folder函数

    def progress_bar(self):
        self.ui.progressBar.setRange(0, 100)
        self.ui.progressBar.setValue(80)

    #运行函数
    def all_run(self):
        text = self.user_output()
        
        #读取文本框的路径
        input_file_1 = self.ui.in_file_lineEdit1.text() 
        input_file_2 = self.ui.in_file_lineEdit2.text() 
        output_file = self.ui.out_file_lineEdit.text() 

        if not input_file_1 or not input_file_2 or not output_file:
            QMessageBox.warning(self, "错误", "请选择视频文件和输出文件夹！")
            return
        
        self.ui.run_pushButton.setEnabled(False)  # 禁用运行按钮
        self.ui.run_pushButton.setText("处理中...") # 可选：改变文字提示用户

        self.worker = WorkerThread(text, input_file_1, input_file_2, output_file)
        self.worker.progress_updated.connect(self.ui.progressBar.setValue) # 连接进度信号
        self.worker.task_finished.connect(self.on_worker_finished) #连接完成信号
        self.worker.start()

    #运行完成窗口
    def on_worker_finished(self):
        QMessageBox.information(self, "成功", "所有任务处理完成！")

        self.ui.run_pushButton.setEnabled(True)   # 恢复运行按钮
        self.ui.run_pushButton.setText("运行")     # 恢复文字

    #提取用户输出
    def user_output(self):
        text = self.ui.input_lineEdit.text()
        return text
    
    #打开输入文件夹
    def open_video_file_1(self):
        # 使用 getOpenFileName 选择单个文件
        # 过滤器设置只显示常见视频格式
        file_path, _ = QFileDialog.getOpenFileName(
            self, 
            "选择视频文件", 
            "", 
            "Video Files (*.mp4 *.avi *.mov *.mkv);;All Files (*)"
        )

        if file_path:
            try:
                # 将选中的视频路径显示在输入框里
                self.ui.in_file_lineEdit1.setText(file_path)
            except Exception as e:
                QMessageBox.warning(self, '错误', f'无法设置路径: {e}')
        return file_path
    
    def open_video_file_2(self):
        # 使用 getOpenFileName 选择单个文件
        # 过滤器设置只显示常见视频格式
        file_path, _ = QFileDialog.getOpenFileName(
            self, 
            "选择视频文件", 
            "", 
            "Video Files (*.mp4 *.avi *.mov *.mkv);;All Files (*)"
        )

        if file_path:
            try:
                # 将选中的视频路径显示在输入框里
                self.ui.in_file_lineEdit2.setText(file_path)
            except Exception as e:
                QMessageBox.warning(self, '错误', f'无法设置路径: {e}')
        return file_path


    #打开输出文件夹
    def open_output_folder(self):
        # 打开选择文件夹对话框
        folder_path = QFileDialog.getExistingDirectory(self, "选择输出文件夹")

        # 2. 检查路径是否为空（用户是否点击了取消）
        if folder_path:
            try:
                self.ui.out_file_lineEdit.setText(folder_path)
            except Exception as e:
                QMessageBox.warning(self, '错误', f'无法设置路径: {e}')
        return folder_path
    
    

if __name__ == '__main__':
    app = QApplication([])
    widget = Widget()
    widget.show()
    sys.exit(app.exec())