import numpy as np


def split_blocks(image, block_size=8):
    h, w = image.shape
    blocks = []
    for y in range(0, h - block_size + 1, block_size):
        for x in range(0, w - block_size + 1, block_size):
            blocks.append((y, x, image[y:y+block_size, x:x+block_size]))
    return blocks


def merge_blocks(image, blocks, block_size=8):
    for y, x, block in blocks:
        image[y:y+block_size, x:x+block_size] = block
    return image
