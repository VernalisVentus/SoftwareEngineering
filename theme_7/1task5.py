import random

movies = [
    "Форсаж",
    "Мстители",
    "Пираты Карибского моря",
    "Гарри Поттер",
    "Властелин колец",
    "Матрица",
    "Назад в будущее",
    "Терминатор",
    "Чужой",
    "Хищник"
]

with open("quotes.txt", "w", encoding="utf-8") as f:
    for movie in movies:
        f.write(movie + "\n")

with open("quotes.txt", "r", encoding="utf-8") as f:
    all_movies = f.readlines()
    random_movie = random.choice(all_movies).strip()

print("Случайный фильм для просмотра:")
print(random_movie)