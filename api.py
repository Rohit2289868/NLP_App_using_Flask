import paralleldots
# paralleldots.set_api_key('ShzLRnHb8LEhGy6uWTWIOyUAxzlYUr7m2aLPzqlzs3k')
paralleldots.set_api_key('IH4OCcC3pwUFU6jRcoyzug4ShpopFEtpLFigQEZImmk')

def NER(text):
    result = paralleldots.ner(text)
    return result