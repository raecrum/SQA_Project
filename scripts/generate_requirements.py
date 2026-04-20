# scripts/generate_requirements.py
import json
import re
import argparse

# ---------- Arguments ----------
parser = argparse.ArgumentParser(description="Generate requirement JSON from CFR Markdown")
parser.add_argument("--input", "-i", required=True, help="Input Markdown file (.md)")
parser.add_argument("--output", "-o", required=True, help="Output JSON file")
parser.add_argument("--cfr", "-c", required=True, help="CFR section (e.g., 21 CFR 117.130)")
parser.add_argument("--mode", choices=["requirements", "structure"], default="requirements",
                    help="Output mode: requirements or structure")

args = parser.parse_args()

INPUT_MD = args.input
OUTPUT_JSON = args.output
CFR_SECTION = args.cfr

# ---------- Read File ----------
with open(INPUT_MD, "r") as f:
    lines = [line.strip() for line in f if line.strip()]

requirements = []
current_req = None

# ---------- Parse ----------
for line in lines:

    # Capture REQ ID
    req_match = re.search(r"(REQ-\d+\.\d+-\d+)", line)
    if req_match:
        current_req = req_match.group(1)
        continue

    # Capture atomic rules
    atomic_match = re.search(r"(â†’|→)\s*([A-Z]\d*)$", line)
    if atomic_match and current_req:
        suffix = atomic_match.group(2)

        description = re.split(r"â†’|→", line)[0].strip()

        # Clean markdown junk
        description = re.sub(r"^[-#\s]*", "", description)  # remove -, ##, spaces
        description = re.sub(r"^\(\w+\)\s*", "", description)  # remove (1), (i)

        requirement_id = f"{current_req}{suffix}"

        if len(suffix) == 1:
            parent = current_req
        else:
            parent = f"{current_req}{suffix[0]}"

        requirements.append({
            "requirement_id": requirement_id,
            "description": description,
            "source": CFR_SECTION,
            "parent": parent
        })

# ---------- Generate Structure ----------
if args.mode == "structure":
    from collections import defaultdict

    structure = defaultdict(list)

    for req in requirements:
        parent = req["parent"]
        req_id = req["requirement_id"]

        suffix = req_id.replace(parent, "")
        structure[parent].append(suffix)

    # Sort for consistency
    for key in structure:
        structure[key] = sorted(structure[key])

    output_data = dict(structure)

else:
    output_data = requirements

# ---------- Save ----------
with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
    json.dump(output_data, f, indent=2)

if args.mode == "structure":
    print(f"Saved structure with {len(output_data)} parents → {OUTPUT_JSON}")
else:
    print(f"Saved {len(output_data)} requirements → {OUTPUT_JSON}")