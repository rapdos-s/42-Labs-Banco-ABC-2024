from collections import Counter


def pegar_separador(param):
  separador = []
  i = 0
  while i < len(param):
    if not param[i].isalnum() and param[i] != "-":
      separador += param[i]
    i += 1
  return set(separador)


def splitinator(texto, separadores):
  for separador in separadores:
    if separador == " ":
      continue
    texto = texto.replace(separador, " ")
  return texto.split()


def dojo(texto):
  ret = []
  palavras = splitinator(texto, pegar_separador(texto))
  palavras_ocorrencias = Counter(palavras).most_common()
  i = 0
  j = 0
  while j < 3 and i < len(palavras_ocorrencias):
    if verifica_tamanho(palavras_ocorrencias[i][0]):
      ret.append(palavras_ocorrencias[i][0])
      j += 1
    i += 1
  return ret


def verifica_tamanho(param):
  if len(param) < 3:
    return False
  return True


def verifica_tipo_texto(param):
  if type(param) == str:
    return True
  else:
    return False


def baby_steps_game(texto):
  if not verifica_tipo_texto(texto):
    return ([])
  # split
  # coutner
  # check_size
  # take_three
  return dojo(texto)


if __name__ == "__main__":

  def test(index, texto, esperado):
    if baby_steps_game(texto) == esperado:
      print(f"🟢 test {index}: OK")
    else:
      print(f"🔴 test {index}: KO: input: [{texto}] esperado: [{esperado}]")

  test(1, "primeiro primeiro primeiro primeiro@primeiro_terceiro segundo segundo segundo segundo segundo terceiro-terceiro +#@ 123", ["primeiro", "segundo", "terceiro"])
  test(2, 42, [])
  test(3, "Hello, World!", ["Hello", "World"])
  test(4, "Hello, World!", ["Hello", "ABC"])
