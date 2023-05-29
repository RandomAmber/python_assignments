# Input a number to check if it's formally a valid IBAN number:

input_number = input()

#step 1
#delete spaces
number = input_number.replace(" ", "")

#step 2
#place the country code and the 2-digit-code into the end of the number
country_code = number[:4]
number = number[4:]
number_country_code = number + country_code

#step 3 
#encode the country code into digits
def encode(string):
    letter_to_number = {
    'A': '10', 'B': '11', 'C': '12', 'D': '13', 'E': '14', 'F': '15',
    'G': '16', 'H': '17', 'I': '18', 'J': '19', 'K': '20', 'L': '21',
    'M': '22', 'N': '23', 'O': '24', 'P': '25', 'Q': '26', 'R': '27',
    'S': '28', 'T': '29', 'U': '30', 'V': '31', 'W': '32', 'X': '33',
    'Y': '34', 'Z': '35'
}
    for letter, number in letter_to_number.items():
        string = string.replace(letter, number)
        
    return string


number_encoded = encode(number_country_code)

#step 4
#check whether number % 97 = 1 and the number.len is 18 digits + 2 letters (or + 4 digits)

number_length = len(number_encoded)
number_int = int(number_encoded)
remainder = number_int % 97
if (remainder == 1) and (number_length == 20):
    print("This was a valid iban number!")
else:
    print("This wasn't a valid iban number!")
