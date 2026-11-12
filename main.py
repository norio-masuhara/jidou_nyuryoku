with open('data.txt', encoding='utf-8') as f:
    lines = f.readlines()
name = lines[0].strip().split('：')[1]
address = lines[1].strip().split('：')[1]
birthday = lines[2].strip().split('：')[1]
shokureki = []
for line in lines[3:]:
    shokureki.append(line.strip())
print(shokureki)
shokureki_text = '\n'.join(shokureki)

with open('template.txt', encoding='utf-8') as f:
    template = f.read()

result = template.format(name=name, address=address, birthday=birthday, shokureki=shokureki_text)
print(result)
with open('output/' + name + '.txt', 'w', encoding='utf-8') as f:
    f.write(result)
