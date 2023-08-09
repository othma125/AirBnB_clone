import re

def extract_args(s):
    # Match the content inside the parentheses
    match = re.search(r'\((.*?)\)', s)
    if not match:
        return []

    args = match.group(1)

    # If there's a '{', extract everything between '{' and '}'
    if '{' in args:
        curly_braces_content = re.search(r'\{(.*?)\}', args)
        if curly_braces_content:
            args = args.replace(curly_braces_content.group(0), '').split(',')
            args = [arg.strip() for arg in args if arg.strip()]
            args.append(curly_braces_content.group(0))
        else:
            args = args.split(',')
    else:
        args = args.split(',')

    return [arg.strip() for arg in args if arg.strip()]

s = "update(d8cb051b-3fd9-40d9-94ec-0b233a2171e1,{'email': '', 'password': '111'})"
print(extract_args(s))

s = "update(d8cb051b-3fd9-40d9-94ec-0b233a2171e1,email, @@)"
print(extract_args(s))
s = "update(d8cb051b-3fd9-40d9-94ec-0b233a2171e1,email, @@)"
print(extract_args(s))
