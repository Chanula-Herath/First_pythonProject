# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1809851
# Date: 11/11/2020

#Assigned variables
pass_credits=0
defer_credits=0
fail_credits=0
credit_range=(0,20,40,60,80,100,120)

#Validations
while True:
    try:
        pass_credits =int(input("Please enter your credits at pass: "))
        if pass_credits not in credit_range:
            raise TypeError        
    except ValueError:
        print("Integer required\n")
    except TypeError:
        print("Out of range.\n")
    
    else:        
        try:
            defer_credits =int(input("Please enter your credit at defer: "))
            if defer_credits not in credit_range:
                raise TypeError
        except ValueError:
            print("Integer required\n")
        except TypeError:
            print("Out of range.\n")
            
        else:
            try:
                fail_credits =int(input("Please enter your credit at fail: ")) 
                if fail_credits not in credit_range:
                    raise TypeError
            except ValueError:
                print("Integer required\n")
            except TypeError:
                print("Out of range.\n")
            
            else:
                total_credits = pass_credits + defer_credits + fail_credits
                if total_credits!=120:
                    print("Total incorrect.\n")

                else:
                    #Conditional statement 
                    if pass_credits==120:
                        print("Progress\n\n")
                        break   
                    elif pass_credits==100:
                        print("Progress (module trailer)\n\n")
                        break
                    elif fail_credits>=80:
                        print("Exclude\n\n")
                        break
                    elif (pass_credits<=80)and(pass_credits>=0):
                        print("Do not Progress – module retriever\n\n")
                        break

                         
    

