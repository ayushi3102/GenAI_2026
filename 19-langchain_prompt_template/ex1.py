from langchain_core.prompts import PromptTemplate
prompt = PromptTemplate.from_template("Write  a {adjective} summary of {topic} in {language}")
formatted_prompt = prompt.format(adjective = 'short',
              topic='GENAI',
              language ='english')

print(formatted_prompt)