import pyglet

width, height = 1000, 600
window = pyglet.window.Window(width, height, 'My Space Invaders')

label = pyglet.text.Label("Hello, Python!")

label.x = window.width / 2
label.y = window.height / 2
label.anchor_x = 'center'
label.anchor_y = 'center'


@window.event
def on_draw():
    label.draw()


pyglet.app.run()
