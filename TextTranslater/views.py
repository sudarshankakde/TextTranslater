# views.py
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from deep_translator import GoogleTranslator  # Change to desired translator if needed


def extract_text(request):
    return render(request, 'index.html')


def translate(request):
    if request.method == "GET":
        text = request.GET.get('text')
        print(len(text))
        target_lang = request.GET.get('targetLanguage') or 'hi' # Marathi
        # Create a translator object using GoogleTranslator (you can change this)
        translator = GoogleTranslator(service_url='https://pypi.org/project/deep-translator/',target=target_lang)
        try:
            # Attempt the translation
            translation = translator.translate(text)
            print(translation)
            return HttpResponse(f"{translation}")
        except Exception as e:
            print(f"An error occurred during translation: {e}")
            return JsonResponse({'text':f"An error occurred during translation: {e}"})