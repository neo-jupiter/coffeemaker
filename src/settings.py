from . import kitchen_settings

SCREEN_WIDTH =  1280
SCREEN_HEIGHT =  720
FPS =  60
loading_screen_path = "assets/loading_screen.jpg"
play_button_path = "assets/play_button.png"
table_path = "assets/table.jpg"
mug_path = "assets/mug.png"
main_menu_path = "assets/main_menu_draft.png"
press_anywhere_path= "assets/press_anywhere_to_begin.png"

class OrderOptions:
    BLACK_COFFEE = "black_coffee"
    MILK_COFFEE = "milk_coffee"
    MILK = "milk"
    


order_options= {
    OrderOptions.BLACK_COFFEE:{
        "coffee",
        "sugar"
    },
    OrderOptions.MILK_COFFEE:{
        "coffee",
        "milk",
        "Sugar"
    },
    OrderOptions.MILK:{
        "milk"
    }
}

dialogues = {
    "I want the bitter one" : OrderOptions.BLACK_COFFEE,
    "Make it extra creamy" : OrderOptions.MILK_COFFEE,
    "Can I have just the white stuff....you know what I am talking about" : OrderOptions.MILK 
}


