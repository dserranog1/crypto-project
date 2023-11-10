from transformers import pipeline
import time

pipe = pipeline("text-classification", model="./model.save")

text = "sdlkhfkwsdfkwejfkwehfkwhef"

print(f"Texto: {text}")
start = time.time()
print(pipe(text))
stop = time.time()

print(f"Elapsed time: {stop - start}")

text = "Esto no es un texto cifrado"

print(f"Texto: {text}")
start = time.time()
print(pipe(text))
stop = time.time()

print(f"Elapsed time: {stop - start}")

text = "This is not a key"

print(f"Texto: {text}")
start = time.time()
print(pipe(text))
stop = time.time()

print(f"Elapsed time: {stop - start}")

text = "Das ist keine Schlüssel"

print(f"Texto: {text}")
start = time.time()
print(pipe(text))
stop = time.time()

print(f"Elapsed time: {stop - start}")