from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import socket
import threading

class Scanner(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=10, **kwargs)
        self.add_widget(Label(text='Nmap App - فحص الشبكة', font_size=24, size_hint_y=0.2))
        self.target = TextInput(hint_text='اكتب IP مثلا 192.168.1.1', multiline=False, size_hint_y=0.15)
        self.add_widget(self.target)
        self.btn = Button(text='ابدأ الفحص', size_hint_y=0.15, background_color=(0, 0.8, 0.4, 1))
        self.btn.bind(on_press=self.start_scan)
        self.add_widget(self.btn)
        self.result = Label(text='النتيجة هتظهر هنا', font_size=16)
        self.add_widget(self.result)

    def start_scan(self, instance):
        self.result.text = 'جاري الفحص...'
        threading.Thread(target=self.scan, daemon=True).start()

    def scan(self):
        host = self.target.text.strip() or '127.0.0.1'
        open_ports = []
        for port in [21, 22, 23, 80, 443, 3306, 8080]:
            try:
                s = socket.socket()
                s.settimeout(1)
                if s.connect_ex((host, port)) == 0:
                    open_ports.append(str(port))
                s.close()
            except:
                pass
        if open_ports:
            self.result.text = 'بورتات مفتوحة: ' + ', '.join(open_ports)
        else:
            self.result.text = 'مفيش بورتات مفتوحة'

class NmapApp(App):
    def build(self):
        return Scanner()

if __name__ == '__main__':
    NmapApp().run()
