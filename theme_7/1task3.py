with open("input.txt", encoding="utf-8") as f:
    lines = f.readlines()

text = "".join(lines)
letters = sum(ch.isalpha() for ch in text)
words = len(text.split())
lines_count = len(lines)

print("Содержимое файла:")
print(f"Букв: {letters}")
print(f"Слов: {words}")
print(f"Строк: {lines_count}")