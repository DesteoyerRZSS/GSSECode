import tkinter as tk

# Planet data (distance from the Sun in astronomical units, and their sizes in Earth radii)
planets = {
    "Mercury": (0.39, 0.38),
    "Venus": (0.72, 0.95),
    "Earth": (1.00, 1.00),
    "Mars": (1.52, 0.53),
    "Jupiter": (5.20, 11.21),
    "Saturn": (9.58, 9.45),
    "Uranus": (19.18, 4.01),
    "Neptune": (30.07, 3.88)
}

# Create a Tkinter window
window = tk.Tk()
window.title("Planets in our Solar System")

# Create a canvas to draw the visualization
canvas = tk.Canvas(window, width=600, height=400)
canvas.pack()

# Calculate the scaling factors for the distances and sizes
max_distance = max(planets.values(), key=lambda x: x[0])[0]
max_size = max(planets.values(), key=lambda x: x[1])[1]
distance_scale = 500 / max_distance
size_scale = 100 / max_size

# Draw the planets on the canvas
for planet, (distance, size) in planets.items():
    x = distance * distance_scale
    y = size * size_scale
    canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill="blue")
    canvas.create_text(x, y + 10, text=planet)

# Run the Tkinter event loop
window.mainloop()