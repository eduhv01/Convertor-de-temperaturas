def celsius_para_fahrenheit(celsius):
  """Converte temperatura em Celsius para Fahrenheit."""
  fahrenheit = (celsius * 9/5) + 32
  return fahrenheit

def celsius_para_kelvin(celsius):
  """Converte temperatura em Celsius para Kelvin."""
  kelvin = celsius + 273.15
  return kelvin

def fahrenheit_para_celsius(fahrenheit):
  """Converte temperatura em Fahrenheit para Celsius."""
  celsius = (fahrenheit - 32) * 5/9
  return celsius

def fahrenheit_para_kelvin(fahrenheit):
  """Converte temperatura em Fahrenheit para Kelvin."""
  kelvin = (fahrenheit - 32) * 5/9 + 273.15
  return kelvin

def kelvin_para_celsius(kelvin):
  """Converte temperatura em Kelvin para Celsius."""
  celsius = kelvin - 273.15
  return celsius

def kelvin_para_fahrenheit(kelvin):
  """Converte temperatura em Kelvin para Fahrenheit."""
  fahrenheit = (kelvin - 273.15) * 9/5 + 32
  return fahrenheit

while True:
  # Menu principal
  print("\nEscolha a conversão desejada:")
  print("1. Celsius para Fahrenheit")
  print("2. Celsius para Kelvin")
  print("3. Fahrenheit para Celsius")
  print("4. Fahrenheit para Kelvin")
  print("5. Kelvin para Celsius")
  print("6. Kelvin para Fahrenheit")
  print("7. Sair")

  opcao = input("Digite sua opção: ")

  if opcao == '1':
    # Celsius para Fahrenheit
    temperatura_celsius = float(input("Digite a temperatura em Celsius: "))
    temperatura_fahrenheit = celsius_para_fahrenheit(temperatura_celsius)
    print(f"{temperatura_celsius:.2f}°C equivalem a {temperatura_fahrenheit:.2f}°F")
  elif opcao == '2':
    # Celsius para Kelvin
    temperatura_celsius = float(input("Digite a temperatura em Celsius: "))
    temperatura_kelvin = celsius_para_kelvin(temperatura_celsius)
    print(f"{temperatura_celsius:.2f}°C equivalem a {temperatura_kelvin:.2f}K")
  elif opcao == '3':
    # Fahrenheit para Celsius
    temperatura_fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    temperatura_celsius = fahrenheit_para_celsius(temperatura_fahrenheit)
    print(f"{temperatura_fahrenheit:.2f}°F equivalem a {temperatura_celsius:.2f}°C")
  elif opcao == '4':
    # Fahrenheit para Kelvin
    temperatura_fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    temperatura_kelvin = fahrenheit_para_kelvin(temperatura_fahrenheit)
    print(f"{temperatura_fahrenheit:.2f}°F equivalem a {temperatura_kelvin:.2f}K")
  elif opcao == '5':
    # Kelvin para Celsius
    temperatura_kelvin = float(input("Digite a temperatura em Kelvin: "))
    temperatura_celsius = kelvin_para_celsius(temperatura_kelvin)
    print(f"{temperatura_kelvin:.2f}K equivalem a {temperatura_celsius:.2f}°C")
  elif opcao == '6':
    # Kelvin para Fahrenheit
    temperatura_kelvin = float(input("Digite a temperatura em Kelvin: "))
    temperatura_fahrenheit = kelvin_para_fahrenheit(temperatura_kelvin)
    print(f"{temperatura_kelvin:.2f}K equivalem a {temperatura_fahrenheit:.2f}°F")
  elif opcao == '7':
    # Sair
    print("Saindo do programa")
    break
  else:
    print("Opção inválida. Tente novamente.")
