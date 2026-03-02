"""
*problem statment
we need to devlop a program . it will tell us if a program is eligible for voting. it will take the person's age as input and tell Allowed to vote or Not Allowed to vote.
but the country has a role, the females will be able to vote if they are 18 years and above and males will be able to vote if they are 20 years and above.
"""
"""
*steps to solve the problem
1. enter input: from user age and gender
2. data verification: type validation( if input data are in correct formet or not)
3. check eligibility: 
    if gender == male and age>=20;
        eligibile
    elif gender == female and age>=18;
        eligibile
    else;
        not eligibile    
"""
#take input:
age=int('input(your age:'))
gender=input('your gender(male/female):')

#data validation:input validation
if gender !='male' or gender !='female':
    print('invalid gender')
    return


