import requests

url = "https://raw.githubusercontent.com/ignaciocastro/a-dove-is-dumb/main/clash.yaml"
response = requests.get(url)
content = response.text

with open('clash.yaml', 'w') as file:
    file.write(content)

lines = content.splitlines()
comments = []
domains = []

in_payload_section = False

for line in lines:
    if line.startswith('#'):
        comments.append(line)
    elif line.strip() == 'payload:':
        in_payload_section = True
    elif in_payload_section and line.strip().startswith('- DOMAIN,'):
        domains.append(line.strip()[2:].strip())

output = '\n'.join(comments) + '\n' + '\n'.join(domains)

with open('clash.list', 'w') as file:
    file.write(output)