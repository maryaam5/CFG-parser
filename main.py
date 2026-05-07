from cfg_input import read_cfg, print_cfg
from parser_engine import parse
from parse_tree import build_parse_tree, draw_parse_tree

def main():

    # 1. CFG input
    print("Enter CFG rules:")
    cfg = read_cfg()

    # 2. print CFG
    print_cfg(cfg)

    # 3. multiple strings loop
    while True:
        string = input("\nEnter string to check (or type 'exit'): ").strip()

        if string.lower() == "exit":
            print("Exiting program...")
            break

        # 4. parsing
        # result, path = parse("S", string, cfg)
        result, path, history = parse("S", string, cfg)
        
        # 5. output
        if result:
            print("\n✔ STRING IS VALID")

            print("\n📌 LEFTMOST DERIVATION:")
            print(" → ".join(path))
            
            # build parse tree
            tree_root = build_parse_tree(history)

            # draw parse tree
            draw_parse_tree(tree_root)
        else:
            print("\n❌ STRING IS INVALID")


if __name__ == "__main__":
    main()