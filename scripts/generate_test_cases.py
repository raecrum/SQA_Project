import json
import argparse

# ---------- Arguments ----------
parser = argparse.ArgumentParser(description="Generate minimal test cases")
parser.add_argument("--input", "-i", required=True, help="Input requirements.json")
parser.add_argument("--output", "-o", required=True, help="Output test_cases.json")
args = parser.parse_args()

# ---------- Load requirements ----------
with open(args.input, "r", encoding="utf-8") as f:
    requirements = json.load(f)

# ---------- Select 10 rules ----------
selected_requirements = [
    "REQ-117.130-001A",
    "REQ-117.130-001B",
    "REQ-117.130-001E",
    "REQ-117.130-001F",
    "REQ-117.130-002A",
    "REQ-117.130-002B",
    "REQ-117.130-003A",
    "REQ-117.130-003A1",
    "REQ-117.130-003B",
    "REQ-117.130-003B3"
]

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