items=input('enter words with inputed sequence of characters')
words=[word for word in items.split(",")]
print(",".join(sorted(list(set(words)))))