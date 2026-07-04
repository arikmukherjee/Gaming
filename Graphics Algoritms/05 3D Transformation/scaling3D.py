import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# ---------- 3D SCALING FUNCTION ----------
def scale3D(points, sx, sy, sz):

    scaled_points = []

    for (x, y, z) in points:

        # Scaling Formula
        new_x = x * sx
        new_y = y * sy
        new_z = z * sz

        scaled_points.append((new_x, new_y, new_z))

    return scaled_points


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
print("=========== 3D SCALING TRANSFORMATION ===========")

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

# Scaling factors
sx = float(input("\nEnter scaling factor along X-axis (sx): "))
sy = float(input("Enter scaling factor along Y-axis (sy): "))
sz = float(input("Enter scaling factor along Z-axis (sz): "))

# Perform Scaling
scaled_points = scale3D(original_points, sx, sy, sz)

# ---------- DISPLAY RESULTS ----------
print("\n========== ORIGINAL 3D POINTS ==========")

for point in original_points:
    print(point, "-", find_position_3d(point[0], point[1], point[2]))

print("\n========== SCALED 3D POINTS ==========")

for point in scaled_points:
    print(point, "-", find_position_3d(point[0], point[1], point[2]))

# ---------- PREPARE DATA ----------
x_original = [p[0] for p in original_points]
y_original = [p[1] for p in original_points]
z_original = [p[2] for p in original_points]

x_scaled = [p[0] for p in scaled_points]
y_scaled = [p[1] for p in scaled_points]
z_scaled = [p[2] for p in scaled_points]

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

# ---------- SCALED OBJECT ----------
ax.scatter(
    x_scaled,
    y_scaled,
    z_scaled,
    color='orange',
    s=80,
    label='Scaled Points'
)

# ---------- CONNECT ORIGINAL POINTS ----------
ax.plot(
    x_original,
    y_original,
    z_original,
    color='blue',
    linewidth=2
)

# ---------- CONNECT SCALED POINTS ----------
ax.plot(
    x_scaled,
    y_scaled,
    z_scaled,
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

# ---------- LABEL SCALED POINTS ----------
for i in range(len(scaled_points)):

    ax.text(
        scaled_points[i][0],
        scaled_points[i][1],
        scaled_points[i][2],
        f"S{i+1}{scaled_points[i]}",
        color='darkorange'
    )

# Labels
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")

# Title
plt.title(
    f"3D Scaling Transformation\n(sx={sx}, sy={sy}, sz={sz})"
)

# Legend
plt.legend()

plt.show()