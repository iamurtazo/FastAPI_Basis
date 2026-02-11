def fence(func):
    def wrapper():
        text = func()
        print("#" * len(text))
        print(text)
        print("#" * len(text))
    return wrapper

@fence
def log():
    text = "some gibberish message here"
    return text

log()
