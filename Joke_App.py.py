import tkinter as tk
import requests

def get_joke():
    url = "https://v2.jokeapi.dev/joke/Any"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data["type"] == "single":
                joke_text.set(data["joke"])
            else:
                joke_text.set(f"{data['setup']} \n\n{data['delivery']}")
        else:
            joke_text.set("Error fetching joke.")
    except Exception as e:
        joke_text.set(f"Error: {e}")

# Crear ventana
root = tk.Tk()
root.title("Joke Generator")
root.geometry("400x300")

# Texto del chiste
joke_text = tk.StringVar()
joke_label = tk.Label(root, textvariable=joke_text, wraplength=350, justify="center", font=("Arial", 12))
joke_label.pack(pady=20)

# Botón para obtener chiste
btn = tk.Button(root, text="Get a Joke 😂", command=get_joke, font=("Arial", 14), bg="lightblue")
btn.pack(pady=10)

# Iniciar loop
root.mainloop()
