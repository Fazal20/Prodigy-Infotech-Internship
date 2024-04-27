def caesar_cipher(text, shift, mode):
  """Encrypts or decrypts text using Caesar cipher.

  Args:
      text: The text to encrypt or decrypt.
      shift: The number of positions to shift the letters (positive for encryption, negative for decryption).
      mode: 'encrypt' or 'decrypt'

  Returns:
      The encrypted or decrypted text.
  """
  alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
  new_text = ''
  for char in text:
    if char not in alphabet:
      # Keep non-alphabetic characters unchanged
      new_text += char
      continue
    new_index = (alphabet.find(char) + shift) % len(alphabet)
    new_text += alphabet[new_index]
  return new_text

if __name__ == '__main__':
  while True:
    print("Caesar Cipher")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
      text = input("Enter message to encrypt: ")
      shift = int(input("Enter shift value: "))
      encrypted_text = caesar_cipher(text, shift, 'encrypt')
      print("Encrypted message:", encrypted_text)
    elif choice == '2':
      text = input("Enter message to decrypt: ")
      shift = int(input("Enter shift value: "))
      decrypted_text = caesar_cipher(text, -shift, 'decrypt')  # Negative shift for decryption
      print("Decrypted message:", decrypted_text)
    elif choice == '3':
      break
    else:
      print("Invalid choice. Please try again.")