amount = eval(input("Enter an amount, for example 11.56: "))

remainingAmount = int(amount*100)

numberofDollars=remainingAmount //100
remainingAmount=remainingAmount % 100

numberofQuarters=remainingAmount //25
remainingAmount=remainingAmount % 25

numberofDimes=remainingAmount //10
remainingAmount=remainingAmount % 10

numberofNickels=remainingAmount //5
remainingAmount=remainingAmount % 5

numberofPennies=remainingAmount

print("Your amount",amount,"consists of \n",
      "\t",numberofDollars,"dollars\n",
"\t",numberofQuarters,"quarters\n",
"\t",numberofDimes,"dimes\n",
"\t",numberofNickels,"nickels\n",
"\t",numberofPennies,"pennies\n")