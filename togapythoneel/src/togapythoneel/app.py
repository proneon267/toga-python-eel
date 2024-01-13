"""
Minimalist Example of using Toga WebView with Python-eel for Electron Style apps using Python.
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

import eel
import threading

@eel.expose
def EnableFan():
	print("Enabled")
	return 1

@eel.expose
def DisableFan():
	print("Disabled")
	return 2
    

class TogaPythonEel(toga.App):

    def start_eel(self, port_number):
        eel.init(self.paths.app / "web")
        eel.start("index.html", mode=None, port=port_number)

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        port_number = 8000
        # Start Eel in a separate thread
        eel_thread = threading.Thread(target=self.start_eel, args=(port_number,))
        eel_thread.start()

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.webview = toga.WebView(style=Pack(flex=1))
        self.webview.url = f"http://localhost:{port_number}/"
        self.main_window.content = self.webview
        self.main_window.show()


def main():
    return TogaPythonEel()
