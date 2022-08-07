from jinja2 import Environment,FileSystemLoader
import os
import subprocess
env = Environment(
    variable_start_string = r'\var{',
    variable_end_string = '}',
    loader=FileSystemLoader("templates")
)

template = env.get_template('supplierReport.tex.jinja')
doc = template.render(title = "jinja test")
with open('index.tex','w') as output:
    output.write(doc)
finishedProcess = subprocess.run(['latexmk',"-auxdir=auxilary","-outdir=output","-pdf","-quiet", "-jobname=test",'index.tex'])
os.startfile('output\\test.pdf')
