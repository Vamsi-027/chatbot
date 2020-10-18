# evaluates expression
def eval_exp():
    expr = input("Enter an expression")
    try:
        print("Result:", eval(expr))
        print("-----------------")
    except Exception as e:
        print("Enter a valid expression")
        print("ERROR:", str(e))
