from PIL import Image

image_path_files = ['Dog_1.jpg','Dog_2.jpg','Dog_3.jpg']

listed_images = [ Image.open(file) for file in image_path_files ]

listed_images[0].save('animation.gif', save_all=True, append_images = listed_images[1:], duration=1000, loop=0)

print("thank you")