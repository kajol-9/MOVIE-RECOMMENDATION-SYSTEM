






import telebot
from telebot import types
import model
from datetime import datetime
import random 

 # Assuming test10 contains your recommendation logic

bot = telebot.TeleBot('API_KEY')


facts = [
    "The first movie ever made is often considered to be 'Roundhay Garden Scene,' created by Louis Le Prince in 1888. It's only about 2.11 seconds long. 🎥",
    "The longest film ever made is 'Logistics,' a 51,420-minute (857 hours) experimental film. 😲",
    "The highest-grossing film of all time, as of my last update, is 'Avengers: Endgame.' 🚀",
    "The Academy Awards, also known as the Oscars, first took place in 1929. 🏆",
    "The first feature-length animated film is 'Snow White and the Seven Dwarfs,' released by Disney in 1937. 🍎",
    "Alfred Hitchcock's 'Psycho' was the first movie to show a flushing toilet on screen. 🚽",
    "James Cameron's 'Avatar' was the first film to gross over $2 billion worldwide. 💰",
    "The shortest performance to win an Oscar for Best Supporting Actor is Anthony Quinn's role in 'Viva Zapata!' (1952), with a screen time of only 8 minutes and 32 seconds. ⏰",
    "The 'Star Wars' franchise has generated over $10 billion in revenue from films, making it one of the most successful movie franchises of all time. 🌌",
    "Mr.MovieMate >>>> ChatGPT when it comes to recommending movies🎥🎬",
    "Marilyn Monroe's iconic white dress from 'The Seven Year Itch' (1955) was sold at auction for $4.6 million in 2011. 👗💎",
    "I'm better at recommending movies🎥 than GPT 4.0 😄",
    "The movie 'The Shawshank Redemption' is based on a novella by Stephen King and initially performed poorly at the box office but later became a beloved classic. 📚",
    "In 'The Dark Knight,' Heath Ledger's portrayal of the Joker was so intense that it reportedly made Michael Caine (Alfred) forget his lines during their scenes together. 🃏",
    "The movie 'Inception' directed by Christopher Nolan has a famous spinning top scene that left audiences debating its ending. 🕰️",
    "The character E.T. in 'E.T. the Extra-Terrestrial' was played by a child with no legs inside the costume. 🛸",
    "The 'Matrix' trilogy popularized the use of slow-motion 'bullet time' sequences in action movies. 🕰️",
    "The famous 'I'll be back' line from 'The Terminator' was originally scripted as 'I'll come back.' Arnold Schwarzenegger suggested the change. 🤖",
    "The 'Harry Potter' film series used a whopping 588 sets, making it one of the most extensive film productions in history. 🪄",
    "Before filming 'The Lord of the Rings' trilogy, Viggo Mortensen (Aragorn) learned to speak Elvish and even got a tattoo in the fictional language. 🧝‍♂️",
    "The movie 'Frozen' was originally conceived as a traditional hand-drawn animation before becoming the computer-animated musical we know today. ❄️",
    "The classic film 'Gone with the Wind' had the most significant number of extras ever used in a film, with over 2,400 actors. 🎬"
]

smiley_emoji = "😄"
popcorn_emoji = "🍿"
camera_emoji = "📷"
thumbs_up_emoji = "👍"
clapperboard_emoji = "🎬"

gifs = [
    "https://media.giphy.com/media/M4yhdWpiRA3P8qeItw/giphy.gif",   #understand meme
    "https://media.giphy.com/media/l0HTYUmU67pLWv1a8/giphy.gif",    #nice meme
    "https://media.giphy.com/media/Kyz8mPqam8pHLNJy3B/giphy.gif",   #fine meme
    "https://media.giphy.com/media/e9YuweWAauJoGT3e1D/giphy.gif",   #bot meme    
    "https://media.giphy.com/media/brsEO1JayBVja/giphy.gif",        #hello meme
    "https://media.giphy.com/media/01u3Rw1zQLSylw2Tn9/giphy.gif",   #chat meme
    "https://media.giphy.com/media/PAqjdPkJLDsmBRSYUp/giphy.gif",   #Welcome meme
    "https://media.giphy.com/media/k7D6JtncCTQnvQ26ee/giphy.gif",   #Recommend meme
    "https://media.giphy.com/media/3o85xIO33l7RlmLR4I/giphy.gif",   #Movie clapperboard GIF
    "https://media.giphy.com/media/3o7aCTPPm4OHfRLSH6/giphy.gif",   #Popcorn GIF
    "https://media.giphy.com/media/xT0xeJpnrWC4XWblEk/giphy.gif",   #Smiley GIF
]

Parameters=["Par1", "Par2", "Par3", "Par4", "Par5", "Par6"]
chat_mode_active = False

@bot.message_handler(commands=['start'])
def greetings(message):
    welcome_meme = "https://media.giphy.com/media/PAqjdPkJLDsmBRSYUp/giphy.gif"
    bot.send_animation(message.chat.id, welcome_meme)
    bot.send_message(message.chat.id, "Welcome!Type '/info' for more information")
    global Parameters
    
@bot.message_handler(commands=['info'])
def introduce(message):
        bot.send_message(message.chat.id, "Hi, I am Mr.MovieMate, a chatbot made by Team Dristhi to provide you Movies that we're sure you will Love!!")
        bot.send_message(message.chat.id, "Commands:\nRecommend: '/recommend'\nChat:'/chat'\nHelp: '/help'\nSkip Question: '/skip'")


@bot.message_handler(commands=['chat'])
def start_chat(message):
    chat_meme = "https://media.giphy.com/media/01u3Rw1zQLSylw2Tn9/giphy.gif"
    bot.send_animation(message.chat.id, chat_meme)
    global chat_mode_active
    chat_mode_active = False
    markup = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(message.chat.id, "You are now in chat mode. Type '/end' to exit this mode whenever you like.", reply_markup=markup)
    chat_mode_active = True

# Create a function to handle the chat mode conversation
@bot.message_handler(func=lambda message: chat_mode_active)
def chat_mode(message):
    user_message = str(message.text).lower()

    if user_message == "/end":
        global chat_mode_active
        chat_mode_active = False
        bot.send_message(message.chat.id, "You have exited chat mode. You can now use other commands.")
    
    elif user_message in ("hello", "hi", "sup","hey", "heyo", "hola", "hii"):
        hello_meme = "https://media.giphy.com/media/brsEO1JayBVja/giphy.gif"
        bot.send_animation(message.chat.id, hello_meme)
        bot.send_message(message.chat.id, f"{smiley_emoji}Hey! How are you?")
        
    elif user_message in ("i am fine"):
        nice_meme = "https://media.giphy.com/media/l0HTYUmU67pLWv1a8/giphy.gif"
        bot.send_animation(message.chat.id, nice_meme)
        bot.send_message(message.chat.id, "nice to hear that, wanna watch some beautiful movies")
        
    elif user_message in ("i am fine what about you", "i am fine, what about you", "i am fine,what about you"):
        fine_meme = "https://media.giphy.com/media/Kyz8mPqam8pHLNJy3B/giphy.gif"
        bot.send_animation(message.chat.id, fine_meme)
        bot.send_message(message.chat.id, "I am also fine, wanna watch some good movies?")
        
    elif user_message in("Yes", "yes", "yup", "absolutely", "why not", "sure", "ofc", "of course", "yeah", "yes it is", "it surely is", "it definately is"):
        bot.send_message(message.chat.id, "Sure then, type '/recommend' for movie recommendations")
        
    elif user_message in("no", "nah", "nope", "not right now", "nahh", "after a while"):
        bot.send_message(message.chat.id, "lets keep chatting then, you also can type 'fact' for some stunning facts about the film industry")
    
    elif user_message in("who are you", "who are you?", "what are you?", "what are you"):
        bot_meme = "https://media.giphy.com/media/e9YuweWAauJoGT3e1D/giphy.gif"
        bot.send_animation(message.chat.id, bot_meme)
        bot.send_message(message.chat.id, "I am Mr.MovieMate, your friend and a recommender chatbot for Drishti Makernova 1.0")
    
    elif user_message in("why do you exist?", "why do you exist"):
        bot.send_message(message.chat.id, "I am Mr.MovieMate, a Chatbot for MAKERNOVA 1.0, and I exist so you don't have to stress about the movies you have to watch")
    
    elif "how are you" in user_message:
        bot.send_message(message.chat.id, "I'm absolutely fine! How can I help you?")
    
    elif user_message in ("recommend", "recommend movies", "recommend me something", "recommend me some movies","suggest", "suggest some movies", "suggest movies", "suggest something"):
        bot.send_message(message.chat.id, "Sure, type '/recommend' to get movie recommendations.")
        
    elif user_message in ("fact", "facts", "tell me a fact", "please tell me a fact", "tell me a movie related fact", "tell me a movie fact", "tell me something interesting", "tell a fact", "tell some facts"):
        random_fact = random.choice(facts)
        bot.send_message(message.chat.id, f"{camera_emoji} Here's a fact from the film industry for you:\n{random_fact}")
        
    elif user_message == "help":
        response =  "Here are some commands you can use:\n" \
                    "/recommend - Get movie recommendations\n" \
                    "/chat - To chat with the bot\n" \
                    "/end - End the conversation\n"\
                    "/skip - To skip a question during recommendation\n"
        bot.send_message(message.chat.id, response)

    elif "time" in user_message:
        now = datetime.now()
        date_time = now.strftime("%H:%M:%S, %d/%m/%Y\nIsn't it a good time to watch some good movies!")
        bot.send_message(message.chat.id, str(date_time))
    
    else:
        understand_meme = "https://media.giphy.com/media/M4yhdWpiRA3P8qeItw/giphy.gif"
        bot.send_animation(message.chat.id, understand_meme)
        bot.send_message(message.chat.id, f"{smiley_emoji}I don't understand you! Type /info for more commands or type /recommend for movie recommendations or /chat to end the chat mode.")
    
    @bot.message_handler(commands=['info'])

    def introduce(message):

        bot.send_message(message.chat.id, "Hi, I am Mr.MovieMate, a chatbot made by Team Dristhi to provide you Movies that we're sure you will LOVE!!")
        bot.send_message(message.chat.id, "Commands:\nRecommend: '/recommend'\nChat:'/chat'\nHelp: '/help'\nSkip Question: '/skip'")
  # Replace with your actual bot token

# Global variables


# Command handler
Parameters = []
Final=[]
@bot.message_handler(commands=['recommend'])
def get_title(message):
    global Parameters
    title_input = bot.send_message(message.chat.id, "What are your top movies? (Enter titles separated by commas)")
    Parameters.append(message.text)

    bot.register_next_step_handler(title_input, ask_language)

def ask_language(message):
    global Parameters
    Parameters.append(message.text)  # Store the input from the user

    markup = types.ReplyKeyboardRemove(selective=False)
    language_input = bot.send_message(message.chat.id, "Which Language Movie do You Want?", reply_markup=markup)
    bot.register_next_step_handler(language_input, ask_preference)

def ask_preference(message):
    global Parameters
    Parameters.append(message.text)  # Store the input from the user

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    preference_options = ["Genre", "Actor", "Director"]
    markup.add(*preference_options)
    preference_reply = bot.send_message(message.chat.id, "For Genre: 0 \nFor Actor: 1\nFor Director: 2", reply_markup=markup)
    bot.register_next_step_handler(preference_reply, ask_specific_preference)

def ask_specific_preference(message):
    global Parameters
    choice=int(message.text)
    Parameters.append(choice)       

    preference_input = None
    if choice == 0:
        preference_input = bot.send_message(message.chat.id, "Enter your preferred genre:")
    elif choice== 1:
        preference_input = bot.send_message(message.chat.id, "Enter your favorite actor:")
    elif choice == 2:
        preference_input = bot.send_message(message.chat.id, "Enter your favorite director:")

    bot.register_next_step_handler(preference_input, process_specific_preference)

def process_specific_preference(message):
    global Parameters
    Parameters.append(message.text)  # Store the input from the user
    show_results(message)  # Call the show_results function after collecting all the inputs

def show_results(message):
    global Parameters
    
    # Perform movie recommendation using your logic
    
    for i in Parameters[1:]:
        Final.append(i)

    recommendations,recommendations2 = model.get_recs(Final[0], Final[1], Final[2], Final[3], model.movies, model.tfidf_df)
    
        

        
    # Send recommendations to the user
    bot.send_message(message.chat.id, "Here are your Recommendations:")
    for movie in recommendations:
        bot.send_message(message.chat.id, movie)
    
    # for movie_title in test10.rec_titles:
    #     bot.send_message(message.chat.id, movie_title)

    bot.send_message(message.chat.id, "Here are your Recommendations:")
    for movie in recommendations2:
        bot.send_message(message.chat.id, movie)
    
    # for movie_title in test10.rec_titles:
    #     bot.send_message(message.chat.id, movie_title)

@bot.message_handler(commands=['info'])
def introduce(message):
    bot.send_message(message.chat.id, "Commands:\nRecommend: '/recommend'\nHelp: '/help'\nSkip Question: '/skip'")

@bot.message_handler(commands=['about'])
def about(message):
    bot.send_message(message.chat.id, "Hello!! I am a Movie Recommendation System presented by Team Dristhi!!")

bot.infinity_polling()


