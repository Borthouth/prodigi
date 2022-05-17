# coding: utf-8

import os
import wget
import logging

from PIL import Image

black = [36, 36, 36]
grey = [56, 78, 87]
teal = [0, 98, 110]
navy = [0, 0, 80]

logger = logging.getLogger('ProdigiTechTest')

def get_file(url):
    logger.info(f'Getting from {url}')
    file_name = os.path.basename(str(url))
    if not file_name.endswith('.png'):
    	return False
    try:
        wget.download(str(url), f"{file_name}")
        return str(file_name)
    except:
        logger.exception(f"Failed to download {file_name} from {url}")
        return False

def get_dominant_colour_quick(pil_image):
	# Quick but not very accurate
    logger.info("Using Quick Process")
    new_image = pil_image.copy()
    new_image = new_image.convert("RGB")
    new_image = new_image.resize((1, 1), resample=0)
    dominant_colour = new_image.getpixel((0, 0))
    
    return dominant_colour
    
def get_dominant_colour_accurate(pil_image, palette_size=16):
    # Slower but more accurate
    logger.info("Using Accurate Process")
    new_image = pil_image.copy()
    new_image.thumbnail((100, 100))
    as_palette = new_image.convert('P', palette=Image.ADAPTIVE, colors=palette_size)
    palette = as_palette.getpalette()
    colour_count = sorted(as_palette.getcolors(), reverse=True)
    palette_index = colour_count[0][1]
    dominant_colour = palette[palette_index*3:palette_index*3+3]

    return dominant_colour

def check_colour(colour_list):
    logger.info("Checking colour")
    if list(colour_list) == list(black):
        return str("Black")

    elif list(colour_list) == list(grey):
        return str("Grey")

    elif list(colour_list) == list(teal):
        return str("Teal")

    elif list(colour_list) == list(navy):
        return str("Navy")
    
    else:
    	return False

