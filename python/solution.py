#!/usr/bin/env python3

from typing import (
    List,
    Tuple,
    Union
)

from utils.image import (
    ImageType,
    PackedImage,
    StrideImage,
)

from utils.function_tracer import FunctionTracer

from utils.eye_pattern import EYE_PATTERNS

import numpy as np


def image_to_matrix(resolution, numbers):
    image_width = resolution.width
    image_height = resolution.height

    matrix = []
    for i in range(image_height):
        row = numbers[i*image_width : i*image_width+image_width]
        matrix.append(row)

    return np.array(matrix)


def find_and_correct_eyes(image_matrix):
    (height, width) = image_matrix.shape

    window_size = 5

    for i in range(height): # process row by row
        for j in range(width):
            if image_matrix[i, j] == 1: # when seeing one, check for eye patterns
                if i > height-window_size or j > width-window_size:
                    image_matrix[i, j] = 0
                else:
                    checked_area = image_matrix[i:i+window_size,j:j+window_size]
                    for eye_pattern in EYE_PATTERNS:
                        if np.allclose(checked_area, eye_pattern):
                            checked_area *= -150
                    if image_matrix[i, j] == 1: # The pixel does not start an eye pattern, set to zero
                        image_matrix[i, j] = 0 

    return image_matrix


def compute_solution(images: List[Union[PackedImage, StrideImage]]):
    ft = FunctionTracer("compute_solution", "seconds")

    for img in images:
        red_matrix = image_to_matrix(img.resolution, img.pixels_red.copy())
        red_matrix = np.where(red_matrix >= 200, 1, 0)
        red_matrix = find_and_correct_eyes(red_matrix)
        red_matrix = red_matrix.flatten()

        img.pixels_red = np.array(img.pixels_red) + red_matrix
        img.pixels_red = img.pixels_red.tolist()
        
    del ft



            