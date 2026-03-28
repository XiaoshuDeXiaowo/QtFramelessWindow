# coding: utf-8
import sys

from qtpy.QtCore import Qt
from qtpy.QtWebEngineWidgets import QWebEngineView
from QtFramelessWindow import AcrylicWindow, FramelessWindow
from QtFramelessWindow import AcrylicWindow


class FramelessWebEngineView(QWebEngineView):
    """ Frameless web engine view """

    def __init__(self, parent):
        if sys.platform == "win32" and isinstance(parent.window(), AcrylicWindow):
            parent.window().setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        super().__init__(parent=parent)

        if sys.platform in ("win32", "darwin"):
            self.setHtml("")

        if isinstance(self.window(), FramelessWindow):
            self.window().updateFrameless()