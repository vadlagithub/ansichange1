#Reads yml file,yaml.load to bring that as in Python Structure and pretty print it

python -c 'import yaml,pprint;pprint.pprint(yaml.load(open("test.yml").read()))'
