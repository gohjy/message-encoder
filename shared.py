import string

#reserved character
reserved_char = "\0"
reserved_char_name = "null"
reserved_char_raw_code = "\\0"

#encodable characters
all_nonreserved_encodable_chars = (string.ascii_letters 
  + string.punctuation 
  + string.digits 
  + " ")

all_encodable_chars = all_nonreserved_encodable_chars + reserved_char
len_num_all_encodable_chars = len(str(len(all_encodable_chars)))

#key string
key_string = "\
Founders' Memorial \
Tanjong Rhu \
Katong Park \
Tanjong Katong \
Marine Parade \
Marine Terrace \
Siglap \
Bayshore\
"
key_string_arb_separator = " "

#group length
group_length = 3

#shift & modulo factors
modulo_factor = int("9" * (len_num_all_encodable_chars * group_length)) + 1
shift_factor = 3957489

#separator
separator = " "