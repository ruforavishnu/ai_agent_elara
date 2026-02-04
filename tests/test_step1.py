import sys
import pkg_resources

required = ["pandas", "numpy", "ccxt", "fastapi"]

print("Python version:")
print(sys.version)
print("-" * 40)

missing = []
for pkg in required:
    if not pkg_resources.working_set.by_key.get(pkg):
        missing.append(pkg)

if missing:
    print("❌ Missing packages:", missing)
else:
    print("✅ All required packages installed")

print("Environment OK")
