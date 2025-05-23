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
