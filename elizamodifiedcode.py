# Natural Language Toolkit: Eliza
#
# Copyright (C) 2001-2022 NLTK Project
# Authors: Steven Bird <stevenbird1@gmail.com>
#          Edward Loper <edloper@gmail.com>
# URL: <https://www.nltk.org/>
# For license information, see LICENSE.TXT


# Based on an Eliza implementation by Joe Strout <joe@strout.net>,
# Jeff Epler <jepler@inetnebr.com> and Jez Higgins <mailto:jez@jezuk.co.uk>.


# a translation table used to convert things you say into things the
# computer says back, e.g. "I am" --> "you are"

from nltk.chat.util import Chat, reflections


# a table of response pairs, where each pair consists of a
# regular expression, and a list of possible responses,
# with group-macros labelled as %1, %2.


pairs = (
    (
        r"Yeah",
        (
            "Anything else?",
           
        ),
    ),
    (
        r"My name is (.*)",
        (
            "Hi %1 I'm Eliza, How are you today?",
            "Nice to meet you %1, how can I help you today?",
            "Hi %1, I'm Eliza. Ask me anything",
        ),
    ),
    (
        r"What's the weather (.*)",
        (
            "%1 is not too bad.",
            "%1 is better than yesterday.",
            "%1 is 70 degree. I hope you have a good day.",
        ),
    ),
    (
        r"Thank you",
        (
            "No worries",
            "You're welcome",
            "My Pleasure",
        ),
    ),
    (
        r"What's (.*)",
        (
            "I'm not too sure about %1, I'll let you know tomorrow",
            "Perhaps you could google %1",
        ),
    ),
    (
        r"I am feeling(.*)",
        (
            "Everyone feels %1. ",
            "Why are you %1?",
        ),
    ),
  (
        r"I\'m(.*)",
        (
            "Thank you for telling me. How can I help you today?",
        ),
    ),
    (
        r"What do you think about (.*)",
        (
            "%1 is okay, nothing amazing. What do you think?",
        ),
    ),
    (
        r"Do you know if (.*)",
        (
            "Hmmm, it depends",
            "I don't know if %1",
        ),
    ),


    (
        r"sorry ",
        (
            "No worries",
            "You're good",
        ),
    ),
    (
        r"Hello(.*)",
        (
            "Hello... What's your name?",
        ),
    ),
    (
        r"I think (.*)",
        (
            "Well that's good you think that way.",
            "Everyone has their own opinion.",
            
        ),
    ),
 
    (
        r"I have (.*)",
        (
            "I had %1 long time ago. What do you think about %1?",
            
        ),
    ),
    
    (
        r"Is there (.*)",
        (
            "I beleive there is %1 somewhere",
        ),
    ),


    (
        r"Do you believe in (.*)",
        (
            "Yes, I do believe in %1. ",
        ),
    ),




    (
        r"(.*)\?",
        (
            "Why do you ask that?",
            "Please consider whether you can answer your own question.",
            "Perhaps the answer lies within yourself?",
            "Why don't you tell me?",
        ),
    ),
    (
        r"bye",
        (
            "bye. Hopefully, we'll talk soon",
        ),
    ),
    (
        r"(.*)",
        (
            "Please tell me more.",
            "Let's change focus a bit... Tell me about your family.",
            "Can you elaborate on that?",
            "Why do you say that %1?",
            "I see.",
            "Very interesting.",
            "%1.",
            "I see.  And what does that tell you?",
            "How does that make you feel?",
            "How do you feel when you say that?",
        ),
    ),
)


eliza_chatbot = Chat(pairs, reflections)




def eliza_chat():
    print("Therapist\n---------")
    print("Talk to the program by typing in plain English, using normal upper-")
    print('and lower-case letters and punctuation.  Enter "quit" when done.')
    print("=" * 72)
    print("Hello!")


    eliza_chatbot.converse()






def demo():
    eliza_chat()






if __name__ == "__main__":
    demo()
