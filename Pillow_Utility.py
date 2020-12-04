from PIL import Image, ImageDraw, ImageFont
from numpy.distutils.fcompiler import none


def draw_border(pillow_image, bounding, color, image_size, caption='', confidence_score=0):

    width, height = image_size
    draw = ImageDraw.Draw(pillow_image)
    draw.polygon([
        bounding.normalized_vertices[0].x *
        width, bounding.normalized_vertices[0].y * width,
        bounding.normalized_vertices[1].x *
        width, bounding.normalized_vertices[1].y * width,
        bounding.normalized_vertices[2].x *
        width, bounding.normalized_vertices[2].y * width,
        bounding.normalized_vertices[3].x *
        width, bounding.normalized_vertices[3].y * width,
        ], fill=none, outline=color)

    #TODO: validation needed
    font_size = width * height // 22000 if width * height > 400000 else 12

    draw.text((bounding.normalized_vertices[0].x * width, bounding.normalized_vertices[0].y * height),
              text=caption, fill=color)

    # insert confidence score
    draw.text((bounding.normalized_vertices[0].x * width, bounding.normalized_vertices[0].y * height + 20),
              text='confidence score: {0:.2f}%'.format(confidence_score), fill=color)

    return pillow_image