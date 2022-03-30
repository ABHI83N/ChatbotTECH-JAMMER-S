from chatterbot import ChatBot
from chatterbot.conversation import Statement
from chatterbot.trainers import ChatterBotCorpusTrainer

# create ChatBot
chatBot = ChatBot("ChatBot",

    logic_adapters=[
 {
            "import_path": "chatterbot.logic.BestMatch",
            "statement_comparison_function": chatterbot.comparisons.LevenshteinDistance,
            "response_selection_method": chatterbot.response_selection.get_first_response
        }
    ]
)

# create ChatBot trainer
trainer = ChatterBotCorpusTrainer(chatBot)

# Train ChatBot with English language corpus
# you can train with different language
# or with your custom .yam file
trainer.train("chatterbot.corpus.english")

# Greeting from chat bot
print("Hi, I am ChatBot")

# keep communicating with ChatBot
while True:
    # take user input/query
    query = input(">>>")
    # response from ChatBot
    # put query on Statement format to avoid runtime alert messages
    # Statement(text=query, search_text=query)
    print(chatBot.get_response(Statement(text=query, search_text=query)))
