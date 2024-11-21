import os

def _join_path(asset_name:str)->str:
    _base_path = os.path.join("assets","kitchen")
    return os.path.join(_base_path,asset_name)

#import paths
base_cup_path = _join_path("base_cup.png")
cofee_jar_path = _join_path("coffee_jar.png")
sugar_jar_path = _join_path("sugar_jar.png")
water_jug_path = _join_path("water_jug.png")
milk_jug_path = _join_path("milk_jug.png")
base_spoon_path = _join_path("base_spoon.png")
spoon_coffee_path = _join_path("spoon_coffee.png")
spoon_sugar_path = _join_path("spoon_sugar.png")
cup_coffee_particles_path = _join_path("cup_coffee.png")
cup_sugar_particles_path = _join_path("cup_sugar.png")
cup_water = _join_path("cup_water.png")
cup_coffee_milk = _join_path("cup_milk.png")
cup_black_coffee_path = _join_path("cup_black_coffee.png")
cup_milk_coffee_path = _join_path("cup_milk_coffee.png")


