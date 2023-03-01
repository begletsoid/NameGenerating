from transformers import pipeline
import warnings

warnings.filterwarnings("ignore")

generator = pipeline('text-generation', model='gpt2')
while True:
    prompt = input('The company... ')  # Сюда суём ключевые слова типа "Creates games"
    generated_sequences = \
        generator(f"The imaginary company {prompt}. The company's name is \"", max_length=20,
                  num_return_sequences=5)
    for sequence in generated_sequences:
        text = sequence['generated_text']
        first_quote_index = text.find('\"')
        second_quote_index = text.find('\"', first_quote_index+1)
        name = text[first_quote_index + 1:second_quote_index]
        name = name if name[-1] not in ('.', ',') else name[:len(name) - 1]
        print(name)
