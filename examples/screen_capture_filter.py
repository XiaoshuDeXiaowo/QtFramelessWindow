# coding:utf-8
import sys

from qtpy.QtCore import Qt
from qtpy.QtWidgets import QApplication

from QtFramelessWindow import FramelessWindow
from QtFramelessWindow.utils import ScreenCaptureFilter


class Window(FramelessWindow):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("PyQt-Frameless-Window")

        # disable screen capture
        self.installEventFilter(ScreenCaptureFilter(self))


if __name__ == "__main__":
    # enable dpi scale
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    from qtpy import QT5
    if QT5:
        QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
        QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    # run app
    app = QApplication(sys.argv)
    demo = Window()
    demo.show()
    sys.exit(app.exec_())
