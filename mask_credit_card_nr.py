'''
1. korisnik unosi broj kreditne kartice
2. maskiramo broj kartice
'''
def mask_credit_card_number(credit_card_number: str, 
                            masking_character: str = '#', 
                            unmasked_numbers: int = 4) -> str:
    # return masking_character * (len(credit_card_number) - unmasked_numbers) + credit_card_number[-unmasked_numbers : ]

    if len(credit_card_number) < unmasked_numbers:
        print('Broj kreditne kartice je prekratak!!!')
        return '1'

    masked_ccn = ''

    index = 0
    for number in credit_card_number:
        if number == '-' or number == ' ':
            masked_ccn += number
            continue
        if index < (len(credit_card_number) - unmasked_numbers):
            masked_ccn += masking_character
            index += 1
        else:
            masked_ccn += number
            index += 1

    # for index, number in enumerate(credit_card_number):
    #     if number == '-' or number == ' ':
    #         masked_ccn += number
    #         continue
    #     if index < (len(credit_card_number) - unmasked_numbers):
    #         masked_ccn += masking_character
    #     else:
    #         masked_ccn += number

    #     # if number == '-' or number == ' ':
    #     #     masked_ccn += number
    #     # elif index < (len(credit_card_number) - unmasked_numbers):
    #     #     masked_ccn += masking_character
    #     # else:
    #     #     masked_ccn += number
    
    return masked_ccn























masked_ccn = ''

credit_card_number = input('Upisite broj kreidtne kartice: ')
user_choice = input('Zelite li mijenjati znak skiravnja brojeva? (Da/Ne) ')
if user_choice.lower() == 'da':
    masking_sign = input('Upisite znak za skiravnje brojeva: ')
    unmasked_numbers = int(input('Koliko brojeva zelite ostaviti otkrivenih?: '))
    masked_ccn = mask_credit_card_number(credit_card_number, 
                                         masking_sign, 
                                         unmasked_numbers=unmasked_numbers)
else:
    masked_ccn = mask_credit_card_number(credit_card_number)


print(masked_ccn)
# 123452342-5644-4658-4586
# #########-####-####-4586
# 12345 32435644 4658 4586
# ***** ******** **58 4586
