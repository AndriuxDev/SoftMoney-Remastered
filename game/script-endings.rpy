label ending1: 
    scene black with dissolve
    pause 1.0
    scene bg end1 with dissolve
    "Satisfied, you get into your car. Now you have enough money to pay for the surgery."
    "Harvey waved at you, and smiling, said goodbye as you drove away."
    "Who could have known that one random encounter today would bring so many emotions?"
    "Relieved, you headed to the hospital, ready to face whatever came next."
    scene black with fade
    stop music fadeout 1.0
    $ ending1.grant()
    pause 1.0
    "Thank you for playing SoftMoney Remastered."
    "We hope you enjoyed the experience."
    "Want a better ending? Maybe hugging Harvey would help."
    window hide
    pause 3.0
    return

label ending2:
    scene black with dissolve
    stop music fadeout 1.0
    pause 1.0
    play music t4
    scene bg end1 with dissolve
    "Satisfied, you get into your car. Now you have enough money to pay for the surgery."
    "Harvey awkwardly waved goodbye, and with a smile, you drove away."
    "It seemed like he wanted to tell you something important, but couldn’t bring himself to say it."
    "Relieved, you headed to the hospital, ready to face whatever came next."
    scene black with fade
    stop music fadeout 1.0
    $ ending2.grant()
    pause 1.0
    "Thank you for playing SoftMoney Remastered..."
    "Thanks for stopping by..."
    "Want a better ending? Perhaps a comb would make Harvey's day."
    window hide
    pause 3.0
    return

label ending3:
    scene black with dissolve
    pause 1.0
    scene bg end2 with dissolve
    "In a rush, you get into your car. How could you give him all your money?"
    "A mix of relief and guilt washes over you—relief that you can now afford the surgery, guilt over the mysterious circumstances."
    "Before Harvey could stop you, you drove away."
    "You couldn\'t sleep all night, thinking about what drove you and your actions today."
    scene black with fade
    pause 1.0
    scene bg end4 with dissolve
    "In the morning, you wake up to a call from your doctor."
    d "Good news, [player]!"
    d "Your treatment has been fully paid for. The person who paid for your surgery wished to remain anonymous."
    "You felt a wave of gratitude and curiosity. An anonymous benefactor? But who could it be?"
    "You thought about Harvey and wondered if he was involved."
    scene black with fade
    pause 3.0
    play music birbs fadein 3.0
    pause 3.0
    "The next morning, you went to Harvey's address to thank him."
    "You even brought a small gift as a token of your appreciation."
    scene bg end5 with dissolve
    "You knocked on the door, but there was no answer."
    player "..."
    scene bg end7
    play audio doorbell
    "With shyness and excitement mixing in your heart, you decided to press on the doorbell."
    scene bg end5
    pause 2.0
    h2 "Hello? Who is it?"
    player "It's me, [player]! I just wanted to thank you for everything."
    h2 "Coming!"
    "You were ready to express your gratitude when the door swung open."
    scene black with fade
    stop music fadeout 1.0
    $ ending3.grant()
    pause 3.0
    "Thank you for playing SoftMoney Remastered!"
    "We hope you enjoyed the experience."
    "AndriuxDev thanks you for your support!"
    "Check out the original {a=https://paper-pepper.itch.io/softmoney}SoftMoney{/a} on Itch.io!"
    "And while you're at it, maybe give {a=https://shroomychrist-studios.itch.io/bloodmoney}BloodMoney{/a} and {a=https://buwu3.itch.io/llllollll}LoveMoney{/a} a try too?"
    "Who knows, maybe you'll enjoy those experiences as well!"
    window hide
    pause 3.0
    return