
## How US taxes work

We take your gross salary. (eg $100,000)

We first take out federal taxes, income brackets are explained in the attached images.

Then based on the state where the person lives, we take out state taxes, again using brackets shown as examples for California and New York attached.

Then there are also city taxes, you can optionally include these in your program.

The caveat is that taxes are not calculated on the full gross salary, instead we first deduct a standard deduction and only calculate taxes based on the deducted amount.

Figures for standard deductions are show in the starter file.

Lastly, we deduct FICA (Federal Insurance Contributions ) from the salary, but crucially, this is calculated based on gross salary before the standard deduction.

## Your task

Givedn a gross salary, GROSS_SALARY and state, STATE, calculate net salary after tax and FICA up to a salary of $100,000. (you can do it for all salary levels if you want)

I recommend you to approach this in a few steps:

1. Calculate federal tax, first remembering to deduct a standard deduction in your calculation. (tip: save a separate variable called 'deducted_salary')
2. Calculate state taxes based on the STATE. (tip: define separate functions for each state and run them based on an if statement)
3. Calculate FICA (remember to use gross salary, not deducted_salary)
4. Save all of the above results into separate variables and deduct them from GROSS_SALARY to get NET_SALARY and TAX_PERCENTAGE which you should finally return