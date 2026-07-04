import matplotlib.pyplot as plt


# ---------- POSITION FUNCTION ----------
def find_polygon_position(vertices):

    xs = [v[0] for v in vertices]
    ys = [v[1] for v in vertices]

    xc = sum(xs) / len(xs)
    yc = sum(ys) / len(ys)

    if xc > 0 and yc > 0:
        return "1st Quadrant"
    elif xc < 0 and yc > 0:
        return "2nd Quadrant"
    elif xc < 0 and yc < 0:
        return "3rd Quadrant"
    elif xc > 0 and yc < 0:
        return "4th Quadrant"
    elif xc == 0 and yc == 0:
        return "Origin"
    elif xc == 0:
        return "On Y-Axis"
    elif yc == 0:
        return "On X-Axis"


# ---------- SCAN LINE POLYGON FILL ----------
def scanline_fill(vertices):

    fill_points = []

    y_min = min(y for x, y in vertices)
    y_max = max(y for x, y in vertices)

    print("\n========== SCAN LINE FILLING ==========")

    for y in range(y_min, y_max + 1):

        intersections = []

        n = len(vertices)

        for i in range(n):

            x1, y1 = vertices[i]
            x2, y2 = vertices[(i + 1) % n]

            # Ignore horizontal edges
            if y1 == y2:
                continue

            # Check if scan line intersects edge
            if y >= min(y1, y2) and y < max(y1, y2):

                x = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
                intersections.append(round(x))

        intersections.sort()

        print(f"Scan Line y = {y} --> Intersections = {intersections}")

        # Fill between pairs of intersections
        for i in range(0, len(intersections), 2):

            if i + 1 < len(intersections):

                x_start = intersections[i]
                x_end = intersections[i + 1]

                for x in range(x_start, x_end + 1):
                    fill_points.append((x, y))

    return fill_points


# ---------- MAIN PROGRAM ----------
print("=========== SCAN LINE POLYGON FILLING ALGORITHM ===========")

n = int(input("Enter number of vertices: "))

vertices = []

for i in range(n):

    x = int(input(f"Enter x{i+1}: "))
    y = int(input(f"Enter y{i+1}: "))

    vertices.append((x, y))

position = find_polygon_position(vertices)

print("\nPolygon is located in:", position)

filled_pixels = scanline_fill(vertices)

# Polygon Boundary
polygon_x = [v[0] for v in vertices] + [vertices[0][0]]
polygon_y = [v[1] for v in vertices] + [vertices[0][1]]

# Filled Pixels
fill_x = [p[0] for p in filled_pixels]
fill_y = [p[1] for p in filled_pixels]

# ---------- PLOTTING ----------
plt.figure(figsize=(10, 10))

# Axes
plt.axhline(0, color='black', linewidth=2)
plt.axvline(0, color='black', linewidth=2)

# Polygon Boundary
plt.plot(
    polygon_x,
    polygon_y,
    color='blue',
    linewidth=2,
    label='Polygon Boundary'
)

# Filled Pixels
plt.scatter(
    fill_x,
    fill_y,
    color='orange',
    s=40,
    label='Filled Pixels'
)

# Vertex Points
for i, (x, y) in enumerate(vertices):

    plt.scatter(x, y, color='red', s=80)

    plt.text(
        x + 0.2,
        y + 0.2,
        f"({x},{y})",
        fontsize=8,
        color='darkgreen'
    )

# Quadrant Labels
plt.text(5, 5, "1st Quadrant", color='green')
plt.text(-15, 5, "2nd Quadrant", color='blue')
plt.text(-15, -5, "3rd Quadrant", color='red')
plt.text(5, -5, "4th Quadrant", color='purple')

# Grid
plt.grid(True, linestyle='--')

plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.title(f"Scan Line Polygon Filling Algorithm\n{position}")

plt.axis('equal')

max_range = max(
    max(abs(x) for x, y in vertices),
    max(abs(y) for x, y in vertices)
) + 5

plt.xlim(-max_range, max_range)
plt.ylim(-max_range, max_range)

plt.legend()
plt.show()