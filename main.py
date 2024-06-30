import decode
import encode

print("Welcome to Message Encoder")
print("""
This encoder converts a textual message into blocks of numbers \
(for example, it might convert \"hello\" into 27900 68916). 
The recipient can then use the decoder to convert the numbers \
back into the original message.

Here is a summary of the steps involved in the encoding cipher:
● ensure the message contains only permitted characters
● add in extra random characters to the message based on a customisable key string
● group message into blocks of characters
● substitute characters into numbers
● perform modular division and shifting of the numbers
● create final message, which is a list of blocks of numbers

The decoding process performs these steps in reverse order.

Several variables used in the encoder are preset here, \
but can be changed from the code itself.
""")
instructions = [
  "encode: encode a message",
  "decode: decode a message",
  "exit: exit the program"
]

func = {}
def init_func():
  global func
  def encoder():
    encode.encode_main()
  def decoder():
    decode.decode_main()
  def end():
    print("Exiting program")
    exit(0)
  def help():
    print("\n".join(instructions))

  func = {
    "encode": encoder,
    "decode": decoder,
    "exit": end,
  }
init_func()

print("Instructions:", "\n".join(instructions), "\n", sep="\n")

while True:
  command = input("Enter a command >>> ")
  if command not in func:
    print("Invalid command!\n")
    continue
  func[command]()
  print()