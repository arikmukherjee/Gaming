import matplotlib.pyplot as plt

# ---------- 2D SHEARING FUNCTION ----------
def shear_object(points, shx, shy):

    sheared_points = []

    for (x, y) in points:

        # Shearing Formula
        new_x = x + shx * y
        new_y = y + shy * x

        sheared_points.append((
            round(new_x, 2),
            round(new_y, 2)
        ))

    return sheared_points


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
print("=========== 2D SHEARING TRANSFORMATION ===========")

# Number of vertices
n = int(input("Enter number of vertices: "))

original_points = []

# Input polygon vertices
print("\nEnter coordinates of polygon:")

for i in range(n):

    x = int(input(f"Enter x{i+1}: "))
    y = int(input(f"Enter y{i+1}: "))

    original_points.append((x, y))

# Shearing factors
shx = float(input("\nEnter shearing factor along X-axis (shx): "))
shy = float(input("Enter shearing factor along Y-axis (shy): "))

# Perform Shearing
sheared_points = shear_object(original_points, shx, shy)

# ---------- DISPLAY RESULTS ----------
print("\n========== ORIGINAL POINTS ==========")

for point in original_points:
    print(point, "-", find_position(point[0], point[1]))

print("\n========== SHEARED POINTS ==========")

for point in sheared_points:
    print(point, "-", find_position(point[0], point[1]))

# ---------- PREPARE FOR PLOTTING ----------
# Original polygon points
x_original = [p[0] for p in original_points]
y_original = [p[1] for p in original_points]

# Close polygon
x_original.append(original_points[0][0])
y_original.append(original_points[0][1])

# Sheared polygon points
x_sheared = [p[0] for p in sheared_points]
y_sheared = [p[1] for p in sheared_points]

# Close sheared polygon
x_sheared.append(sheared_points[0][0])
y_sheared.append(sheared_points[0][1])

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

# ---------- SHEARED OBJECT ----------
plt.plot(
    x_sheared,
    y_sheared,
    marker='o',
    color='orange',
    linewidth=2,
    label='Sheared Object'
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

# ---------- LABEL SHEARED POINTS ----------
for i in range(len(sheared_points)):

    plt.text(
        sheared_points[i][0] + 0.2,
        sheared_points[i][1] + 0.2,
        f"H{i+1}{sheared_points[i]}",
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

plt.title(f"2D Shearing Transformation\n(shx={shx}, shy={shy})")

# Limits
all_x = x_original + x_sheared
all_y = y_original + y_sheared

max_range = max(
    max(map(abs, all_x)),
    max(map(abs, all_y))
) + 5

plt.xlim(-max_range, max_range)
plt.ylim(-max_range, max_range)

plt.axis('equal')
plt.legend()

plt.show()