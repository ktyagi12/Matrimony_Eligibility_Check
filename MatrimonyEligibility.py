#Matrimony Application
'''
PROBLEM STMT: Take input of 2 user (Name, Gender and Age) and check eligibility   of marriage.
'''
print '*' * 150
gender_user1 = 'f'
gender_user2 = 'm'   
def user1():
    print '\t\t\tUser 1 Details'
    name_usr1 = raw_input('\t\t\tEnter your name: ')
    gender_user1 = raw_input('\t\t\tEnter your gender: ').upper()
    year_of_birth_user1 = input('\t\t\tEnter your year of birth (YYYY): ')
    print '=' * 100
    if(gender_user1 == '' or year_of_birth_user1 == '' or name_usr1 == '' ):
        print 'SORRY! You have not entered the details..'
        user1()
    else:
        if (gender_user1 == 'FEMALE' or gender_user1 == 'F'):
            if(year_of_birth_user1 <=2000):
                print ('\t\t\t..WELCOME BEAUTIFUL TO KTYAGI MATRIMONY..')
            else:
                print ('\t\t\t..SORRY LADY, YOU ARE NOT ELIGIBLE FOR MARRIAGE RIGHT NOW.')
                exit()    
        elif(gender_user1 == 'MALE' or gender_user1 == 'M'):
            if(year_of_birth_user1 <=1998):
                print ('\t\t\t..WELCOME HANDSOME TO KTYAGI MATRIMONY..')
            else:
                print ('\t\t\t..SORRY YOUNG MAN, YOU ARE NOT ELIGIBLE FOR MARRIAGE RIGHT NOW.')
                exit()
        else:
            print('\t\t\tWE ARE EXTREMELY SORRY. WE HAVE NO OPTIONS FOR YOU GUYS..')
            exit()
        
def user2():
    print '=' * 100
    print '\t\t\tUser 2 Details'
    name_usr2 = raw_input('\t\t\tEnter your name: ')
    gender_user2 = raw_input('\t\t\tEnter your gender: ').upper()
    year_of_birth_user2 = input('\t\t\tEnter your year of birth (YYYY): ')
    if(gender_user2 == '' or year_of_birth_user2 == '' or name_usr2 == '' ):
       print 'SORRY! You have not entered the details..'
       user2()
    else:    
        if (gender_user2 == 'FEMALE' or gender_user2 == 'F'):
           if(year_of_birth_user2 <=2000):
               print ('\t\t\t..WELCOME BEAUTIFUL TO KTYAGI MATRIMONY..')
           else:
               print ('\t\t\t..SORRY LADY, YOU ARE NOT ELIGIBLE FOR MARRIAGE RIGHT NOW.')
               exit()
                
        elif(gender_user2 == 'MALE' or gender_user2 == 'M'):
            if(year_of_birth_user2 <=1998):
                print ('\t\t\t..WELCOME HANDSOME TO KTYAGI MATRIMONY..')
            else:
                print ('\t\t\t..SORRY YOUNG MAN, YOU ARE NOT ELIGIBLE FOR MARRIAGE RIGHT NOW.')
                exit()
        else:
            print('\t\t\tWE ARE EXTREMELY SORRY. WE HAVE NO OPTIONS FOR YOU GUYS..')
            exit()

print '*' * 100
print('\t\t\tWE MAKE MATCHES....')
user1()
user2()
if(gender_user1 != gender_user2):
    print '\t\t\t WUHUUU!!! FOUND A MATCH FOR YOU.'
else:
    print '\t\t\t SORRY!! YOU GUYS CANNOT MARRY..'
    
