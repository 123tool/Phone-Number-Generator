import phonenumbers

class LeadValidator:
    @staticmethod
    def validate(number_list):
        valid_numbers = []
        invalid_count = 0
        
        for num in number_list:
            try:
                parsed_num = phonenumbers.parse(num, None)
                if phonenumbers.is_valid_number(parsed_num):
                    # Kita simpan dalam format internasional yang bersih
                    formatted = phonenumbers.format_number(parsed_num, phonenumbers.PhoneNumberFormat.E164)
                    valid_numbers.append(formatted)
                else:
                    invalid_count += 1
            except:
                invalid_count += 1
                
        return valid_numbers, invalid_count
