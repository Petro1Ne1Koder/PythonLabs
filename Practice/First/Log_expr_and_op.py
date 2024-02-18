var1 = 5
var2 = 10

log_expr_and1 = (var1 < var2) and (var1 != var2)
log_expr_and2 = (var1 == var2) and (var1 > var2)

log_expr_or1 = (var1 < var2) or (var1 != var2)
log_expr_or2 = (var1 == var2) or (var1 > var2)

print("Logical expression with AND operators:", log_expr_and1, log_expr_and2)
print("Logical expression with OR operators:", log_expr_or1, log_expr_or2)