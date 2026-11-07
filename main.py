with open('data.txt', encoding='utf-8') as f:
    lines = f.readlines()
name = lines[0].strip()
address = lines[1].strip()
birthday = lines[2].strip()

with open('template.txt', encoding='utf-8') as f:
    template = f.read()

result = template.format(name=name, address=address, birthday=birthday)
print(result)
with open('output/' + name + '.txt', 'w', encoding='utf-8') as f:
    f.write(result)
