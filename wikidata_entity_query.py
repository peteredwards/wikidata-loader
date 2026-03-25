from wikidata.client import Client
client = Client()
entity = client.get('P18', load=True)
print(entity.label)
print(entity.description)

