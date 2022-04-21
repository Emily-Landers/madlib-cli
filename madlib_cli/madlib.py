import re

        
with open("assets/dark_and_stormy_template.txt","w") as ds:
    ds.write("It was a {Adjective} and {Adjective} {Noun}.")

def read_template(file_path):
    with open(file_path,"r") as line_template:
        return line_template.read()
    
def parse_template(line_template):
    pattern = r"\{(\w+\s*\w+\s*\w+\s*\w+)\}"
    actual_stripped = re.sub(pattern,"{}", line_template)
    actual_parts = tuple(re.findall(pattern, line_template))
    return (actual_stripped, actual_parts)

def merge(stripped_line, user_input):
    new_string = stripped_line.format(*user_input)
    return new_string

welcome_msg()

#sis = "I the {Adjective} and {Adjective} {A First Name} have {Past Tense Verb}{A First Name}'s {Adjective} sister and plan to steal her {Adjective} {Plural Noun}!".format()

#quest = "What are a {Large Animal} and backpacking {Small Animal} to do? Before you can help {A Girl's Name}, you'll have to collect the {Adjective} {Plural Noun} and {Adjective} {Plural Noun} that open up the {Number 1-50} worlds connected to A {First Name's} Lair. There are {Number} {Plural Noun} and {Number} {Plural Noun} in the game, along with hundreds of other goodies for you to find.".format()
