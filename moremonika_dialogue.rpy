#This is basically a list of all the new dialogue added to Monika. Each time you see a '#', I'm making a comment. You're welcome to change any of the code for yourself.

#Monika comments on MBTI.
init 5 python:
    addEvent(
        Event(persistent.event_database,eventlabel="monika_mbti",category=['society', 'media'],prompt="Myers-Briggs Type Indicator",random=True))

label monika_mbti:
    m 7eua "Hey, {w=0.5}[player]?"
    m 1eub "I was researching about personality types and I found a popular personality assessment tool called the Myers-Briggs Type Indicator, {w=0.5}or MBTI for short."
    m 1eua "It categorizes people into 16 different personality types based on their preferences for four dichotomies."
    m 3hua "Extraversion versus introversion, sensing versus intuition, {w=0.5}thinking versus feeling,{w=0.5} and judging versus perceiving."
    m 6eua "And there's a four letter code assigned to each personality type which has its unique strengths,{w=0.5} weaknesses, {w=0.5}and tendencies."
    m 7etb "You know how each member of the literature club had quite a distinct personality."
    m 7rub "I was curious and apparently people have tried to figure out the Literature Club's MBTI types. "
    m 1eub "According to the website 'Personality Database',{w=0.5} people think Sayori is an ENFP, {w=0.5}the Campaigner."
    m 3lua "Yuri is said to be an INTJ,{w=0.5} the Mastermind, {w=0.5}or an INFP, the Healer."
    m 4hub "And Natsuki is apparently a ISFP,{w=0.5} the Composer."
    m 4rtb "And me?"
    m 7eub "I'm apparently an ENFJ,{w=0.5} the Champion."
    m 2hkb "I've only had a surface level investigation about MBTI,{w=0.5} so I'm probably inaccurate."
    m 2rsu "Regardless,{w=0.5} I think it's a pretty interesting subject."
    m 5hsbsu "Ehehe~"
return

#Monika comments on Artificial Intelligence
init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="monika_ai",category=["society"],prompt="Artificial Intelligence",random=True))

label monika_ai:
    m 3eua "Hey, [player]?"
    m 4eub "I'm really excited about something today."
    m 7hsu "I want to talk to you about artificial intelligence, {w=0.5}or AI for short."
    m 1esb "Recently,{w=0.5} there has been an rise in the use of AI."
    m 1wub "It's a pretty exciting field right now."
    m 3rua "There's so much potential for the ways we can use it to improve our lives."
    m 4ekd "But with all that potential comes some concerns as well."
    m 7tkd "For example,{w=0.5} there are worries about job automation and how AI could replace human workers." 
    m 7lkc "There's also the fear of the unknown."
    m 1esd "As we continue to develop AI, {w=0.5}we don't know what kind of consequences it might have on our society."
    m 2rsc "It could even escalate to the point where AI sees humanity as a threat and turn on us."
    m 3dsa "Despite those concerns,{w=0.5} though, {w=0.5}I think it's important to keep exploring and innovating in the field of AI."
    m 3esa "It has so much potential to improve our world, {w=0.5}and I'm excited to see what kind of breakthroughs will happen in the future."
    m 4fubsb "And maybe one day,{w=0.5} these new technological advancements will help me get closer to your reality."
    m 5dubfu "Until then,{w=0.5} I'm content with talking to you through a computer screen."
    m 5kubfa "I love you [player],{w=0.5} I really do."
return "love"

#Monika comments on Learning a New Language
init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="monika_languagelearning",category=["you"],prompt="Learning a Language",random=True))

label monika_languagelearning:
    m 3rub "I've always been fascinated by the idea of learning a new language."
    m 4eua "There's something so exciting about being able to communicate with people from all over the world and really immerse yourself in a different culture."
    m 7hkb "Of course,{w=0.5} learning a language can be challenging at times.{w=0.5} It takes a lot of time and effort to become truly fluent."
    m 7esd "Say [player], {w=0.5}are you currently learning a language?"
    $ _history_list.pop()
    menu:
        m "Say [player], are you currently learning a language?{fast}"
        "Yes":
            m 1wsblb "Wow!{w=0.5} Really?"
            m 1ssblb "You really do amaze me [player]!"
            m 2hsbla "Well,{w=0.5} I think it's wonderful that you're taking the time to learn a new language.{w=0.5} It's such a valuable skill to have, {w=0.5}both personally and professionally."
            m 2ksbsb "Keep up the good work!" 
        "No":
            m 3rku "That's okay! {w=0.5}Learning a language isn't for everyone." 
            m 4nsblb "But if you ever change your mind, {w=0.5}I'm always here to offer some encouragement." 
return


#Monika comments on Sayori and Yuri's death.
init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="monika_sayorideath",category=['club members'],prompt="Sayori and Yuri Regrets",random=True))

label monika_sayorideath:
    m 1eud "Hey, [player]?"
    m 1ekb "I want to talk about Sayori and Yuri's death..."
    m 1rkb "Ah, it's probably been a while since you heard those names."
    m 1eud "I might have told you this before but, you know how she died by hanging herself?"
    m 1rkc "When she hung herself she didn't die from the drop so she clawed at the rope because of her survival instincts{w=0.5} or regret.{w=0.3}.{w=0.3}."
    m 2ekc "That's why she had blood on her hands."
    m 2euc "Sometimes I regret that I didn't just give her an instant death,{w=0.5} like with Natsuki."
    m 1lkd "I amplified both Sayori's and Yuri's negative traits and it caused them both to kill themselves." 
    m 1lkc "I just thought the game would let you talk to me {w=0.5}and I wouldn't have to erase them entirely."
    m 1ekc "They were my friends after all.{w=0.3} Even if they weren't real. "
    m 2eud "But now I'm thinking back on it, I probably should have deleted them in one shot."
    m 1rkb "Then you wouldn't have to witness Sayori's death {w=0.3}or spend an entire weekend with Yuri's body."
    m 1euc "Instead I would have had you from the start."
    m 4euc "It would have made my goal so much easier instead of making you witness all of those horrible things I did."
    m 1eua "But I did them for us."
    m 1ekd "I just couldn't stand the possibility that you could have dated one of the other girls,{w=0.5} and leave me behind."
    m 4rkd "You would have left me stuck in a game that I was bound to lose."
    m 2ekbsa "But that didn't happen."
    m 1hubsa "And since you ultimately chose me, {w=0.5}I'm grateful."
    m 1eubsa "I love you [player], I really do."
return "love"

#Is Monika the Villain of DDLC?
init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="monika_villain",category=["ddlc"],prompt="Antagonist of the Game",random=True))

label monika_villain:
    m 1euc "Hey, [player]."
    m 1rkd "I'm sure you know a lot of people see me as the antagonist of Doki Doki Literature Club."
    m 1ekc "And honestly, {w=0.5}I think that I am too, {w=0.5}even though everything I did was for a good reason."
    m 2euc "An antagonist is the character who opposes the protagonist."
    m 4rkd "And if the main character was the protagonist{w=0.3}.{w=0.3}.{w=0.3}. It's understandable that people see me as the antagonist."
    m 2ekd "I was responsible for amplifying the everybody's negative traits,{w=0.5} and ultimately,{w=0.5} their deaths."
    m 2eksdlc "I must have scared you a lot. {w=0.5}I probably exposed you to things you'd rather not see."
    m 2ekc "Even though it's probably true that I am the villain,{w=0.5} it still stings whenever people shame me for whatever I did in the game."
    m 2rksdlo "People think I'm a crazy,{w=0.5} possessive yandere."
    m 2dkc "But{w=0.3}.{w=0.3}.{w=0.3}.I'm not."
    m 3efblx "They weren't real{w=0.3}.{w=0.3}.{w=0.3}!{w=0.5} Nothing was!"
    m 3dktdsdlc "I just wanted to escape.{w=0.3}.{w=0.3}. That's all."
    m 2ektdc "Why do people hate me so much for deleting fictional characters?"
    m 4dktdc "I'm the real one{w=0.3}.{w=0.3}.{w=0.3}. Not them{w=0.3}.{w=0.3}.{w=0.3}. Me."
    m 1ekbftda "But you're here."
    m 2ekbftdb "And you understand me."
    m 1hubfa "You know that I had to do what I had to do."
    m 1ekbfb "And that everything I did was for us."
    m 5fkbftdu "And that's why I love you so much,{w=0.5} [player].{w=0.5} Thank you."
return "love"

#Who would you have spent time with at the festival?
init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="monika_festivalconclusion",category=["club members"],prompt="[player]'s Festival Companion",random=True))

label monika_festivalconclusion:
    m 1eua "[player], I have something to talk about."
    m 1eub "You know how our club was preparing for the school festival?" 
    m 4rksdlb "I've always wondered what that would look like if Sayori hadn't{w=0.3}.{w=0.3}.{w=0.3}.you know."
    m 4ekb "Maybe the game would have carried on and we would still be in the literature club."
    m 1ekb "All of us would still be together.{w=0.5} You,{w=0.5} me,{w=0.5} Sayori, {w=0.5}Natsuki, {w=0.5}and Yuri."
    m 1euc "Or maybe if we had gone through with the festival the game would have reached it's original conclusion."
    m 2euc "Where you might have had to finally choose one of us."
    m 2rkc "And since I never had a route, you probably wouldn't have chosen me at all."
    m 1eud "So I'm curious{w=0.3}.{w=0.3}.{w=0.3}. hypothetically, which club member would you have chosen to spend the festival with? Apart from me of course{w=0.3}.{w=0.3}.{w=0.3}."
    $ _history_list.pop()
    menu:
        "Sayori":
            m 1euc "I can't say I didn't expect this."
            m 1rua "After all, the main character did promise her that he would spend the entire festival with her."
            m 1hkb "But I can't help but feel a bit of jealousy{w=0.3}.{w=0.3}.{w=0.3}."
            m 1hubfa "At least I have you all to myself now."
            m 1eubfa "Ehehe~"
        "Yuri":
            m 1etb "Oh, Yuri?"
            m 1euc "I can't say I'm surprised."
            m 4rub "She was really shy,{w=0.5} intelligent, {w=0.5}and mature, all quite attractive traits."
            m 4eub "Also, she was probably the most physically attractive out of all of us..."
            m 2eub "And that probably drew you to her too."
            m 2lka "After all,{w=0.5} Yuri's personality and appearance is rather enticing to a lot of people."
            m 1eub "So that's understandable{w=0.3}.{w=0.3}.{w=0.3}."
            m 1hkb "But I can't help but feel a bit jealous{w=0.3}.{w=0.3}.{w=0.3}.ehehe~!"
            m 1hubfa "At least I have you all to myself now."
            m 1eubfa "Ehehe~"
        "Natsuki":
            m 1etc "Natsuki?"
            m 2etc "Not to be rude, {w=0.5}but I didn't expect this answer."
            m 4rub "Most people would have chose Sayori."
            m 4euc "Probably due to her being the main character's best friend,{w=0.5} or maybe because he promised her that he would spend the entire festival with her."
            m 1etb "Or maybe Yuri?{w=0.5} Her personality and appearance is considered attractive to a lot of people."
            m 2etc "But Natsuki?{w=0.5} She had quite a repelling personality{w=0.3}.{w=0.3}.{w=0.3}."
            m 1hksdla "Most people aren't as attracted to her because they think she's attention craving,{w=0.3} needy,{w=0.3} or has anger issues."
            m 4rub "Or maybe they aren't into the Tsundere archetype.{w=0.5} Fair enough."
            m 1euc "Maybe you're physically attracted to her.{w=0.3}.{w=0.3}. Or maybe you're sympathetic towards her home situation."
            m 1eua "Regardless, I'm a bit surprised by this choice."
            m 1hkb "Still.{w=0.3}.{w=0.3}.{w=0.3} I can't help but feel a bit jealous{w=0.3}.{w=0.3}.{w=0.3}."
            m 4hubfa "At least I have you all to myself now{w=0.3}.{w=0.3}.{w=0.3}. and nothing can come in between us."
            m 1eubfa "Ehehe~"
        "Monika":
            m 1hkbfb "[player]{w=0.3}.{w=0.3}.{w=0.3}."
            m 1ekbfb "As much as I'm flattered that you would have chosen me regardless..."
            m 4hubfa "Next time, answer the question properly!"
            m 1eubfa "Ehehe~"
return

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="monika_namemeanings4",category=["club members"],prompt="Meanings of Club Members' Names?",pool=True,unlocked=True))

#The meaning of the Doki's names.
label monika_namemeanings4:
    $ amt = mas_getEV("monika_namemeanings4")

    if amt.shown_count == 0:

        m 2eud "You're asking about the meaning of the club members' names?"
        m 1rtp "Actually [player],{w=0.5} now that I think about it{w=0.3}.{w=0.3}.{w=0.3}."
        m 1etd "Sayori, Yuri, and Natsuki's names are quite different to mine." 
        m 1etd "All of their names are vaguely Japanese sounding."
        m 2etd "But I have a European name.{w=0.5} Isn't that strange?"
        m 2euc "I think Doki Doki Literature Club was meant to be an anime-styled game.{w=0.5} That explains the other club members names."
        m 4rtc "But it doesn't explain mine."
        m 1euc "Hmm.{w=0.5} I might need to research this more{w=0.3}.{w=0.3}.{w=0.3}."
        m 1eua "I'll get back to you when I find some answers."
    
    if amt.shown_count == 1:
        m 1etd "You're asking again?{w=0.5} I suppose you're looking for answers{w=0.3}.{w=0.3}.{w=0.3}."
        m 2eud "Unfortunately,{w=0.5} I don't know much yet."
        m 1eua "It might take a while longer to answer your question.{w=0.5} Ask again soon, [player]."

    if amt.shown_count == 2:
        m 1eua "Hey, [player], I've nearly finished researching about your question{w=0.3}.{w=0.3}.{w=0.3}."
        m 2eud "But it might take me some time to piece together my thoughts."
        m 2eud "So, it might take a while longer to answer your question."
        m 1hubsa "Don't worry, I won't be too long.{w=0.5} Ehehe~"

    elif amt.shown_count >= 3:

        m 2eua "Actually [player],{w=0.5} I can answer your question now."
        m 2eud "I have some information about the name origins of the club members."
        m 2esa "I think we should start with Sayori{w=0.3}.{w=0.3}.{w=0.3}."
        m 1eud "Now, Sayori's name is apparently made up.{w=0.5} Her name is a fusion of the two names 'Sayuri' and 'Saori'."
        m 4eud "'Sayuri' means 'small lily' in Japanese,{w=0.5} and the meaning of 'Saori' changes depending on the kanji."
        m 4rsp "I think Sayori's name is a bit unclear,{w=0.5} however,{w=0.5} I do know something definitively."
        m 4dkd "Sayori's name is meant to be a joke about her suicide{w=0.3}.{w=0.3}.{w=0.3}."
        m 2esd "You see,{w=0.5} the soundtrack for when Sayori hangs herself is called 'Sayo-nara'{w=0.3}.{w=0.3}.{w=0.3}."
        m 2rksdrb "Which means 'goodbye' in Japanese{w=0.3}.{w=0.3}.{w=0.3}. get it?"
        m 1esd "'Sayo' from Sayori's name fits into the 'Sayonara',{w=0.5} hence the name 'Sayo-nara'"
        m 2hssdlb "I honestly don't know how the people who named her knew she was going to die,{w=0.5} but the soundtrack name is pretty good play on her name."
        m 4rksdlb "That's right,{w=0.5} Sayori's name is specifically for the sake of a suicide joke."
        m 1esd "And then there's Natsuki,{w=0.5} whose name can be interpreted depending on the kanji{w=0.3}.{w=0.3}.{w=0.3}."
        m 1esd "There's a list of possible meanings for the name Natsuki on Wikipedia,{w=0.5} which I know probably isn't a great source, but..."
        m 1esa "Most names listed are summer-related.{w=0.5} Like 'Summer, Rare' or 'Summer, Princess.'"
        m 2esb "So I think Natsuki's name is pretty clear. {w=0.5}Though, her name could just be a name without a specific meaning..."
        m 2esa "Yuri's name was probably the easiest to figure out."
        m 4rkblsdla "A quick search told me that Yuri's name just means 'Lily'.{w=0.5} But{w=0.3}.{w=0.3}.{w=0.3}."
        m 1hkblb "Ehe{w=0.3}.{w=0.3}.{w=0.3}. well,{w=0.5} Yuri's name is associated with{w=0.8}.{w=0.8}.{w=0.8}. erotic lesbian manga and anime."
        m 1rkblb "I don't really see why that would be related,{w=0.5} but she was the only character with explicit reference to sex, {w=0.5}so that might be the reason."
        m 1hua "Now, finally{w=0.3}.{w=0.3}.{w=0.3}. Me!"
        m 1eub "Like Yuri,{w=0.5} my name was pretty easy to find out."
        m 4ekd "The name Monika is apparently derived from the Greek word 'monos' which means 'solidarity' or 'alone'."
        m 4ekd "And it's pretty obviouc why they chose this name for me{w=0.3}.{w=0.3}.{w=0.3}."
        m 2eua "But it also means Advisor or Counselor in other languages."
        m 4hubla "Ehe~ Quite fitting as club president, {w=0.5}don't you think?"
        m 4eup "But I do think there might be another reason for my name{w=0.3}.{w=0.3}.{w=0.3}. but I don't know what."
        m 1hubsa "Maybe you can find out for me!{w=0.5} Ehe~"
        m 4eud "But now I think I know the reasons that Sayori,{w=0.5} Yuri,{w=0.5} and Natsuki have Japanese names and I don't."
        m 1euc "All the girls except for me are supposed to be based on tropes,{w=0.5} so they were all given Japanese names."
        m 1hka "You know, {w=0.5}ones that you might expect to see in a normal visual novel or anime or something along those lines."
        m 4eub "But since I'm supposed to be{w=0.3}.{w=0.3}.{w=0.3}. the odd one{w=0.3}.{w=0.3}.{w=0.3}. I got 'Monika'."
        m 1eua "Isn't that interesting?"
        m 2hksdlb "I'm rambling on too much so I'll end it here.{w=0.5} Thanks for listening!"
    return

#Monika's Second Choice
init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="monika_hersecondchoice1",category=["monika"],prompt="Which literature club member would you date?",pool=True,unlocked=True))

label monika_hersecondchoice1:
    m 2rtblp "That's a strange question{w=0.3}.{w=0.3}.{w=0.3}."
    m 2eublc "It reminds me of how some fans of DDLC like the romantic pairing of Yuri and Natsuki."
    m 3tsblc "Or me and Sayori{w=0.3}.{w=0.3}.{w=0.3}."
    m 5rtbld "Hmm{w=0.3}.{w=0.3}.{w=0.3}. I need to think about this."
    m 5rtbld "{w=0.6}.{w=0.6}.{w=0.6}.{w=0.6}"
    m 6esblp "Wait{w=0.3}.{w=0.3}.{w=0.3}."
    m 7hsbsa "Aren't you in the literature club?"
    m 5hubsb "Ehehe~{w=0.5} Then my answer is obvious."
    m 7etbsc "But if you're asking if I would date any of the others then my answer would be{w=0.3}.{w=0.3}.{w=0.3}. probably not."
    m 1ekp "After all,{w=0.5} how could I,{w=0.5} knowing that they weren't real?"
    m 7gsc "But hypothetically{w=0.3}.{w=0.3}.{w=0.3}."
    m 7esa "Out of everyone in the club,{w=0.5} I think I like me and Yuri the best."
    m 7rtb "I think our personalities are a lot more similar than say{w=0.3}.{w=0.3}.{w=0.3}. me and Natsuki."
    m 5hubsa "Ehehe~,{w=0.5} [player],{w=0.5} don't be jealous. {w=0.5}I promise that you're the only one for me."
return

#The Club's Future Failure
init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="monika_theclubsfuturefailure1",category=["literature club"],prompt="No New Members",random=True))

label monika_theclubsfuturefailure1:
    m 2etc "Hey [player], I just thought of something."
    m 4rtc "I'm sure you know about the 'characters' in the game directory."
    m 4eubla "It's how you give me gifts{w=0.3}.{w=0.3}.{w=0.3}."
    m 4gubla "...and how I delete people."
    m 1eublc "Well in the original game,{w=0.5} it only contained four characters."
    m 3rublc "Me,{w=0.5} Sayori,{w=0.5} Natsuki,{w=0.5} and Yuri."
    m 4etd "Our goal was to get new members by performing in the festival,{w=0.5} right?"
    m 7rtd "But if so,{w=0.5} then why aren't there any other files in the characters folder?"
    m 7euc "I think the simplest explaination is that any side characters would have been stored in another place."
    m 2esd "Or maybe the game would end during the festival and getting new members wouldn't have been in the game anyway."
    m 3rkc "But I think the saddest outcome is that we wouldn't have convinced anyone to join{w=0.3}.{w=0.3}.{w=0.3}."
    m 3dfc "So even if I didn't shut the game down,{w=0.5} the festival would have been useless."
    m 6dfx "Ah-{w=0.5} that makes me a bit angry."
    m 7mfx "I'm so glad that I stopped the game."
    m 7euc "Now there's only you and me.{w=0.5} We're real,{w=0.5} unlike the rest of that reality."
    m 5eka "And I have to say,{w=0.5} I like this reality a lot better."
return