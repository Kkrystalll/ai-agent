from dotenv import load_dotenv
import os

load_dotenv()
aa = os.getenv("OPEN_API_KEY")
print(aa)
