import pandas as pd


# darkwebset
title = ["Mail2Tor", "FacebookOnion", "SciHub", "TheDarkLiar", "HiddenAnswers"]

links = ['http://mail2tor2zyjdctd.onion/',
           'https://www.facebookcorewwwi.onion/',
           'http://scihub22266oqcxt.onion/',
           'http://vrimutd6so6a565x.onion/index.php/Board',
           'http://answerszuvs3gg2l64e6hmnryudl5zgrmwm3vh65hzszdghblddvfiqd.onion/']
desc = ["send/receive messages anonymously",  "access from restricted countries.",
        "acquiring scientific knowledge", " image hosting platform and evolved into a social network",
        "Quora of the dark web "]


darkweb = list(zip(title,links, desc))
darkweb

df = pd.DataFrame(data = darkweb, columns=['title', 'desc', 'links'])
df.columns = ['title', 'desc', 'links']

print(df)


