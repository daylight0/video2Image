import os
import cv2
import sys

from PySide6.QtGui import *
from ui_untitled import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *

class videoToImage(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super(videoToImage, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("视频转图像")

        self.timer_camera = QTimer()     #定义定时器

        self.setMinimumSize(340, 590)
        self.setMaximumSize(340, 590)
        
        png = QPixmap('./image/1.png')
        self.display.setPixmap(png)
        #图片自适应窗口大小
        self.display.setScaledContents(True)

        '''关联信号与槽'''
        # 选择文件按钮
        self.chooseFile.clicked.connect(self.selectFile)

        # 打开串口按钮
        self.startConvert.clicked.connect(self.startConv)

        self.saveRoute.clicked.connect(self.savePath)


        # 临时路径存储变量
        self.tempPath = 0
        self.tempSavePath = 0


        # 每次启动将显示窗口显示在屏幕中间
        screen = QGuiApplication.primaryScreen().size()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, 
                  (screen.height() - size.height()) / 2)

    def selectFile(self):
        """
            选择文件
        """
        self.display.clear()

        videoName, _ = QFileDialog.getOpenFileName(self, "Open", "", "*.avi;;*.mp4;;All Files(*)")
        self.fileName.setText(videoName)
        self.tempPath = videoName
        if videoName != "":  # “”为用户取消
            self.cap = cv2.VideoCapture(videoName)
            self.timer_camera.start(100)
            self.timer_camera.timeout.connect(self.openFrame)


    def savePath(self):
        """
            选择文件夹
        """
        foldername = QFileDialog.getExistingDirectory(self, "Select Directory", "./")
        self.fileName_1.setText(foldername)
        self.tempSavePath = foldername

    def startConv(self):
        """ 
            Slot function to start the progamme
        """
        self.timer_camera.stop()   # 停止计时器
        cap = cv2.VideoCapture(self.tempPath)

        print("123")
        if self.tempSavePath != 0:
            print("456")
            print(self.tempSavePath)
            print(os.path.join(self.tempSavePath + "/out"))
            if not os.path.exists(os.path.join(self.tempSavePath + "/out")):
                print("4321")
                os.mkdir(os.path.join(self.tempSavePath + "/out"))
        else:
            if not os.path.exists(os.path.join(os.getcwd() + "/out")):
                os.mkdir(os.path.join(os.getcwd() + "/out"))
        
        tempNum = 0
        while(cap.isOpened()):
            tempNum = tempNum+1
            ret, frame = cap.read()
            if ret==True:
                cv2.imwrite(os.path.join(os.getcwd() + "/out/image-") +str(tempNum)+'.jpg',frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break
        cap.release()
        cv2.destroyAllWindows()

    def openFrame(self):
        """ 
            Slot function to capture frame and process it
        """
        
        if(self.cap.isOpened()):
            ret, self.frame = self.cap.read()
            if ret:
                frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
                height, width, bytesPerComponent = frame.shape
                bytesPerLine = bytesPerComponent * width
                q_image = QImage(frame.data,  width, height, bytesPerLine,
                                 QImage.Format_RGB888).scaled(self.display.width(), self.display.height())
                self.display.setPixmap(QPixmap.fromImage(q_image))
            else:
                self.cap.release()
                self.timer_camera.stop()   # 停止计时器

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlg = videoToImage()
    dlg.show()
    sys.exit(app.exec_())