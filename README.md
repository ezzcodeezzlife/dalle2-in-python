# Get Access
[labs.openai.com/waitlist](https://labs.openai.com/waitlist)

# Installation
```bash
pip install dalle2
```

# Usage
## Setup
1. Go to https://labs.openai.com/
1. Open Network Tab in Developer Tools
1. Type a prompt and press "Generate"
1. Look for fetch to https://labs.openai.com/api/labs/tasks
1. In the request header look for authorization then get the Bearer Token

```python
from dalle2 import Dalle2
dalle = Dalle2("sess-xxxxxxxxxxxxxxxxxxxxxxxxxxxx")
```

## Generate images
```python
generations = dalle.generate("portal to another dimension, digital art")
print(generations)
```

```
✔️ Task created with ID: task-xsuhOthvBXLEjddn3ynyiiOR
⌛ Waiting for task to finish...
...task not completed yet
...task not completed yet
...task not completed yet
...task not completed yet
🙌 Task completed!

[
  {
    'id': 'generation-sCnERSYDPP0Zu14fsdXEcKmL',
    'object': 'generation',
    'created': 1553332711,
    'generation_type': 'ImageGeneration',
    'generation': {
      'image_path': 'https://openailabsprodscus.blob.core.windows.net/private/user-hadpVzldsfs28CwvEZYMUT/generations/generation...'
    },
    'task_id': 'task-nERkiKsdjVCSZ50yD69qewID',
    'prompt_id': 'prompt-2CtaLQsgUbJHHDoJQy9Lul3T',
    'is_public': false
  },
  # 3 more ... 
]
```

## Download images
```python
file_paths = dalle.download(generations)
print(file_paths)
```

```
✔️ Downloaded: C:\...\generation-XySidj4N8EN6Ok9ed15BZ2bs.png
✔️ Downloaded: C:\...\generation-IK3UdxDz77FA5SLKpQPIITdU.png
✔️ Downloaded: C:\...\generation-uNejKBXz1z6EQxJAT9pAZbof.png
✔️ Downloaded: C:\...\generation-Ol1wEqNprf34vNohmJz0iUiE.png

[
  'C:/.../generation-pvi9TEWrhciLyFIlfgF1XUHF.png',
  'C:/.../generation-xp545V8jsqhSKKyJydHZPL50.png',
  'C:/.../generation-wNODqnBhvzYvXasonBn1anIA.png',
  'C:/.../generation-InPSaWWxpapT8TJD0kI71hNM.png'
]
```

## Generate images and download them
```python
file_paths = dalle.generate_and_download("portal to another dimension, digital art")
```

```
✔️ Task created with ID: task-xsuhOthvBXLEjddn3ynyiiOR
⌛ Waiting for task to finish...
...task not completed yet
...task not completed yet
...task not completed yet
...task not completed yet
🙌 Task completed!
✔️ Downloaded: C:\...\generation-XySidj4N8EN6Ok9ed15BZ2bs.png
✔️ Downloaded: C:\...\generation-IK3UdxDz77FA5SLKpQPIITdU.png
✔️ Downloaded: C:\...\generation-uNejKBXz1z6EQxJAT9pAZbof.png
✔️ Downloaded: C:\...\generation-Ol1wEqNprf34vNohmJz0iUiE.png
```

## Generate a specific number of images
```python
generations = dalle.generate_amount("portal to another dimension", 8) # Every generation has batch size 4 -> amount % 4 == 0 works best
```

```
✔️ Task created with ID: task-lm0V4nZasgAFasd7AsStE67
⌛ Waiting for task to finish...
...task not completed yet
...task not completed yet
...task not completed yet
...task not completed yet
🙌 Task completed!
✔️ Task created with ID: task-WcetZOHt8asdvHb433gi
⌛ Waiting for task to finish...
...task not completed yet
...task not completed yet
...task not completed yet
...task not completed yet
🙌 Task completed!
```

## Generate images from a masked file
DALL·E supports an "inpainting" API that fills-in transparent parts of an image.
The website provides a tool to paint over an existing image to indicate which
parts you want to be transparent. This Python package call assumes that the
image you provide has already been processed to have transparent parts.

```python
# make the right half of a saved image transparent
from PIL import Image, ImageDraw

image = Image.open('my_image.png')
m, n = image.size

area_to_keep = (0, 0, m//2, n)
image_alpha = Image.new("L", image.size, 0)
draw = ImageDraw.Draw(image_alpha)
draw.rectangle(area_to_keep, fill=255)

image_rgba = image.copy()
image_rgba.putalpha(image_alpha)
image_rgba.save('image_with_transparent_right_half.png')

# ask DALL·E to fill-in the transparent right half
generations = dalle.generate_from_masked_image(
    "portal to another dimension, digital art",
    "image_with_transparent_right_half.png",
)
```

```
✔️ Task created with ID: task-xsuhOthvBXLEjddn3ynyiiOR
⌛ Waiting for task to finish...
...task not completed yet
...task not completed yet
...task not completed yet
...task not completed yet
...task not completed yet
🙌 Task completed!
```

# Other languages

[Nodejs Package](https://github.com/ezzcodeezzlife/dalle-node)
