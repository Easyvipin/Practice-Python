# startswith() and endswith() String Methods
# wap check the tags are closed

String = '''<div><p>hello world</p> </div>'''
value = String.endswith('</div>')


if String.startswith('<div>') == String.endswith('</div>'):
    print("Tags are closed")
else:
    print("Please close the tags")

#Tags are closed