import re

def welcome():
    print("Welcome to madlibs! input your answers when prompted")
        
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


