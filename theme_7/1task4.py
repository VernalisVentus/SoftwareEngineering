import re

with open("input.txt", "r", encoding="utf-8") as f:
    banned_words = [line.strip() for line in f if line.strip()]

sentence = "Это плохое и запрещенное СЛОВО не стоит использовать"

pattern = r'\b(' + '|'.join(re.escape(word) for word in banned_words) + r')\b'
result = re.sub(pattern, lambda m: '*' * len(m.group()), sentence, flags=re.IGNORECASE)

print("Результат:")
print(result)