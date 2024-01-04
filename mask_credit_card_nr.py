'''
1. korisnik unosi broj kreditne kartice
2. maskiramo broj kartice
'''
def mask_credit_card_number(credit_card_number: str, 
                            masking_character: str = '#', 
                            unmasked_numbers: int = 4) -> str:
    return masking_character * (len(credit_card_number) - unmasked_numbers) + credit_card_number[-unmasked_numbers : ]























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
# 12345-5644-4658-4586
# #####-####-####-4586
# 12345 5644 4658 4586
# ***** **** **58 4586
