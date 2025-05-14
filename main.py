from ursina import *

# Inicializar la aplicación Ursina
app = Ursina()

# Crear el jugador como un cubo controlable
player = Entity(model='cube', color=color.azure, scale=(1, 2, 1), collider='box', position=(0, 1, 0))

# Crear el suelo
ground = Entity(model='plane', scale=100, texture='white_cube', texture_scale=(100, 100), collider='box')

# Configurar la cámara en tercera persona
camera.parent = player
camera.position = (0, 10, -20)
camera.rotation_x = 30

# Función de actualización para manejar el movimiento del jugador
def update():
    speed = 5 * time.dt
    if held_keys['w']:
        player.z -= speed
    if held_keys['s']:
        player.z += speed
    if held_keys['a']:
        player.x -= speed
    if held_keys['d']:
        player.x += speed

# Ejecutar la aplicación
app.run()
