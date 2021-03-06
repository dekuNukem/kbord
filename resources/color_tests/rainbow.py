import os
import random
import colorsys
from PIL import Image, ImageDraw

colour_values = [16, 127, 255]

def make_color():
	rrr = random.choice(colour_values)
	ggg = random.choice(colour_values)
	bbb = random.choice(colour_values)
	hsv = colorsys.rgb_to_hsv(rrr/256, ggg/256, bbb/256)
	return (rrr, ggg, bbb, hsv[0], hsv[1], hsv[2])

already_done = set()
this_color = set((0, 0, 0))
for x in range(1,17):
	while 1:
		this_color = make_color()
		if this_color[0] == this_color[1] == this_color[2]:
			continue
		if this_color not in already_done:
			break
	already_done.add(this_color)

already_done = sorted(already_done, key=lambda x: (x[4], x[3]))
already_done = list(already_done)

im = Image.new('RGB', (300,500), (255, 255, 255))
draw = ImageDraw.Draw(im)

# x, y
draw.rectangle(((0, 0), (100, 100)), fill=(already_done[0][0], already_done[0][1], already_done[0][2]))
draw.rectangle(((100, 0), (200, 100)), fill=(already_done[1][0], already_done[1][1], already_done[1][2]))
draw.rectangle(((200, 0), (300, 100)), fill=(already_done[2][0], already_done[2][1], already_done[2][2]))

draw.rectangle(((0, 100), (100, 200)), fill=(already_done[3][0], already_done[3][1], already_done[3][2]))
draw.rectangle(((100, 100), (200, 200)), fill=(already_done[4][0], already_done[4][1], already_done[4][2]))
draw.rectangle(((200, 100), (300, 200)), fill=(already_done[5][0], already_done[5][1], already_done[5][2]))

draw.rectangle(((0, 200), (100, 300)), fill=(already_done[6][0], already_done[6][1], already_done[6][2]))
draw.rectangle(((100, 200), (200, 300)), fill=(already_done[7][0], already_done[7][1], already_done[7][2]))
draw.rectangle(((200, 200), (300, 300)), fill=(already_done[8][0], already_done[8][1], already_done[8][2]))

draw.rectangle(((0, 300), (100, 400)), fill=(already_done[9][0], already_done[9][1], already_done[9][2]))
draw.rectangle(((100, 300), (200, 400)), fill=(already_done[10][0], already_done[10][1], already_done[10][2]))
draw.rectangle(((200, 300), (300, 400)), fill=(already_done[11][0], already_done[11][1], already_done[11][2]))

draw.rectangle(((0, 400), (100, 500)), fill=(already_done[12][0], already_done[12][1], already_done[12][2]))
draw.rectangle(((100, 400), (200, 500)), fill=(already_done[13][0], already_done[13][1], already_done[13][2]))
draw.rectangle(((200, 400), (300, 500)), fill=(already_done[14][0], already_done[14][1], already_done[14][2]))

im.save("image.png", "PNG")

