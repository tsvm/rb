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


def list_to_matrix(resolution, numbers):
    image_width = resolution.width
    image_height = resolution.height

    matrix = []
    for i in range(image_height):
        row = numbers[i*image_width : i*image_width+image_width]
        matrix.append(row)

    return np.array(matrix)


def eye_correction_matrix(image_matrix):
    """
    The input is an image matrix with values 1 in the positions with potential eye patterns
    
    Returns image matrix with value -150 in the positions of the pixels of eye patterns
    """
    (height, width) = image_matrix.shape

    window_size = 5

    for i in range(height): # process row by row
        for j in range(width):
            # When seeing pixel with value 1, check for eye patterns
            if image_matrix[i, j] == 1: 
                if i > height-window_size or j > width-window_size:
                    image_matrix[i, j] = 0
                else:
                    checked_area = image_matrix[i:i+window_size,j:j+window_size]
                    for eye_pattern in EYE_PATTERNS:
                        if np.allclose(checked_area, eye_pattern):
                            # If we found an eye pattern, set it to the value that needs to be subtracted
                            checked_area *= -150
                    if image_matrix[i, j] == 1: 
                        # The pixel does not start an eye pattern, set to zero
                        image_matrix[i, j] = 0 

    return image_matrix


def compute_solution(images: List[Union[PackedImage, StrideImage]]):
    ft = FunctionTracer("compute_solution", "seconds")

    # We only need to consider the red pixels in order to find eyes for correction
    for img in images:
        # 1. Turn the red values array into a matrix representing the image
        red_matrix = list_to_matrix(img.resolution, img.pixels_red.copy())
        # 2. We are interested in pixels with red value > 200.
        #    Set those to 1 and the rest to 0.
        red_matrix = np.where(red_matrix >= 200, 1, 0)
        # 3. Search for eye patterns and correct them.
        #    Get a matrix with values for correcting eyes.
        red_matrix = eye_correction_matrix(red_matrix)
        # 4. Make it in format of the red values array
        red_matrix = red_matrix.flatten()
        # 5. Sum the red pixels with the eye correcting array
        img.pixels_red = np.array(img.pixels_red) + red_matrix
        img.pixels_red = img.pixels_red.tolist()
        
    del ft



            