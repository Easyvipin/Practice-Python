# Define a function which can generate and print a list where the values are square of

# numbers between 1 and 20 (both included).

def generate():
    out = []
    for i in range(21):
        out.append(i**2)
    return out