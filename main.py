# -*- coding: utf-8 -*-

import kivy

kivy.require('1.10.0')
from kivy.lang import Builder
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition, \
    NoTransition
from kivy.uix.scrollview import ScrollView
from kivy.properties import ObjectProperty, NumericProperty
import json
from kivy.uix.label import Label
from kivy.storage.jsonstore import JsonStore
from os.path import join


Window.clearcolor = (1, 1, 1, 1)
# Window.size = (720, 1280)

Builder.load_string('''
#:kivy 1.10
#:import SmartTile kivymd.grid.SmartTile
#:import MDBottomNavigationItem kivymd.tabs.MDBottomNavigationItem
''')

sushi_buttons = ''
cart_head = '''
<Cart>:
    name: 'Cart'
    BoxLayout:
        orientation: 'vertical'
        ActionBar:
            background_color: (0, 5, 0, 0.8)
            pos_hint: {'top':1}
            ActionView:
                use_sperator: True
                ActionPrevious: 
                    app_icon: 'Images/panda.png'
                    title: 'Caffe Panda'
                    with_previous: True
                    on_release: root.manager.current = 'Menu'
                ActionOverflow:
                ActionButton:
                    icon: 'ico.png'
'''
cart_buttons_head = '''
        ScrollView:
            BoxLayout:
                orientation: 'vertical'
'''

cart_label = '''       
                Label:
                    text: 'Ваша корзина пуста'
                    color: (0, 0, 0, 0.5)
                    font_size: 30

'''

cart_shop = ''
chicago_roll_head = '''
<Chicago_Roll>:
    name: 'Chicago_Roll'
    BoxLayout:
        orientation: 'vertical'
        ActionBar:
            background_color: (0, 5, 0, 0.8)
            pos_hint: {'top':1}
            ActionView:
                use_sperator: True
                ActionPrevious:
                    app_icon: 'Images/panda.png'
                    title: 'Caffe Panda'
                    with_previous: True
                    on_release: root.manager.current = 'Sushi'
                ActionOverflow:
                ActionButton:
                    icon: 'ico.png'
                    on_release: root.manager.current = 'Cart'
'''
chicago_roll_info = '''
        BoxLayout:
            cols: 1
            orientation: 'vertical' 
            size_hint_x: 1
            size_hint_y: 3
            spacing: 3
            padding: 3
'''
chicago_button = '''
            Image:
                source: 'Images/Sushi/CicagoRoll.png'
'''
chicago_summ = '''
        RelativeLayout:
            pos: self.parent.pos
            size: self.parent.size
            BoxLayout:
                size_hint_y: 1
                size_hint_x: 1
                spacing: 3
                padding: 3
                MDIconButton:
                    pos_hint:{"center_x":0,"center_y":0.5}
                    id: minus
                    icon: 'minus'
                    on_release: root.minus()
                MyLabel:
                    id: lb1
                    pos_hint: {'center_x': 0, 'center_y': 0.5}
                    text: "Кол-во: {}".format(self.value)
                    color: 0, 0, 0, 0.5
                    font_size: 30
                MDIconButton:
                    pos_hint:{"center_x":0,"center_y":0.5}
                    id: plus
                    icon: 'plus'
                    on_release: root.fc()
                MDFlatButton:
                    id: cartbutton
                    text: "Добавить в корзину"
                    pos_hint: {'center_x': 0, 'center_y': 0.5}

'''
chicago_text = '''
        ScrollView:
            BoxLayout:
                orientation: 'vertical'
                size_hint_y: None
                height: 300
'''
chicago_roll_label = ''


class Sushi(Screen):
    pass

class MyLabel(Label):
    value = NumericProperty(1)
 
class Chicago_Roll(ScrollView, Screen):

    def fc(self):
        if self.ids.lb1.value < 10:
            self.ids.lb1.value += 1
    def minus(self):
        if self.ids.lb1.value > 1: 
            self.ids.lb1.value -= 1
        
    chicago_roll_label = ''
    list_chicago = [
        {
            'txt': 'Чикаго ролл',
            'size': 35,
            'col': (0, 0, 0, 0.5),
            'font': 'Roboto'
        },
        {
            'txt': '260 руб.',
            'size': 30,
            'col': (0, 0, 0, 0.5),
            'font': 'Roboto'
        },
        {
            'txt': 'бекон,',
            'size': 20,
            'col': (0, 0, 0, 0.5),
            'font': 'Roboto'
        },
        {
            'txt': 'лосось жаренный,',
            'size': 20,
            'col': (0, 0, 0, 0.5),
            'font': 'Roboto'
        },
        {
            'txt': 'сливочный сыр,',
            'size': 20,
            'col': (0, 0, 0, 0.5),
            'font': 'Roboto'
        },
        {
            'txt': 'огурец.',
            'size': 20,
            'col': (0, 0, 0, 0.5),
            'font': 'Roboto'
        },
        {
            'txt': '8шт./290гр.',
            'size': 20,
            'col': (0, 0, 0, 0.5),
            'font': 'Roboto'
        },
    ]
    templ = '''
                Label:
                    text: '{}'
                    font_size: {}
                    color: {}
                    font_name: '{}'
    '''
    for i in range(len(list_chicago)):
        chicago_roll_label += templ.format(list_chicago[i]['txt'],
                                           list_chicago[i]['size'],
                                           list_chicago[i]['col'],
                                           list_chicago[i]['font'])
    cr = chicago_roll_head + chicago_roll_info + chicago_button + chicago_summ + chicago_text + chicago_roll_label
    Chicago_Roll = Builder.load_string(cr)
    
class Cart(ScrollView, Screen):

    cart_shop = '[]'
    if cart_shop == '[]':
        cart_shop = cart_label
    # else:
    #     for i in range(len(cart)):
    #         cart_shop += cart.format(cart)
    cart = cart_head + cart_buttons_head + cart_shop
    Cart = Builder.load_string(cart)


class PandaManager(ScreenManager):
    pass

class Menu(Screen):
    pass

class PandaApp(App):
    

    def load_json(self):
        with open('assets/main.json', encoding='utf-8') as json_data:
            d = json.load(json_data)
        return d

    def build(self):
        # import pprint
        self.main_data = self.load_json()
        with open('kv/manager.kv', encoding='utf8') as f:
            Builder.load_string(f.read())
        with open('kv/main_screen.kv', encoding='utf8') as f:
            Builder.load_string(f.read())
        with open('kv/ms_item.kv', encoding='utf8') as f:
            Builder.load_string(f.read())
        with open('kv/ms_item_2.kv', encoding='utf8') as f:
            Builder.load_string(f.read())
        with open('kv/sushi_screan.kv', encoding='utf8') as f:
            Builder.load_string(f.read())

        self.icon = 'Images/panda.png'
        root = PandaManager(transition=NoTransition())
# прорисовка меню
        main_menu = self.main_data['main_menu']
        for i in range(1, len(main_menu)):
            wid = Builder.template('PictButton', **{
                'img': main_menu[str(i)]['img'],
                'link': main_menu[str(i)]['lnk'],
            })

            root.ids['Menu'].ids['main_screen_container'].add_widget(wid)
# прорисовка списка товаров
        sushi = self.main_data['second_level']['Sushi']

        for i in range(1, len(sushi)):
            wid = Builder.template('PictButtonMenu', **{
                'img': sushi[str(i)]['img'],
                'txt': sushi[str(i)]['txt'],
                'price': sushi[str(i)]['price'],
                'lnk': sushi[str(i)]['lnk']
            })
            root.ids['Sushi'].ids['sushi_container'].add_widget(wid)

        self.bind(on_start=self.post_build_init)

        return root

    def post_build_init(self,ev):
        from kivy.base import EventLoop
        EventLoop.window.bind(on_keyboard=self.hook_keyboard)

    def hook_keyboard(self, window, key, *largs):
        if key == 27:
            if self.root.current == 'Menu':
                return False
            elif self.root.current == 'Chicago_Roll':
                self.root.current = 'Sushi'
            else:
                self.root.current = 'Menu'
            return True 


if __name__ == '__main__':
    PandaApp().run()
