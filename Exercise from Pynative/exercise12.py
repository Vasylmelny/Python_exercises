# Calculate income tax for the given income by adhering to the rules below
#
# Taxable Income	Rate (in %)
# First $10,000	0
# Next $10,000	10
# The remaining	20
# Expected Output:
#
# For example, suppose the income is 45000, and the income tax payable is
#
# 10000*0% + 10000*10%  + 25000*20% = $6000

tax = int(input("Enter the tax: "))
bablo2 = 0
if tax < 10000:
    bablo1 = 0
elif tax <= 20000:
    bablo1 = tax - 10000
else:
    bablo1 = 10000
    bablo2 = tax - 20000
barysh = bablo1 * 0.1 + bablo2 * 0.2
print(barysh)