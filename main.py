#!/home/viktor/Dokumente/Kreschendo/Projekte/FoodManagerMD/vpython/bin/python
# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.metrics import dp
from kivy.storage.jsonstore import JsonStore
from kivy.utils import platform
from kivy.uix.screenmanager import Screen
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.label import Label
from kivy.properties import BooleanProperty
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.boxlayout import BoxLayout

from kivymd.dialog import MDDialog
from kivymd.label import MDLabel
from kivymd.snackbar import Snackbar
from kivymd.theming import ThemeManager
from kivymd.textfields import MDTextField

from datetime import datetime
from math import floor, ceil
import os
from shutil import copyfile

# from kivy.core.window import Window
# Window.size = (600, 800)


class WelcomeScreen(Screen):
    pass


class ViewItemsScreen(Screen):
    pass


class RecipesScreen(Screen):
    pass


class OverViewScreen(Screen):
    pass


class InputItemsScreen(Screen):
    pass


class HistoryScreen(Screen):
    pass


class BuyingItemsScreen(Screen):
    pass


class AddRecipesScreen(Screen):
    pass

class AboutScreen(Screen):
    pass


class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior, RecycleBoxLayout):
    ''' Adds selection and focus behaviour to the view. '''
    pass


class SelectableItemLabel(RecycleDataViewBehavior, Label):
    ''' Add selection support to the Label '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        return super(SelectableItemLabel, self).refresh_view_attrs(rv, index, data)

    def on_touch_down(self, touch):
        ''' Add selection on touch down '''
        if super(SelectableItemLabel, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        ''' Respond to the selection of items in the view. '''
        global selection_item
        self.selected = is_selected
        if is_selected:
            selection_item = rv.data[index]['text']
            fmapp.change_item_image_info()


class SelectableAddItemToRecipeLabel(RecycleDataViewBehavior, Label):
    ''' Add selection support to the Label '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        return super(SelectableAddItemToRecipeLabel, self).refresh_view_attrs(rv, index, data)

    def on_touch_down(self, touch):
        ''' Add selection on touch down '''
        if super(SelectableAddItemToRecipeLabel, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        ''' Respond to the selection of items in the view. '''
        global selection
        self.selected = is_selected
        if is_selected:
            selection = rv.data[index]['text']
            fmapp.show_item_weight_recipe()


class SelectableRecipeItemLabel(RecycleDataViewBehavior, Label):
    ''' Add selection support to the Label '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        return super(SelectableRecipeItemLabel, self).refresh_view_attrs(rv, index, data)

    def on_touch_down(self, touch):
        ''' Add selection on touch down '''
        if super(SelectableRecipeItemLabel, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        ''' Respond to the selection of items in the view. '''
        global selection_iteminrecipe
        self.selected = is_selected
        if is_selected:
            selection_iteminrecipe = rv.data[index]['text']
            # fmapp.show_item_weight_recipe()


class SelectableRecipeLabel(RecycleDataViewBehavior, Label):
    ''' Add selection support to the Label '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        return super(SelectableRecipeLabel, self).refresh_view_attrs(rv, index, data)

    def on_touch_down(self, touch):
        ''' Add selection on touch down '''
        if super(SelectableRecipeLabel, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        ''' Respond to the selection of items in the view. '''
        global selection_recipe
        self.selected = is_selected
        if is_selected:
            selection_recipe = rv.data[index]['text']
            fmapp.show_items_in_recipe()


class SelectableRecipeAtHomeLabel(RecycleDataViewBehavior, Label):
    ''' Add selection support to the Label '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        return super(SelectableRecipeAtHomeLabel, self).refresh_view_attrs(rv, index, data)

    def on_touch_down(self, touch):
        ''' Add selection on touch down '''
        if super(SelectableRecipeAtHomeLabel, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        ''' Respond to the selection of items in the view. '''
        global selection_viarecipe
        self.selected = is_selected
        if is_selected:
            selection_viarecipe = rv.data[index]['text']


class SelectableItemAtHomeLabel(RecycleDataViewBehavior, Label):
    ''' Add selection support to the Label '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        return super(SelectableItemAtHomeLabel, self).refresh_view_attrs(rv, index, data)

    def on_touch_down(self, touch):
        ''' Add selection on touch down '''
        if super(SelectableItemAtHomeLabel, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        ''' Respond to the selection of items in the view. '''
        global selection_itemathome
        self.selected = is_selected
        if is_selected:
            selection_itemathome = rv.data[index]['text']
            fmapp.show_item_weight_used_home(selectedItem=selection_itemathome)


class SelectableRecipeAddCartLabel(RecycleDataViewBehavior, Label):
    ''' Add selection support to the Label '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        return super(SelectableRecipeAddCartLabel, self).refresh_view_attrs(rv, index, data)

    def on_touch_down(self, touch):
        ''' Add selection on touch down '''
        if super(SelectableRecipeAddCartLabel, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        ''' Respond to the selection of items in the view. '''
        global selection_recipetocart
        self.selected = is_selected
        if is_selected:
            selection_recipetocart = rv.data[index]['text']


class SelectableItemAddCartLabel(RecycleDataViewBehavior, Label):
    ''' Add selection support to the Label '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        return super(SelectableItemAddCartLabel, self).refresh_view_attrs(rv, index, data)

    def on_touch_down(self, touch):
        ''' Add selection on touch down '''
        if super(SelectableItemAddCartLabel, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        ''' Respond to the selection of items in the view. '''
        global selection_itemtocart
        self.selected = is_selected
        if is_selected:
            selection_itemtocart = rv.data[index]['text']
            fmapp.show_cartitem_weight_used_home(selection_itemtocart)


class SelectableCartViewLabel(RecycleDataViewBehavior, Label):
    ''' Add selection support to the Label '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        return super(SelectableCartViewLabel, self).refresh_view_attrs(rv, index, data)

    def on_touch_down(self, touch):
        ''' Add selection on touch down '''
        if super(SelectableCartViewLabel, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        ''' Respond to the selection of items in the view. '''
        global selection_cartview
        self.selected = is_selected
        if is_selected:
            selection_cartview = rv.data[index]['text']


class SelectableInCartItemLabel(RecycleDataViewBehavior, Label):
    ''' Add selection support to the Label '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        return super(SelectableInCartItemLabel, self).refresh_view_attrs(rv, index, data)

    def on_touch_down(self, touch):
        ''' Add selection on touch down '''
        if super(SelectableInCartItemLabel, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        ''' Respond to the selection of items in the view. '''
        global selection_incartitem
        self.selected = is_selected
        if is_selected:
            selection_incartitem = rv.data[index]['text']


class SelectableStagedItemLabel(RecycleDataViewBehavior, Label):
    ''' Add selection support to the Label '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        return super(SelectableStagedItemLabel, self).refresh_view_attrs(rv, index, data)

    def on_touch_down(self, touch):
        ''' Add selection on touch down '''
        if super(SelectableStagedItemLabel, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        ''' Respond to the selection of items in the view. '''
        global selection_stageditem
        self.selected = is_selected
        if is_selected:
            selection_stageditem = rv.data[index]['text']


# APP CLASS
class FoodManagerApp(App):
    theme_cls = ThemeManager()
    title = "Food Manager"
    theme_cls.theme_style = 'Dark'
    icon = 'img/groceries.png'
    theme_cls.primary_palette = 'Teal'

    if platform == 'android':
        dir_path = ''
    else:
        dir_path = f'{os.getcwd()}/'

    edit_recipe_bool = False
    edit_item_bool = False

    menu_items = [
        {'viewclass': 'MDMenuItem',
         'text': 'Settings'},
        {'viewclass': 'MDMenuItem',
         'text': 'Themes'}
    ]

    def permission_exception(function):
        """
        A decorator that wraps the passed in function and throws a permission denied warning.
        """
        # @functools.wraps(function)
        def wrapper(self, *args, **kwargs):
            try:
                function(self, *args, **kwargs)
            except:
                self.show_permission_warning()                
        return wrapper

    @permission_exception
    def create_dir_structure(self):        
        if not os.path.exists(self.dir_path + 'data/'):
            os.makedirs(self.dir_path + 'data/')
        if not os.path.exists(self.dir_path + 'img/'):
            os.makedirs(self.dir_path + 'img/')

    @permission_exception
    def create_backup_dirs(self):
        if platform == 'android':
            if not os.path.exists('/storage/emulated/0/FoodManager'):
                os.makedirs('/storage/emulated/0/FoodManager/')

    @permission_exception
    def back_up(self):
        self.create_backup_dirs()
        if platform == 'android':
            if os.path.exists('data/athome.json'):
                copyfile(
                    'data/athome.json',
                    '/storage/emulated/0/FoodManager/athome.json'
                )

            if os.path.exists('data/cartitemlist.json'):
                copyfile(
                    'data/cartitemlist.json',
                    '/storage/emulated/0/FoodManager/cartitemlist.json'
                )

            if os.path.exists('data/foodmanager.json'):
                copyfile(
                    'data/foodmanager.json',
                    '/storage/emulated/0/FoodManager/foodmanager.json'
                )

            if os.path.exists('data/recipes.json'):
                copyfile(
                    'data/recipes.json',
                    '/storage/emulated/0/FoodManager/recipes.json'
                )

            if os.path.exists('/storage/emulated/0/FoodManager/history.json'):
                copyfile(
                    'data/history.json',
                    '/storage/emulated/0/FoodManager/history.json'
                )

    #########################################################
    # WELCOME
    #########################################################
    @permission_exception
    def restore_files(self):
        if platform == 'android':
            if os.path.exists('/storage/emulated/0/FoodManager/athome.json'):
                copyfile('/storage/emulated/0/FoodManager/athome.json',
                         'data/athome.json')

            if os.path.exists('/storage/emulated/0/FoodManager/cartitemlist.json'):
                copyfile('/storage/emulated/0/FoodManager/cartitemlist.json',
                         'data/cartitemlist.json')

            if os.path.exists('/storage/emulated/0/FoodManager/foodmanager.json'):
                copyfile('/storage/emulated/0/FoodManager/foodmanager.json',
                         'data/foodmanager.json')

            if os.path.exists('/storage/emulated/0/FoodManager/recipes.json'):
                copyfile('/storage/emulated/0/FoodManager/recipes.json',
                         'data/recipes.json')

            if os.path.exists('/storage/emulated/0/FoodManager/history.json'):
                copyfile('/storage/emulated/0/FoodManager/history.json',
                         'data/history.json')

            self.show_snackbar('Data restored!')
            self.init_data()
            self.refresh_all()
        self.dialog.dismiss()

    def show_restore_warning_dialog(self):
        content = MDLabel(font_style='Body1',
                          theme_text_color='Secondary',
                          text="Are you sure you want to overwrite your internal data with external data from /storage/emulated/0/FoodManager?",
                          size_hint_y=None,
                          valign='top')
        content.bind(texture_size=content.setter('size'))
        self.dialog = MDDialog(title="Warning: Restore data?",
                               content=content,
                               size_hint=(.8, None),
                               height=dp(200),
                               auto_dismiss=True)
        self.dialog.add_action_button("Yes",
                                      action=lambda *x: self.restore_files())
        self.dialog.add_action_button("No",
                                      action=lambda *x: self.dialog.dismiss())
        self.dialog.open()

    #########################################################
    # OVERVIEW
    #########################################################
    def view_home_items(self):
        homeitemsInput = [drow[0] +
                          ' | ' +
                          str(drow[1]['TotalWeight']) +
                          ' (=' + str(drow[1]['ItemWeight']) +
                          ' x ' + str(drow[1]['Count']) +
                          ')' for drow in self.athome.find()]

        FoodWeight, FoodCost = 0, 0

        for itm in homeitemsInput:
            FoodWeight += float(itm.split(' | ')[1].split('g (=')[0])
            FoodCost += (float(self.store.get(itm.split(' | ')[0])['FoodCost']) *
                         float(itm.split(' | ')[1].split('g (=')[0]) /
                         float(self.store.get(itm.split(' | ')[0])['FoodWeight']))

        homeInfoView_item_strings = ['Cost: {}€'.format(round(float(FoodCost), 2)),
                                     'Weight: {}g'.format(FoodWeight)]
        self.root.ids.overview_screen.ids.homeInfoView.data = [{'text': str(x)} for x in homeInfoView_item_strings]

        homeitemsInput.sort()
        self.root.ids.overview_screen.ids.homeitems.data = [{'text': str(x)} for x in homeitemsInput]
        # self.root.ids.overview_screen.ids.homeitems.item_strings = homeitemsInput
        # self.root.ids.buyingitems_screen.ids.actualitemsatHome.item_strings = homeitemsInput
        self.root.ids.buyingitems_screen.ids.actualitemsatHome.data = [{'text': str(x)} for x in homeitemsInput]

    def view_cart_items(self):
        cartlistInput = [drow[0] +
                         ' | ' +
                         str(drow[1]['TotalWeight']) +
                         ' (=' + str(drow[1]['ItemWeight']) +
                         ' x ' + str(drow[1]['Count']) +
                         ')' for drow in self.cartlist.find()]

        FoodWeight, FoodCost = 0, 0

        for itm in cartlistInput:
            FoodWeight += float(itm.split(' | ')[1].split('g')[0])
            FoodCost += round(float(self.store.get(itm.split(' | ')[0])['FoodCost']) * float(itm.split(
                ' | ')[1].split('g')[0]) / float(self.store.get(itm.split(' | ')[0])['FoodWeight']), 2)

        cartInfoView_item_strings = ['Cost: {}€'.format(round(float(FoodCost), 2)),
                                     'Weight: {}g'.format(FoodWeight)]
        self.root.ids.overview_screen.ids.cartInfoView.data = [{'text': str(x)} for x in cartInfoView_item_strings]

        cartlistInput.sort()
        self.root.ids.overview_screen.ids.buyitems.data = [{'text': str(x)} for x in cartlistInput]
        self.root.ids.buyingitems_screen.ids.cartDB.data = [{'text': str(x)} for x in cartlistInput]
        # self.root.ids.overview_screen.ids.buyitems.item_strings = cartlistInput
        # self.root.ids.buyingitems_screen.ids.cartDB.item_strings = cartlistInput

    def view_recipe_items(self):
        availabelRecipes = []
        recipeInput = []
        counter = []
        for drow in self.recipe.find():
            for ahome in self.athome.find():
                for its in list(set(drow[1]['Items'])):
                    if (ahome[0] == its.split(' | ')[0] and float(ahome[1]['TotalWeight'].split('g')[0]) >= float(
                            its.split(' | ')[1].split('g')[0])):
                        recipeInput.append(drow[0])
                        counter.append(
                            floor(
                                float(ahome[1]['TotalWeight'].split('g')[0]) / float(
                                    its.split(' | ')[1].split('g')[0])))

        for rec in set(recipeInput):
            indices = [i for i, x in enumerate(recipeInput) if x == rec]
            mins = [counter[i] for i in indices]
            for rec2 in self.recipe.find():
                if rec2[0] == rec and len(set(rec2[1]['Items'])) == float(recipeInput.count(rec)):
                    availabelRecipes.append(rec + ' x ' + str(min(mins)))

        availabelRecipes.sort()
        self.root.ids.overview_screen.ids.recitems.data = [{'text': str(x)} for x in availabelRecipes]
        self.root.ids.buyingitems_screen.ids.actualrecipesatHome.data = [{'text': str(x)} for x in availabelRecipes]

    def view_recipe_cart_items(self):
        availabelRecipes = []
        recipeInput = []
        counter = []
        for drow in self.recipe.find():
            for acart in self.cartlist.find():
                for its in list(set(drow[1]['Items'])):
                    if (acart[0] == its.split(' | ')[0] and float(acart[1]['TotalWeight'].split('g')[0]) >= float(
                            its.split(' | ')[1].split('g')[0])):
                        recipeInput.append(drow[0])
                        counter.append(
                            floor(
                                float(acart[1]['TotalWeight'].split('g')[0]) / float(
                                    its.split(' | ')[1].split('g')[0])))

        for rec in set(recipeInput):
            indices = [i for i, x in enumerate(recipeInput) if x == rec]
            mins = [counter[i] for i in indices]
            for rec2 in self.recipe.find():
                if rec2[0] == rec and len(set(rec2[1]['Items'])) == float(recipeInput.count(rec)):
                    availabelRecipes.append(rec + ' x ' + str(min(mins)))

        availabelRecipes.sort()
        self.root.ids.overview_screen.ids.cartitemsrecipes.data = [{'text': str(x)} for x in availabelRecipes]
        # self.root.ids.overview_screen.ids.cartitemsrecipes.item_strings = availabelRecipes

    def view_na_recipes(self):
        cartRecs = [cartitemrecs['text'].split(' x ')[0] for cartitemrecs in
                    self.root.ids.overview_screen.ids.cartitemsrecipes.data]
        homeRecs = [homeitemrecs['text'].split(' x ')[0] for homeitemrecs in
                    self.root.ids.overview_screen.ids.recitems.data]
        cartRecs.extend(homeRecs)
        recs = [recipe[0] for recipe in self.recipe.find()]
        narecipes_item_strings = list(set(recs).difference(cartRecs))

        self.root.ids.overview_screen.ids.narecipes.data = [{'text': str(x)} for x in narecipes_item_strings]

    def show_cart_warning_dialog(self):
        content = MDLabel(font_style='Body1',
                          theme_text_color='Secondary',
                          text="Are you sure you want to delete all cart items you have added so far?",
                          size_hint_y=None,
                          valign='top')
        content.bind(texture_size=content.setter('size'))
        self.dialog = MDDialog(title="Delete Cart Items?",
                               content=content,
                               size_hint=(.8, None),
                               height=dp(200),
                               auto_dismiss=False)
        self.dialog.add_action_button("Yes",
                                      action=lambda *x: self.manual_cart_deletion())
        self.dialog.add_action_button("No",
                                      action=lambda *x: self.dialog.dismiss())
        self.dialog.open()

    def manual_cart_deletion(self):
        self.refresh_cart_list()
        self.dialog.dismiss()
        self.refresh_all()

    def show_home_warning_dialog(self):
        content = MDLabel(font_style='Body1',
                          theme_text_color='Secondary',
                          text="Are you sure you want to delete all home items you have added so far?",
                          size_hint_y=None,
                          valign='top')
        content.bind(texture_size=content.setter('size'))
        self.dialog = MDDialog(title="Delete Home Items?",
                               content=content,
                               size_hint=(.8, None),
                               height=dp(200),
                               auto_dismiss=False)
        self.dialog.add_action_button("Yes",
                                      action=lambda *x: self.manual_home_deletion())
        self.dialog.add_action_button("No",
                                      action=lambda *x: self.dialog.dismiss())
        self.dialog.open()

    def manual_home_deletion(self):
        self.refresh_home_list()
        self.dialog.dismiss()
        self.refresh_all()

    def show_home_dialog(self):
        content = MDLabel(font_style='Body1',
                          theme_text_color='Secondary',
                          text="These are all your items at home.",
                          size_hint_y=None,
                          valign='top')
        content.bind(texture_size=content.setter('size'))
        self.dialog = MDDialog(title="Home Items",
                               content=content,
                               size_hint=(.8, None),
                               height=dp(200),
                               auto_dismiss=False)
        self.dialog.add_action_button("Dismiss",
                                      action=lambda *x: self.dialog.dismiss())
        self.dialog.open()

    def show_cart_dialog(self):
        content = MDLabel(font_style='Body1',
                          theme_text_color='Secondary',
                          text="These are all your items which you want to buy.",
                          size_hint_y=None,
                          valign='top')
        content.bind(texture_size=content.setter('size'))
        self.dialog = MDDialog(title="Cart Items",
                               content=content,
                               size_hint=(.8, None),
                               height=dp(200),
                               auto_dismiss=False)
        self.dialog.add_action_button("Dismiss",
                                      action=lambda *x: self.dialog.dismiss())
        self.dialog.open()

    #########################################################
    # INPUT ITEMS
    #########################################################

    def add_item(self, strFood, strWeight, strCost):
        if not self.edit_item_bool:
            if strFood and strWeight and strCost:
                try:
                    float(strWeight)
                    float(strCost)
                    # self.store.put(strFood.replace(" ", "_"),
                    #                FoodWeight=strWeight,
                    #                FoodCost=strCost,
                    #                TimeID=datetime.strftime(datetime.now(), '%d.%m.%Y %H:%M:%S'))

                    self.store.put(strFood,
                                FoodWeight=strWeight,
                                FoodCost=strCost,
                                TimeID=datetime.strftime(datetime.now(), '%d.%m.%Y %H:%M:%S'))

                    self.show_snackbar('Added ' + strFood + ' !')
                    self.root.ids.inputitems_screen.ids.itemname.text = ""
                    self.root.ids.inputitems_screen.ids.itemweight.text = ""
                    self.root.ids.inputitems_screen.ids.itemcost.text = ""

                except Exception as e:
                    self.show_input_datatype_error_dialog(str(e))
            else:
                self.show_input_incomplete_error_dialog()
        else:
            if strFood and strWeight and strCost:
                try:
                    self.show_warning_update_item_dialog(strFood, strWeight, strCost)

                except Exception as e:
                    self.show_input_datatype_error_dialog(str(e))
            else:
                self.show_input_incomplete_error_dialog()

            self.edit_item_bool = False


    def show_input_datatype_error_dialog(self, text):
        content = MDLabel(font_style='Body1',
                          theme_text_color='Secondary',
                          text=text,
                          size_hint_y=None,
                          valign='top')
        content.bind(texture_size=content.setter('size'))
        self.dialog = MDDialog(title="Datatype Input Error",
                               content=content,
                               size_hint=(.8, None),
                               height=dp(200),
                               auto_dismiss=False)
        self.dialog.add_action_button("Dismiss",
                                      action=lambda *x: self.dialog.dismiss())
        self.dialog.open()

    def show_input_incomplete_error_dialog(self):
        content = MDLabel(font_style='Body1',
                          theme_text_color='Secondary',
                          text="Please fill out every cell!",
                          size_hint_y=None,
                          valign='top')
        content.bind(texture_size=content.setter('size'))
        self.dialog = MDDialog(title="Incomplete Input Error",
                               content=content,
                               size_hint=(.8, None),
                               height=dp(200),
                               auto_dismiss=False)
        self.dialog.add_action_button("Dismiss",
                                      action=lambda *x: self.dialog.dismiss())
        self.dialog.open()

    #########################################################
    # VIEW ITEMS
    #########################################################    

    def change_item_image_info(self):
        if selection_item:
            self.root.ids.viewitems_screen.ids.itemID.text = selection_item
            FoodCost = self.store.get(selection_item)['FoodCost']
            FoodWeight = self.store.get(selection_item)['FoodWeight']
            self.root.ids.viewitems_screen.ids.infoView.text = ''.join(
                ['Cost: {}€\n'.format(FoodCost), 'Weight: {}g\n'.format(FoodWeight)])

    def update_item(self):
        foodInput = [drow[0] for drow in self.store.find()]
        foodInput.sort()
        self.root.ids.viewitems_screen.ids.dbOutput.data = [{'text': str(x)} for x in foodInput]

    def delete_item(self):
        try:
            if selection_item:
                self.show_snackbar(
                    'Removed ' + selection_item)
                recipeToDelete = [rec[0] for rec in self.recipe.find(
                ) for itm in rec[1]['Items'] if itm.split(' | ')[0] == selection_item]

                for drec in recipeToDelete:
                    self.recipe.delete(drec)

                if self.athome.exists(selection_item):
                    self.athome.delete(selection_item)
                if self.cartlist.exists(selection_item):
                    self.cartlist.delete(selection_item)
                if self.history.exists(selection_item):
                    self.history.delete(selection_item)
                if self.store.exists(selection_item):
                    self.store.delete(selection_item)

                self.root.ids.viewitems_screen.ids.searchItems.text = ""
                self.dialog.dismiss()
                self.refresh_all()
        except Exception as e:
            self.dialog.dismiss()
            self.show_warning_no_item_selected_to_delete()

    def show_warning_no_item_selected_to_delete(self):
        content = MDLabel(font_style='Body1',
                          theme_text_color='Secondary',
                          text="No item was selected to be deleted.",
                          size_hint_y=None,
                          valign='top')
        content.bind(texture_size=content.setter('size'))
        self.dialog = MDDialog(title="No item selected!",
                               content=content,
                               size_hint=(.8, None),
                               height=dp(200),
                               auto_dismiss=True)
        self.dialog.add_action_button("Dismiss",
                                      action=lambda *x: self.dialog.dismiss())
        self.dialog.open()

    def filter_items(self, searchText):
        lfoodInput = [drow[0].lower() for drow in self.store.find()]
        foodInput = [drow[0] for drow in self.store.find()]
        indices = [i for i, s in enumerate(lfoodInput) if searchText.lower() in s]
        fitems = [foodInput[i] for i in indices]
        fitems.sort()
        self.root.ids.viewitems_screen.ids.dbOutput.data = [{'text': str(x)} for x in fitems]

    def show_warning_delete_item_dialog(self):
        content = MDLabel(font_style='Body1',
                          theme_text_color='Secondary',
                          text="Deleting an item will delete recipes, cart items and home items in which the item is present! Are you sure you want to proceed?",
                          size_hint_y=None,
                          valign='top')
        content.bind(texture_size=content.setter('size'))
        self.dialog = MDDialog(title="Warning Item Deletion!",
                               content=content,
                               size_hint=(.8, None),
                               height=dp(200),
                               auto_dismiss=True)
        self.dialog.add_action_button("Yes",
                                      action=lambda *x: self.delete_item())
        self.dialog.add_action_button("No",
                                      action=lambda *x: self.dialog.dismiss())
        self.dialog.open()

    #########################################################
    # EDIT Items
    #########################################################
    def edit_item(self):
        try:
            self.root.ids.inputitems_screen.ids.itemname.text = selection_item
            self.root.ids.inputitems_screen.ids.itemweight.text = self.store.get(selection_item)['FoodWeight']
            self.root.ids.inputitems_screen.ids.itemcost.text = self.store.get(selection_item)['FoodCost']
            self.root.ids.scr_mngr.transition.direction = 'left'
            self.root.ids.scr_mngr.current = 'input'
            self.edit_item_bool = True

        except Exception as e:
            self.show_warning_no_item_selected_to_edit()

    def show_warning_no_item_selected_to_edit(self):
        content = MDLabel(font_style='Body1',
                          theme_text_color='Secondary',
                          text=f"Select an item in the list to be edited.",
                          size_hint_y=None,
                          valign='top')
        content.bind(texture_size=content.setter('size'))
        self.dialog = MDDialog(title="No item selected!",
                               content=content,
                               size_hint=(.8, None),
                               height=dp(200),
                               auto_dismiss=True)
        self.dialog.add_action_button("Dismiss",
                                      action=lambda *x: self.dialog.dismiss())
        self.dialog.open()


    def show_warning_update_item_dialog(self, name, weight, cost):
        content = MDLabel(font_style='Body1',
                          theme_text_color='Secondary',
                          text=f"Should the item {selection_item} be updated? {selection_item} will also be updated in the recipes items, at home items and in cart items.",
                          size_hint_y=None,
                          valign='top')
        content.bind(texture_size=content.setter('size'))
        self.dialog = MDDialog(title=f"Update item {selection_item}?",
                               content=content,
                               size_hint=(.8, None),
                               height=dp(200),
                               auto_dismiss=True)
        self.dialog.add_action_button("Yes",
                                      action=lambda *x: self.update_edit_item(name, weight, cost, False))
        self.dialog.add_action_button("No",
                                      action=lambda *x: self.dialog.dismiss())
        self.dialog.open()
        
    def show_warning_edited_item_already_exists(self, name, weight, cost):
        self.dialog.dismiss()
        content = MDLabel(font_style='Body1',
                          theme_text_color='Secondary',
                          text=f"The item {name} already exists in the database. Are you sure you want to overwrite it?",
                          size_hint_y=None,
                          valign='top')
        content.bind(texture_size=content.setter('size'))
        self.dialog = MDDialog(title=f"Item {name} already exist.",
                               content=content,
                               size_hint=(.8, None),
                               height=dp(200),
                               auto_dismiss=True)
        self.dialog.add_action_button("Yes",
                                      action=lambda *x: self.update_edit_item(name, weight, cost, True))
        self.dialog.add_action_button("No",
                                      action=lambda *x: self.dialog.dismiss())
        self.dialog.open()

    def update_edit_item(self, name, weight, cost, overwritebool=False):
        if not self.store.exists(name) or overwritebool:
    
            if selection_item:
                self.show_snackbar('Updated ' + selection_item)

                # Update in store
                if self.store.exists(selection_item):
                    self.store.delete(selection_item)
                    self.store.put(name,
                                   FoodWeight=weight,
                                   FoodCost=cost,
                                   TimeID=datetime.strftime(datetime.now(), '%d.%m.%Y %H:%M:%S'))

                # Update at home
                if self.athome.exists(selection_item):
                    totalweight = float(self.athome.get(selection_item)['TotalWeight'].split('g')[0])
                    weight = float(weight)
                    count = round(totalweight/weight,1)

                    self.athome.delete(selection_item)
                    self.athome.put(name,
                                    TotalWeight=str(totalweight)+'g',
                                    ItemWeight=str(weight)+'g',
                                    Count=count,
                                    TimeID=datetime.strftime(datetime.now(), '%d.%m.%Y %H:%M:%S'))

                # Update in cart
                if self.cartlist.exists(selection_item):
                    totalweight = float(self.cartlist.get(selection_item)['TotalWeight'].split('g')[0])
                    weight = float(weight)
                    count = round(totalweight/weight,1)

                    self.cartlist.delete(selection_item)
                    self.cartlist.put(name,
                                      TotalWeight=str(totalweight)+'g',
                                      ItemWeight=str(weight)+'g',
                                      Count=str(count),
                                      TimeID=datetime.strftime(datetime.now(), '%d.%m.%Y %H:%M:%S'))

                # Update in recipe
                ##################

                # Convert to a dict
                recipe_hash_table = {}
                temp_recipes = self.recipe.find()
                weight = float(weight)

                for hrec in temp_recipes:
                    recipe_hash_table[hrec[0]] = hrec[1]['Items']

                found = False
                for recipe_name, item_list in recipe_hash_table.items():

                    new_item_list = []
                    for it in item_list:
                        item_name, recipe_weight, item_weight, count = self.get_item_attributes_from_recipe_string(it)
                        if item_name == selection_item:
                            count = round(recipe_weight / weight, 1)
                            it = self.set_recipe_string_from_item_attributes(name, recipe_weight, weight, count)
                            found = True

                        new_item_list.append(it)

                    if found:
                        self.recipe.delete(recipe_name)
                        self.recipe.put(recipe_name,
                                        Items=new_item_list,
                                        TimeID=datetime.strftime(datetime.now(), '%d.%m.%Y %H:%M:%S'))
                        found = False

                # Update in history
                if self.history.exists(selection_item):
                    totalweight = float(self.history.get(selection_item)['TotalWeight'].split('g')[0])
                    weight = float(weight)
                    count = round(totalweight/weight,1)

                    self.history.delete(selection_item)
                    self.history.put(name,
                                     TotalWeight=str(totalweight)+'g',
                                     ItemWeight=str(weight)+'g',
                                     Count=count,
                                     TimeID=datetime.strftime(datetime.now(), '%d.%m.%Y %H:%M:%S'))

            self.go_view_items_screen()
        else:
            self.show_warning_edited_item_already_exists(name, weight, cost)


    def show_warning_dismiss_edits_dialog(self):
        content = MDLabel(font_style='Body1',
                          theme_text_color='Secondary',
                          text="Should all changes made to the items be dismissed?",
                          size_hint_y=None,
                          valign='top')
        content.bind(texture_size=content.setter('size'))
        self.dialog = MDDialog(title="Dismiss changes?",
                               content=content,
                               size_hint=(.8, None),
                               height=dp(200),
                               auto_dismiss=True)
        self.dialog.add_action_button("Yes",
                                      action=lambda *x: self.go_view_items_screen())
        self.dialog.add_action_button("No",
                                      action=lambda *x: self.dialog.dismiss())
        self.dialog.open()

    def go_view_items_screen(self):
        self.root.ids.scr_mngr.transition.direction = 'right'
        self.root.ids.scr_mngr.current = 'viewitems'
        self.refresh_all()
        self.root.ids.inputitems_screen.ids.itemname.text = ""
        self.root.ids.inputitems_screen.ids.itemweight.text = ""
        self.root.ids.inputitems_screen.ids.itemcost.text = ""
        self.dialog.dismiss()

    #########################################################
    # RECIPES
    #########################################################

    def add_item_to_recipe(self):
        try:
            selectedItemsOutput = self.root.ids.addrecipes_screen.ids.selecteditemsOutput.data
            itemName = [inam['text'].split(' | ')[0] for inam in selectedItemsOutput]
            itemWeight = [itm['text'].split(' | ')[1].split('g')[0] for itm in selectedItemsOutput]

            itemsDict = {itemName[i]: float(itemWeight[i]) for i in range(len(itemName))}
            itemSliderWeight = float(round(self.root.ids.addrecipes_screen.ids.weight_slider_recipe.value))
            storedItemWeight = float(self.store.get(selection)['FoodWeight'])

            if selection in itemsDict:
                currentItemWeight = str(itemSliderWeight + itemsDict[selection])
                itemCount = str(round((itemSliderWeight + itemsDict[selection]) / storedItemWeight, 1))
                genItemString = f'{selection} | {currentItemWeight}g (={str(storedItemWeight)}g x {itemCount})'
                for ind, it in enumerate(selectedItemsOutput):
                    if it['text'].split(' | ')[0] == selection:
                        self.root.ids.addrecipes_screen.ids.selecteditemsOutput.data[ind] = {'text': genItemString}
            else:
                currentItemWeight = str(itemSliderWeight)
                itemCount = str(round((itemSliderWeight) / storedItemWeight, 1))
                genItemString = f'{selection} | {currentItemWeight}g (={str(storedItemWeight)}g x {itemCount})'
                self.root.ids.addrecipes_screen.ids.selecteditemsOutput.data.append({'text': genItemString})
        except Exception as e:
            self.show_warning_no_item_selected_to_add_to_recipe()

    def show_warning_no_item_selected_to_add_to_recipe(self):
        content = MDLabel(font_style='Body1',
                          theme_text_color='Secondary',
                          text="No item was selected to be added to the recipe",
                          size_hint_y=None,
                          valign='top')
        content.bind(texture_size=content.setter('size'))
        self.dialog = MDDialog(title="No item selected!",
                               content=content,
                               size_hint=(.8, None),
                               height=dp(200),
                               auto_dismiss=True)
        self.dialog.add_action_button("Dismiss",
                                      action=lambda *x: self.dialog.dismiss())
        self.dialog.open()

    def show_items(self):
        foodInput = [drow[0] for drow in self.store.find()]
        foodInput.sort()

        self.root.ids.addrecipes_screen.ids.itemsOutput.data = [{'text': str(x)} for x in foodInput]
        self.root.ids.buyingitems_screen.ids.itemView.data = [{'text': str(x)} for x in foodInput]

    def add_recipe(self, recipeName):
        if not self.edit_recipe_bool:
            if recipeName and len(self.root.ids.addrecipes_screen.ids.selecteditemsOutput.data) > 0:
                self.show_snackbar('Added Recipe ' + recipeName)
                # Convert dict to list
                item_strings = [it['text'] for it in self.root.ids.addrecipes_screen.ids.selecteditemsOutput.data]
                self.recipe.put(recipeName, Items=item_strings, TimeID=datetime.strftime(
                    datetime.now(), '%d.%m.%Y %H:%M:%S'))
                self.root.ids.addrecipes_screen.ids.recipeInput.text = ""
                self.delete_all_item_from_recipe()
            else:
                self.show_recipe_input_incomplete_error_dialog()
        else:
            self.show_warning_update_recipe_dialog(recipeName)
            self.edit_recipe_bool = False

    def aggregate_items_in_recipe(self):
        print(self.root.ids.addrecipes_screen.ids.selecteditemsOutput.data[0]['text'])
        itemName = [itm.split(' | ') for itm in self.root.ids.addrecipes_screen.ids.selecteditemsOutput.data[0]['text']]
        print(itemName)
        itemName = self.root.ids.selecteditemsOutput.data[0]['text'].split(' | ')[0]
        print(itemName)
        itemWeight = [itm.split(' | ')[1].split('g')[0] for itm in
                      self.root.ids.addrecipes_screen.ids.selecteditemsOutput.data[0]['text']]
        self.root.ids.addrecipes_screen.ids.selecteditemsOutput.data[0]['text'] = [itminlist + ' | ' + str(
            sum([float(itemWeight[i]) for i in [i for i, s in enumerate(itemName) if itminlist in s]])) +
                                                                                   'g (=' +
                                                                                   self.store.get(itminlist)[
                                                                                       'FoodWeight'] +
                                                                                   'g x ' +
                                                                                   str(round(sum(
                                                                                       [float(itemWeight[i]) for i in
                                                                                        [i for i, s in
                                                                                         enumerate(itemName) if
                                                                                         itminlist in s]]) / float(
                                                                                       self.store.get(itminlist)[
                                                                                           'FoodWeight']), 1)) + ')'
                                                                                   for itminlist in set(itemName)]
        self.root.ids.addrecipes_screen.ids.selecteditemsOutput.data[0]['text'].sort()

    def show_recipe(self):
        recipeInput = [drow[0] for drow in self.recipe.find()]
        self.root.ids.recipes_screen.ids.recipeOutput.data = [{'text': str(x)} for x in recipeInput]
        if self.root.ids.buyingitems_screen.ids.recipechkbox.active:
            self.root.ids.buyingitems_screen.ids.recipeView.data = self.root.ids.overview_screen.ids.narecipes.data
        else:
            recipeInput.sort()
            self.root.ids.buyingitems_screen.ids.recipeView.data = [{'text': str(x)} for x in recipeInput]

    def show_items_in_recipe(self):
        FoodWeight, FoodCost = 0, 0
        self.root.ids.recipes_screen.ids.recipeID.text = selection_recipe

        homerecList = []
        for rec in self.recipe.get(selection_recipe)['Items']:
            if self.athome.exists(rec.split(' | ')[0]):
                homerecList.append(rec.split(' | ')[0] + ' | ' + self.athome.get(rec.split(' | ')[0])[
                    'TotalWeight'] + '/{0}'.format(rec.split(' | ')[1]))
            else:
                homerecList.append(rec.split(' | ')[0] + ' | 0g/{0}'.format(rec.split(' | ')[1]))

        for itm in homerecList:
            FoodWeight += float(itm.split('g/')[1].split('g')[0])
            FoodCost += (float(self.store.get(itm.split(' | ')[0])['FoodCost']) * float(itm.split(
                'g/')[1].split('g')[0]) / float(self.store.get(itm.split(' | ')[0])['FoodWeight']))

        self.root.ids.recipes_screen.ids.recipeInfoView.text = ''.join(['Cost: {}€\n'.format(round(float(FoodCost), 2)),
                                                                        'Weight: {}g\n'.format(FoodWeight)])

        homerecList.sort()
        self.root.ids.recipes_screen.ids.itemsinrecipeOutput.data = [{'text': str(x)} for x in homerecList]

    def delete_item_from_recipe(self):
        try:
            if selection_iteminrecipe:
                self.root.ids.addrecipes_screen.ids.selecteditemsOutput.data.remove({'text': selection_iteminrecipe})
        except Exception as e:
            self.show_warning_no_item_selected_to_delete_from_recipe()

    def show_warning_no_item_selected_to_delete_from_recipe(self):
        content = MDLabel(font_style='Body1',
                          theme_text_color='Secondary',
                          text="No item was selected to be deleted from recipe",
                          size_hint_y=None,
                          valign='top')
        content.bind(texture_size=content.setter('size'))
        self.dialog = MDDialog(title="No item selected!",
                               content=content,
                               size_hint=(.8, None),
                               height=dp(200),
                               auto_dismiss=True)
        self.dialog.add_action_button("Dismiss",
                                      action=lambda *x: self.dialog.dismiss())
        self.dialog.open()

    def delete_all_item_from_recipe(self):
        self.root.ids.addrecipes_screen.ids.selecteditemsOutput.data = []

    def filter_recipes(self, recText):
        lrecipeInput = [drow[0].lower() for drow in self.recipe.find()]
        recipeInput = [drow[0] for drow in self.recipe.find()]
        indices = [i for i, s in enumerate(lrecipeInput) if recText.lower() in s]
        fitems = [recipeInput[i] for i in indices]
        fitems.sort()
        self.root.ids.recipes_screen.ids.recipeOutput.data = [{'text': str(x)} for x in fitems]

    def filter_items2(self, itemText):
        lfoodInput = [drow[0].lower() for drow in self.store.find()]
        foodInput = [drow[0] for drow in self.store.find()]
        indices = [i for i, s in enumerate(lfoodInput) if itemText.lower() in s]
        fitems = [foodInput[i] for i in indices]
        fitems.sort()
        self.root.ids.addrecipes_screen.ids.itemsOutput.data = [{'text': str(x)} for x in fitems]

    def show_item_weight_recipe(self):
        foodWeight = [drow[1]['FoodWeight']
                      for drow in self.store.find() if drow[0] == selection]
        # self.root.ids.weight_text.text = str(foodWeight[0])+' g'
        self.root.ids.addrecipes_screen.ids.weight_slider_recipe.max = float(foodWeight[0])
        self.root.ids.addrecipes_screen.ids.weight_slider_recipe.value = float(foodWeight[0])

    def delete_recipe(self):
        try:
            if selection_recipe:
                if self.recipe.exists(selection_recipe):
                    self.recipe.delete(selection_recipe)
                    self.root.ids.recipes_screen.ids.itemsinrecipeOutput.data = []
                    self.root.ids.recipes_screen.ids.recipeInfoView.text = ''
                    self.root.ids.recipes_screen.ids.recipeID.text = ''
            self.dialog.dismiss()
            self.refresh_all()
        except Exception as e:
            self.dialog.dismiss()
            self.show_warning_no_recipe_selected_to_delete()

    def show_warning_no_recipe_selected_to_delete(self):
        content = MDLabel(font_style='Body1',
                          theme_text_color='Secondary',
                          text="No recipe was selected to be deleted.",
                          size_hint_y=None,
                          valign='top')
        content.bind(texture_size=content.setter('size'))
        self.dialog = MDDialog(title="No recipe selected!",
                               content=content,
                               size_hint=(.8, None),
                               height=dp(200),
                               auto_dismiss=True)
        self.dialog.add_action_button("Dismiss",
                                      action=lambda *x: self.dialog.dismiss())
        self.dialog.open()

    def show_recipe_input_incomplete_error_dialog(self):
        content = MDLabel(font_style='Body1',
                          theme_text_color='Secondary',
                          text='Recipe is incomplete!\nPlease give recipe name and add at least one item.',
                          size_hint_y=None,
                          valign='top')
        content.bind(texture_size=content.setter('size'))
        self.dialog = MDDialog(title="Recipe Incomplete Error",
                               content=content,
                               size_hint=(.8, None),
                               height=dp(200),
                               auto_dismiss=True)
        self.dialog.add_action_button("Dismiss",
                                      action=lambda *x: self.dialog.dismiss())
        self.dialog.open()

    def show_warning_delete_recipe_dialog(self):
        content = MDLabel(font_style='Body1',
                          theme_text_color='Secondary',
                          text="Delete Recipe entirely? Are you sure you want to proceed?",
                          size_hint_y=None,
                          valign='top')
        content.bind(texture_size=content.setter('size'))
        self.dialog = MDDialog(title="Warning Recipe Deletion!",
                               content=content,
                               size_hint=(.8, None),
                               height=dp(200),
                               auto_dismiss=True)
        self.dialog.add_action_button("Yes",
                                      action=lambda *x: self.delete_recipe())
        self.dialog.add_action_button("No",
                                      action=lambda *x: self.dialog.dismiss())
        self.dialog.open()

    #########################################################
    # EDIT RECIPES
    #########################################################
    def edit_recipe(self):
        try:
            self.root.ids.addrecipes_screen.ids.recipeInput.text = selection_recipe
            items_list = self.recipe.get(selection_recipe)['Items']
            self.root.ids.addrecipes_screen.ids.selecteditemsOutput.data = [{'text': it} for it in items_list]
            self.root.ids.scr_mngr.transition.direction = 'left'
            self.root.ids.scr_mngr.current = 'addrecipes'
            self.edit_recipe_bool = True
        except Exception as e:
            self.show_warning_no_recipe_selected_to_edit()

    def update_recipe(self, name, overwritebool=False):
        if not self.recipe.exists(name) or overwritebool:
            if name and len(self.root.ids.addrecipes_screen.ids.selecteditemsOutput.data) > 0:
                self.recipe.delete(selection_recipe)
                self.show_snackbar(f'Update Recipe {selection_recipe}')
                # Convert dict to list
                item_strings = [it['text'] for it in self.root.ids.addrecipes_screen.ids.selecteditemsOutput.data]
                self.recipe.put(name, Items=item_strings, TimeID=datetime.strftime(datetime.now(), '%d.%m.%Y %H:%M:%S'))
                self.root.ids.addrecipes_screen.ids.recipeInput.text = ""
                self.delete_all_item_from_recipe()
                self.dialog.dismiss()
                self.refresh_all()
                self.root.ids.scr_mngr.transition.direction='right'
                self.root.ids.scr_mngr.current = 'recipes'
            else:
                self.show_recipe_input_incomplete_error_dialog()
        else:
            self.show_warning_edited_recipe_already_exists(name)

    def show_warning_no_recipe_selected_to_edit(self):
        content = MDLabel(font_style='Body1',
                          theme_text_color='Secondary',
                          text=f"Select a recipe in the list to be edited.",
                          size_hint_y=None,
                          valign='top')
        content.bind(texture_size=content.setter('size'))
        self.dialog = MDDialog(title="No recipe selected!",
                               content=content,
                               size_hint=(.8, None),
                               height=dp(200),
                               auto_dismiss=True)
        self.dialog.add_action_button("Dismiss",
                                      action=lambda *x: self.dialog.dismiss())
        self.dialog.open()

    def show_warning_update_recipe_dialog(self, name):
        content = MDLabel(font_style='Body1',
                          theme_text_color='Secondary',
                          text=f"Should the recipe {selection_recipe} be updated?",
                          size_hint_y=None,
                          valign='top')
        content.bind(texture_size=content.setter('size'))
        self.dialog = MDDialog(title=f"Update recipe {selection_recipe}?",
                               content=content,
                               size_hint=(.8, None),
                               height=dp(200),
                               auto_dismiss=True)
        self.dialog.add_action_button("Yes",
                                      action=lambda *x: self.update_recipe(name))
        self.dialog.add_action_button("No",
                                      action=lambda *x: self.dialog.dismiss())
        self.dialog.open()

    def show_warning_edited_recipe_already_exists(self, name):
        self.dialog.dismiss()
        content = MDLabel(font_style='Body1',
                          theme_text_color='Secondary',
                          text=f"The recipe {name} already exists in the database. Are your sure you want to overwrite the recipe?",
                          size_hint_y=None,
                          valign='top')
        content.bind(texture_size=content.setter('size'))
        self.dialog = MDDialog(title=f"Recipe {name} already exist.",
                               content=content,
                               size_hint=(.8, None),
                               height=dp(200),
                               auto_dismiss=True)
        self.dialog.add_action_button("Yes",
                                      action=lambda *x: self.update_recipe(name, True))
        self.dialog.add_action_button("No",
                                      action=lambda *x: self.dialog.dismiss())
        self.dialog.open()

    #########################################################
    # ADD HOME ITEMS
    #########################################################
    def add_item_at_home_from_cart(self):
        pass
        # if self.root.ids.cartDB.adapter.selection:
        #     self.root.ids.itemsatHome.item_strings.append(self.root.ids.cartDB.adapter.selection[0].text.split(' x ')[0])
        #     if float(self.root.ids.cartDB.adapter.selection[0].text.split(' x ')[1]) == 1:
        #         self.root.ids.cartDB.item_strings.remove(
        #         self.root.ids.cartDB.adapter.selection[0].text)
        #     else:            
        #         self.root.ids.cartDB.item_strings[self.root.ids.cartDB.item_strings.index(
        #             self.root.ids.cartDB.adapter.selection[0].text)] = self.root.ids.cartDB.adapter.selection[0].text.split(' x ')[0] + ' x '+str(float(self.root.ids.cartDB.adapter.selection[0].text.split(' x ')[1])-1)

    def add_all_items_at_home_from_cart(self):
        if len(self.root.ids.buyingitems_screen.ids.cartDB.data) != 0:
            self.reset_items_at_home()
            self.refresh_all()
            self.root.ids.buyingitems_screen.ids.itemsatHome.data = self.root.ids.buyingitems_screen.ids.cartDB.data
            self.root.ids.buyingitems_screen.ids.cartDB.data = []

    def refresh_cart_list(self):
        tempdeleteItems = [drow[0] for drow in self.cartlist.find()]
        for di in tempdeleteItems:
            self.cartlist.delete(di)

    def undo_staged_item(self):
        try:
            global selection_stageditem

            if selection_stageditem:
                self.root.ids.buyingitems_screen.ids.cartDB.data.append({'text': selection_stageditem})
                for index, itm in enumerate(self.root.ids.buyingitems_screen.ids.itemsatHome.data):

                    if itm['text'] == selection_stageditem:
                        del self.root.ids.buyingitems_screen.ids.itemsatHome.data[index]
                        if len(self.root.ids.buyingitems_screen.ids.cartDB.data) < 1:
                            selection_stageditem = None
                        break

        except Exception as e:
            self.show_warning_no_item_selected_for_undo()

    def show_warning_no_item_selected_for_undo(self):
        content = MDLabel(font_style='Body1',
                          theme_text_color='Secondary',
                          text='No item selected for undo.',
                          size_hint_y=None,
                          valign='top')
        content.bind(texture_size=content.setter('size'))
        self.dialog = MDDialog(title="No item selected!",
                               content=content,
                               size_hint=(.8, None),
                               height=dp(200),
                               auto_dismiss=True)
        self.dialog.add_action_button("Dismiss",
                                      action=lambda *x: self.dialog.dismiss())
        self.dialog.open()

    def reset_items_at_home(self):
        self.root.ids.buyingitems_screen.ids.itemsatHome.data = []

    def commit_delta_items_in_cart(self):
        for ci in self.root.ids.buyingitems_screen.ids.cartDB.data:
            ci = ci['text']
            self.cartlist.put(ci.split(' | ')[0],
                              Count=str(round(float(ci.split(' | ')[1].split('g')[0]) / float(
                                  ci.split(' | ')[2].split('(=')[1].split('g')[0]), 1)),
                              TotalWeight=ci.split(' | ')[1],
                              ItemWeight=ci.split(' | ')[2].split('(=')[1],
                              TimeID=datetime.strftime(datetime.now(), '%d.%m.%Y %H:%M:%S'))

    def commit_item_at_home(self):
        for ci in self.root.ids.buyingitems_screen.ids.itemsatHome.data:
            ci = ci['text']
            itemWeight = float(ci.split('(=')[1].split('g')[0])
            if self.athome.exists(ci.split(' | ')[0]):
                totalWeight = float(self.athome.get(ci.split(' | ')[0])['TotalWeight'].split('g')[0]) + float(
                    ci.split(' | ')[1].split('g')[0])
                self.athome.put(ci.split(' | ')[0],
                                TotalWeight=str(totalWeight) + 'g',
                                ItemWeight=str(itemWeight) + 'g',
                                Count=round(totalWeight / itemWeight, 1),
                                TimeID=datetime.strftime(
                                    datetime.now(), '%d.%m.%Y %H:%M:%S'))
            else:
                totalWeight = float(ci.split(' | ')[1].split('g')[0])
                self.athome.put(ci.split(' | ')[0],
                                TotalWeight=str(totalWeight) + 'g',
                                ItemWeight=str(itemWeight) + 'g',
                                Count=round(totalWeight / itemWeight, 1),
                                TimeID=datetime.strftime(
                                    datetime.now(), '%d.%m.%Y %H:%M:%S'))

    def aggregate_items_in_home(self):
        itemName = [itm['text'].split(' | ')[0] for itm in self.root.ids.buyingitems_screen.ids.itemsatHome.data]
        itemWeight = [itm['text'].split(' | ')[1].split('g')[0] for itm in
                      self.root.ids.buyingitems_screen.ids.itemsatHome.data]
        itemsatHome_item_strings = [itminlist + ' | ' + str(
            sum([float(itemWeight[i]) for i in [i for i, s in enumerate(itemName) if itminlist in s]])) +
                                    'g (=' +
                                    self.store.get(itminlist)['FoodWeight'] +
                                    'g x ' +
                                    str(round(sum([float(itemWeight[i]) for i in
                                                   [i for i, s in enumerate(itemName) if itminlist in s]]) / float(
                                        self.store.get(itminlist)['FoodWeight']), 1)) + ')'
                                    for itminlist in set(itemName)]

        self.root.ids.buyingitems_screen.ids.itemsatHome.data = [{'text': str(x)} for x in itemsatHome_item_strings]

    def add_caritem_to_home(self):
        try:
            global selection_incartitem

            if selection_incartitem:
                self.root.ids.buyingitems_screen.ids.itemsatHome.data.append({'text': selection_incartitem})
                for index, itm in enumerate(self.root.ids.buyingitems_screen.ids.cartDB.data):

                    if itm['text'] == selection_incartitem:
                        del self.root.ids.buyingitems_screen.ids.cartDB.data[index]
                        if len(self.root.ids.buyingitems_screen.ids.cartDB.data) < 1:
                            selection_incartitem = None
                        break
        except Exception as e:
            self.show_warning_no_item_selected_to_add_staging()

    def show_warning_no_item_selected_to_add_staging(self):
        content = MDLabel(font_style='Body1',
                          theme_text_color='Secondary',
                          text="No item was selected to be staged from cart",
                          size_hint_y=None,
                          valign='top')
        content.bind(texture_size=content.setter('size'))
        self.dialog = MDDialog(title="No item selected!",
                               content=content,
                               size_hint=(.8, None),
                               height=dp(200),
                               auto_dismiss=True)
        self.dialog.add_action_button("Dismiss",
                                      action=lambda *x: self.dialog.dismiss())
        self.dialog.open()

    def refresh_home_list(self):
        tempdeleteItems = [drow[0] for drow in self.athome.find()]
        for di in tempdeleteItems:
            self.athome.delete(di)

    def show_total_cost_cart_items(self):
        totalCost = 0

        for itm in self.root.ids.buyingitems_screen.ids.cartDB.data:
            totalCost += (float(self.store.get(itm['text'].split(' | ')[0])['FoodCost']) * float(
                itm['text'].split(' | ')[1].split('g')[0]) / float(
                self.store.get(itm['text'].split(' | ')[0])['FoodWeight']))

        self.root.ids.buyingitems_screen.ids.totalCostCartItems.text = '{}€'.format(round(totalCost, 2))

    #########################################################
    # USED HOME ITEMS
    #########################################################
    def remove_item_at_home(self):
        try:
            if selection_itemathome:
                self.update_athome(selection_itemathome,
                                   self.root.ids.buyingitems_screen.ids.weight_slider_usedhome.value)
        except Exception as e:
            self.show_warning_no_item_selected_to_be_consumed()

    def show_warning_no_item_selected_to_be_consumed(self):
        content = MDLabel(font_style='Body1',
                          theme_text_color='Secondary',
                          text="No item was selected to be consumed from at home items",
                          size_hint_y=None,
                          valign='top')
        content.bind(texture_size=content.setter('size'))
        self.dialog = MDDialog(title="No item selected!",
                               content=content,
                               size_hint=(.8, None),
                               height=dp(200),
                               auto_dismiss=True)
        self.dialog.add_action_button("Dismiss",
                                      action=lambda *x: self.dialog.dismiss())
        self.dialog.open()

    def remove_items_via_recipe(self):
        try:
            if selection_viarecipe:
                recItems = self.recipe.get(selection_viarecipe.split(' x ')[0])['Items']

                for itm in recItems:
                    self.update_athome(itm)
        except Exception as e:
            self.show_warning_no_recipe_selected_to_be_consumed()

    def show_warning_no_recipe_selected_to_be_consumed(self):
        content = MDLabel(font_style='Body1',
                          theme_text_color='Secondary',
                          text="No recipe was selected to be consumed from at home items",
                          size_hint_y=None,
                          valign='top')
        content.bind(texture_size=content.setter('size'))
        self.dialog = MDDialog(title="No recipe selected!",
                               content=content,
                               size_hint=(.8, None),
                               height=dp(200),
                               auto_dismiss=True)
        self.dialog.add_action_button("Dismiss",
                                      action=lambda *x: self.dialog.dismiss())
        self.dialog.open()

    def update_athome(self, item, slider_value=None):
        itemWeight = float(self.athome.get(item.split(' | ')[0])['ItemWeight'].split('g')[0])
        if slider_value:
            totalWeight = round(float(self.athome.get(item.split(' | ')[0])['TotalWeight'].split('g')[0]) -
                                float(slider_value))
            self.save_history(item, itemWeight, float(slider_value))
        else:
            wasted = float(item.split('| ')[1].split('g')[0])
            totalWeight = round(float(self.athome.get(item.split(' | ')[0])['TotalWeight'].split('g')[0]) -
                                wasted)
            self.save_history(item, itemWeight, wasted)

        if totalWeight <= 0:
            self.athome.delete(item.split(' | ')[0])
        else:
            self.athome.put(item.split(' | ')[0],
                            TotalWeight=str(totalWeight) + 'g',
                            ItemWeight=str(itemWeight) + 'g',
                            Count=round(totalWeight / itemWeight, 1),
                            TimeID=datetime.strftime(
                                datetime.now(), '%d.%m.%Y %H:%M:%S'))

    def save_history(self, itm, itemWeight, wastedWeight):
        # Save in history.json for analysis
        if self.history.exists(itm.split(' | ')[0]):
            totalWeight = round(float(self.history.get(itm.split(' | ')[0])['TotalWeight'].split('g')[0]) +
                                wastedWeight)
            self.history.put(itm.split(' | ')[0],
                             TotalWeight=str(totalWeight) + 'g',
                             ItemWeight=str(itemWeight) + 'g',
                             Count=round(totalWeight / itemWeight, 1),
                             TimeID=datetime.strftime(
                                 datetime.now(), '%d.%m.%Y %H:%M:%S'))
        else:
            totalWeight = round(wastedWeight)
            self.history.put(itm.split(' | ')[0],
                             TotalWeight=str(totalWeight) + 'g',
                             ItemWeight=str(itemWeight) + 'g',
                             Count=round(totalWeight / itemWeight, 1),
                             TimeID=datetime.strftime(
                                 datetime.now(), '%d.%m.%Y %H:%M:%S'))

    def show_item_weight_used_home(self, selectedItem):
        self.root.ids.buyingitems_screen.ids.weight_slider_usedhome.max = float(
            selectedItem.split(' | ')[1].split(' (=')[0].replace('g', ''))
        self.root.ids.buyingitems_screen.ids.weight_slider_usedhome.value = float(
            selectedItem.split(' | ')[1].split(' (=')[0].replace('g', ''))

    #########################################################
    # CREATE ITEM LIST
    #########################################################
    def add_recipe_to_cart(self):
        try:
            if selection_recipetocart:
                for recipeItem in self.recipe.get(selection_recipetocart)['Items']:
                    self.root.ids.buyingitems_screen.ids.cartView.data.append({'text': recipeItem})

            cartViewOutput = self.root.ids.buyingitems_screen.ids.cartView.data
            itemName = [itm['text'].split(' | ')[0] for itm in cartViewOutput]
            itemWeight = [itm2['text'].split(' | ')[1].split('g')[0] for itm2 in cartViewOutput]
            # itemsDict = {itemName[i]: float(itemWeight[i]) for i in range(len(itemName))}

            cartView_item_strings = [itminlist + ' | ' + str(float(self.store.get(itminlist)['FoodWeight']) *
                                                             sum([float(itemWeight[i]) for i in
                                                                 [i for i, s in enumerate(
                                                                     itemName) if itminlist in s]]) / float(
                self.store.get(itminlist)['FoodWeight'])) +
                                     'g (=' +
                                     self.store.get(itminlist)['FoodWeight'] +
                                     'g x ' +
                                     str(round(sum([float(itemWeight[i]) for i in [i for i, s in enumerate(
                                         itemName) if itminlist in s]]) / float(
                                         self.store.get(itminlist)['FoodWeight']),
                                             1)) + ')'
                                     for itminlist in set(itemName)]

            cartView_item_strings.sort()
            self.root.ids.buyingitems_screen.ids.cartView.data = [{'text': str(x)} for x in cartView_item_strings]
        except Exception as e:
            self.show_warning_no_recipe_selected_to_add_to_cart()

    def show_warning_no_recipe_selected_to_add_to_cart(self):
        content = MDLabel(font_style='Body1',
                          theme_text_color='Secondary',
                          text='No recipe selected for adding to cart.',
                          size_hint_y=None,
                          valign='top')
        content.bind(texture_size=content.setter('size'))
        self.dialog = MDDialog(title="No recipe selected!",
                               content=content,
                               size_hint=(.8, None),
                               height=dp(200),
                               auto_dismiss=True)
        self.dialog.add_action_button("Dismiss",
                                      action=lambda *x: self.dialog.dismiss())
        self.dialog.open()

    def add_item_to_cart(self):
        try:
            if selection_itemtocart:
                cartViewOutput = self.root.ids.buyingitems_screen.ids.cartView.data
                itemName = [inam['text'].split(' | ')[0] for inam in cartViewOutput]
                itemWeight = [itm['text'].split(' | ')[1].split('g')[0] for itm in cartViewOutput]
                itemsDict = {itemName[i]: float(itemWeight[i]) for i in range(len(itemName))}
                itemSliderWeight = float(round(self.root.ids.buyingitems_screen.ids.cart_item_weight_slider.value, 1))
                storedItemWeight = float(self.store.get(selection_itemtocart)['FoodWeight'])

                if selection_itemtocart in itemsDict:
                    currentItemWeight = str(itemSliderWeight + itemsDict[selection_itemtocart])
                    itemCount = str(round((itemSliderWeight + itemsDict[selection_itemtocart]) / storedItemWeight, 1))
                    genItemString = f'{selection_itemtocart} | {currentItemWeight}g (={str(storedItemWeight)}g x {itemCount})'
                    for ind, it in enumerate(cartViewOutput):
                        if it['text'].split(' | ')[0] == selection_itemtocart:
                            self.root.ids.buyingitems_screen.ids.cartView.data[ind] = {'text': genItemString}
                else:
                    currentItemWeight = str(itemSliderWeight)
                    itemCount = str(round((itemSliderWeight) / storedItemWeight, 1))
                    genItemString = f'{selection_itemtocart} | {currentItemWeight}g (={str(storedItemWeight)}g x {itemCount})'
                    self.root.ids.buyingitems_screen.ids.cartView.data.append({'text': genItemString})
        except Exception as e:
            self.show_warning_no_item_selected_to_add_to_cart()

    def show_warning_no_item_selected_to_add_to_cart(self):
        content = MDLabel(font_style='Body1',
                          theme_text_color='Secondary',
                          text='No item selected for adding to cart.',
                          size_hint_y=None,
                          valign='top')
        content.bind(texture_size=content.setter('size'))
        self.dialog = MDDialog(title="No item selected!",
                               content=content,
                               size_hint=(.8, None),
                               height=dp(200),
                               auto_dismiss=True)
        self.dialog.add_action_button("Dismiss",
                                      action=lambda *x: self.dialog.dismiss())
        self.dialog.open()

    def reset_items_in_cart(self):
        self.root.ids.buyingitems_screen.ids.cartView.data = []
        self.root.ids.buyingitems_screen.ids.filter_items_button.disabled = False

    def delete_item_at_cart(self):
        try:
            if selection_cartview:
                for index, its in enumerate(self.root.ids.buyingitems_screen.ids.cartView.data):
                    if its['text'] == selection_cartview:
                        del self.root.ids.buyingitems_screen.ids.cartView.data[index]
        except Exception as e:
            self.show_warning_no_item_selected_to_undo_from_cart()

    def show_warning_no_item_selected_to_undo_from_cart(self):
        content = MDLabel(font_style='Body1',
                          theme_text_color='Secondary',
                          text='No item selected for undoing from cart.',
                          size_hint_y=None,
                          valign='top')
        content.bind(texture_size=content.setter('size'))
        self.dialog = MDDialog(title="No item selected!",
                               content=content,
                               size_hint=(.8, None),
                               height=dp(200),
                               auto_dismiss=True)
        self.dialog.add_action_button("Dismiss",
                                      action=lambda *x: self.dialog.dismiss())
        self.dialog.open()

    def commit_items_in_cart(self):
        # itemsinCart = [drow[0] for drow in self.cartlist.find()]
        for ci in self.root.ids.buyingitems_screen.ids.cartView.data:
            ci = ci['text']
            if self.cartlist.exists(ci.split(' | ')[0]):
                totalWeight = float(ci.split(' | ')[1].split('g')[0]) + float(
                    self.cartlist.get(ci.split(' | ')[0])['TotalWeight'].split('g')[0])
                itemWeight = float(ci.split('(=')[1].split('g')[0])
                self.cartlist.put(ci.split(' | ')[0],
                                  TotalWeight=str(totalWeight) + 'g',
                                  ItemWeight=str(itemWeight) + 'g',
                                  Count=round(totalWeight / itemWeight, 1),
                                  TimeID=datetime.strftime(datetime.now(), '%d.%m.%Y %H:%M:%S'))
            else:
                self.cartlist.put(ci.split(' | ')[0],
                                  TotalWeight=str(float(ci.split(' | ')[1].split('g')[0])) + 'g',
                                  ItemWeight=str(ci.split('(=')[1].split('g')[0]) + 'g',
                                  Count=str(ci.split('g x ')[1]).replace(')', ''),
                                  TimeID=datetime.strftime(datetime.now(), '%d.%m.%Y %H:%M:%S'))
        self.root.ids.buyingitems_screen.ids.filter_items_button.disabled = False

    def filter_recipes_Item_List(self, recText, chkbxState):
        if chkbxState == True:
            lrecipeInput = [drow['text'].lower() for drow in self.root.ids.narecipes.item_strings]
            recipeInput = [drow['text'] for drow in self.root.ids.narecipes.item_strings]
            indices = [i for i, s in enumerate(
                lrecipeInput) if recText.lower() in s]
            recipeView_item_strings = [
                recipeInput[i] for i in indices]
            self.root.ids.recipeView.data = [{'text': str(x)} for x in recipeView_item_strings]
        else:
            lrecipeInput = [drow[0].lower() for drow in self.recipe.find()]
            recipeInput = [drow[0] for drow in self.recipe.find()]
            indices = [i for i, s in enumerate(
                lrecipeInput) if recText.lower() in s]
            recipeView_item_strings = [
                recipeInput[i] for i in indices]
            recipeView_item_strings.sort()
            self.root.ids.buyingitems_screen.ids.recipeView.data = [{'text': str(x)} for x in recipeView_item_strings]

    def filter_items_Item_List(self, itemText):
        lfoodInput = [drow[0].lower() for drow in self.store.find()]
        foodInput = [drow[0] for drow in self.store.find()]
        indices = [i for i, s in enumerate(
            lfoodInput) if itemText.lower() in s]
        itemView_item_strings = [foodInput[i] for i in indices]
        itemView_item_strings.sort()
        self.root.ids.buyingitems_screen.ids.itemView.data = [{'text': str(x)} for x in itemView_item_strings]

    def show_cartitem_weight_used_home(self, selectedItem):
        foodWeight = [drow[1]['FoodWeight'] for drow in self.store.find() if drow[0] == selectedItem]
        self.root.ids.buyingitems_screen.ids.cart_item_weight_slider.max = float(foodWeight[0])
        self.root.ids.buyingitems_screen.ids.cart_item_weight_slider.value = float(foodWeight[0])

    def check_if_item_already_at_home(self):
        filteredItems = []

        for itm in self.root.ids.buyingitems_screen.ids.cartView.data:
            itm = itm['text']
            item_name, recipe_weight, item_weight, count = self.get_item_attributes_from_recipe_string(itm)
            
            if self.athome.exists(item_name):
                if recipe_weight - float(self.athome.get(item_name)['TotalWeight'].split('g')[0]) <= 0.0:
                    continue
                else:
                    actual_weight = round(recipe_weight - float(self.athome.get(item_name)['TotalWeight'].split('g')[0]), 1)
                    actual_count = round(actual_weight/item_weight, 1)
                    item_string = f'{item_name} | {actual_weight}g (={item_weight}g x {actual_count})'
                    filteredItems.append(item_string)
            else:
                filteredItems.append(itm)

        self.root.ids.buyingitems_screen.ids.cartView.data = [{'text': str(x)} for x in filteredItems]
        self.refresh_all()
        self.root.ids.buyingitems_screen.ids.filter_items_button.disabled = True

    #########################################################
    # HISTORY
    #########################################################
    def show_history(self):
        FoodWeight, FoodCost = 0, 0

        # View Items
        hili = []
        for hist in self.history.find():
            if (self.history.exists(hist[0])):
                hili.append(
                    hist[0] + ' | ' + str(hist[1]['TotalWeight']) + ' (=' + str(hist[1]['ItemWeight']) + ' x ' + str(
                        hist[1]['Count']) + ')')

        hili.sort()
        self.root.ids.history_screen.ids.analysisView.data = [{'text': str(x)} for x in hili]

        # View Info
        for itm in hili:
            FoodWeight += float(itm.split(' | ')[1].split('g')[0])
            FoodCost += (float(self.store.get(itm.split(' | ')[0])['FoodCost']) * float(itm.split(
                ' | ')[1].split('g')[0]) / float(self.store.get(itm.split(' | ')[0])['FoodWeight']))

        analysisInfoView_item_strings = ['Cost: {}€'.format(round(float(FoodCost), 2)),
                                         'Weight: {}g'.format(FoodWeight)]
        self.root.ids.history_screen.ids.analysisInfoView.data = [{'text': str(x)} for x in
                                                                  analysisInfoView_item_strings]

        # View Recipes

        availabelRecipes = []
        recipeInput = []
        counter = []
        for drow in self.recipe.find():
            for ahome in self.history.find():
                for its in list(set(drow[1]['Items'])):
                    if (ahome[0] == its.split(' | ')[0] and float(ahome[1]['TotalWeight'].split('g')[0]) >= float(
                            its.split(' | ')[1].split('g')[0])):
                        recipeInput.append(drow[0])
                        counter.append(
                            floor(
                                float(ahome[1]['TotalWeight'].split('g')[0]) / float(
                                    its.split(' | ')[1].split('g')[0])))

        for rec in set(recipeInput):
            indices = [i for i, x in enumerate(recipeInput) if x == rec]
            mins = [counter[i] for i in indices]
            for rec2 in self.recipe.find():
                if rec2[0] == rec and len(set(rec2[1]['Items'])) == float(recipeInput.count(rec)):
                    availabelRecipes.append(rec + ' x ' + str(min(mins)))

        availabelRecipes.sort()
        self.root.ids.history_screen.ids.analysisrecView.data = [{'text': str(x)} for x in availabelRecipes]

    def get_item_attributes_from_recipe_string(self, item_string):
        item_name = item_string.split(' | ')[0]
        recipe_weight = float(item_string.split(' | ')[1].split('g')[0])
        item_weight = float(item_string.split('(=')[1].split('g')[0])
        count = float(item_string.split(' x ')[1].split(')')[0])
        return item_name, recipe_weight, item_weight, count

    def set_recipe_string_from_item_attributes(self, item_name, recipe_weight, item_weight, count):
        if isinstance(item_name, str) and isinstance(recipe_weight, float) and isinstance(item_weight,
                                                                                          float) and isinstance(count,
                                                                                                                float):
            item_weight = round(item_weight, 1)
            recipe_weight = round(recipe_weight, 1)
            count = round(count, 1)
            recipe_string = f'{item_name} | {recipe_weight}g (={item_weight}g x {count})'
            return recipe_string

    @permission_exception
    def init_data(self):
        self.store = JsonStore(self.dir_path + 'data/foodmanager.json')
        self.athome = JsonStore(self.dir_path + 'data/athome.json')
        self.recipe = JsonStore(self.dir_path + 'data/recipes.json')
        self.cartlist = JsonStore(self.dir_path + 'data/cartitemlist.json')
        self.history = JsonStore(self.dir_path + 'data/history.json')

    def refresh_all(self):
        self.view_home_items()
        self.view_cart_items()
        self.view_recipe_items()
        self.view_recipe_cart_items()
        self.view_na_recipes()
        self.update_item()
        self.show_recipe()
        self.show_items()
        self.show_total_cost_cart_items()
        self.show_history()

    def show_snackbar(self, snack_text):
        Snackbar(text=snack_text).show()

    def show_permission_warning(self):
        content = MDLabel(font_style='Body1',
                          theme_text_color='Secondary',
                          text=f'To back up or restore your items and recipes on your device please enable external read and write permissions in the settings.',
                          size_hint_y=None,
                          valign='top')
        content.bind(texture_size=content.setter('size'))
        self.dialog = MDDialog(title="Permission denied",
                               content=content,
                               size_hint=(.8, None),
                               height=dp(200),
                               auto_dismiss=True)
        self.dialog.add_action_button("Dismiss",
                                      action=lambda *x: self.dialog.dismiss())
        self.dialog.open()

    def on_start(self):
        self.create_dir_structure()
        self.init_data()

    def on_pause(self):
        return True

    def on_stop(self):
        pass


if __name__ == '__main__':
    fmapp = FoodManagerApp()
    fmapp.run()
