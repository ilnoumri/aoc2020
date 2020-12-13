from lib import open_file
import sys
try:
    if sys.argv[1] == "--sample":
        bus_info = open_file("13/sample")
    else:
        bus_info = open_file("13/input")
except:
    bus_info = open_file("13/input")

min_timestamp= int(bus_info[0])
bus_rules = bus_info[1].split(",")
buses_id = [int(elt) for elt in bus_rules if elt != "x"]
buses_id_part2 = [int(elt) if elt != "x" else 0 for elt in bus_rules]

def find_nearest_timestamp(min_timestamp, bus_id):
    res = bus_id
    while res < min_timestamp:
        res += bus_id
    return res

def get_nearest_timestamps(min_timestamp, buses_id):
    nearest_timestamps = {}
    for bus in buses_id:
        res = find_nearest_timestamp(min_timestamp, bus)
        nearest_timestamps[bus] = res
    return nearest_timestamps

def get_closest_departure(nearest_timestamps):
    min_k = ""
    min_v = float("inf")
    for k, v in nearest_timestamps.items():
        if v < min_v:
            min_v = v
            min_k = k
    return (min_k, min_v)

'''
I could not find part2 in an acceptable amount of time. Turns out the solution was to use chinese remainders theorem
Source of the following code : https://topaz.github.io/paste/#XQAAAQDnBgAAAAAAAAARiEJHiiMzw3cPM/1Vl+2nx/DqKkM2yi+HVdpp+qLh9Jwh+ZECcFH/z2ezeBhLAAlXqL8dinkTJIQhuZMH73+dkdSjscwmffdV6cqa61BCB7CldrqNrR2QHGOlysYcvD2LvLAroBVLTU+CAz/FfzHpYDNhRjlYYJsH2lkufgqG4xMDB8ubXRP99/gqEFcJCRsLGOe8NPQoZ71a50UXEkBwifHBw30t3OpjGzUSD9w3ksgLLhkOHmN4M/gNNcbTOtLzbRnAN4xEcyidH6HjnXd2VZuOtgJ9G0UUA+dSrlBCil6QAUcLBAsGl3z3g8G/A8ae2WKfwEuSQf4yxf4sRBvLt+kRki5Yk1uALppHOYPAXDNvLKyI5IhJ0jAizVUMjK03UHDEZBN7+9bIYaJhMcxZLAkE1wlasvMvkRj4jCrpTV9OkglkKsMI2njeVhIGLvafiP7cpwC3pTvM8Vb7gSIdV7b5b2WbY2zXKC3kjYJzFDJS7H2Q43zVXRxdsaLYUj3vDqh2jbiyIkxH3avrxdftJjDu14SXMKis1JWr7QlG42LIa7Lno9jwbGq3bJRKYT293YiAeK4opEP5nPh+t1krm5JAbawPvVyYEwXXgByoHaqI7bAzJYJavxjYipoTDLIfOay6umUalgtoENAsHPO5tD0Fg1pp2xw1E7bq8NGZMZD+qCwf4FlhjxZoCq2/f2p2bY6HJltDYeWVsDWUmdoc75rgbNNHf3Z+SS0b8cvLIKc+M3vYlTplsbOZ6oU9BVUDVJ1g5bO5W9QcC4L9hWmBRfGELwIZjfvAE3QKV7a2NTvFMNxTF2WischDWPxrPUidU/VD5dyxq8I+WM5zb0oP2mp+09+mJzDMl5/OE0BRioe1TA5cuZvrYrqFGdn39FkHsvmFunaP9h86g66m4rq/k/ger0+aUKc429RyBrSO4MeBJIcXeaN4qaTpHiHMeOwUQeV6Idkz8uIzNF0ccXhef9nAkNvS/2zrx/VFgoRna+uMdyPercln0W/LsqADwGtcxha0B6vWTOKD44YpMeQzbK2yvTOfWrNh5uG6Ua+dlFIFDTxxrZU4+LCRPoM1s0enQN4UgqTlZJJ+VlzP5X6LdChd/+rGa/Q=
'''
def bezout_coeffs(a, b):
    os, s = (1, 0)
    ot, t = (0, 1)
    while b != 0:
        q = a//b
        a, b = b, a - q * b
        os, s = s, os - q * s
        ot, t = t, ot - q * t
    return os, ot

def part2():
    mods = [(bus, (bus - i) % bus) for i, bus in enumerate(buses_id_part2) if bus > 0]
    mod, time = mods[0]
    for next_mod, offset in mods[1:]:
        m1, m2 = bezout_coeffs(mod, next_mod)
        time = time * m2 * next_mod + offset * m1 *mod
        mod *= next_mod
        time %= mod
    return time

print("### PART 1")
nearest_timestamp = get_nearest_timestamps(min_timestamp, buses_id)
closest_bus_id, closest_timestamp = get_closest_departure(nearest_timestamp)
print(closest_bus_id * (closest_timestamp - min_timestamp))

print("### PART 2")
print(part2())
