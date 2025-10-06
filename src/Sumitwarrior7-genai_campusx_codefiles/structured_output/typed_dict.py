from typing import TypedDict, Annotated, Literal
from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv

load_dotenv()

chat_model = ChatMistralAI(
    model="mistral-large-latest",
    temperature=0
)

# Use of Annotated is optional but it gives llm better understanding of what all keys are all about in the TupedDict
# The only disadvantage here is that the output will have no validation checks on the keys of TupedDict
class Review(TypedDict):
    key_themes: Annotated[list[str], "Write down all the key themes listed in the review"]
    summary: Annotated[str, "A brief summary about the review"]
    sentiment: Annotated[Literal["pos", "neg", "neu"], "Return sentiment of the review either positive, negative or neutral"]

structured_model = chat_model.with_structured_output(Review)


reviews = [
    "I've been using this fitness tracker for about three months now and I'm thoroughly impressed with its capabilities. The heart rate monitoring is surprisingly accurate when compared to my previous device. Battery life exceeds the advertised 7 days - I typically get around 9 days with moderate use. The sleep tracking feature has been eye-opening and has helped me establish a much healthier sleep routine. The companion app is intuitive and provides detailed insights without overwhelming you with data. My only complaint would be that the strap sometimes causes skin irritation during intense workouts when I sweat a lot, but this is minor compared to all the positives.",
    "This online course on advanced photography techniques was a complete disappointment despite the promising curriculum. The instructor frequently rambled and went off-topic, making the 10-hour course feel unnecessarily bloated. Many of the editing techniques taught are outdated and don't work well with current software versions. The course materials contained several errors that were never addressed despite multiple students pointing them out in the discussion forum. The lack of structured feedback on assignments made it difficult to gauge improvement. The only redeeming quality was the lighting section, which contained some useful practical demonstrations. Save your money and look elsewhere for photography education."
]
resp = structured_model.invoke(reviews[0])
# print(resp)
print(resp["key_themes"])