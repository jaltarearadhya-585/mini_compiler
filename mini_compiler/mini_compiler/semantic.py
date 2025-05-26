def semantic_analysis(parsed_tree):
    # Simple semantic analysis (for illustration purposes)
    if parsed_tree[0] == 'binop':
        print("Semantic analysis: Valid binary operation")
    elif parsed_tree[0] == 'id':
        print(f"Semantic analysis: Variable '{parsed_tree[1]}' is valid.")
    else:
        print("Semantic analysis: Error!")
