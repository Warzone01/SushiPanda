# -*- coding: utf-8 -*-

import kivy

kivy.require('1.10.0')

from kivy.lang import Builder
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition, \
    NoTransition
from kivy.uix.scrollview import ScrollView
from kivy.properties import ObjectProperty
import json

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
            size_hint_y: 1
            size_hint_x: 1
            height: 1000
            orientation: 'vertical'
'''
chicago_button = '''
            SmartTileWithLabel:
                allow_stretch: False
                mipmap: False
                box_color: (1, 1, 1, 0.5)
                source: 'Images/Sushi/CicagoRoll.jpg'
                text: 'Добавить в корзину'
'''
chicago_summ = '''
        BoxLayout:
            size_hint_y: 0.3
            size_hint_x: None
            MDIconButton:
                icon: 'minus'
                size_hint_x: None
                pos_hint: {'center_x': 0.25, 'center_y': 0.8}
            Label:
                text: '1'
                color: 0, 0, 0, 0.5
                size_hint_x: None
                pos_hint: {'center_x': 0.25, 'center_y': 0.8}
            MDIconButton:
                icon: 'plus'
                size_hint_x: None
                pos_hint: {'center_x': 0.25, 'center_y': 0.8}
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
 
class Chicago_Roll(ScrollView, Screen):
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

        # Builder.load_file('kv/manager.kv')
        # Builder.load_file('kv/main_screen.kv')
        # Builder.load_file('kv/ms_item.kv')
        # Builder.load_file('kv/ms_item_2.kv')
        # Builder.load_file('kv/sushi_screan.kv')

        self.icon = 'Images/panda.png'
        root = PandaManager(transition=NoTransition())

        main_menu = self.main_data['main_menu']
        for i in range(1, len(main_menu)):
            wid = Builder.template('PictButton', **{
                'img': main_menu[str(i)]['img'],
                'link': main_menu[str(i)]['lnk'],
            })

            root.ids['Menu'].ids['main_screen_container'].add_widget(wid)

        sushi = self.main_data['second_level']['Sushi']

        for i in range(1, len(sushi)):
            wid = Builder.template('PictButtonMenu', **{
                'img': sushi[str(i)]['img'],
                'txt': sushi[str(i)]['txt'],
                'price': sushi[str(i)]['price'],
                'lnk': sushi[str(i)]['lnk']
            })
            root.ids['Sushi'].ids['sushi_container'].add_widget(wid)

        return root


if __name__ == '__main__':
    PandaApp().run()
