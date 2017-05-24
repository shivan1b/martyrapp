from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.screenmanager import FadeTransition
from kivy.animation import Animation
from kivy.lang import Builder
from kivy.uix.rst import RstDocument
from kivy.factory import Factory
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior


with open('data/about.rst') as f:
	desc = f.read()

sm = ScreenManager(transition=FadeTransition())

class DescMartyr(Screen):
    Builder.load_string('''
<DescMartyr>
    name: 'DescMartyr'
    canvas.before:
    	Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size
    BoxLayout
        orientation: 'vertical'
        spacing: dp(4)
        ScrollView
            BoxLayout
                Image
                    source: 'data/desc.jpg'
            	RstDocument
            		id: lbl
        ''')


class PicScreen(Screen):
	 Builder.load_string('''
<PicScreen>
    name: 'PicScreen'
    canvas.before:
    	Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size
    ''')


dscm = DescMartyr()
dscm.ids.lbl.text = desc

anim = Animation(pos=(0,0), size=(400,600), duration=2.)


class ImBut(ButtonBehavior, Image):
    Builder.load_string('''
<ImBut>
    source: 'data/patel.jpg'
    halign: 'center'
    padding: dp(10), dp(10)
    valign: 'middle'
    allow_stretch: True
            ''')


class Martyr(App):
    '''
    Shows a martyr's picture on click of which about martyr is shown
    '''
    def build(self):
        self.scr1 = PicScreen()
        self.imbut = Factory.ImBut()
        self.imbut.bind(on_press=self.callback)
        self.scr1.add_widget(self.imbut)
        sm.add_widget(self.scr1)
        sm.current = 'PicScreen'
        return sm

    def callback(self, *args):
        anim.start(self.imbut)
        self.imbut.size_hint = None, None
        anim.bind(on_complete=self.setscr)

    def setscr(self, *args):
        sm.add_widget(dscm)
        sm.current = 'DescMartyr'


Martyr().run()