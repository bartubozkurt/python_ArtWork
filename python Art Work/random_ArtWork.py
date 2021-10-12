import random
import uuid

from PIL import Image, ImageDraw

run_id = uuid.uuid1()

print(f'Processing run_id: {run_id}')

image = Image.new('RGB', (1000, 1000))
width, height = image.size

ellipse_width, ellipse_height = 30, 30

""" rectangle_width = 50
rectangle_height = 50 """

lines_width,lines_height = 45, 90


arc_width, arc_height = 100, 150

pieslice_width, pieslice_height = 25,  50


""" number_of_squares = random.randint(10, 550)
number_of_ellipse = random.randint(10, 550) """
number_of_lines = random.randint(10, 50)
number_of_arc = random.randint(10,50)
number_of_pieslice = random.randint(10,15)


draw_image = ImageDraw.Draw(image)


for i in range(number_of_arc):
    arc_x = random.randint(0, width)
    arc_y = random.randint(0, height)

    arc_shape = [
        (arc_x, arc_y),
        (arc_x + arc_width, arc_y + arc_height)]
    draw_image.arc(
        arc_shape,
        start=30,
        end=270,
        fill=(
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )
    )
    for i in range(number_of_pieslice):
        pie_x = random.randint(0, width)
        pie_y = random.randint(0, height)

        pieslice_shape = [
            (pie_x, pie_y),
            (pie_x + pieslice_width, pie_y + pieslice_height)]
        draw_image.pieslice(
            pieslice_shape,
            start=30,
            end=270,
            fill=(
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255)
            )
        )
        for k in range(number_of_lines):
            line_x = random.randint(0, width)
            line_y = random.randint(0, height)

            lines_shape = [(line_x,line_y),
                            (line_x + lines_width,
                            line_y + lines_height)]
            draw_image.line(
                    lines_shape,
                    fill= (
                    random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(0, 255)
                    )
            )


image.save(f'./output/{run_id}.png')