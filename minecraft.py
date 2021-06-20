import random
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
grass_texture = load_texture('minecraft/grass_block.png')
stone_texture = load_texture('minecraft/stone_block.png')
brick_texture = load_texture('minecraft/brick_block.png')
dirt_texture = load_texture('minecraft/dirt_block.png')
sky_texture = load_texture('minecraft/skybox.png')
arm_texture = load_texture('minecraft/arm_texture.png')

def update():
    if held_keys['left mouse'] or held_keys['right mouse']:
        hand.active()
    else:
        hand.passive()

class Voxel(Button):
    def __init__(self, position=(0, 0, 0)):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=0.5,
            texture='white_cube',
            color=color.color(0, 0, random.uniform(0, 9)),
            highlight_color=color.lime

        )

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                voxel = Voxel(position= self.position + mouse.normal)
            if  key == 'right mouse down':
                destroy(self)

class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent=scene,
            model='sphere',
            texture = sky_texture,
            scale=150,
            double_sided=True,
        )

class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model='minecraft/arm',
            texture=arm_texture,
            scale=0.2,
            rotation=Vec3(150,-10,0),
            position=Vec2(0.4,-0.6),
        )

    def active(self):
        self.position = Vec2(0.3,-0.5)

    def passive(self):
        self.position = Vec2(0.4,-0.6)

for z in range(20):
    for x in range(20):
        voxel = Voxel(position=(x,0,z))
player = FirstPersonController()
sky = Sky()
hand = Hand()

app.run()
