# python3
# cap.py - 単語の先頭を大文字にするモジュール

def just_do_it(text):
    # "<test>に含まれるすべての単語をタイトルケースに"
    from string import capwords
    return capwords(text)