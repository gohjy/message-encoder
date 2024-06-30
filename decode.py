import shared


def decode_main():
  print("Running decoder\n")
  
  #shift, modulo, substitute, reserved char, ungroup, random characters (key string) ##
  
  # print("enter variables:")
  key_string = ""
  # key_string = input("key string press enter to use default: ")
  if key_string == "":
    key_string = shared.key_string
  key_string_arb_separator = ""
  # key_string_arb_separator = input(
  #   "key string arb separator press enter to use default: "
  # )
  if key_string_arb_separator == "":
    key_string_arb_separator = shared.key_string_arb_separator
  group_length = ""
  # group_length = input("group length press enter to use default: ")
  group_length = shared.group_length if group_length == "" else int(group_length)
  shift_factor = ""
  # shift_factor = input("shift factor press enter to use default: ")
  shift_factor = shared.shift_factor if shift_factor == "" else int(shift_factor)
  modulo_factor = ""
  # modulo_factor = input("modulo factor press enter to use default: ")
  modulo_factor = shared.modulo_factor if modulo_factor == "" else int(modulo_factor)
  
  # print("\n\n")
  encoded_message = input("Please enter the encoded message: ")
  message_encoded_list = encoded_message.split(shared.separator)
  # print("Encoded list:", message_encoded_list)
  message_encoded_int_list = [int(i) for i in message_encoded_list]
  # print("Encoded int list:", message_encoded_int_list)
  
  # print()
  #shift
  message_unshift_list = [(i - shift_factor) for i in message_encoded_int_list]
  # print("Unshifted list:", message_unshift_list)
  #modulo
  message_unmodulo_list = [(i % modulo_factor) for i in message_unshift_list]
  # print("Unmodulo list:", message_unmodulo_list)
  
  # print()
  #substitute
  message_string_list = [str(i) for i in message_unmodulo_list]
  # print("String list:", message_string_list)
  message_padded_list = [
    i.zfill(
      group_length * shared.len_num_all_encodable_chars
    ) for i in message_string_list
  ]
  # print("Padded list:", message_padded_list)
  # print()
  message_alpha_list = []
  for char_group in message_padded_list:
    message_alpha_list.append("")
    char_codes = [
      int(char_group[
          n:n+(shared.len_num_all_encodable_chars)
          ]) for n in range(0, len(char_group), shared.len_num_all_encodable_chars)
    ]
    for char_code in char_codes:
      if char_code < len(shared.all_encodable_chars):
        message_alpha_list[-1] += shared.all_encodable_chars[char_code]
      else:
        print(
          "Error: message contains invalid character code \"", char_code, "\"", sep=""
        )
        return
  # print("Message decoded into original:", message_alpha_list)
  
  # print()
  #reserved char
  message_no_reserved = message_alpha_list[:-1]
  message_no_reserved.append(message_alpha_list[-1].rstrip(shared.reserved_char))
  # print("Message without reserved char:", message_no_reserved)
  
  # print()
  #ungroup
  message_string = "".join(message_alpha_list)
  # print("Message ungrouped:", message_string)
  
  # print()
  #random chars
  message_final = ""
  j = 0
  k = 0
  for k in range(len(message_string)):
    if key_string[j] != key_string_arb_separator:
      message_final += message_string[k]
    j += 1
    if j >= len(key_string):
      j = 0
  
  print("FINAL MESSAGE:", message_final)

if __name__ == "__main__":
  decode_main()