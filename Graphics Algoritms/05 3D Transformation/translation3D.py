import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# ---------- 3D TRANSLATION FUNCTION ----------
def translate3D(points, tx, ty, tz):

    translated_points = []

    for (x, y, z) in points:

        # Translation Formula
        new_x = x + tx
        new_y = y + ty
        new_z = z + tz

        translated_points.append((new_x, new_y, new_z))

    return translated_points


# ---------- POSITION FUNCTION ----------
def find_position_3d(x, y, z):

    if x > 0 and y > 0 and z > 0:
        return "Positive Octant"

    elif x < 0 and y < 0 and z < 0:
        return "Negative Octant"

    elif x == 0 and y == 0 and z == 0:
        return "Origin"

    else:
        return "Mixed Region"


# ---------- MAIN PROGRAM ----------
print("=========== 3D TRANSLATION TRANSFORMATION ===========")

# Number of vertices
n = int(input("Enter number of 3D points: "))

original_points = []

# Input 3D points
print("\nEnter coordinates (x, y, z):")

for i in range(n):

    x = int(input(f"Enter x{i+1}: "))
    y = int(input(f"Enter y{i+1}: "))
    z = int(input(f"Enter z{i+1}: "))

    original_points.append((x, y, z))

# Translation values
tx = int(input("\nEnter translation along X-axis (tx): "))
ty = int(input("Enter translation along Y-axis (ty): "))
tz = int(input("Enter translation along Z-axis (tz): "))

# Perform Translation
translated_points = translate3D(original_points, tx, ty, tz)

# ---------- DISPLAY RESULTS ----------
print("\n========== ORIGINAL 3D POINTS ==========")

for point in original_points:
    print(point, "-", find_position_3d(point[0], point[1], point[2]))

print("\n========== TRANSLATED 3D POINTS ==========")

for point in translated_points:
    print(point, "-", find_position_3d(point[0], point[1], point[2]))

# ---------- PREPARE DATA ----------
x_original = [p[0] for p in original_points]
y_original = [p[1] for p in original_points]
z_original = [p[2] for p in original_points]

x_translated = [p[0] for p in translated_points]
y_translated = [p[1] for p in translated_points]
z_translated = [p[2] for p in translated_points]

# ---------- 3D PLOTTING ----------
fig = plt.figure(figsize=(10, 10))

ax = fig.add_subplot(111, projection='3d')

# ---------- ORIGINAL OBJECT ----------
ax.scatter(
    x_original,
    y_original,
    z_original,
    color='blue',
    s=80,
    label='Original Points'
)

# ---------- TRANSLATED OBJECT ----------
ax.scatter(
    x_translated,
    y_translated,
    z_translated,
    color='orange',
    s=80,
    label='Translated Points'
)

# ---------- CONNECT ORIGINAL POINTS ----------
ax.plot(
    x_original,
    y_original,
    z_original,
    color='blue',
    linewidth=2
)

# ---------- CONNECT TRANSLATED POINTS ----------
ax.plot(
    x_translated,
    y_translated,
    z_translated,
    color='orange',
    linewidth=2
)

# ---------- LABEL ORIGINAL POINTS ----------
for i in range(len(original_points)):

    ax.text(
        original_points[i][0],
        original_points[i][1],
        original_points[i][2],
        f"O{i+1}{original_points[i]}",
        color='blue'
    )

# ---------- LABEL TRANSLATED POINTS ----------
for i in range(len(translated_points)):

    ax.text(
        translated_points[i][0],
        translated_points[i][1],
        translated_points[i][2],
        f"T{i+1}{translated_points[i]}",
        color='darkorange'
    )

# Labels
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")

# Title
plt.title(
    f"3D Translation Transformation\n(tx={tx}, ty={ty}, tz={tz})"
)

# Legend
plt.legend()

plt.show()