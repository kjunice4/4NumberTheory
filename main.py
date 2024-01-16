# 4 random numbers from 0-9
# Each number generated must be used and can only be used once
# Try to build functions from 0 - 100
# Create keyboard for user input

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

#Opening Page
Builder.load_string("""
<Homepage>:
    id: Homepage
    name: "Homepage"
    
    GridLayout:
        cols: 1
        
        Button:
            font_size: '20sp'
            background_color: 0, 0 , 0 , 1
            size_hint_y: None
            height: 200
            text: "Tap anywhere to continue"
            on_release:
                app.root.current = "Menu"
                root.manager.transition.direction = "left" 
        
        Button:
            font_size: '20sp'
            background_color: 0, 0 , 0 , 1
            size_hint_y: None
            height: 200
            text: "4 Number Theory Game"
            on_release:
                app.root.current = "Menu"
                root.manager.transition.direction = "left" 
                
        Button:
            background_normal: "JuniceIndustries_Logo.png"
            on_release:
                app.root.current = "Menu"
                root.manager.transition.direction = "left" 
                
""")

# Menu
Builder.load_string("""
<Menu>
    id:Menu
    name:"Menu"
    
    ScrollView:
        name: "Scroll"
        do_scroll_x: False
        do_scroll_y: True
        
        GridLayout:
            cols: 1
            padding:10
            spacing:10
            size_hint: 1, None
            width:100
            height: self.minimum_height
            
            Label:
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Menu"
            
            Button:
                text: "Play 4 Number Theory"   
                font_size: '20sp'
                background_color: 0, 0 , 1 , 1
                size_hint_y: None
                height: 200
                padding: 10, 10
                on_release:
                    app.root.current = "FourNumberTheory"
                    root.manager.transition.direction = "left" 
            
            Button:
                font_size: '20sp'
                background_color: 1, 0, 1, 1
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "How to Play Four Number Theory"
                on_release:
                    app.root.current = "HowToPage"
                    root.manager.transition.direction = "left"        
            
            Button:
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Visit KSquared-Mathematics"
                on_release:
                    import webbrowser
                    webbrowser.open('https://www.juniceindustries.com') 
                    
            Label:
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Share 4 Number Theory Game"
                    
            Image:
                source: 'KSquared_QR.png'
                size_hint_y: None
                height: 800
                width: 800
""")

#Updates
Builder.load_string("""
<HowToPage>
    id:HowToPage
    name:"HowToPage"
    
    ScrollView:
        name: "Scroll"
        do_scroll_x: False
        do_scroll_y: True
    
        GridLayout:
            cols: 1
            padding:10
            spacing:10
            size_hint: 1, None
            width:100
            height: self.minimum_height
            
            Label:
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "How to play 4 Number Theory"
            
            Button:
                id: steps
                text: "Menu"   
                font_size: '20sp'
                size_hint_y: None
                background_color: 0, 0 , 1 , 1
                height: 200
                padding: 10, 10
                on_release:
                    app.root.current = "Menu"
                    root.manager.transition.direction = "right" 
            
""")

#EXPONENTS STEPS
Builder.load_string("""
<FourNumberTheory>
    id:FourNumberTheory
    name:"FourNumberTheory"

    ScrollView:
        name: "Scroll"
        do_scroll_x: False
        do_scroll_y: True
        
        GridLayout:
            cols: 1
            padding:10
            spacing:10
            size_hint: 1, None
            width:100
            height: self.minimum_height
            
            Label:
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "4 Number Theory"
            
            BoxLayout:
                cols: 2
                padding:10
                spacing:10
                size_hint: 1, None
                width:300
                size_hint_y: None
                height: self.minimum_height 

                Button:
                    text: "Menu"   
                    font_size: '20sp'
                    size_hint_y: None
                    height: 200
                    padding: 10, 10
                    background_color: 0, 0 , 1 , 1
                    on_release:
                        app.root.current = "Menu"
                        root.manager.transition.direction = "right" 
                        
                Button:
                    id: steps
                    text: "Backspace"   
                    font_size: '20sp'
                    size_hint_y: None
                    background_color: 1, 0 , 0 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        input.text = input.text[:-1]
                        
            TextInput:
                id: input
                text: input.text
                hint_text: "Entry:"
                multiline: False
                font_size: '35sp'
                size_hint_y: None
                height: 100
                padding: 10  
                keyboard: False
            
            Button:
                id: steps
                text: "Calculate"   
                font_size: '20sp'
                size_hint_y: None
                background_color: 0, 1 , 0 , 1
                height: 200
                padding: 10, 10
                on_release:
                    FourNumberTheory.steps(input.text)
                    
            BoxLayout:
                cols: 2
                padding:10
                spacing:10
                size_hint: 1, None
                width:300
                size_hint_y: None
                height: self.minimum_height
                
                Button:
                    text: "("   
                    font_size: '30sp'
                    size_hint_y: None
                    background_color: 0, 1, 1, 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        input.text = input.text + "("
                        
                Button:
                    text: ")"   
                    font_size: '30sp'
                    size_hint_y: None
                    background_color: 0, 1, 1, 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        input.text = input.text + ")"   
                        
            BoxLayout:
                cols: 2
                padding:10
                spacing:10
                size_hint: 1, None
                width:300
                size_hint_y: None
                height: self.minimum_height 
                
                Button:
                    text: "^("   
                    font_size: '30sp'
                    size_hint_y: None
                    background_color: 1, 1, 1, 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        input.text = input.text + "^("
                        
                Button:
                    text: "√("   
                    font_size: '30sp'
                    size_hint_y: None
                    background_color: 1, 1, 1, 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        input.text = input.text + "√("
                        
                Button:
                    text: ")!"   
                    font_size: '30sp'
                    size_hint_y: None
                    background_color: 1, 1, 1, 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        input.text = input.text + ")!"          
                        
            BoxLayout:
                cols: 2
                padding:10
                spacing:10
                size_hint: 1, None
                width:300
                size_hint_y: None
                height: self.minimum_height 
                
                Button:
                    text: "+"   
                    font_size: '30sp'
                    size_hint_y: None
                    background_color: 1, 1, 0, 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        input.text = input.text + "+"
                        
                Button:
                    text: "-"   
                    font_size: '30sp'
                    size_hint_y: None
                    background_color: 1, 1, 0, 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        input.text = input.text + "-"
                        
                Button:
                    text: "*"   
                    font_size: '30sp'
                    size_hint_y: None
                    background_color: 1, 1, 0, 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        input.text = input.text + "*"
                        
                Button:
                    text: "/"   
                    font_size: '30sp'
                    size_hint_y: None
                    background_color: 1, 1, 0, 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        input.text = input.text + "/"
                
            BoxLayout:
                cols: 2
                padding:10
                spacing:10
                size_hint: 1, None
                width:300
                size_hint_y: None
                height: self.minimum_height 
                
                Button:
                    text: "0"   
                    font_size: '30sp'
                    size_hint_y: None
                    background_color: 1, 0, 1, 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        input.text = input.text + "0"
                        
                Button:
                    text: "1"   
                    font_size: '30sp'
                    size_hint_y: None
                    background_color: 1, 0, 1, 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        input.text = input.text + "1"
                        
                Button:
                    text: "2"   
                    font_size: '30sp'
                    size_hint_y: None
                    background_color: 1, 0, 1, 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        input.text = input.text + "2"
                        
                Button:
                    text: "3"   
                    font_size: '30sp'
                    size_hint_y: None
                    background_color: 1, 0, 1, 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        input.text = input.text + "3"
                        
                Button:
                    text: "4"   
                    font_size: '30sp'
                    size_hint_y: None
                    background_color: 1, 0, 1, 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        input.text = input.text + "4"
                        
            BoxLayout:
                cols: 2
                padding:10
                spacing:10
                size_hint: 1, None
                width:300
                size_hint_y: None
                height: self.minimum_height 
                
                Button:
                    text: "5"   
                    font_size: '30sp'
                    size_hint_y: None
                    background_color: 1, 0, 1, 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        input.text = input.text + "5"
                        
                Button:
                    text: "6"   
                    font_size: '30sp'
                    size_hint_y: None
                    background_color: 1, 0, 1, 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        input.text = input.text + "6"
                        
                Button:
                    text: "7"   
                    font_size: '30sp'
                    size_hint_y: None
                    background_color: 1, 0, 1, 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        input.text = input.text + "7"
                        
                Button:
                    text: "8"   
                    font_size: '30sp'
                    size_hint_y: None
                    background_color: 1, 0, 1, 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        input.text = input.text + "8"
                        
                Button:
                    text: "9"   
                    font_size: '30sp'
                    size_hint_y: None
                    background_color: 1, 0, 1, 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        input.text = input.text + "9"
                        
            GridLayout:
                id: list_of_steps
                cols: 1
                size_hint: 1, None
                height: self.minimum_height   

""")

class FourNumberTheory(Screen):
    sm = ScreenManager()

    def __init__(self, **kwargs):
        super(FourNumberTheory, self).__init__(**kwargs)
    
    layouts = []
    def steps(self,entry):
        print()
        layout = GridLayout(cols=1,size_hint_y= None)
        self.ids.list_of_steps.add_widget(layout)
        self.layouts.append(layout)
        
        try:
            print("FourNumberTheory = ",entry)
            print(eval(str(entry.replace("^","**"))))
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = '20sp', size_hint_y= None, height=100))
            self.layouts.append(layout)  
                
class Homepage(Screen):
    pass            

class Menu(Screen):
    pass

class HowToPage(Screen):
    pass

sm = ScreenManager()
sm.add_widget(Homepage(name="Homepage"))
sm.add_widget(Menu(name="Menu"))     
sm.add_widget(FourNumberTheory(name="FourNumberTheory"))     
sm.add_widget(HowToPage(name="HowToPage"))
sm.current = "Homepage"   

class FourNumberTheory(App):
    def __init__(self, **kwargs):
        super(FourNumberTheory, self).__init__(**kwargs)
        Window.bind(on_keyboard=self._key_handler)
    
    def _key_handler(self, instance, key, *args):
        print("key:",key)
        if key == 27:
            sm.current = sm.current
            return True
    
    
    def build(app):
        return sm

if __name__ == '__main__':
    FourNumberTheory().run()
    
