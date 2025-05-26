# Quick Start

In this guide we will see how we can get up and running with the OpenAI API in around 20 minutes. For a more advanced example see [Advanced](advanced.md).



## Virtual Environment

Start by enabling a Virtual Environment in folder on your computer. I have create a folder structure based in my root folder `$HOME/git/ai-python/quick_start` and enabled a Virtual Environment in that folder using the following commands.

```shell
cd
mkdir -p git/ai-python/quick_start
cd git/ai-python/quick_start
python3 -m venv .venv
. .venv/bin/activate
```



## Installing pip-modules

We will now move on to installing the required modules that allows us to interact with the OpenAI API. We will install two modules `openai` and `python-dotenv` (for secure handling of API-keys). We then take a snapshot of the installed dependencies using the `pip freeze` command and store that in `requirements.txt`.

```shell
pip install python-dotenv openai
python -m pip freeze > requirements.txt
```



## .env-file

As described above the `python-dotenv` module allows us to easily store API-keys securely. Create a `.env` file and add the following contents, replace YOURAPIKEY with the actual API-key.

```shell
touch .env
```

```text
OPENAI_API_KEY="YOURAPIKEY"
OPENAI_API_ENDPOINT="https://bth-ai.azure-api.net/student/openai/deployments/gpt-4o-mini/chat/completions"
```

If you upload your code to GitHub or other remote repositories please include the `.env`-file in your `.gitignore` file.


## Coding

Ok, now we have everything in place and we can start coding our interaction with the API. Start by creating a `quick_start.py` file, either through your texteditor or terminal using `touch quick_start.py`.

In the file we import the modules that we installed earlier together with the built-in `os` module.

```python
import os
from dotenv import load_dotenv
load_dotenv()

from openai import AzureOpenAI
```

We then use the `AzureOpenAI` constructor of the `openai` module to create the `client` instance that we are going to use to connect to OpenAI API.

```python
import os
from dotenv import load_dotenv
load_dotenv()

from openai import AzureOpenAI

client = AzureOpenAI(
  azure_endpoint=os.getenv("OPENAI_API_ENDPOINT"),
  api_key=os.getenv("OPENAI_API_KEY"),
  api_version="2025-01-01-preview"
)
```

The `os.getenv` method fetches the stored values from the `.env` file and a client is created for us. Now we want to start interacting with our client programmatically.

First we say which model we want to use. And then we create a list of messages that is our interaction with the API. When we use the `role: system` key-value pair we explain to the AI-model what role we want it to take. So in this case it is simply a helpful assistant. This can be tailored, see the [advanced](advanced.md) example for more.

The second message we send is a chat message from us the user. In this case "Do elephants eat bananas?", this is similar to opening ChatGPT in the webbrowser and typing "Do elephants eat bananas?".

```python
import os
from dotenv import load_dotenv
load_dotenv()

from openai import AzureOpenAI

client = AzureOpenAI(
  azure_endpoint=os.getenv("OPENAI_API_ENDPOINT"),
  api_key=os.getenv("OPENAI_API_KEY"),
  api_version="2025-01-01-preview"
)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Do elephants eat bananas?"},
    ]
)

print(response.choices[0].message.content)

print(response.usage)
```

In the example above I print the response from the API and usage data to see the amount of tokens used for this request.
