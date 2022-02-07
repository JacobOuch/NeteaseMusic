import base64

string1 = """
wE95dBS55zMK8ZLmoIA9ozjNoLrfNsm8zvCAhiNNGUICeHdtHKZVnbbJ53RIIYlJTOrLh4LbRgEF5r0cyVNuIfCZqiFKIFa523iNjFVmUFk0PgL9gEc0h4NncGhQA56snXuARwYW0hBy4iVaiu/1vYGgb+QQqGHbXUOfAchVRAuLpciTaD7DAppQcQjlphOlTtnqd3qXRdiuyhfBLYFsh79NhvR0NEQwcHJFse5lGM9Cle6FUns3oI7dLKSY27iuNoAq/HAoXT5PJ+gDCMfrOA==
"""
decoded = base64.b64decode(string1)
# with open(".\shiliujinzhi.txt", 'w') as f:
#     f.write(str(base64.b64decode(string1), 'utf-8'))

print(decoded.decode('utf-8'))
print(type(decoded))