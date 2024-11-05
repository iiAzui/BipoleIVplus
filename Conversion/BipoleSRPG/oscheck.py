import sys
print(sys.platform)
os = sys.platform
if os == "win32":
    TextMul = 0.6
else:
    TextMul = 1