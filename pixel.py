from PIL import Image

def encrypt_decrypt(image_path, key, mode):
  """Encrypts or decrypts an image using XOR operation on pixels.

  Args:
      image_path: Path to the image file.
      key: A secret key (integer) used for encryption/decryption.
      mode: 'encrypt' or 'decrypt'
  """
  img = Image.open(image_path)
  width, height = img.size
  pixels = img.load()

  # Loop through each pixel and apply XOR with key
  for i in range(width):
    for j in range(height):
      r, g, b = pixels[i, j]
      if mode == 'encrypt':
        new_r, new_g, new_b = r ^ key, g ^ key, b ^ key
      else:
        new_r, new_g, new_b = r ^ key, g ^ key, b ^ key
      pixels[i, j] = (new_r, new_g, new_b)

  # Save the modified image
  img.save(f"{image_path[:-4]}_{mode}.png")  # Add suffix based on mode

if __name__ == '__main__':
  while True:
    print("Image Encryption Tool")
    print("1. Encrypt Image")
    print("2. Decrypt Image")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
      image_path = input("Enter image path: ")
      key = int(input("Enter secret key (integer): "))
      encrypt_decrypt(image_path, key, 'encrypt')
      print("Image encrypted successfully!")
    elif choice == '2':
      image_path = input("Enter encrypted image path: ")
      key = int(input("Enter secret key used for encryption: "))
      encrypt_decrypt(image_path, key, 'decrypt')
      print("Image decrypted successfully!")
    elif choice == '3':
      break
    else:
      print("Invalid choice. Please try again.")