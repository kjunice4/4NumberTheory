# 4 random numbers from 0-9
# Each number generated must be used and can only be used once
# Try to build functions with the 4 given numbers to answer random numbers from 0 - 100
# Create dataframe to keep track of how many answered correctly

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

import random

#Opening Page
Builder.load_string("""
<Homepage>:
    id: Homepage
    name: "Homepage"
    
    GridLayout:
        cols: 1
        
        Button:
            background_normal: "4numbertheory_logo.png"
            on_release:
                app.root.current = "Menu"
                root.manager.transition.direction = "left" 
        
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
                    text: "New 4 Numbers & Answer"   
                    font_size: '15sp'
                    size_hint_y: None
                    height: 200
                    padding: 10, 10
                    background_color: 1, 0 , 1 , 1
                    on_release:
                        evaluated_answer.clear_widgets()
                        FourNumberTheory.newnumbers()
                        
            BoxLayout:
                cols: 2
                padding:10
                spacing:10
                size_hint: 1, None
                width:300
                size_hint_y: None
                height: self.minimum_height
                
                Label:
                    font_size: '20sp'
                    size_hint_y: None
                    height: 100
                    padding: 10, 10
                    text: "Solve For:"
                    
                Label:
                    font_size: '20sp'
                    size_hint_y: None
                    height: 100
                    padding: 10, 10
                    text: "Using:"
            
            BoxLayout:
                cols: 1
                size_hint: 1, None
                width:300
                size_hint_y: None
                height: self.minimum_height        
                
                BoxLayout:
                    id: answer
                    cols: 0
                    size_hint: 1, None
                    height: self.minimum_height          
            
                BoxLayout:
                    id: four_numbers
                    cols: 0
                    size_hint: 1, None
                    height: self.minimum_height             
            
            TextInput:
                id: input
                text: input.text
                hint_text: "Entry:"
                multiline: False
                font_size: '35sp'
                size_hint_y: None
                height: 150
                padding: 10  
                keyboard: False
                
            GridLayout:
                id: evaluated_answer
                cols: 1
                size_hint: 1, None
                height: self.minimum_height   
                
            BoxLayout:
                cols: 2
                padding:10
                spacing:10
                size_hint: 1, None
                width:300
                size_hint_y: None
                height: self.minimum_height
                
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
                        
                Button:
                    id: steps
                    text: "Calculate"   
                    font_size: '20sp'
                    size_hint_y: None
                    background_color: 0, 1 , 0 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        evaluated_answer.clear_widgets()
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
                        
                Button:
                    text: "."   
                    font_size: '30sp'
                    size_hint_y: None
                    background_color: 1, 1, 1, 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        input.text = input.text + "."          
                        
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
                        
""")

class FourNumberTheory(Screen):
    sm = ScreenManager()

    def __init__(self, **kwargs):
        super(FourNumberTheory, self).__init__(**kwargs)
        
        answer = str(random.randrange(0, 100))
        self.ids.answer.add_widget(Label(text= answer ,font_size = '20sp', size_hint_y= None, height=100))
        
        number1 = str(random.randrange(0, 9))
        number2 = str(random.randrange(0, 9))
        number3 = str(random.randrange(0, 9))
        number4 = str(random.randrange(0, 9))
        self.ids.four_numbers.add_widget(Label(text= number1 + " , " + number2 + " , " + number3 + " , " + number4 ,font_size = '20sp', size_hint_y= None, height=100))
    
    def steps(self,entry):
        
        print("FourNumberTheory = ",entry)
        self.ids.evaluated_answer.add_widget(Label(text= entry ,font_size = '20sp', size_hint_y= None, height=100))
        
        #Factorials function
        if entry.count("!") >= 1:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            exclamation_mark_index = entry.find("!")
            print("found ! at index: ",exclamation_mark_index)
            
            #Left Par
            left_entry = entry[:exclamation_mark_index+1]
            print('left_entry: ',left_entry)
            
            #find last (
            left_par_of_left_entry_index = left_entry.rfind("(")
            print('left_par_of_left_entry_index :',left_par_of_left_entry_index)
            
            
            print('---------------------------------------------')
            factorize = left_entry[left_par_of_left_entry_index:]
            print('factorize: ',factorize) #use this for replacement later
            
            right_par_of_factorize_index = factorize.rfind(")")
            print('right_par_of_factorize_index :',right_par_of_factorize_index)
            
            left_par_of_factorize_index = factorize.rfind("(")
            print('left_par_of_factorize_index :',left_par_of_factorize_index)
            
            content_to_factorize = factorize[left_par_of_factorize_index+1:right_par_of_factorize_index]
            print("content_to_factorize: ",content_to_factorize)
            
            #use eval incase there is math logic within parenthesis
            evaled_content_to_factorize = str(eval(str(content_to_factorize)))
            print("evaled_content_to_factorize: ",evaled_content_to_factorize)
            
            i = 1
            j = 1
            while i <= int(evaled_content_to_factorize):
                j = j * i
                print(j)
                i = i + 1
            
            entry = entry.replace(str(factorize),str(j))
            print("entry: ",entry)
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        
        #square root function
        if entry.count("√") >= 1:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            sqr_root_index = entry.find("√")
            print("found √ at index: ",sqr_root_index)
            
            #Left Par
            right_entry = entry[sqr_root_index:]
            print('right_entry: ',right_entry)
            
            #find first )
            right_par_of_left_entry_index = right_entry.find(")")
            print('right_par_of_left_entry_index: ',right_par_of_left_entry_index)
            print(right_entry[:right_par_of_left_entry_index+1])
            
            found_entry_to_replace = right_entry[:right_par_of_left_entry_index+1]
            print("found_entry_to_replace: ",found_entry_to_replace)
            
            content_to_square_root = right_entry[2:right_par_of_left_entry_index]
            print("content_to_square_root: ",content_to_square_root)
            
            #use eval incase there is math logic within parenthesis
            evaled_content_to_square_root = str(eval(str(content_to_square_root)))
            print("evaled_content_to_square_root: ",evaled_content_to_square_root)
            
            square_rooted_result = int(evaled_content_to_square_root) ** 0.5
            print("square_rooted_result",square_rooted_result)
            
            entry = entry.replace(str(found_entry_to_replace),str(int(square_rooted_result)))
            print("entry: ",entry)
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            
            #once entry is cleaned, set up rules for using each number and using each number once
            #match number to solve with entry evaled
            #add next number button to solve at end, clear button when pressed
        try:
            evaled_answer = str(eval(str(entry.replace("^","**"))))
            print("evaluated_answer : ",evaled_answer)
            self.ids.evaluated_answer.add_widget(Label(text= evaled_answer ,font_size = '20sp', size_hint_y= None, height=100))
    
        except Exception:
            self.ids.evaluated_answer.add_widget(Label(text= "Invalid Input" ,font_size = '20sp', size_hint_y= None, height=100))



        
    def newnumbers(self):
        
        self.ids.answer.clear_widgets()
        self.ids.four_numbers.clear_widgets()
        
        answer = str(random.randrange(0, 100))
        self.ids.answer.add_widget(Label(text= answer ,font_size = '20sp', size_hint_y= None, height=100))
        
        number1 = str(random.randrange(0, 9))
        number2 = str(random.randrange(0, 9))
        number3 = str(random.randrange(0, 9))
        number4 = str(random.randrange(0, 9))
        self.ids.four_numbers.add_widget(Label(text= number1 + " , " + number2 + " , " + number3 + " , " + number4 ,font_size = '20sp', size_hint_y= None, height=100))
    
        
                
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
    
