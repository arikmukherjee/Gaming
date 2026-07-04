import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# ---------- 3D SHEARING FUNCTION ----------
def shear3D(points, shxy, shxz, shyx, shyz, shzx, shzy):

    sheared_points = []

    for (x, y, z) in points:

        # 3D Shearing Formula
        new_x = x + shxy * y + shxz * z
        new_y = y + shyx * x + shyz * z
        new_z = z + shzx * x + shzy * y

        sheared_points.append((
            round(new_x, 2),
            round(new_y, 2),
            round(new_z, 2)
        ))

    return sheared_points


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
print("=========== 3D SHEARING TRANSFORMATION ===========")

# Number of points
n = int(input("Enter number of 3D points: "))

original_points = []

# Input points
print("\nEnter coordinates (x, y, z):")

for i in range(n):

    x = int(input(f"Enter x{i+1}: "))
    y = int(input(f"Enter y{i+1}: "))
    z = int(input(f"Enter z{i+1}: "))

    original_points.append((x, y, z))

# Shearing factors
print("\nEnter 3D Shearing Factors:")

shxy = float(input("shxy : "))
shxz = float(input("shxz : "))

shyx = float(input("shyx : "))
shyz = float(input("shyz : "))

shzx = float(input("shzx : "))
shzy = float(input("shzy : "))

# Perform Shearing
sheared_points = shear3D(
    original_points,
    shxy, shxz,
    shyx, shyz,
    shzx, shzy
)

# ---------- DISPLAY RESULTS ----------
print("\n========== ORIGINAL 3D POINTS ==========")

for point in original_points:
    print(point, "-", find_position_3d(point[0], point[1], point[2]))

print("\n========== SHEARED 3D POINTS ==========")

for point in sheared_points:
    print(point, "-", find_position_3d(point[0], point[1], point[2]))

# ---------- PREPARE DATA ----------
x_original = [p[0] for p in original_points]
y_original = [p[1] for p in original_points]
z_original = [p[2] for p in original_points]

x_sheared = [p[0] for p in sheared_points]
y_sheared = [p[1] for p in sheared_points]
z_sheared = [p[2] for p in sheared_points]

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

# ---------- SHEARED OBJECT ----------
ax.scatter(
    x_sheared,
    y_sheared,
    z_sheared,
    color='orange',
    s=80,
    label='Sheared Points'
)

# ---------- CONNECT ORIGINAL POINTS ----------
ax.plot(
    x_original,
    y_original,
    z_original,
    color='blue',
    linewidth=2
)

# ---------- CONNECT SHEARED POINTS ----------
ax.plot(
    x_sheared,
    y_sheared,
    z_sheared,
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

# ---------- LABEL SHEARED POINTS ----------
for i in range(len(sheared_points)):

    ax.text(
        sheared_points[i][0],
        sheared_points[i][1],
        sheared_points[i][2],
        f"H{i+1}",
        color='darkorange'
    )

# Labels
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")

# Title
plt.title(
    "3D Shearing Transformation"
)

# Legend
plt.legend()

plt.show()