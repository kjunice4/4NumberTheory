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
            size_hint_y: None
            height:1200
            on_release:
                app.root.current = "Menu"
                root.manager.transition.direction = "left" 
        
        Button:
            font_size: '20sp'
            background_color: 0, 0 , 0 , 1
            size_hint_y: None
            height:300
            text: "4 Number Theory Game"
            on_release:
                app.root.current = "Menu"
                root.manager.transition.direction = "left" 
                
        Button:
            font_size: '20sp'
            background_color: 0, 0 , 0 , 1
            size_hint_y: None
            height:300
            text: "A Junice Industries Product"
            on_release:
                app.root.current = "Menu"
                root.manager.transition.direction = "left" 
                
        Button:
            font_size: '20sp'
            background_color: 0, 0 , 0 , 1
            size_hint_y: None
            height:300
            text: "Tap anywhere to Continue"
            on_release:
                app.root.current = "Menu"
                root.manager.transition.direction = "left" 
                
""")

# Menu
Builder.load_string("""
<Menu>
    id:Menu
    name:"Menu"
    
    GridLayout:
        cols: 1
        
        Label:
            font_size: '20sp'
            height:200
            padding: 10, 10
            text: "Menu"
        
        Button:
            text: "Play 4 Number Theory"   
            font_size: '20sp'
            background_color: 0, 0 , 1 , 1
            height:300
            padding: 10, 10
            on_release:
                app.root.current = "FourNumberTheory"
                root.manager.transition.direction = "left" 
        
        Button:
            font_size: '20sp'
            background_color: 1, 0, 1, 1
            height:300
            padding: 10, 10
            text: "How to Play Four Number Theory"
            on_release:
                app.root.current = "HowToPage"
                root.manager.transition.direction = "left"        
        
        Button:
            font_size: '20sp'
            height:300
            padding: 10, 10
            text: "Visit KSquared-Mathematics"
            on_release:
                import webbrowser
                webbrowser.open('https://www.juniceindustries.com') 
                
        Label:
            font_size: '20sp'
            height:200
            padding: 10, 10
            text: "Share 4 Number Theory Game"
                
        Image:
            source: 'KSquared_QR.png'
            size_hint_y: None
            height:800
            width:800
""")

#Updates
Builder.load_string("""
<HowToPage>
    id:HowToPage
    name:"HowToPage"
    
    GridLayout:
        cols: 1
        
        Label:
            font_size: '20sp'
            height:200
            padding: 10, 10
            text: "How to play 4 Number Theory"
        
        Button:
            id: steps
            text: "Menu"   
            font_size: '20sp'
            background_color: 0, 0 , 1 , 1
            height:200
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
    
    GridLayout:
        cols: 1
        
        Button:
            text: "Menu"   
            font_size: '20sp'
            height:200
            background_color: 0, 0 , 1 , 1
            on_release:
                app.root.current = "Menu"
                root.manager.transition.direction = "right" 
        
        BoxLayout:
            cols: 2
    
            Button:
                text: "New Numbers & Answer"   
                font_size: '15sp'
                height:200
                background_color: 1, 0 , 1 , 1
                on_release:
                    FourNumberTheory.newnumbers()
                    evaluated_answer.clear_widgets()
                    equal.clear_widgets()
                    input.text = ""
                    
            Button:
                text: "New Answer"   
                font_size: '20sp'
                height:200
                background_color: 0, 1 , 1 , 1
                on_release:
                    FourNumberTheory.nextAnswer()
                    evaluated_answer.clear_widgets()
                    equal.clear_widgets()
                    input.text = ""
                    
        BoxLayout:
            cols: 2
            
            Label:
                font_size: '20sp'
                text: "Use:"
            
            Label:
                font_size: '20sp'
                text: "To Solve for:"
                
        BoxLayout:
            cols: 1
            
            BoxLayout:
                id: four_numbers
                cols: 0
                
            BoxLayout:
                id: answer
                cols: 0
        
        BoxLayout:
            id: evaluated_answer
            cols: 0
            height:100
            
        BoxLayout:
            id: equal
            cols: 0
            height:100
        
        BoxLayout:
            cols: 2
            
            Button:
                id: steps
                text: "Clear"   
                font_size: '20sp'
                background_color: 1, 0 , 0 , 1
                height:200
                on_release:
                    input.text = ''
                    evaluated_answer.clear_widgets()
                    equal.clear_widgets()
            
            Button:
                id: steps
                text: "Backspace"   
                font_size: '20sp'
                background_color: 1, 0 , 1 , 1
                height:200
                on_release:
                    input.text = input.text[:-1]
                    
        TextInput:
            id: input
            text: input.text
            hint_text: "Entry:"
            multiline: False
            font_size: '35sp'
            height:200
            keyboard: False
            
        BoxLayout:
            cols: 2
            
            Button:
                id: steps
                text: "Calculate"   
                font_size: '20sp'
                background_color: 0, 1 , 0 , 1
                height:200
                on_release:
                    evaluated_answer.clear_widgets()
                    equal.clear_widgets()
                    FourNumberTheory.steps(input.text)   
                    
        BoxLayout:
            cols: 2
            
            Button:
                text: "("   
                font_size: '30sp'
                height:200
                background_color: 0, 1 , 1 , 1
                on_release:
                    input.text = input.text + "("
                    
            Button:
                text: ")"   
                font_size: '30sp'
                height:200
                background_color: 0, 1 , 1 , 1
                on_release:
                    input.text = input.text + ")"  
                    
            Button:
                text: "|("   
                font_size: '30sp'
                height:200
                background_color: 1, 1 , 0 , 1
                on_release:
                    input.text = input.text + "|(" 
                    
            Button:
                text: ")|"   
                font_size: '30sp'
                height:200
                background_color: 1, 1 , 0 , 1
                on_release:
                    input.text = input.text + ")|"
                    
        BoxLayout:
            cols: 2
            
            Button:
                text: "^("   
                font_size: '30sp'
                height:200
                background_color: 1, 1 , 1 , 1
                on_release:
                    input.text = input.text + "^("
                    
            Button:
                text: "√("   
                font_size: '30sp'
                height:200
                background_color: 1, 1 , 1 , 1
                on_release:
                    input.text = input.text + "√("
                    
            Button:
                text: ")!"   
                font_size: '30sp'
                height:200
                background_color: 1, 1 , 1 , 1
                on_release:
                    input.text = input.text + ")!"   
                    
        BoxLayout:
            cols: 2
            
            Button:
                text: "."   
                font_size: '30sp'
                height:200
                background_color: 1, 1 , 1 , 1
                on_release:
                    input.text = input.text + "."    
            
            Button:
                text: "*"   
                font_size: '30sp'
                height:200
                background_color: 0, 0 , 0 , 1
                on_release:
                    input.text = input.text + "*"
                    
             Button:
                 text: "/"   
                 font_size: '30sp'
                 height:200
                 background_color: 0, 0 , 0 , 1
                 on_release:
                     input.text = input.text + "/"
                    
        BoxLayout:
            cols: 2
            
            Button:
                text: "1"   
                font_size: '30sp'
                height:200
                background_color: 0, 0 , 0 , 1
                on_release:
                    input.text = input.text + "1"
                    
            Button:
                text: "2"   
                font_size: '30sp'
                height:200
                background_color: 0, 0 , 0 , 1
                on_release:
                    input.text = input.text + "2"
                    
            Button:
                text: "3"   
                font_size: '30sp'
                height:200
                background_color: 0, 0 , 0 , 1
                on_release:
                    input.text = input.text + "3"
                    
            Button:
                text: "+"   
                font_size: '30sp'
                height:200
                background_color: 0, 1 , 0 , 1
                on_release:
                    input.text = input.text + "+"
                    
        BoxLayout:
            cols: 2
            
            Button:
                text: "4"   
                font_size: '30sp'
                height:200
                background_color: 0, 0 , 0 , 1
                on_release:
                    input.text = input.text + "4"
                    
            Button:
                text: "5"   
                font_size: '30sp'
                height:200
                background_color: 0, 0 , 0 , 1
                on_release:
                    input.text = input.text + "5"
            
            Button:
                text: "6"   
                font_size: '30sp'
                height:200
                background_color: 0, 0 , 0 , 1
                on_release:
                    input.text = input.text + "6"
                    
            Button:
                text: "-"   
                font_size: '30sp'
                height:200
                background_color: 1, 0 , 0 , 1
                on_release:
                    input.text = input.text + "-"
            
        BoxLayout:
            cols: 2
            
            Button:
                text: "7"   
                font_size: '30sp'
                height:200
                background_color: 0, 0 , 0 , 1
                on_release:
                    input.text = input.text + "7"
                    
            Button:
                text: "8"   
                font_size: '30sp'
                height:200
                background_color: 0, 0 , 0 , 1
                on_release:
                    input.text = input.text + "8"
                    
            Button:
                text: "9"   
                font_size: '30sp'
                height:200
                background_color: 0, 0 , 0 , 1
                on_release:
                    input.text = input.text + "9"
                        
            Button:
                text: "0"   
                font_size: '30sp'
                height:200
                background_color: 0, 0 , 0 , 1
                on_release:
                    input.text = input.text + "0"
""")

class FourNumberTheory(Screen):
    sm = ScreenManager()
    
    def nextAnswer(self):
        self.ids.answer.clear_widgets()
        self.answer = str(random.randrange(0, 100))
        self.ids.answer.add_widget(Label(text= self.answer ,font_size = '20sp', size_hint_y= None, height=100))
    
    def newnumbers(self):
        self.ids.answer.clear_widgets()
        self.ids.four_numbers.clear_widgets()
        
        self.answer = str(random.randrange(0, 100))
        self.ids.answer.add_widget(Label(text= self.answer ,font_size = '20sp', size_hint_y= None, height=100))
        
        self.number1 = str(random.randrange(0, 9))
        self.number2 = str(random.randrange(0, 9))
        self.number3 = str(random.randrange(0, 9))
        self.number4 = str(random.randrange(0, 9))
        print("Numbers: ",self.number1 + " " + self.number2 + " " + self.number3 + " " +self.number4)
        self.ids.four_numbers.add_widget(Label(text= self.number1 + " , " + self.number2 + " , " + self.number3 + " , " + self.number4 ,font_size = '20sp', size_hint_y= None, height=100))
        
    def __init__(self, **kwargs):
        super(FourNumberTheory, self).__init__(**kwargs)
        
        self.answer = str(random.randrange(0, 100))
        self.ids.answer.add_widget(Label(text= self.answer ,font_size = '20sp', size_hint_y= None, height=100))
        
        self.number1 = str(random.randrange(0, 9))
        self.number2 = str(random.randrange(0, 9))
        self.number3 = str(random.randrange(0, 9))
        self.number4 = str(random.randrange(0, 9))
        print("Numbers: ",self.number1 + " " + self.number2 + " " + self.number3 + " " +self.number4)
        self.ids.four_numbers.add_widget(Label(text= self.number1 + " , " + self.number2 + " , " + self.number3 + " , " + self.number4 ,font_size = '20sp', size_hint_y= None, height=100))
    
    def steps(self,entry):
        
        print("FourNumberTheory = ",entry)
        
        while len(entry) > 0:
            try:
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
                
            except Exception:
                self.ids.evaluated_answer.add_widget(Label(text= "Invalid Factorial Input" ,font_size = '20sp', size_hint_y= None, height=100))
                break
            
            try:
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
                    
                    square_rooted_result = float(evaled_content_to_square_root) ** 0.5
                    print("square_rooted_result",square_rooted_result)
                    
                    entry = entry.replace(str(found_entry_to_replace),str(float(square_rooted_result)))
                    print("entry: ",entry)
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                
            except Exception:
                self.ids.evaluated_answer.add_widget(Label(text= "Invalid Square Root Input" ,font_size = '20sp', size_hint_y= None, height=100))
                break
            
            
                #once entry is cleaned, set up rules for using each number and using each number once
                #match number to answer to solve with entry evaled
                #add next number button to solve at end, clear button when pressed
            try:
                evaled_answer = str(eval(str(entry.replace("^","**").replace("|(","abs(").replace(")|",")"))))
                print("evaluated_answer : ",evaled_answer)
                print("answer to solve: ",self.answer)
                
                #was each number used atleast once?
                if str(entry).count(str(int(self.number1))) >= 1 and str(entry).count(str(int(self.number2))) >= 1 and str(entry).count(str(int(self.number3))) >= 1 and str(entry).count(str(int(self.number4))) >= 1:
                    print('ALL NUMBERS USED ONLY ONCE!!!!!!!!!!!!!!!!!!!!!!')
                    self.ids.evaluated_answer.add_widget(Label(text= entry ,font_size = '20sp', size_hint_y= None, height=100))
                    
                else:
                    print('ALL NUMBERS NOT USED')
                    self.ids.equal.add_widget(Label(text= "Not all numbers used only once!" ,font_size = '20sp', size_hint_y= None, height=100))
                    break
                
                #Does evaled answer equal random answer?
                if float(evaled_answer) == float(self.answer):
                    self.ids.equal.add_widget(Label(text= str(evaled_answer) ,font_size = '20sp', size_hint_y= None, height=100))
                    self.ids.equal.add_widget(Label(text= "Correct!" ,font_size = '20sp', size_hint_y= None, height=100))
                    break
                else:
                    self.ids.equal.add_widget(Label(text= "Nope! Try again!" ,font_size = '20sp', size_hint_y= None, height=100))
                break
            
            except Exception:
                self.ids.evaluated_answer.add_widget(Label(text= "Invalid Input" ,font_size = '20sp', size_hint_y= None, height=100))
                break
    
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
    
