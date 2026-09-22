from langchain_core.prompts import FewShotPromptTemplate,PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

examples = [{'text':'i love this phone','sentiment':'positive'},
            {'text':'prodcur is terrible','sentiment':'negative'},
            {'text':'you service was excellent','sentiment':'positive'}]

example_prompt = PromptTemplate.from_template("Text:{text}\nSentiment:{sentiment}")
few_shot = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix ='classify the sentiment of the folloeing text',
    suffix = 'Text:{input}\nSentiment:',
    input_variables = ['input']
    )

llm = ChatGoogleGenerativeAI(model = 'gemini-2.5-flash')

user_input = input("Type a sentence:")
prompt = few_shot.format(input = user_input)
res = llm.invoke(prompt)
print(res.content)