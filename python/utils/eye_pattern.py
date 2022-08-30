#!/usr/bin/env python3

from typing import Tuple

import numpy as np

EyePattern = Tuple[str, str, str, str, str]

EYE_PATTERN_1: EyePattern = (
  "/---\\",
  "|   |",
  "|-o-|",
  "|   |",
  "\\---/"
)

EYE_PATTERN_2: EyePattern = (
  "/---\\",
  "| | |",
  "| 0 |",
  "| | |",
  "\\---/"
)

EYE_PATTERN_3: EyePattern = (
  "/---\\",
  "| | |",
  "|-q-|",
  "| | |",
  "\\---/"
)

EYE_PATTERN_4: EyePattern = (
  "/---\\",
  "|\\ /|",
  "| w |",
  "|/ \\|",
  "\\---/"
)


# Eye patterns presented as numbers

EYE_PATTERN_1_NUM = np.array([[1, 1, 1, 1, 1],
                              [1, 0, 0, 0, 1],
                              [1, 1, 1, 1, 1],
                              [1, 0, 0, 0, 1],
                              [1, 1, 1, 1, 1]])


EYE_PATTERN_2_NUM = np.array([[1, 1, 1, 1, 1],
                              [1, 0, 1, 0, 1],
                              [1, 0, 1, 0, 1],
                              [1, 0, 1, 0, 1],
                              [1, 1, 1, 1, 1]])


EYE_PATTERN_3_NUM = np.array([[1, 1, 1, 1, 1],
                              [1, 0, 1, 0, 1],
                              [1, 1, 1, 1, 1],
                              [1, 0, 1, 0, 1],
                              [1, 1, 1, 1, 1]])
  

EYE_PATTERN_4_NUM = np.array([[1, 1, 1, 1, 1],
                              [1, 1, 0, 1, 1],
                              [1, 0, 1, 0, 1],
                              [1, 1, 0, 1, 1],
                              [1, 1, 1, 1, 1]])

EYE_PATTERNS = [EYE_PATTERN_1_NUM, EYE_PATTERN_2_NUM, EYE_PATTERN_3_NUM, EYE_PATTERN_4_NUM]

