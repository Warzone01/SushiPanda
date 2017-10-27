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

Window.clearcolor = (1, 1, 1, 1)
# Window.size = (720, 1280)

Builder.load_string('''
#:kivy 1.10
#:import SmartTile kivymd.grid.SmartTile
#:import MDBottomNavigationItem kivymd.tabs.MDBottomNavigationItem
''')

# Меню суши
sushi_head = '''
<Sushi>:
    name: 'Sushi'
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
                    on_release: root.manager.current = 'Cart'
'''

# Настройки кнопок
sushi_buttons_head = '''
        ScrollView:
            GridLayout:
                orientation: 'vertical'
                cols: 2
                size_hint_y: None
                row_default_height: (self.width - self.cols*self.spacing[0])/2
                row_force_default: True
                height: self.minimum_height
                padding: 0
                spacing: 0
'''
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
                on_press: cart_shop.append(chicago_button)

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
    sushi_buttons = ''
    img_list_sushi = [
        {
            'img': 'Images/Sushi/CicagoRoll.jpg',
            'txt': 'Чикаго Ролл',
            'price': ' 260руб',
            'lnk': 'Chicago_Roll'
        },
        {
            'img': 'Images/Sushi/LavaSLososem.jpg',
            'txt': 'Лава с лососем',
            'price': ' 260руб',
            'lnk': 'Chicago_Roll'
        },
        {
            'img': 'Images/Sushi/LavaSKrabom.jpg',
            'txt': 'Лава с крабом',
            'price': ' 260руб',
            'lnk': 'Chicago_Roll'
        },
        {
            'img': 'Images/Sushi/LavaSKrevetkoi.jpg',
            'txt': 'Лава с криветкой',
            'price': ' 260руб',
            'lnk': 'Chicago_Roll'
        },
        {
            'img': 'Images/Sushi/LavaSUgrem.jpg',
            'txt': 'Лава с угрём',
            'price': ' 260руб',
            'lnk': 'Chicago_Roll'
        },
        {
            'img': 'Images/Sushi/RollOvosh.jpg',
            'txt': 'Ролл в темпурной крошке(Овощной)',
            'price': ' 260руб',
            'lnk': 'Chicago_Roll'
        },
        {
            'img': 'Images/Sushi/RollLosos.jpg',
            'txt': 'Ролл в темпурной крошке с лососем',
            'price': ' 260руб',
            'lnk': 'Chicago_Roll'
        },
        {
            'img': 'Images/Sushi/RollChicken.jpg',
            'txt': 'Ролл в темпурной крошке с курой',
            'price': ' 260руб',
            'lnk': 'Chicago_Roll'
        },
        {
            'img': 'Images/Sushi/HanMaki.jpg',
            'txt': 'Хан маки',
            'price': ' 260руб',
            'lnk': 'Chicago_Roll'
        },
        {
            'img': 'Images/Sushi/FreshRoll.jpg',
            # 'txt': 'Фреш ролл',
            'txt': 'Филадельфия де люкс',
            'price': ' 260руб',
            'lnk': 'Chicago_Roll'
        },
        {
            'img': 'Images/Sushi/SamuraiMaki.jpg',
            'txt': 'Самурай маки',
            'price': ' 260руб',
            'lnk': 'Chicago_Roll'
        },
        {
            'img': 'Images/Sushi/SakuraMaki.jpg',
            'txt': 'Сакура маки',
            'price': ' 260руб',
            'lnk': 'Chicago_Roll'
        },
        {
            'img': 'Images/Sushi/PandaMaki.jpg',
            'txt': 'Панда маки',
            'price': ' 260руб',
            'lnk': 'Chicago_Roll'
        },
        {
            'img': 'Images/Sushi/MunhenRoll.jpg',
            'txt': 'Мюнхен ролл',
            'price': ' 260руб',
            'lnk': 'Chicago_Roll'
        },
        {
            'img': 'Images/Sushi/MonteKarlo.jpg',
            'txt': 'Монте карло',
            'price': ' 260руб',
            'lnk': 'Chicago_Roll'
        },
        {
            'img': 'Images/Sushi/MaiamiMaki.jpg',
            'txt': 'Майами маки',
            'price': ' 260руб',
            'lnk': 'Chicago_Roll'
        },
        {
            'img': 'Images/Sushi/LeonaRoll.jpg',
            'txt': 'Леона ролл',
            'price': ' 260руб',
            'lnk': 'Chicago_Roll'
        },
        {
            'img': 'Images/Sushi/LiteRoll.jpg',
            'txt': 'Лайт ролл',
            'price': ' 260руб',
            'lnk': 'Chicago_Roll'
        },
        {
            'img': 'Images/Sushi/KanadskiiRoyalo.jpg',
            'txt': 'Канадский тобияко роял',
            'price': ' 260руб',
            'lnk': 'Chicago_Roll'
        },
        {
            'img': 'Images/Sushi/KanadaSKrevetkoi.jpg',
            'txt': 'Канада с креветкой',
            'price': ' 260руб',
            'lnk': 'Chicago_Roll'
        },
        {
            'img': 'Images/Sushi/CaliforniaMaki.jpg',
            'txt': 'Калифорния маки',
            'price': ' 260руб',
            'lnk': 'Chicago_Roll'
        },
        {
            'img': 'Images/Sushi/GonkongRoll.jpg',
            'txt': 'Гонконг ролл',
            'price': ' 260руб',
            'lnk': 'Chicago_Roll'
        },
        {
            'img': 'Images/Sushi/GeishaMaki.jpg',
            'txt': 'Гейша маки',
            'price': ' 260руб',
            'lnk': 'Chicago_Roll'
        },
        {
            'img': 'Images/Sushi/BengalskiRoll.jpg',
            'txt': 'Бенгальский ролл',
            'price': ' 260руб',
            'lnk': 'Chicago_Roll'
        },
        {
            'img': 'Images/Sushi/VeneciaRoll.jpg',
            'txt': 'Венеция ролл',
            'price': ' 260руб',
            'lnk': 'Chicago_Roll'
        },
    ]
    templ = '''
                SmartTileWithLabel:
                    allow_stretch: False
                    mipmap: False
                    box_color: (1, 1, 1, 0.5)
                    source: "{}"
                    text: '{}' + '\\n {}'
                    on_release: root.manager.current = '{}'
    '''
    for i in range(len(img_list_sushi)):
        sushi_buttons += templ.format(img_list_sushi[i]['img'],
                                      img_list_sushi[i]['txt'],
                                      img_list_sushi[i]['price'],
                                      img_list_sushi[i]['lnk'])
    ss = sushi_head + sushi_buttons_head + sushi_buttons
    Sushi = Builder.load_string(ss)


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
    cr = chicago_roll_head + chicago_roll_info + chicago_button + chicago_text + chicago_roll_label
    Chicago_Roll = Builder.load_string(cr)


class Cart(ScrollView, Screen):
    # cart_shop = '[]'
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
    img_list_menu = [
        {
            "img": 'Images/Menu/Candies.jpg',
            "lnk": 'Sushi'
        },
        {
            'img': 'Images/Menu/Garneir.jpg',
            'lnk': 'Sushi'
        },
        {
            'img': 'Images/Menu/Homosakki.jpg',
            'lnk': 'Sushi'
        },
        {
            'img': 'Images/Menu/Hot.jpg',
            'lnk': 'Sushi'
        },
        {
            'img': 'Images/Menu/MoreRolls.jpg',
            'lnk': 'Sushi'
        },
        {
            'img': 'Images/Menu/Nigiri.jpg',
            'lnk': 'Sushi'
        },
        {
            'img': 'Images/Menu/Packs.jpg',
            'lnk': 'Sushi'
        },
        {
            'img': 'Images/Menu/Pasta.jpg',
            'lnk': 'Sushi'
        },
        {
            'img': 'Images/Menu/Pizza.jpg',
            'lnk': 'Sushi'
        },
        {
            'img': 'Images/Menu/Rolls.jpg',
            'lnk': 'Sushi'
        },
        {
            'img': 'Images/Menu/Salades.jpg',
            'lnk': 'Sushi'
        },
        {
            'img': 'Images/Menu/Soup.jpg',
            'lnk': 'Sushi'
        },
        {
            'img': 'Images/Menu/Sushi.jpg',
            'lnk': 'Sushi'
        },
        {
            'img': 'Images/Menu/Thakuski.jpg',
            'lnk': 'Sushi'
        },
    ]

    def build(self):
        # import pprint
        Builder.load_file('kv/manager.kv')
        Builder.load_file('kv/main_screen.kv')
        Builder.load_file('kv/ms_item.kv')

        self.icon = 'Images/panda.png'
        root = PandaManager(transition=NoTransition())

        for i in range(len(self.img_list_menu)):
            wid = Builder.template('PictButton', **{
                'img': self.img_list_menu[i]['img'],
                'link': self.img_list_menu[i]['lnk'],
            })

            root.ids['Menu'].ids['main_screen_container'].add_widget(wid)

        return root


if __name__ == '__main__':
    PandaApp().run()
