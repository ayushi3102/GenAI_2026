
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from google.api_core.exceptions import DeadlineExceeded, Unauthorized

load_dotenv()


class AIService:

    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            timeout=20
        )

        self.prompt = ChatPromptTemplate.from_messages([
            (
                "system",
                "You are a professional technical consultant. Answer briefly."
            ),
            ("human", "{user_input}")
        ])

        self.chain = self.prompt | self.llm

    async def get_response(self, text: str):
        try:
            response = await self.chain.ainvoke({
                "user_input": text
            })

            return response.content

        except DeadlineExceeded:
            raise Exception("The AI took too long to respond.")

        except Unauthorized:
            raise Exception("Authentication failed.")

        except Exception as ex:
            raise Exception(f"An unexpected error occurred: {ex}")
