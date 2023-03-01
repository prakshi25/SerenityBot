import random
import re

# Define some responses
greetings = ['Hi there!', 'Hello!', 'Hey!', 'Howdy!', 'Hola', 'Namaste', 'Bonjour' , 'Ciao', 'Konnichiwa', 'Privyet']
intro_statements = ['Nice to meet you {}!', 'It\'s great to talk to you, {}!', 'Hello, {}!', 'Good to see you, {}!']
questions = ['How was your day?', 'How are you feeling today?', 'What\'s on your mind?', 'How\'s your day been?']
motivations = ['Why don\'t you try meditating for a few minutes?', 'Have you considered calling a friend or family member?', 'How about drawing to release some tension?', 'You can fill color in pictures, it will help you calm down.', 'Jot down your thoughts in a journal to clear your mind.', 'Listen to your favourite songs, to change your mood.']
relaxation_techniques = ['Try some deep breathing exercises. Breathe in for 4 seconds, hold for 7 seconds, and breathe out for 8 seconds. Repeat this for a few minutes.', 'Progressive muscle relaxation can be helpful. Tense and relax each muscle group, starting with your toes and working your way up to your head.', 'Guided meditation or mindfulness exercises can also be beneficial. There are many apps and videos available to help you get started.']
connection_methods = ['Why don\'t you try joining a club or group that interests you?', 'Volunteering is a great way to meet new people and give back to the community.', 'Reaching out to an old friend or family member can be a good way to reconnect.']
encouragements = ['You are strong and capable, and you can get through this.', 'Take things one step at a time.', 'Remember to take care of yourself and prioritize your well-being.']
good_responses = ['Glad to hear that you had a good day!', 'That\'s great news!', 'Keep up the positive attitude!', 'You have got this.']
unknown_responses = ['I\'m sorry, I didn\'t understand. Could you please rate your day on a scale of 1 to 10?', 'I\'m not sure what you mean. Can you clarify?', 'Could you tell me more about that?']
thanks_responses = ['Great!', 'Thank you!', 'Glad to know that!', 'You are welcome!']
bye_responses = ['Okay, take care. Bye! See ya tomorrow.', 'Remember I am always here for you, you can talk to me about anything at anytime!']
exit_words = ['bye', 'see', 'talk', 'later']

# Define a function to get a response from the chatbot
def get_response(user_input,user_name):
    # Check for a greeting
    if any(greeting in user_input.lower() for greeting in ['hi there!', 'hello!', 'hey!', 'howdy!', 'hola', 'namaste', 'bonjour' , 'ciao', 'konnichiwa', 'privyet']):
        return random.choice(greetings)

    # Check for a question about the user's day
    elif any(question in user_input.lower() for question in ['day', 'feeling', 'mind']):
        return random.choice(questions)

    # Check if the user had a bad day and provide motivation
    elif any(feeling in user_input.lower() for feeling in ['bad', 'awful', 'terrible', 'not good']):
        return random.choice(motivations) + ' ' + random.choice(encouragements)

    # Check if the user had a good day
    elif any(feeling in user_input.lower() for feeling in ['good', 'great', 'wonderful', 'fantastic']):
        return random.choice(good_responses)

    # Check if the user says okay or thanks
    elif any(feedback in user_input.lower() for feedback in ['okay', 'thank', 'kind', 'helpful', 'best friend']):
        response = random.choice(thanks_responses)
        # Ask if the user wants to share more
        response += ' Is there something else you want to share with me?'
        return response

    # Check if the user mentions feeling anxious or stressed
    elif any(emotion in user_input.lower() for emotion in ['anxious', 'stressed', 'worried', 'fear']):
        return 'I\'m sorry to hear that.' + random.choice(relaxation_techniques)

    # Check if the user mentions feeling lonely or isolated
    elif any(emotion in user_input.lower() for emotion in ['lonely', 'isolated', 'alone']):
        return 'It can be tough to feel alone.' +  random.choice(connection_medthods)

    # Check if the user mentions feeling overwhelmed
    elif any(emotion in user_input.lower() for emotion in ['overwhelmed', 'too much']):
        return 'Feeling overwhelmed is completely normal.'
    
    elif any(feeling in user_input.lower() for feeling in ['happy', 'excited', 'joyful']):
        return random.choice(['That\'s great, {}!', 'I\'m so happy for you, {}!', 'Keep that positive attitude, {}!', 'You\'re amazing, {}!']).format(user_name)
        
    else:
        return random.choice(['I\'m sorry, I didn\'t understand.', 'Can you please rephrase that?', 'I\'m not sure what you mean.', 'Could you please clarify?'])
    
def main():
    user_name = None
    while True :
        if user_name is None:
            user_input = input('Welcome, My name is Serenity Bot! What\'s your name: ')
        else:
            if any(word in user_input.lower() for word in exit_words):
                random.choice(['Goodbye, {}! Take care.', 'See you later, {}!', 'Talk to you soon, {}!', 'It was great chatting with you, {}!']).format(user_name)
                break
            else:
                user_input = input(f'{user_name}, how can I assist you today? ')
            response = get_response(user_input, user_name)
        if user_name is None:
            user_name = user_input.capitalize()
            print(random.choice(intro_statements).format(user_name))
        else:
            print(response)
        
if __name__ == '__main__':
    main()
