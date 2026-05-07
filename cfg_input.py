def read_cfg():
    cfg = {}

    while True:
        rule = input().strip()

        if rule.lower() == "done":
            break

        # support both → and ->
        if "→" in rule:
            left, right = rule.split("→")
        elif "->" in rule:
            left, right = rule.split("->")
        else:
            print("❌ Invalid format")
            continue

        left = left.strip()
        right = right.strip()

        # validation
        if len(left) != 1 or not left.isupper():
            print("❌ Left side must be ONE uppercase uppercase letter")
            continue

        if right == "":
            print("❌ Right side cannot be empty")
            continue

        productions = [p.strip() for p in right.split("|")]

        # epsilon support
        productions = ["" if p == "ε" else p for p in productions]

        if left not in cfg:
            cfg[left] = []

        cfg[left].extend(productions)

    return cfg


def print_cfg(cfg):
    print("\nCFG Rules:")
    for left in cfg:
        right = " | ".join([p if p != "" else "ε" for p in cfg[left]])
        print(f"{left} → {right}")