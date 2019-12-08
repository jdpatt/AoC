"""Advent of Code 2019 Day 8"""
import re
from shared.common import get_input


def layers_from_image(width, height, image):
    return re.findall("." * height * width, image)


def pixel_from_layers(layers):
    pixel = []
    for index, layer in enumerate(layers):
        pixel.append(layer[0])
        layers[index] = layer[1:]
    return "".join(pixel), layers


def stack_and_decode_layers(width, height, layers):
    pixels = [[0 for i in range(width)] for j in range(height)]
    for row in range(height):
        for column in range(width):
            pixel, layers = pixel_from_layers(layers)
            pixels[row][column] = decode_color(pixel)
    return pixels


def decode_color(pixel):
    for color in pixel:
        if color == "1":
            return "1"
        elif color == "0":
            return "."


if __name__ == "__main__":
    PUZZLE = get_input("input8.txt")
    width = 25
    height = 6
    layers = layers_from_image(width, height, PUZZLE)
    number_of_zeros = [layer.count("0") for layer in layers]
    lowest = number_of_zeros.index(min(number_of_zeros))
    ones = layers[lowest].count("1")
    twos = layers[lowest].count("2")
    print(f"Part 1: {ones * twos}")

    pixels = stack_and_decode_layers(width, height, layers)
    print("Part 2:")
    for row in pixels:
        print("".join(row))


def test_layers_from_image():
    assert layers_from_image(3, 2, "123456789012") == ["123456", "789012"]


def test_decode_color():
    assert decode_color("0120") == "0"
    assert decode_color("2120") == "1"
    assert decode_color("2210") == "1"
    assert decode_color("0000") == "0"


def test_pixel_from_layers():
    assert pixel_from_layers(["123456", "789012"]) == ("17", ["23456", "89012"])
