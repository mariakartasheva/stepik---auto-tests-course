def name_length(name):
    if len(name) > 0:
        return str(len(name))
    print("wtf") 
    return ''

def my_name(name, job):
    print("Hello, my name is " + name + ". I am a " + job + ". My name's length is " + name_length(name))

my_name('Dima', 'developer')
my_name('Ira', 'doctor')
my_name('Dasha', 'cook')
my_name('', '?')

# Играю с гитом :D