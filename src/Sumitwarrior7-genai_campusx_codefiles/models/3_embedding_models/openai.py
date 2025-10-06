from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-large",
    dimensions=69
)

# For a single document
vector = embedding_model.embed_query("It's not who i am underneath, but what i do that defines me")
print(vector)


# For a list of documents
documents = [
    "It's not who I am underneath, but what I do that defines me",
    "Why do we fall, sir? So that we can learn to pick ourselves up",
    "Some men just want to watch the world burn",
    "You either die a hero or live long enough to see yourself become the villain",
    "The night is darkest just before the dawn",
    "I'm Batman",
    "Fear is a tool. When that light hits the sky, it's not just a call. It's a warning",
    "A hero can be anyone, even a man doing something as simple as putting a coat around a young boy's shoulders",
    "Theatricality and deception are powerful agents to the uninitiated",
    "I won't kill you, but I don't have to save you",
    "You think darkness is your ally. You merely adopted the dark. I was born in it, molded by it",
    "I'm whatever Gotham needs me to be",
    "If you're good at something, never do it for free",
    "The training is nothing. The will is everything!",
]
vectors = embedding_model.embed_documents(documents)
print(vectors)