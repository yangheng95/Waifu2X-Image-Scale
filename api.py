# -*- coding: utf-8 -*-
# file: api.py.py
# time: 20:37 2022/12/6 
# author: yangheng <hy345@exeter.ac.uk>
# github: https://github.com/yangheng95
# huggingface: https://huggingface.co/yangheng
# google scholar: https://scholar.google.com/citations?user=NPq5a_0AAAAJ&hl=en
# Copyright (C) 2021. All Rights Reserved.
import base64
import requests
from PIL import Image
from io import BytesIO

import requests

url = "https://images.pexels.com/photos/666839/pexels-photo-666839.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"

response = requests.get(url)
image = Image.open(BytesIO(response.content))
# convert image to base64 string
image = base64.b64encode(image.tobytes()).decode('utf-8')

response = requests.post("http://127.0.0.1:7860/run/magnify_image", json={
    "data": [
        "data:image/png;base64,{}".format(image),
        2,
    ]}).json()

data = response["data"]

img = Image.open(BytesIO(response.content))
img.show()
img.save('test_api.png')
