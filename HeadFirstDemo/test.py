from HeadFirstDemo.demomain import load_data

file_list = ['james.txt', 'julie.txt', 'mikey.txt', 'sarah.txt']
athlete_dict = load_data(file_list)

print(athlete_dict['Julie Jones'].top3())
print(athlete_dict['James Lee'].top3())

