from dotenv import load_dotenv

load_dotenv()
import os


def main():
    print("Hello from langchain-practice!")
    print(os.environ.get("GOOGLE_API_KEY", "Environment variable not set."))


if __name__ == "__main__":
    main()
