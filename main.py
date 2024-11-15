from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

screen_helper = """
ScreenManager:
    MenuScreen:
    StudentScreen:

<MenuScreen>:
    name: 'main'
    MDRoundFlatButton:
        text: "Student Registration"
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        on_press: root.manager.current = 'student'

<StudentScreen>:
    name: 'student'
    ScrollView:
        scroll_type: ['bars', 'content']
        bar_width: 10
        bar_color: 0.53, 0.81, 0.92, 1
        bar_inactive_color: 0.7, 0.7, 0.7, 1
        effect_cls: 'ScrollEffect'
        padding: [0, 0, 20, 0]  
        MDBoxLayout:
            orientation: 'vertical'
            padding: 20
            spacing: 30  # Increase spacing between elements
            size_hint_y: None
            height: self.minimum_height

            MDLabel:
                text: "Welcome"
                halign: "center"
                font_style: "H5"
                size_hint_y: None
                height: self.texture_size[1] + 20 

            MDLabel:
                text: "Student Registration"
                halign: "center"
                font_style: "H5"
                size_hint_y: None
                height: self.texture_size[1] + 20  

            MDTextField:
                hint_text: "Enter Username"
                size_hint_x: 0.8
                pos_hint: {'center_x': 0.5}

            MDTextField:
                hint_text: "Enter Name"
                size_hint_x: 0.8
                pos_hint: {'center_x': 0.5}

            MDTextField:
                hint_text: "Enter Enrollment Number"
                size_hint_x: 0.8
                pos_hint: {'center_x': 0.5}

            MDTextField:
                hint_text: "Enter Student Password"
                password: True
                size_hint_x: 0.8
                pos_hint: {'center_x': 0.5}

            MDRoundFlatButton:
                text: "Submit"
                pos_hint: {'center_x': 0.5}
                on_press: app.submit_form()

            MDRoundFlatButton:
                text: "Go Back"
                pos_hint: {'center_x': 0.5}
                on_press: root.manager.current = 'main'
"""

class MenuScreen(Screen):
    pass

class StudentScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(MenuScreen(name='main'))
sm.add_widget(StudentScreen(name='student'))

class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_string(screen_helper)

    def submit_form(self):
        print("Form submitted!")

MyApp().run()
