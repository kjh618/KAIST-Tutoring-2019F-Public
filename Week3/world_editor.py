from cs1robots import *

world_name = input('World name: ')

try:
    load_world(world_name)
except:
    print(f"{world_name} doesn't exist. Creating new world:")
    avenues = int(input('Width: '))
    streets = int(input('Height: '))
    create_world(avenues, streets)

print('Press enter to finish editing and save the world.')
edit_world()
save_world(world_name)
