import yaml

raw_dict = yaml.load(open('chaos.yaml', 'r'))
src_dict = []
raw_keys = []

for d in raw_dict:
    if d['value']:
        src_dict.append(d)
        raw_keys.append(d['name'])


minor_suits = ['cups', 'swords', 'wands', 'pentacles']
minor_values = map(lambda x: str(x + 2), range(9)) + ['ace', 'page', 'knight', 'queen', 'king']
cards = ['the fool', 'the magician', 'the high priestess', 'the empress', 'the emperor', 'the hierophant', 'the lovers',
         'the chariot', 'justice', 'the hermit', 'wheel of fortune', 'strength', 'the hanged man', 'death',
         'temperance', 'the devil', 'the tower', 'the star', 'the moon', 'the sun', 'judgment', 'the world']

for minor_suit in minor_suits:
    for minor_value in minor_values:
        card_name = minor_value + ' of ' + minor_suit
        cards.append(card_name)

for card_name in cards:
    if card_name not in raw_keys:
        src_dict.append({'name': card_name, 'value': []})


print "%s/%s entries filled" % (len(raw_keys), len(cards))
print len(src_dict)
yaml.dump(src_dict, open('chaos.yaml', 'w'))
