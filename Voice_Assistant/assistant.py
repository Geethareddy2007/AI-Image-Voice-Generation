import pyttsx3

engine = pyttsx3.init()

question = input("Ask me a question: ")

if "artificial intelligence" in question.lower():
    answer = "Artificial Intelligence is the simulation of human intelligence by machines."

elif "machine learning" in question.lower():
    answer = "Machine Learning allows computers to learn from data without explicit programming."

else:
    answer = "Sorry, I do not know the answer."

print("\nAssistant:", answer)

engine.say(answer)
engine.runAndWait()