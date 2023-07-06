# from functools import wraps
lang='ta'

translations = {
    "samosa_buy": {
        "ta": "எனக்கு சமோசா வாங்கித் தர முடியுமா?",
        "en": "Can you buy me Samosa?",
        "hi": "क्या आप मेरे लिए समोसा खरीद सकते हैं?",
        "ma": "എനിക്ക് സമൂസ വാങ്ങി തരുമോ?",
        "te": "నాకు సమోసా కొనగలవా?"
    }
}

def traslate(target_function):
    global lang
    # @wraps(target_function)
    def wrapper(*args, **kwargs):
        # msg,lang=target_function(*args, **kwargs)
        msg=target_function(*args, **kwargs)
        # return translations[msg][lang] + " Please!!!"
        return translations[msg][lang]
        # return msg+" Please!!!"
    return wrapper

@traslate
# def say(lang='en'):
def say():
    # msg="Can you buy me Samosa?"
    msg="samosa_buy"
    return msg
    # return msg,lang

@traslate
def sayit(phrase="Please!"):
    return phrase

print(say())
# print(say("ta"))
