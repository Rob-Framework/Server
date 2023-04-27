from PIL import Image
from clip_interrogator import Config, Interrogator

def interrogate(img): 
    image = Image.fromarray(img)
    ci = Interrogator(Config(clip_model_name="ViT-L-14/openai"))
    result = ci.interrogate(image)
    return result