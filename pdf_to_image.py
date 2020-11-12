from pdf2image import convert_from_path, convert_from_bytes
import os

from defs_utils import *


matematica = list_dir(complete_name('Matemática'), True)


for file in matematica:
    input(file)
    images = convert_from_path(file)

    break





