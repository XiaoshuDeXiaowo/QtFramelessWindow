"""
QtFramelessWindow
======================
A cross-platform frameless window based on PyQt/PySide, support Win32, macOS and Linux.


Examples are available at https://github.com/XiaoshuDeXiaowo/QtFramelessWindow/tree/main/examples.

:copyright: Copyright (c) 2021-2026 by zhiyiYo. Copyright (c) 2026 XiaoshuDeXiaowo
:license: LGPLv3, see LICENSE for more details.
"""

__version__ = "0.0.1"
__author__ = "zhiyiYo, XiaoshuDeXiaowo"

import sys

from qtpy.QtWidgets import QDialog, QMainWindow

from .titlebar import TitleBar, TitleBarButton, SvgTitleBarButton, StandardTitleBar, TitleBarBase

if sys.platform == "win32":
    from .windows import AcrylicWindow
    from .windows import WindowsFramelessWindow as FramelessWindow
    from .windows import WindowsWindowEffect as WindowEffect
elif sys.platform == "darwin":
    from .mac import AcrylicWindow
    from .mac import MacFramelessWindow as FramelessWindow
    from .mac import MacWindowEffect as WindowEffect
else:
    from .linux import LinuxFramelessWindow as FramelessWindow
    from .linux import LinuxWindowEffect as WindowEffect

    AcrylicWindow = FramelessWindow


class FramelessDialog(QDialog, FramelessWindow):
    """ Frameless dialog """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.titleBar.minBtn.hide()
        self.titleBar.maxBtn.hide()
        self.titleBar.setDoubleClickEnabled(False)
        self.windowEffect.disableMaximizeButton(self.winId())


class FramelessMainWindow(QMainWindow, FramelessWindow):
    """ Frameless main window """

    def __init__(self, parent=None):
        super().__init__(parent)