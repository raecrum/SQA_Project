import json
import argparse

# ---------- Arguments ----------
parser = argparse.ArgumentParser(description="Generate minimal test cases")
parser.add_argument("--requirements", "-r", required=True, help="Input requirements.json")
parser.add_argument("--selection", "-s", required=True, help="Input selected rules file (json)")
parser.add_argument("--output", "-o", required=True, help="Output test_cases.json")
args = parser.parse_args()

# ---------- Load requirements ----------
with open(args.requirements, "r", encoding="utf-8") as f:
    requirements = json.load(f)

# ---------- Load selected rules ----------
with open(args.selection, "r", encoding="utf-8") as f:
    selection_data = json.load(f)

selected_requirements = set()

# Case 1: selection file is a list of requirement IDs
if isinstance(selection_data, list):
    selected_requirements = set(selection_data)

# Case 2: selection file is expected_structure.json (dict)
elif isinstance(selection_data, dict):
    for parent, children in selection_data.items():
        for child in children:
            selected_requirements.add(parent + child)

# ---------- Generate test cases ----------
test_cases = []
tc_id = 1

for req in requirements:
    if req["requirement_id"] in selected_requirements:

        test_case = {
            "test_case_id": f"TC-{tc_id:03}",
            "requirement_id": req["requirement_id"],
            "description": f"Verify that {req['description'].lower()}",
            "input_data": f"Sample input data for {req['requirement_id']}",
            "expected_output": f"System correctly performs: {req['description']}"
        }

        test_cases.append(test_case)
        tc_id += 1

# ---------- Save ----------
with open(args.output, "w", encoding="utf-8") as f:
    json.dump(test_cases, f, indent=2)

print(f"Generated {len(test_cases)} test cases → {args.output}")