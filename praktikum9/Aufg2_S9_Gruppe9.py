import numpy as np

def f(x): return np.cos(x**2)

T00 = np.pi*((f(0) + f(np.pi))/2)
print(f"T00 = {T00}")

sum_T10 = 0
for i in range (1, 2):
    sum_T10 =  sum_T10 + f((i*np.pi)/2)

T10 = (np.pi/2)*(((f(0) + f(np.pi))/2) + sum_T10)
print(f"T10 = {T10}")


sum_T20 = 0
for i in range (1, 4):
    sum_T20 =  sum_T20 + f((i*np.pi)/4)

T20 = (np.pi/4)*(((f(0) + f(np.pi))/2) + sum_T20)
print(f"T20 = {T20}")

sum_T30 = 0
for i in range (1, 8):
    sum_T30 =  sum_T30 + f((i*np.pi)/8)

T30 = (np.pi/8)*(((f(0) + f(np.pi))/2) + sum_T30)
print(f"T30 = {T30}")

sum_T40 = 0
for i in range (1, 16):
    sum_T40 =  sum_T40 + f((i*np.pi)/16)

T40 = (np.pi/16)*(((f(0) + f(np.pi))/2) + sum_T40)
print(f"T40 = {T40}")

print(f"-------")

T01 = (4*T10 - T00)/3
print(f"T01 = {T01}")

T11 = (4*T20 - T10)/3
print(f"T11 = {T11}")

T21 = (4*T30 - T20)/3
print(f"T21 = {T21}")

T31 = (4*T40 - T30)/3
print(f"T*1 = {T31}")

print(f"-------")

T02 = (16*T11 - T01)/15
print(f"T01 = {T01}")

T12 = (16*T21 - T11)/15
print(f"T11 = {T11}")

T22 = (16*T31 - T21)/15
print(f"T21 = {T21}")

print(f"-------")

T03 = (64*T12 - T02)/63
print(f"T03 = {T03}")

T13 = (64*T22 - T12)/63
print(f"T13 = {T13}")

print(f"-------")

T04 = (256*T13 - T03)/255
print(f"T04 = {T04}")
