import random
import string

import shared


def encode_main():
  print("Running encoder\n")
  
  #prerequisites
  print(
    "Message may contain lowercase and uppercase letters, \
digits, punctuation and space."
  )
  # get message
  message = input("Please enter message: ")

  # check for empty message
  if message == "":
    print("Error: message cannot be empty")
    return
  # check for reserved character
  if shared.reserved_char in message:
    print(
      f"""Error: message may not contain {
        shared.reserved_char_name
      } character ({
  shared.reserved_char_raw_code
      }"""
    )
    return
  # else:
  #   print(
  #     "Reserved character not found in message, continuing to process message ...\n"
  #   )
  
  #add null characters
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
  
  random_message = []
  
  j = 0
  k = 0
  while True:
    if key_string[j % len(key_string)] != key_string_arb_separator:
      random_message.append(message[k])
      k += 1
    else:
      xx_temp = random.choice(shared.all_nonreserved_encodable_chars)
      random_message.append(xx_temp)
      
    j += 1
    if k == len(message):
      break
      
  
  message = "".join(random_message)
  # print("Message with null (random) characters added:", message)
  # print("Continuing to process message ...\n")
  
  #group message
  ## reserved char
  group_length = ""
  # group_length = input("group length press enter to use default: ")
  group_length = shared.group_length if group_length == "" else int(group_length)
  
  # print("Current length of message:", len(message))
  # print("Now adding reserved char (" + shared.reserved_char + ")...")
  
  num_reserved_chars = group_length - (
    len(message) % group_length
  )
  
  if num_reserved_chars == group_length:
    num_reserved_chars = 0
  message += (
    shared.reserved_char * num_reserved_chars
  )
  # print("New length of message:", len(message))
  # print()
  
  
  message_grouped_list = [
    message[
      n:n+(group_length)
    ] for n in range(
      0, len(message), group_length
    )
  ]
  # print("Message grouped:", message_grouped_list)
  # print()
  #encode message
  ##substitution
  message_encoded_list = []
  for char_group in message_grouped_list:
    message_encoded_list.append("")
    for char in char_group:
      if char in shared.all_encodable_chars:
        message_encoded_list[-1] += str(
          shared.all_encodable_chars.index(char)
        ).zfill(
          shared.len_num_all_encodable_chars
        )
      else:
        print("Error: message contains invalid character \"", char, "\"", sep="")
        return
  # print("Message encoded into numbers:", message_encoded_list)
  
  message_encoded_int_list = [int(i) for i in message_encoded_list]
  # print("Message turned into ints:" , message_encoded_int_list)
  # print()
  
  ##modulo & shift
  shift_factor = ""
  # shift_factor = input("shift factor press enter to use default: ")
  shift_factor = shared.shift_factor if shift_factor == "" else int(shift_factor)
  message_shifted_list = [(i + shift_factor) for i in message_encoded_int_list]
  # print("Shift factor:", shift_factor)
  # print("Shifted list:" , message_shifted_list)
  modulo_factor = ""
  # modulo_factor = input("modulo factor press enter to use default: ")
  modulo_factor = shared.modulo_factor if modulo_factor == "" else int(modulo_factor)
  
  message_modulo_list = [(i % modulo_factor) for i in message_shifted_list]
  # print("Modulo factor:", modulo_factor)
  # print("Modulo list:", message_modulo_list)
  
  # final message
  message_final_encoded_str = " ".join([str(i) for i in message_modulo_list])
  
  print("ENCODED MESSAGE:", message_final_encoded_str, sep=shared.separator)

if __name__ == "__main__":
  encode_main()