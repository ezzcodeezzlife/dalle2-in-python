# Get Access

[labs.openai.com/waitlist](https://labs.openai.com/waitlist)

- Go to https://labs.openai.com/
- Open Network Tab in Developer Tools
- Type a promt and press "Generate"
- Look for fetch to https://labs.openai.com/api/labs/tasks
- In the request header look for authorization then get the Bearer Token


# Usage
```bash
pip install dalle2
```
```python
from dalle2 import Dalle2

dalle = Dalle2("sess-xxxxxxxxxxxxxxxxxxxxxxxxxxxx")
generations = dalle.generate("portal to another dimension, digital art")


print(generations)
```

```
✔️  Task created with ID: task-f77yxcsdf3OEm and PROMT: portal to another dimension, digital art
⌛ Waiting for task to finish .. 
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
  {
    'id': 'generation-hZWt2Nasrx8R0tJjbaROfKVy',
    'object': 'generation',
    'created': 1553332711,
    'generation_type': 'ImageGeneration',
    'generation': {
      'image_path': 'https://openailabsprodscus.blob.core.windows.net/private/user-hadpVzldsfs28CwvEZYMUT/generations/generation...'
    },
    'task_id': 'task-nERkiKhjasdSZ50yD69qewID',
    'prompt_id': 'prompt-2CtaLasdUbJHHfoJQy9Lul3T',
    'is_public': false
  },
  # 4 more ... 
]
```

or download all generations

```python
from dalle2 import Dalle2

dalle = Dalle2("sess-xxxxxxxxxxxxxxxxxxxxxxxxxxxx")
generations = dalle.generate_and_download("portal to another dimension, digital art")

```

```
✔️  Task created with ID: task-f77sayxcSGdfOEm and PROMT: portal to another dimension, digital art
⌛ Waiting for task to finish .. 
🙌 Task completed!
Download to directory: C:\Users\pc\dalle2
✔️  Downloaded:  generation-fAq4Lyxcm7pQVDBQEWJ.jpg
✔️  Downloaded:  generation-zqfBC3yyxcPXRlW6zLP.jpg
✔️  Downloaded:  generation-soR3ryxcoeixzdyHG.jpg
✔️  Downloaded:  generation-lT5L4yxc2DOiGRwJi.jpg
✔️  Downloaded:  generation-01DvPryxcq2BX1NOREL.jpg
✔️  Downloaded:  generation-AAs4yxcczH1vl19FidR.jpg

```


[![Test In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1EEgZNAI58V_OiEfRJQSsQV_xkhHzQeRB?usp=sharing)


