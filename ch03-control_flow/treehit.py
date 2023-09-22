tree_hit = 0
plan_tree = 100

while tree_hit < 10:
    tree_hit += 1 # treehit = tree_hit + 1 tree_hit++ (X)
    plan_tree -= 1
    print(f"나무를{tree_hit}번 찍었습니다.")
    if tree_hit == 10:
        print("나무넘어갑니다.")

