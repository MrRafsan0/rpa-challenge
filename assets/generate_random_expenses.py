# generate random expenses
import random
categories=["Food", "Transportation", "Entertainment", "Shopping", "Utilities", "Other"]
shops=['lidl', 'prisma', 'k-market', 'alepa', 's-market', 'asia', 'ikea', 'hesburger', 'theburger', 'kotipizza']
for i in range(20):
    day=random.randint(1,30)
    month=random.randint(8,11)
    amount=4+10*random.random()
    print(f'{day}/{month} {random.choice(shops)} {amount:.2f} {random.choice(categories).lower()}')
