import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math

# ---------- 3D ROTATION FUNCTIONS ----------

# Rotation about X-axis
def rotate_x(points, angle):

    rotated_points = []

    theta = math.radians(angle)

    for (x, y, z) in points:

        new_x = x
        new_y = y * math.cos(theta) - z * math.sin(theta)
        new_z = y * math.sin(theta) + z * math.cos(theta)

        rotated_points.append((
            round(new_x, 2),
            round(new_y, 2),
            round(new_z, 2)
        ))

    return rotated_points


# Rotation about Y-axis
def rotate_y(points, angle):

    rotated_points = []

    theta = math.radians(angle)

    for (x, y, z) in points:

        new_x = x * math.cos(theta) + z * math.sin(theta)
        new_y = y
        new_z = -x * math.sin(theta) + z * math.cos(theta)

        rotated_points.append((
            round(new_x, 2),
            round(new_y, 2),
            round(new_z, 2)
        ))

    return rotated_points


# Rotation about Z-axis
def rotate_z(points, angle):

    rotated_points = []

    theta = math.radians(angle)

    for (x, y, z) in points:

        new_x = x * math.cos(theta) - y * math.sin(theta)
        new_y = x * math.sin(theta) + y * math.cos(theta)
        new_z = z

        rotated_points.append((
            round(new_x, 2),
            round(new_y, 2),
            round(new_z, 2)
        ))

    return rotated_points


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
print("=========== 3D ROTATION TRANSFORMATION ===========")

# Number of vertices
n = int(input("Enter number of 3D points: "))

original_points = []

# Input points
print("\nEnter coordinates (x, y, z):")

for i in range(n):

    x = int(input(f"Enter x{i+1}: "))
    y = int(input(f"Enter y{i+1}: "))
    z = int(input(f"Enter z{i+1}: "))

    original_points.append((x, y, z))

# Choose rotation axis
print("\nChoose Rotation Axis:")
print("1. X-axis")
print("2. Y-axis")
print("3. Z-axis")

choice = int(input("Enter your choice: "))

# Rotation angle
angle = float(input("Enter rotation angle (in degrees): "))

# Perform Rotation
if choice == 1:
    rotated_points = rotate_x(original_points, angle)
    axis_name = "X-axis"

elif choice == 2:
    rotated_points = rotate_y(original_points, angle)
    axis_name = "Y-axis"

elif choice == 3:
    rotated_points = rotate_z(original_points, angle)
    axis_name = "Z-axis"

else:
    print("Invalid Choice!")
    exit()

# ---------- DISPLAY RESULTS ----------
print("\n========== ORIGINAL 3D POINTS ==========")

for point in original_points:
    print(point, "-", find_position_3d(point[0], point[1], point[2]))

print("\n========== ROTATED 3D POINTS ==========")

for point in rotated_points:
    print(point, "-", find_position_3d(point[0], point[1], point[2]))

# ---------- PREPARE DATA ----------
x_original = [p[0] for p in original_points]
y_original = [p[1] for p in original_points]
z_original = [p[2] for p in original_points]

x_rotated = [p[0] for p in rotated_points]
y_rotated = [p[1] for p in rotated_points]
z_rotated = [p[2] for p in rotated_points]

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

# ---------- ROTATED OBJECT ----------
ax.scatter(
    x_rotated,
    y_rotated,
    z_rotated,
    color='orange',
    s=80,
    label='Rotated Points'
)

# ---------- CONNECT ORIGINAL POINTS ----------
ax.plot(
    x_original,
    y_original,
    z_original,
    color='blue',
    linewidth=2
)

# ---------- CONNECT ROTATED POINTS ----------
ax.plot(
    x_rotated,
    y_rotated,
    z_rotated,
    color='orange',
    linewidth=2
)

# ---------- LABEL ORIGINAL POINTS ----------
for i in range(len(original_points)):

    ax.text(
        original_points[i][0],
        original_points[i][1],
        original_points[i][2],
        f"O{i+1}",
        color='blue'
    )

# ---------- LABEL ROTATED POINTS ----------
for i in range(len(rotated_points)):

    ax.text(
        rotated_points[i][0],
        rotated_points[i][1],
        rotated_points[i][2],
        f"R{i+1}",
        color='darkorange'
    )

# Axis Labels
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")

# Title
plt.title(
    f"3D Rotation about {axis_name}\nAngle = {angle}°"
)

# Legend
plt.legend()

plt.show()