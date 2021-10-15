from ctypes import WINFUNCTYPE, windll, c_bool, c_int, POINTER, create_unicode_buffer
from subprocess import call
import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui


def dont_procrastinate(mode):
    
    windows = windll.user32.EnumWindows    
    proc = WINFUNCTYPE(c_bool, POINTER(c_int), POINTER(c_int))
    get_window_text = windll.user32.GetWindowTextW
    get_window_length = windll.user32.GetWindowTextLengthW
    is_window_visible = windll.user32.IsWindowVisible
    titles = []

    def foreach_window(hwnd, lParam):
        if is_window_visible(hwnd):
            length = get_window_length(hwnd)
            buff = create_unicode_buffer(length + 1)
            get_window_text(hwnd, buff, length + 1)
            titles.append(buff.value)
        return True

    windows(proc(foreach_window), 0)

    if mode == 0:
        return

    elif mode == 1:

        if any('YouTube' in title for title in titles):
            call("TASKKILL /F /IM chrome.exe")
    
    elif mode == 2:

        if any('YouTube' in title for title in titles):
            call("TASKKILL /F /IM chrome.exe")

        if any('Twitter' in title for title in titles):
            call("TASKKILL /F /IM chrome.exe")

        if any('Instagram' in title for title in titles):
            call("TASKKILL /F /IM chrome.exe")

    elif mode == 3:

        if any('YouTube' in title for title in titles):
            call("TASKKILL /F /IM chrome.exe")

        if any('Twitter' in title for title in titles):
            call("TASKKILL /F /IM chrome.exe")

        if any('Instagram' in title for title in titles):
            call("TASKKILL /F /IM chrome.exe")

        if any('WhatsApp' in title for title in titles):
            call("TASKKILL /F /IM chrome.exe")

    else:
        print('ERRO')


class App(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)    
        self.trayIcon = QtWidgets.QSystemTrayIcon(QtGui.QIcon('assets/icon.ico'))
        self.mode = 0
        self.modeStr = 'Light Mode'
        self.trayIcon.setToolTip('Anti-Procrastinator is OFF')

        self.menu = QtWidgets.QMenu()

        self.turnOff = self.menu.addAction('Turn OFF')
        self.turnOff.triggered.connect(lambda checked, index=0: self.change_mode(index))

        self.separator2 = self.menu.addAction('a')
        self.separator2.setSeparator(True)

        self.lightMode = self.menu.addAction(QtGui.QIcon('assets/leaf.ico'), 'Light Mode')
        self.hardMode = self.menu.addAction(QtGui.QIcon('assets/hot.ico'), 'Hard Mode')
        self.hardcoreMode = self.menu.addAction(QtGui.QIcon('assets/skull.ico'), 'HARDCORE MODE')

        self.lightMode.triggered.connect(lambda checked, index=1: self.change_mode(index))
        self.hardMode.triggered.connect(lambda checked, index=2: self.change_mode(index))
        self.hardcoreMode.triggered.connect(lambda checked, index=3: self.change_mode(index))

        self.separator = self.menu.addAction('a')
        self.separator.setSeparator(True)

        self.exitAction = self.menu.addAction(QtGui.QIcon('assets/icon.ico'), 'Exit ')
        self.exitAction.triggered.connect(sys.exit)

        self.trayIcon.setContextMenu(self.menu)

        timer = QtCore.QTimer(self)

        timer.timeout.connect(self.anti_procrastinator)
        timer.start(1000)

    def change_mode(self, mode):
        self.mode = mode
        self.modeStr = 'Light Mode' if self.mode == 1 else ('Hard Mode' if self.mode == 2 else ('HARDCORE MODE' if self.mode == 3 else 'OFF'))
        self.trayIcon.setToolTip(f'Anti-Procrastinator is at {self.modeStr}')

    def anti_procrastinator(self):
        dont_procrastinate(self.mode)


if __name__ == '__main__':
    try:
        qt = QtWidgets.QApplication(sys.argv)
        app = App()
        app.trayIcon.show()
        qt.exec_()

    except Exception as e:
        print(e)
