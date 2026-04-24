import json
import sys
import myLogger

logObj = myLogger.giveMeLoggingObject()

# Load requirements and expected structure
with open("requirements.json") as f:
    requirements = json.load(f)

with open("expected_structure.json") as f:
    expected_structure = json.load(f)

# Build set of actual requirement IDs
actual_ids = {r["requirement_id"] for r in requirements}

failures = []

# Check all expected enumerations exist
for parent, suffixes in expected_structure.items():
    for s in suffixes:
        rid = f"{parent}{s}"
        if rid not in actual_ids:
            failures.append(f"Missing requirement: {rid}")
            logObj.warning(f"Missing requirement: {rid}")

# Optional: check for extra/unexpected requirements
for rid in actual_ids:
    # Find the most specific (longest) parent key that is a prefix of this ID
    matching_parents = [p for p in expected_structure if rid.startswith(p) and rid != p]
    if matching_parents:
        parent = max(matching_parents, key=len)
        suffix = rid[len(parent):]
        if suffix not in expected_structure[parent]:
            failures.append(f"Unexpected requirement: {rid}")

if failures:
    print("\n".join(failures))
    logObj.error(f"Validation FAILED with {len(failures)} issue(s)")
    sys.exit(1)
else:
    print(" Validation passed: all enumerations complete.")
    logObj.info(f"Validation passed: {len(requirements)} requirements checked")