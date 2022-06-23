def get_y(m, b, x):
  y = (m * x) + b
  return y
print(get_y(1, 0, 7) == 7)
print(get_y(5, 10, 3) == 25)

#Write your calculate_error() function here
def calculate_error(m, b, point):
  x_point = point[0]
  y_point = point[1]
  y_value = get_y(m,b, x_point)
  distance = y_value - y_point
  return abs(distance)

#this is a line that looks like y = x, so (3, 3) should lie on it. thus, error should be 0:
print(calculate_error(1, 0, (3, 3)))
#the point (3, 4) should be 1 unit away from the line y = x:
print(calculate_error(1, 0, (3, 4)))
#the point (3, 3) should be 1 unit away from the line y = x - 1:
print(calculate_error(1, -1, (3, 3)))
#the point (3, 3) should be 5 units away from the line y = -x + 1:
print(calculate_error(-1, 1, (3, 3)))

#Write your calculate_all_error function here
total_errors = 0
def calculate_all_error(m, b, points):
  total_errors = 0
  for point in points:
    error = calculate_error(m, b, point)
    total_errors = total_errors  + error
  return total_errors

#every point in this dataset lies upon y=x, so the total error should be zero:
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(1, 0, datapoints))

#every point in this dataset is 1 unit away from y = x + 1, so the total error should be 4:
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(1, 1, datapoints))

#every point in this dataset is 1 unit away from y = x - 1, so the total error should be 4:
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(1, -1, datapoints))


#the points in this dataset are 1, 5, 9, and 3 units away from y = -x + 1, respectively, so total error should be
# 1 + 5 + 9 + 3 = 18
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(-1, 1, datapoints))

possible_ms = [i * 0.1 for i in range(-100, 101, 1)]
print(possible_ms)

possible_bs = [i * 0.1 for i in range(-200, 201, 1)]
print(possible_bs)