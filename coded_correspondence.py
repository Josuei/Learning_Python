alphabet = "abcdefghijklmnopqrstuvwxyz"
symbols = " !.?!"
message_encrypt = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
message_decrypt = ""
for letter in message_encrypt:
  if letter not in symbols:
    index_letter = alphabet.find(letter) + 10 - 26
    dec_letter = alphabet[index_letter]
    message_decrypt += dec_letter
  else:
    message_decrypt += letter
print(message_decrypt)

message_to_send = "hey! it was nice to receive your message and learn about caesar cipher. it was challenging. do you know another encrypting systems which we can use to communicate between us?"
message_to_send_encrypt = ""
for letter in message_to_send:
  if letter not in symbols:
    index_letter_ms = alphabet.find(letter) - 10
    enc_letter = alphabet[index_letter_ms]
    message_to_send_encrypt += enc_letter
  else:
    message_to_send_encrypt += letter
print(message_to_send_encrypt)

first_message = "jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud."
def decoder(message, offset):
  message_decrypt = ""
  for letter in message:
    if letter not in symbols:
      index_letter = alphabet.find(letter) + offset - 26
      dec_letter = alphabet[index_letter]
      message_decrypt += dec_letter
    else:
      message_decrypt += letter
  return message_decrypt
def coder(message, offset):
  message_encrypt = ""
  for letter in message:
    if letter not in symbols:
      index_letter_ms = alphabet.find(letter) - offset
      enc_letter = alphabet[index_letter_ms]
      message_encrypt += enc_letter
    else:
      message_encrypt += letter
  return message_encrypt
print(decoder(first_message, 10))

#Vigênere cipher
alphabet = "abcdefghijklmnopqrstuvwxyz"
symbols = " '!.?!"
message_coded = "dfc aruw fsti gr vjtwhr wznj? vmph otis! cbx swv jipreneo uhllj kpi rahjib eg fjdkwkedhmp!"
message_keyword = "friends"

#Contador de caracteres especiales
def counter_symbols(characters):
  num_symbols = 0
  for c in characters:
    if c in symbols:
      num_symbols += 1
  return num_symbols

#Descifrador Vigènere
def vigenere_decoder(message, keyword):
  keyword_message = ""
  decrypted_code = ""
  for index in range(len(message)):
    if index - counter_symbols(message[:index]) < len(keyword):
      keyword_message += keyword[index - counter_symbols(message[:index])]
    else:
      keyword_message += keyword[(index - counter_symbols(message[:index])) % len(keyword)]
  else:
    keyword_message += message[index]
  for index in range(len(message)):
    if message[index] not in symbols:
      index_l1 = alphabet.find(message[index])
      index_l2 = alphabet.find(keyword_message[index])
      dec_letter = alphabet[index_l1 - index_l2]
      decrypted_code += dec_letter
    else:
      decrypted_code += message[index]
  return decrypted_code
print(vigenere_decoder(message_coded, message_keyword))

messaage_to_code = "hi! vishal this was really challenging and even harder to write a function to decipher the coded message. but i did. i hope you're well, do you have another challenge for me?"
#Cifrador Vigênere
def vigenere_coder(message, keyword):
  keyword_message = ""
  crypted_code = ""
  for index in range(len(message)):
    if index - counter_symbols(message[:index]) < len(keyword):
      keyword_message += keyword[index - counter_symbols(message[:index])]
    else:
      keyword_message += keyword[(index - counter_symbols(message[:index])) % len(keyword)]
  else:
    keyword_message += message[index]
  for index in range(len(message)):
    if message[index] not in symbols:
      index_l1 = alphabet.find(message[index])
      index_l2 = alphabet.find(keyword_message[index])
      cod_letter = alphabet[index_l1 + index_l2 - len(alphabet)]
      crypted_code += cod_letter
    else:
      crypted_code += message[index]
  return crypted_code
coded_message = vigenere_coder(messaage_to_code, message_keyword)
print(coded_message)
print(vigenere_decoder(coded_message, message_keyword))