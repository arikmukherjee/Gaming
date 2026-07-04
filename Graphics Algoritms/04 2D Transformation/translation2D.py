import matplotlib.pyplot as plt

# ---------- TRANSLATION FUNCTION ----------
def translate_object(points, tx, ty):

    translated_points = []

    for (x, y) in points:

        new_x = x + tx
        new_y = y + ty

        translated_points.append((new_x, new_y))

    return translated_points


# ---------- POSITION FUNCTION ----------
def find_position(x, y):

    if x > 0 and y > 0:
        return "1st Quadrant"
    elif x < 0 and y > 0:
        return "2nd Quadrant"
    elif x < 0 and y < 0:
        return "3rd Quadrant"
    elif x > 0 and y < 0:
        return "4th Quadrant"
    elif x == 0 and y == 0:
        return "Origin"
    elif x == 0:
        return "On Y-Axis"
    elif y == 0:
        return "On X-Axis"


# ---------- MAIN PROGRAM ----------
print("=========== 2D TRANSLATION TRANSFORMATION ===========")

# Number of vertices
n = int(input("Enter number of vertices: "))

original_points = []

# Input vertices
print("\nEnter coordinates of polygon:")

for i in range(n):

    x = int(input(f"Enter x{i+1}: "))
    y = int(input(f"Enter y{i+1}: "))

    original_points.append((x, y))

# Translation values
tx = int(input("\nEnter translation along X-axis (tx): "))
ty = int(input("Enter translation along Y-axis (ty): "))

# Perform Translation
translated_points = translate_object(original_points, tx, ty)

# ---------- DISPLAY RESULTS ----------
print("\n========== ORIGINAL POINTS ==========")

for point in original_points:
    print(point, "-", find_position(point[0], point[1]))

print("\n========== TRANSLATED POINTS ==========")

for point in translated_points:
    print(point, "-", find_position(point[0], point[1]))

# ---------- PREPARE FOR PLOTTING ----------
# Original polygon points
x_original = [p[0] for p in original_points]
y_original = [p[1] for p in original_points]

# Close the polygon
x_original.append(original_points[0][0])
y_original.append(original_points[0][1])

# Translated polygon points
x_translated = [p[0] for p in translated_points]
y_translated = [p[1] for p in translated_points]

# Close translated polygon
x_translated.append(translated_points[0][0])
y_translated.append(translated_points[0][1])

# ---------- PLOTTING ----------
plt.figure(figsize=(10, 10))

# Axes
plt.axhline(0, color='black', linewidth=2)
plt.axvline(0, color='black', linewidth=2)

# ---------- ORIGINAL OBJECT ----------
plt.plot(
    x_original,
    y_original,
    marker='o',
    color='blue',
    linewidth=2,
    label='Original Object'
)

# ---------- TRANSLATED OBJECT ----------
plt.plot(
    x_translated,
    y_translated,
    marker='o',
    color='orange',
    linewidth=2,
    label='Translated Object'
)

# ---------- LABEL ORIGINAL POINTS ----------
for i in range(len(original_points)):

    plt.text(
        original_points[i][0] + 0.2,
        original_points[i][1] + 0.2,
        f"O{i+1}{original_points[i]}",
        fontsize=9,
        color='blue'
    )

# ---------- LABEL TRANSLATED POINTS ----------
for i in range(len(translated_points)):

    plt.text(
        translated_points[i][0] + 0.2,
        translated_points[i][1] + 0.2,
        f"T{i+1}{translated_points[i]}",
        fontsize=9,
        color='darkorange'
    )

# Quadrant Labels
plt.text(5, 5, "1st Quadrant", color='green')
plt.text(-15, 5, "2nd Quadrant", color='blue')
plt.text(-15, -5, "3rd Quadrant", color='red')
plt.text(5, -5, "4th Quadrant", color='purple')

# Grid
plt.grid(True, linestyle='--')

# Labels
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.title("2D Translation Transformation")

# Limits
all_x = x_original + x_translated
all_y = y_original + y_translated

max_range = max(
    max(map(abs, all_x)),
    max(map(abs, all_y))
) + 5

plt.xlim(-max_range, max_range)
plt.ylim(-max_range, max_range)

plt.axis('equal')
plt.legend()

plt.show()