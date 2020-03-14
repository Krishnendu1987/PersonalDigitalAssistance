# Start again from tutorial #4 sentdx
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
import os



kivy.require("1.11.1")



class ConnectPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2

        if os.path.isfile("prev_details.txt"):
            with open("prev_details.txt", "r") as f:
                d = f.read().split(",")
                prev_fname = d[0]
                prev_lastname = d[1]
                prev_phonenumber = d[2]
        else:
            prev_fname = ""
            prev_lastname = ""
            prev_phonenumber = ""


        self.add_widget(Label(text = "First Name:"))
        self.fname = TextInput(text=prev_fname, multiline = False)
        self.add_widget(self.fname)

        self.add_widget(Label(text="Last Name :"))
        self.lastname = TextInput(text=prev_lastname, multiline=False)
        self.add_widget(self.lastname)

        self.add_widget(Label(text="Phone Number :"))
        self.phonenumber = TextInput(text= prev_phonenumber, multiline=False)
        self.add_widget(self.phonenumber)

        self.join = Button(text = "Join")
        self.join.bind(on_press = self.join_button)
        self.add_widget(Label())
        self.add_widget(self.join)

    def join_button(self, instance):
        lastname = self.lastname.text
        fname = self.fname.text
        phonenumber= self.phonenumber.text



        with open("prev_details.txt", "w") as f:
            f.write(f"{fname},{lastname},{phonenumber}")

        info = f"Attempting to Join {fname} {lastname} of Phone Number: {phonenumber}"
        chat_app.info_page.update_info(info)
        chat_app.screen_manager.current = "Info"




class InfoPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.message = Label(halign= "center", valign= "middle", font_size= 30)
        self.message.bind(width= self.update_text_width)
        self.add_widget(self.message)

    def update_info(self, message):
        self.message.text = message

    def update_text_width(self, *_):
        self.message.text_size = (self.message.width*0.9, None)




class EpicApp(App):
    def build(self):
        self.screen_manager = ScreenManager()

        self.connect_page = ConnectPage()
        screen = Screen(name = "Connect")
        screen.add_widget(self.connect_page)
        self.screen_manager.add_widget(screen)

        self.info_page = InfoPage()
        screen = Screen(name="Info")
        screen.add_widget(self.info_page)
        self.screen_manager.add_widget(screen)

        return self.screen_manager


if __name__ == "__main__":
   chat_app = EpicApp()
   chat_app.run()




