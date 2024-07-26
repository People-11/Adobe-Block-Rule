import requests

url = "https://raw.githubusercontent.com/ignaciocastro/a-dove-is-dumb/main/clash.txt"
response = requests.get(url)
content = response.text

with open('clash.list', 'w') as file:
    file.write(content)

lines = content.splitlines()
comments = []
domains = []

for line in lines:
    if line.startswith('#'):
        comments.append(line)
    elif line.startswith('DOMAIN'):
        domains.append(f"  - {line}")

output = '\n'.join(comments) + '\n' + 'payload:\n' + '\n'.join(domains)

with open('clash.yaml', 'w') as file:
    file.write(output)
