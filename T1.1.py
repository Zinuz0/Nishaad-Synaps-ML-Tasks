Kevin = {"Halsey", "Taylor Swift", "Mitski", "Joji", "Shawn Mendes", "Sabrina Carpenter", "Nicky Minaj", "Conan Gray","One Direction","Justin Beiber"}

Stuart = {"Kendirck Lamar","Steve Lacy","Tyler the Creator","Joji","TheWeeknd","Coldplay","Kanye West","Travis Scott","Frank Ocean","Brent Faiyaz"}

Bob = {"Conan Gray", "Joji", "Dove Cameron", "Mitski", "Arctic Monkeys", "Steve Lacy", "Kendrick Lamar", "Isabel LaRosa", "Shawn Mendes", "Coldplay"}

Edith = {"Metallica", "Billie Eilish", "TheWeeknd", "Mitski", "NF", "Conan Gray", "Kendrick Lamar", "Nicky Minaj", "Kanye West", "Coldplay"}

set1 = Kevin.intersection(Stuart)
set2 = Kevin.intersection(Bob)
set3 = Kevin.intersection(Edith)
set4 = Stuart.intersection(Bob)
set5 = Stuart.intersection(Edith)
set6 = Bob.intersection(Edith)

print(len(set1))
print(len(set2))
print(len(set3))
print(len(set4))
print(len(set5))
print(len(set6))

