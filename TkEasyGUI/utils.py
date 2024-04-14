import pyperclip

def set_clipboard(text):
    """copy text to clipboard"""
    pyperclip.copy(text)

def get_clipboard():
    """get text from clipboard"""
    return pyperclip.paste()


