import sys
import logging
import argparse
import subprocess
import json

logging.basicConfig(level=logging.INFO)

def parse_args():
    p = argparse.ArgumentParser()

    p.add_argument("-o", "--output", help="Write output to file")

    return p.parse_args()


def main():
    args = parse_args()

    merged = {
        "openapi": "3.0.0",
        "components": {
            "schemas": {},
        },
    }
    res = subprocess.check_output(["kubectl", "get", "--raw", "/openapi/v3"])
    schemas = json.loads(res)
    apicount = len([x for x in schemas["paths"] if x.startswith("apis")])
    logging.info(f"Extracting {apicount} schemas")

    for path, spec in schemas.get("paths", {}).items():
        if not path.startswith("apis"):
            continue

        apicount += 1
        logging.info(f"...extracting {path}")
        res = subprocess.check_output(
            ["kubectl", "get", "--raw", spec["serverRelativeURL"]]
        )
        schema = json.loads(res)
        merged["components"]["schemas"].update(schema["components"]["schemas"])

    with sys.stdout if args.output is None else open(args.output, "w") as fd:
        json.dump(merged, fd, indent=2)


if __name__ == "__main__":
    main()
