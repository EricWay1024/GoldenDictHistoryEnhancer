import requests

def get_example_sentences(word):
    
    def helper():
        response = requests.get(f'https://api.dictionaryapi.dev/api/v1/entries/en/{word}').json()[0]
        result = []
        for value in response['meaning'].values():
            for meaning in value:
                if meaning.get('example'):
                    result.append(meaning['example'])
        return result
    
    for _ in range(10):
        try:
            return helper()
        except:
            pass
    else:
        raise RuntimeError('API Failure')





