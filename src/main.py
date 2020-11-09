'''
            Quotes App

=========================================

This program generates a random quote everything time the user requests by pressing a button. Uses the Kivy framework.


'''
#Things to Add: Export it to Play Store, add a way to maxmize window automatically, etc. 

import random as r
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.core.window import Window

class quotesApp(App):
    def build(self):
        Window.clearcolor = (0.98, 0.28, 1, 1)
        main_layout = FloatLayout(size = (500, 500))
        self.welcome = Label(text = "The Most Wonderful Quotes of All-Time!", pos_hint = {"x" : .018, "y": .41}, font_size = '40sp', color =(1, 1, 1, 1), markup = True,)
        main_layout.add_widget(self.welcome)
        self.quote = TextInput(multiline = "True", readonly = True, halign = "center", font_size=50, size_hint = (.71,.55),
                               pos_hint = {"x": .15,"y": .30},background_color = (0.98, 0.28, 1, 1)) 
        main_layout.add_widget(self.quote)
        self.author = TextInput(multiline = "False", readonly = True, halign = "center", font_size = 25, size_hint = (.43, .10), pos_hint = {"x": .285,"y": .175},
                                background_color = (0.98, 0.28, 1, 1))
        main_layout.add_widget(self.author)
        nextButton = Button(text = "Click for a Quote", size_hint = (.3, .1), pos_hint = {"x": .355, "y": .055}, background_color = (0.98, 0.28, 1, 1))
        nextButton.bind(on_press = self.onButtonPress)
        main_layout.add_widget(nextButton)

        return main_layout

    def onButtonPress(self, instance):
        quotesNAuthors = {
    "Nelson Mandela": "The greatest glory in living lies not in never falling, but in rising every time we fall.",
    "Walt Disney" : "The way to get started is to quit talking and begin doing.",
    "Steve Jobs" : "Your time is limited, so don't waste it living someone else's life. Don't be trapped by dogma – which is living with the results of other people's thinking.",
    "Eleanor Roosevelt":"If life were predictable it would cease to be life, and be without flavor.",
    "Oprah Winfrey" : "If you look at what you have in life, you'll always have more. If you look at what you don't have in life, you'll never have enough.",
    "James Cameron" : "If you set your goals ridiculously high and it's a failure, you will fail above everyone else's success.",
    "John Lennon" : "Life is what happens when you're busy making other plans.",
    "Mother Teresa" : "Spread love everywhere you go. Let no one ever come to you without leaving happier.",
    "Franklin D. Roosevelt" : "When you reach the end of your rope, tie a knot in it and hang on.",
    "Margaret Mead" :"Always remember that you are absolutely unique. Just like everyone else.",
    "Robert Louis Stevenson" :"Don't judge each day by the harvest you reap but by the seeds that you plant.",
    "Eleanor Roosevelt" : "The future belongs to those who believe in the beauty of their dreams.",
    "Benjamin Franklin" :"Tell me and I forget. Teach me and I remember. Involve me and I learn." ,
    "Helen Keller": "The best and most beautiful things in the world cannot be seen or even touched - they must be felt with the heart.",
    "Aristotle" : "It is during our darkest moments that we must focus to see the light.",
    "Anne Frank" : "Whoever is happy will make others happy too." ,
    "Ralph Waldo Emerson" : "Do not go where the path may lead, go instead where there is no path and leave a trail.",
    "Maya Angelou" :"You will face many defeats in life, but never let yourself be defeated.",
    "Abraham Lincoln" : "In the end, it's not the years in your life that count. It's the life in your years.",
    "Babe Ruth" : "Never let the fear of striking out keep you from playing the game.",
    "Helen Keller" : "Life is either a daring adventure or nothing at all.",
    "Thomas Edison" : "Many of life's failures are people who did not realize how close they were to success when they gave up.",
    "Dr. Seuss" : "You have brains in your head. You have feet in your shoes. You can steer yourself any direction you choose.",
    "Oscar Wilde" :"Life is never fair, and perhaps it is a good thing for most of us that it is not.",
    "Tony Robbins" : "The only impossible journey is the one you never begin.",
    "Albert Einstein" : "Only a life lived for others is a life worthwhile.",
    "Dalai Lama" : "The purpose of our lives is to be happy.",
    "Mae West" : "You only live once, but if you do it right, once is enough.",
    "Henry David Thoreau" :"Go confidently in the direction of your dreams! Live the life you've imagined.",
    "Confucius" :"Life is really simple, but we insist on making it complicated.",
    "Jonathan Swift" : "May you live all the days of your life.",
    "Hans Christian Andersen" : "Life itself is the most wonderful fairy tale.",
    "John Wooden" :  "Do not let making a living prevent you from making a life.",
    "D. H. Lawrence" :"Life is ours to be spent, not to be saved.",
    "Marilyn Monroe" :"Keep smiling, because life is a beautiful thing and there's so much to smile about.",
    "James M. Barrie" : "Life is a long lesson in humility.",
    "Robert Frost" : "In three words I can sum up everything I've learned about life: it goes on.",
    "Bob Marley" : "Love the life you live. Live the life you love.",
    "Charles Dickens" :  "Life is made of ever so many partings welded together.",
    "Ray Bradbury" :  "Life is trying things to see if they work." ,
    "Winston Churchill" : "Success is not final; failure is not fatal: It is the courage to continue that counts.",
    "Steve Jobs": "If you really look closely, most overnight successes took a long time.",
    "John D. Rockefeller" :"The secret of success is to do the common thing uncommonly well.",
    "Thomas Jefferson" :"I find that the harder I work, the more luck I seem to have.",
    "Barack Obama" : "The real test is not whether you avoid this failure, because you won't. It's whether you let it harden or shame you into inaction, or whether you learn from it; whether you choose to persevere.",
    "Zig Ziglar" : "Don't be distracted by criticism. Remember -- the only taste of success some people get is to take a bite out of you.",
    "Conrad Hilton" : "Success seems to be connected with action. Successful people keep moving. They make mistakes but they don't quit.",
    "Colin Powell" : "There are no secrets to success. It is the result of preparation, hard work, and learning from failure.",
    "Herman Melville" : "It is better to fail in originality than to succeed in imitation.",
    "Jim Rohn" :"Successful people do what unsuccessful people are not willing to do. Don't wish it were easier; wish you were better.",
    "James Cameron" : "If you set your goals ridiculously high and it's a failure, you will fail above everyone else's success.",
    "Steve Jobs" : "If you really look closely, most overnight successes took a long time.",
    "David Brinkley" : "A successful man is one who can lay a firm foundation with the bricks others have thrown at him.",
    "Albert Einstein" : "Try not to become a man of success. Rather become a man of value.",
    "John D. Rockefeller" : "Don't be afraid to give up the good to go for the great.",
    "Winston Churchill" : "Success is walking from failure to failure with no loss of enthusiasm.",
    "Thomas J. Watson" : "If you want to achieve excellence, you can get there today. As of this second, quit doing less-than-excellent work.",
    "Gurbaksh Chahal" : "If you genuinely want something, don't wait for it -- teach yourself to be impatient.",
    "Vidal Sassoon" : "The only place where success comes before work is in the dictionary.",
    "Alexander Graham Bell" : "Before anything else, preparation is the key to success.",
    "Wayne Gretzky" : "You miss 100% of the shots you don't take.",
    "Henry Ford" : "Whether you think you can or you think you can't, you're right.",
    "Rosa Parks": "I have learned over the years that when one's mind is made up, this diminishes fear.",
    "Mother Teresa" : "I alone cannot change the world, but I can cast a stone across the water to create many ripples.",
    "Audrey Hepburn" : "Nothing is impossible, the word itself says, ‘I'm possible!'",
    "Ayn Rand" : "The question isn't who is going to let me; it's who is going to stop me.",
    "Ralph Waldo Emerson" : "The only person you are destined to become is the person you decide to be.",
    "Theodore Roosevelt" : "Believe you can and you're halfway there.",
    "Maya Angelou" : "I've learned that people will forget what you said, people will forget what you did, but people will never forget how you made them feel.",
    "Vince Lombardi" : "Winning isn't everything, but wanting to win is.",
    "Amelia Earhart" : "The most difficult thing is the decision to act, the rest is merely tenacity.",
    "Socrates" : "An unexamined life is not worth living.",
    "George Addair" : "Everything you've ever wanted is on the other side of fear.",
    "Norman Vaughan" : "Dream big and dare to fail.",
    "Beverly Sills" : "You may be disappointed if you fail, but you are doomed if you don't try.",
    "Charles Swindoll" : "Life is 10% what happens to me and 90% of how I react to it.",
    "Les Brown" : "Too many of us are not living our dreams because we are living our fears.",
    "Benjamin Franklin" : "I didn't fail the test. I just found 100 ways to do it wrong.",
    "Sheryl Sandberg" : "If you're offered a seat on a rocket ship, don't ask what seat! Just get on.",
    "Florence Nightingale" : "I attribute my success to this: I never gave or took any excuse.",
    "Vincent van Gogh" : "I would rather die of passion than of boredom.",
    "Gloria Steinem": "Dreaming, after all, is a form of planning.",
    "Napolean Hill" : "Whatever the mind of man can conceive and believe, it can achieve.",
    "Aristotle" : "First, have a definite, clear practical ideal; a goal, an objective. Second, have the necessary means to achieve your ends; wisdom, money, materials, and methods. Third, adjust all your means to that end.",
    "Mark Twain" : "Twenty years from now you will be more disappointed by the things that you didn't do than by the ones you did do. So, throw off the bowlines, sail away from safe harbor, catch the trade winds in your sails. Explore, Dream, Discover.",
    "Mahatma Gandhi" : "Live as if you were to die tomorrow. Learn as if you were to live forever.",
    "Bernard M. Baruch" : "Be who you are and say what you feel, because those who mind don’t matter and those who matter don’t mind.",
    "Plato" : "Wise men speak because they have something to say; fools because they have to say something.",
    "Mahatma Gandhi" : "You must be the change you wish to see in the world.",
    "Martin Luther King Jr." : "Darkness cannot drive out darkness; only light can do that. Hate cannot drive out hate; only love can do that",
    "E.E Cummings" : "It takes courage to grow up and turn out to be who you really are.",
    "Leonardo Da Vinci": "As a well-spent day brings happy sleep, so a life well spent brings happy death.",
    "Herbert Hoover": "Children are our most valuable resource.",
    "J.K. Rowling" : "It takes a great deal of courage to stand up to your enemies, but even more to stand up to your friends.",
    "Frank Zappa" : "A mind is like a parachute. It doesn’t work if it isn’t open.",
    "Deepam Chatterjee" : "When you are totally at peace with yourself, nothing can shake you.",
    "Muhammad Ali" : "Peace comes from within. Do not seek it without.",
    "Andrew Hendrixson" : "Anyone who has ever made anything of importance was disciplined.",
    "Coco Chanel" : "Don’t spend time beating on a wall, hoping to transform it into a door.",
    "Billie Jean King": "Champions keep playing until they get it right.",
    "Neil Barringham" : "The grass is greener where you water it.",
    "Ernest Hemingway": "But man is not made for defeat. A man can be destroyed but not defeated.",
    "Indira Gandhi" : "You cannot shake hands with a clenched fist.",
    "Jane Austen" : "There is no charm equal to tenderness of heart.",
    "Edgar Allen Poe" : "All that we see or seem is but a dream within a dream.",
    "George Washington" : "It is far better to be alone, than to be in bad company.",
    "Thomas Carlyle" : "Permanence, perseverance and persistence in spite of all obstacles, discouragements, and impossibilities: It is this, that in all things distinguishes the strong soul from the weak.",
    "Sun Tzu" : "The supreme art of war is to subdue the enemy without fighting.",
    "Buddha" : "Do not dwell in the past, do not dream of the future, concentrate the mind on the present moment." 
}
        for i in range(1):
            authors, quotes = r.choice(list(quotesNAuthors.items()))
            self.quote.text = ' "' + quotes + ' " '
            self.author.text = " - " + authors
            return quotes, authors
        
        
    



if __name__ == '__main__':
    app = quotesApp()
    app.run()



