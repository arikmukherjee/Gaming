import matplotlib.pyplot as plt

# ---------- SCALING FUNCTION ----------
def scale_object(points, sx, sy):

    scaled_points = []

    for (x, y) in points:

        # Scaling Formula
        new_x = x * sx
        new_y = y * sy

        scaled_points.append((new_x, new_y))

    return scaled_points


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
print("=========== 2D SCALING TRANSFORMATION ===========")

# Number of vertices
n = int(input("Enter number of vertices: "))

original_points = []

# Input polygon vertices
print("\nEnter coordinates of polygon:")

for i in range(n):

    x = int(input(f"Enter x{i+1}: "))
    y = int(input(f"Enter y{i+1}: "))

    original_points.append((x, y))

# Scaling factors
sx = float(input("\nEnter scaling factor along X-axis (sx): "))
sy = float(input("Enter scaling factor along Y-axis (sy): "))

# Perform Scaling
scaled_points = scale_object(original_points, sx, sy)

# ---------- DISPLAY RESULTS ----------
print("\n========== ORIGINAL POINTS ==========")

for point in original_points:
    print(point, "-", find_position(point[0], point[1]))

print("\n========== SCALED POINTS ==========")

for point in scaled_points:
    print(point, "-", find_position(point[0], point[1]))

# ---------- PREPARE FOR PLOTTING ----------
# Original polygon points
x_original = [p[0] for p in original_points]
y_original = [p[1] for p in original_points]

# Close polygon
x_original.append(original_points[0][0])
y_original.append(original_points[0][1])

# Scaled polygon points
x_scaled = [p[0] for p in scaled_points]
y_scaled = [p[1] for p in scaled_points]

# Close scaled polygon
x_scaled.append(scaled_points[0][0])
y_scaled.append(scaled_points[0][1])

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

# ---------- SCALED OBJECT ----------
plt.plot(
    x_scaled,
    y_scaled,
    marker='o',
    color='orange',
    linewidth=2,
    label='Scaled Object'
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

# ---------- LABEL SCALED POINTS ----------
for i in range(len(scaled_points)):

    plt.text(
        scaled_points[i][0] + 0.2,
        scaled_points[i][1] + 0.2,
        f"S{i+1}{scaled_points[i]}",
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

plt.title(f"2D Scaling Transformation (sx={sx}, sy={sy})")

# Limits
all_x = x_original + x_scaled
all_y = y_original + y_scaled

max_range = max(
    max(map(abs, all_x)),
    max(map(abs, all_y))
) + 5

plt.xlim(-max_range, max_range)
plt.ylim(-max_range, max_range)

plt.axis('equal')
plt.legend()

plt.show()