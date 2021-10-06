import pandas as pd


# set
A = {
    'א' : 'יתגבר כארי',
    'ב' : 'יקום בזריזות',
    'ג' : 'מודה אני',
    'ד' : 'ישים אמונה על הלב',
    'ה' : 'לא להתבייש מהמלעיגים',
    'ו' : 'להצניע מעשים טובים',
    'ז' : 'נטילה',
    'ח' : 'אם גם בלילה',

}

Prepared_Table = list(zip(A))
Prepared_Table

df = pd.DataFrame(data = Prepared_Table, columns=['A','A[0]'])
df.columns = ['א']

print(df)
