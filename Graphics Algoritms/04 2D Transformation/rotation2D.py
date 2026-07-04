import matplotlib.pyplot as plt
import math

# ---------- ROTATION FUNCTION ----------
def rotate_object(points, angle):

    rotated_points = []

    # Convert degree to radian
    theta = math.radians(angle)

    for (x, y) in points:

        # Rotation Formula
        new_x = x * math.cos(theta) - y * math.sin(theta)
        new_y = x * math.sin(theta) + y * math.cos(theta)

        # Round values for clean plotting
        rotated_points.append((round(new_x, 2), round(new_y, 2)))

    return rotated_points


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
print("=========== 2D ROTATION TRANSFORMATION ===========")

# Number of vertices
n = int(input("Enter number of vertices: "))

original_points = []

# Input vertices
print("\nEnter coordinates of polygon:")

for i in range(n):

    x = int(input(f"Enter x{i+1}: "))
    y = int(input(f"Enter y{i+1}: "))

    original_points.append((x, y))

# Rotation angle
angle = float(input("\nEnter rotation angle (in degrees): "))

# Perform Rotation
rotated_points = rotate_object(original_points, angle)

# ---------- DISPLAY RESULTS ----------
print("\n========== ORIGINAL POINTS ==========")

for point in original_points:
    print(point, "-", find_position(point[0], point[1]))

print("\n========== ROTATED POINTS ==========")

for point in rotated_points:
    print(point, "-", find_position(point[0], point[1]))

# ---------- PREPARE FOR PLOTTING ----------
# Original polygon points
x_original = [p[0] for p in original_points]
y_original = [p[1] for p in original_points]

# Close polygon
x_original.append(original_points[0][0])
y_original.append(original_points[0][1])

# Rotated polygon points
x_rotated = [p[0] for p in rotated_points]
y_rotated = [p[1] for p in rotated_points]

# Close rotated polygon
x_rotated.append(rotated_points[0][0])
y_rotated.append(rotated_points[0][1])

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

# ---------- ROTATED OBJECT ----------
plt.plot(
    x_rotated,
    y_rotated,
    marker='o',
    color='orange',
    linewidth=2,
    label='Rotated Object'
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

# ---------- LABEL ROTATED POINTS ----------
for i in range(len(rotated_points)):

    plt.text(
        rotated_points[i][0] + 0.2,
        rotated_points[i][1] + 0.2,
        f"R{i+1}{rotated_points[i]}",
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

plt.title(f"2D Rotation Transformation ({angle}°)")

# Limits
all_x = x_original + x_rotated
all_y = y_original + y_rotated

max_range = max(
    max(map(abs, all_x)),
    max(map(abs, all_y))
) + 5

plt.xlim(-max_range, max_range)
plt.ylim(-max_range, max_range)

plt.axis('equal')
plt.legend()

plt.show()