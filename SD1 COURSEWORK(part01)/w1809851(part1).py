# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1809851
# Date: 11/11/2020

#Assigned variables
pass_credits=0
defer_credits=0
fail_credits=0

#user inputs
pass_credits = int(input("Please enter your credits at pass: "))
defer_credits = int(input("Please enter your credit at defer: "))
fail_credits = int(input("Please enter your credit at fail: "))

#Conditional statement
if pass_credits==120:
    print("Progress")    
elif pass_credits==100:
    print("Progress (module trailer)")
elif fail_credits>=80:
    print("Exclude")       
elif (pass_credits<=80)and(pass_credits>=0):
    print("Do not Progress – module retriever")


