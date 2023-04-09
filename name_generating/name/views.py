from django.http import JsonResponse
from django.shortcuts import render
from transformers import pipeline
import warnings
import json

def get_names(request):
    warnings.filterwarnings("ignore")
    generator = pipeline('text-generation', model='gpt2')
    prompt = request.GET.get('prompt', None)
    generated_sequences = generator(f"The imaginary company {prompt}. The company's name is \"", max_length=20,
                                    num_return_sequences=5)
    generated_names = []
    for sequence in generated_sequences:
        text = sequence['generated_text']
        first_quote_index = text.find('\"')
        second_quote_index = text.find('\"', first_quote_index+1)
        name = text[first_quote_index + 1:second_quote_index]
        name = name if name[-1] not in ('.', ',') else name[:len(name) - 1]
        generated_names.append(name)
    print('RES', generated_names)
    res = JsonResponse(generated_names, safe=False)
    res['Content-Type'] = 'application/json'
    res['Access-Control-Allow-Origin'] = '*'
    return res
