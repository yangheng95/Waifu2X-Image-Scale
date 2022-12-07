import os
import random
from io import BytesIO

import autocuda
import requests
from pyabsa.utils.pyabsa_utils import fprint

import gradio as gr
import torch
from PIL import Image
import datetime
import time
from Waifu2x.magnify import ImageMagnifier

magnifier = ImageMagnifier()

start_time = time.time()

CUDA_VISIBLE_DEVICES = ''
device = autocuda.auto_cuda()

dtype = torch.float16 if device != 'cpu' else torch.float32

def magnify_image(image, scale_factor=2):
    start_time = time.time()
    image = magnifier.magnify(image, scale_factor=scale_factor)
    fprint(f'Inference time: {time.time() - start_time:.2f}s')
    return image

with gr.Blocks() as demo:
    if not os.path.exists('imgs'):
        os.mkdir('imgs')

    gr.Markdown('# Free Image Scale Up Demo')
    gr.Markdown('## 免费图片分辨率放大演示')
    gr.Markdown('## Powered by Waifu2x')
    gr.Markdown("## Author: [yangheng95](https://github.com/yangheng95)  Github:[Github](https://github.com/yangheng95/SuperResolutionAnimeDiffusion)")

    with gr.Row():
        with gr.Column(scale=40):
            with gr.Group():
                image_in = gr.Image(label="Image", height=512, tool="editor", type="pil")

                with gr.Row():
                    scale_factor = gr.Slider(1, 8, label='Scale factor (to magnify image) (1, 2, 4, 8)',
                                             value=2,
                                             step=1)
                with gr.Row():
                    generate = gr.Button(value="Magnify", label="Magnify")

            error_output = gr.Markdown()

        with gr.Column(scale=60):
            gr.Markdown('## Click the right button to save the magnified image')
            gr.Markdown('## 右键点击图片保存放大后的图片')
            with gr.Group():
                image_out = gr.Image(height=512)
    inputs = [image_in, scale_factor]
    outputs = [image_out]
    generate.click(magnify_image, inputs=inputs, outputs=outputs, api_name="magnify_image")

print(f"Space built in {time.time() - start_time:.2f} seconds")

demo.launch(enable_queue=True, share=False)
