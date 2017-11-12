# Created by: Younes Elfeitori
# Created on: Nov 2017
# Created for: ICS3U
# This program recieves the hight and radius and gives back the volume of a cylinder

PI = 3.14

import ui

def calculate_volume(radius,height):
    # volume calculation
    volume = (2 * PI * radius ** 2 * height)
    return volume

def calculate_volume_button_touch_up_inside(sender):
    # runs the calculate button
    user_radius = int(view['radius_textfield'].text)
    user_height = int(view['height_textfiled'].text)
    answer = calculate_volume(user_radius , user_height)
    
    view['answer_label'].text = str(answer)
    
view = ui.load_view()
view.present('sheet')
