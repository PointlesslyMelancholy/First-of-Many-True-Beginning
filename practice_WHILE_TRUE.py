wherever = ''
proceed = False

while True:
    wherever = input('> ').upper()

    if wherever == 'HELP':
        print('''
Last thing you heard before your throat dried and the final leaf fell off your favorite tree was leave.
You are leaving HOME. You can see the HORIZON in the distant. Where the husks seem to stare towards the sea.
In a small neighborhood, the sunset looks so nice to stare out and sit at the edge of the CLIFF.
To your left, the STREETS which makes you feel lonely whenever walking here. To your right, the BARN where many stay to forever leave your life.
Don't ask about the kids. Where will you go? 
''')
        
    elif wherever == 'HOME':
        if not proceed:
            print('You can\'t go home again. They keep scratching and clawing at you. You can feel them staring at everything wrong with you.')
        else:
            proceed = True
            print('Why are you going back. Don\'t mention HOME. Don\'t try to GO HOME.')
    elif wherever == 'GO HOME':
        print('You decided to GO HOME. You decided to GO HOME. You decIded to GO HOME. what did I say... DON\'T TRY TO GO HOME.')
        print('''
Alas, home is here. Home is there. Wherever you go, it is there. There, you decided to stay home. There, you forgot to live and dream.
There, you went inside, drowned out your worse thoughts and dreads. The eyes stared as you walked by theIr quiet gaze of disappointment. No one speaks but everyone knows.
I tried to make you dream or reach towards the HORIZON towards
another ending. You sat on your prison, the sun gleams softly through the shut curtains. Unlike the world, you went to sleep and Never woke up.
''')
        break
    
    elif wherever == 'STREETS':
        if proceed:
            print('Choices have been made. You\'ve been taught this, stay the course. I don\'t like to chase you to find somewhere better.')
        else:
            proceed = True
            print('What a wonderful day, without conTradiction and... and other things.... don\'t look back, I mean it. Just CONTINUE TO THE TREE.')
    elif wherever == 'CONTINUE TO THE TREE':
        print('''
One foot in front of the other. The tree might be scary but remember when you looked at the sunset? When your childhood was as blissful as it can be in the warm gaze of the impartial world.
One foot in front of the other. It's okay to mourn such a delicate world of innocence. Yes, the world is cruel but take a seat.
Let tHe leaves fall around you, let the tears from the past flow in this present. Let us be for now, I am here, little one.
May you be able to dream once more.
''')
        break
    
    elif wherever == 'HORIZON':
        if proceed:
            print('Choices have been made. Be content with the choices you\'ve made. After all, stay the course.')
        else:
            proceed = True
            print('We leave for the horizon littered with shells of dreams, and a dEad generation.')
            
            print('Can we finally FADE away and dream the world away and let every pointless, sad thing drift away to the HORIZON from whence we came from?')
    elif wherever == 'FADE':
        print('''
As we fade away at the spot where the sun somberly caresses your face, I\'ll cease to be. As you sink into the wet sand with every wave crashing against you, taking more of your tragic essence;
You\'ll forget to dream forevermore, little one, among the rest who stare off... to worlds without substance because you were enough, just as you were now....
What a sad and beautiful day to have such a nice sunset which will never remember how to caress or exist as one with you.
''')
        break

    elif wherever == 'CLIFF':
        if proceed:
            print('Where will you go when that route is so near yet so far from grasping at it. Stay the course.')
        else:
            proceed = True
            print('As those thoughts flood your head, the people continue to walk past and your hands continue to tremble at the thought of the Moon simply gazing at your torment.')
            print('In those cases, one brief respite in all of the drowning, was to let your thoughts and feelings leak through your hands. Just CRY. Let everything flow.')
    elif wherever == 'CRY':
        print('''
As you make your way to the top of the cliff side, among the fictional Lunar Tears, you place your hand on the bench as you steady yourself to sit.
The waves crash below, the sunset looming behind you, quietly beckoning to say goodbye for today. For today and forever it might want since it's aware of your choice today. Finally, you let
Those tears fall on to the ground below, sprouting roots from each drop of exhausted, husk of an alien, yet tragic, familiar childhood. Let everything out.
Aren't you tired of everything making you exist in a world that can't even hold you? Become everything that this current world says not to be. Become rOoted to the world, watch as the seasons
becoming the monotonous change of everything. I will, watch over you. Like I always have and forever until the Sun becomes ever so bright for this world.
''')
        print('Here you sit, the roots wrap around you without resistance. Branches sprout from your aching heart. People pass by, admiring your testament to forever wait for that one day.')
        print('That one day where the world embraces you once more. So, now, I\'ll wait with you. Watch over you while look for the sunrise.')
        print('Never sleeping yet always dreaMing of seeing that Sun set in that good day. While the world passes by behind you.')
        break

    elif wherever == 'BARN':
        if proceed:
            print('The odd farmer keEps staying right beside the bright, red barn. Wondering why you keep contempletating on moving to another location when it doesn\'t matter.')
            print('Stay the course echoes in your head.')
        else:
            proceed = True
            print('''
While the street seem to beckon for your true feelings to escape that shell of yours, you seem drawn to continue to the barn where the odd, yet friendly old man greets you.
Just a simple hand wave. You sense he\'s waiting for a question about the kids perhaps? Maybe about his seemingly innocous BARN? Something glimmers from within but first,
where will your curiosity beckoN you to ask? INQUIRE about the barn or the KIDS?
''')
    elif wherever == 'INQUIRE':
        print('''
You approach the elderly man, you notice there has never been a house beside the barn. There is no man, there is only a figure with no face yet expressive absence of features.
The town before you bleeds into the darkness and stars that surround this barn. This innocous barn keeps drawing your gaze.
The figure speaks, "I know what pains you... others come and never leave their fantastical worlds... I oversee such peculiar lands and this one is no different...."
His voice is ethereal and speaks only in truth.
"You need not speak... you chose this route this time... either curiosity begged to be scratched... or you finally wish to see what the mind can create without any limitations...."

He opens the barn, there is a hole that leads to nowhere except to where your mind desires. Your hand twitches at a scent you can only recognize. Your eyes see the darkness yet perceive so
many wishes granted and limitations surpassed. How wonderful for you. You step into the dark as you let it envelop your whole being. There are no tears shed, there is no ill sensations felt
and it doesn't confuse you as many things do. In the warmth and a blanket of amazing bliss among the imaginations of many, you continue forward the never-ending cave.
''')
        print('The figure is delighted to bring another being into a world full of sweet nothings.')
        print('It\'s okay, little one, but you ran away in the truest sense. How long will you run towards a future where nothing is real?')
        break

    elif wherever == 'KIDS':
        print('The old man\'s eyes noticeably become piTch black. Last thing you hear is your own screaming before everything... goes....')
        break

    elif wherever == 'IN THE MOMENT':
        print('''
Despite the endings, despite it all happening and none occuring all at once, you decide to be in the moment.
You walk past all these endings that could've happened. Some good and some worse. However, all could be up in the air since all happened and none existed. A world that could be
and can never be still happened yet here you are. Listening to the town, listening to the sirens blaring among the music of life all the while the sunset and oncoming bliss of the night
is soon to guide you to view of the stars. Everything could be happening all at once, but here you are in the moment. The world is grim but the stars shine so brightly tonight
while the moon makes all the shadows dissipate into nothingness. Sleep comes for you and with a deep breath, with all sensation leaving your body, and everything around you becomes steady and warm.
As you close your eyes in the middle of wherever safe is for you, you repeat to yourself, 'It's okay to be here, it's okay to live. I just want to live. Since I am enough.'
''')
        print('May you find peace in the waking world.')
        break
