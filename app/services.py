from PIL import Image

def get_avg_rgb_img(image, width, height):

    pixel = []

    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x, y))
            pixel.append([r, g, b])

    avr = [sum(x) // len(x) for x in zip(*pixel)]

    avg_color = (','.join(str(x) for x in avr))

    return avg_color