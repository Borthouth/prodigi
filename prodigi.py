# coding: utf-8

"""
Requirements:
    python3.6
    python3.6 -m pip install wget
    python3.6 -m pip install pillow 
    NOTE: if pillow install fails use "python3.6 -m pip install --upgrade pillow 


Description:
    

Variables:


Output:

"""

import os
import requests 
import json

from PIL import Image
from urllib.parse import urlparse

from django.views.generic import View

from prodigi_utils import (
    get_file,
    get_dominant_colour_quick,
    get_dominant_colour_accurate,
    check_colours,
)

class ProdigiTechTest(View):

    def get(self, request):
        """
        Return the filename and RGB values

        @param request: Django HttpRequest object

        @return: Django HttpResponse containing JSON list of image RGB values
        """
        url = request.GET.get('url', '')
        accuracy = request.GET.get('accuracy', 1)

        filename = get_file(url)
        if not filename:
            return HTTPResponse(f"No file found using URL {url}", status=500)

  
        # Find dominant colour
        pil_image = Image.open(f"{filename}")

        if int(accuracy) == 0:
            dominant_colour_quick = get_dominant_colour_quick(pil_image)
            colour_result = check_colour(dominant_colour_quick)

        else:
            dominant_colour_accurate = get_dominant_colour_accurate(pil_image)
            colour_result = check_colour(dominant_colour_quick)

        if not colour_result:
        	return HTTPResponse(f"{filename} Does not match known colours", status=500)
 
        json_colour = []
        json_colour.append[{'file': str(file), 'colour': str(colour_result)}]
        return HTTPResponse(json.dumps(json_colour), content_type="application/json")
     