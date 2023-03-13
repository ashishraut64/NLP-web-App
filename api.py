import paralleldots
paralleldots.set_api_key('J50GkqUXl89OjCTOReqbuOCsZvGKYNEGigfDsIgnIgo')
def ner(text):
    ner = paralleldots.ner(text);
    return ner
def emotion(text):
    emotion = paralleldots.emotion(text);
    return emotion