from django.shortcuts import render
import requests, deepl, os, json
from dotenv import load_dotenv
load_dotenv()

# Create your views here.

# API Keys
deepl_auth_key = os.getenv('deepl_key', None)
writesonic_auth_key = os.getenv('writesonic_key', None)
url = os.getenv('url_key', None)

# Activates DeepL Translator
translator = deepl.Translator(deepl_auth_key)

# How to Use DeepL Translator
# result = translator.translate_text('How are you', target_lang='JA')
# print(result.text)

"""
Future plan: result = translator.translate_text(openai_response, target_lang='JA')
             romaji = openai(f'Please provide the romaji for the following sentence: result.text')
             english = openai(f'Please translate this sentence into English: result.text')
"""

# Homepage

def index(request):
    return render(request, 'translate_japanese/index.html', {})

# English - Japanese Assistant

def enja(request):
    chatbot_response = None
    message = None
    payload = {
    "enable_google_results": False,
    "enable_memory": False,
    "input_text": request.POST.get('inquiry')
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "X-API-KEY": writesonic_auth_key
    }
    response = requests.post(url, json=payload, headers=headers)

    if request.method == 'POST':
        parsed_json = json.loads(response.text)
        message = parsed_json['message']

        chat_input = message
        result = translator.translate_text(chat_input, source_lang='EN', target_lang='JA')
        message = result.text

    if message is not None:
        return render(request, 'translate_japanese/enja.html', {'chatbot_response': message})
    else:
       return render(request, 'translate_japanese/enja.html', {})

# Japanese - English Assistant

def jaen(request):
    chatbot_response = None
    message = None
    payload = {
    "enable_google_results": False,
    "enable_memory": False,
    "input_text": request.POST.get('inquiry')
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "X-API-KEY": writesonic_auth_key
    }
    response = requests.post(url, json=payload, headers=headers)

    if request.method == 'POST':
        parsed_json = json.loads(response.text)
        message = parsed_json['message']

        chat_input = message
        result = translator.translate_text(chat_input, source_lang='JA', target_lang='EN-US')
        message = result.text

    if message is not None:
        return render(request, 'translate_japanese/jaen.html', {'chatbot_response': message})
    else:
       return render(request, 'translate_japanese/jaen.html', {})

# Japanese - Japanese Assistant

def jaja(request):
    chatbot_response = None
    message = None
    payload = {
    "enable_google_results": False,
    "enable_memory": False,
    "input_text": request.POST.get('inquiry')
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "X-API-KEY": writesonic_auth_key
    }
    response = requests.post(url, json=payload, headers=headers)

    if request.method == 'POST':
        parsed_json = json.loads(response.text)
        message = parsed_json['message']

        chat_input = message
        result = translator.translate_text(chat_input, source_lang='JA', target_lang='JA')
        message = result.text

    if message is not None:
        return render(request, 'translate_japanese/jaja.html', {'chatbot_response': message})
    else:
       return render(request, 'translate_japanese/jaja.html', {})