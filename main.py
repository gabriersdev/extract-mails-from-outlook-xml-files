import xmltodict
import csv

ok = True
i = 1

# max_indices = 1081
max_indices = 1

data = [
    ["Email", "Full Name"],
]

while ok:
  filepath = f"./files/email ({i}).xml"
  print(f"Abrindo o arquivo {filepath}")

  try:
    try:
      with open(filepath, 'r', encoding='utf-8') as file:
        xml_data = file.read()
    except UnicodeDecodeError:
      with open(filepath, 'r', encoding='utf-16') as file:
        xml_data = file.read()

    # Converter XML para dicionário Python
    data_dict = xmltodict.parse(xml_data)

    # Manipular o JSON (adicione a lógica que você precisar) - exemplo: Modificar o valor do CDATA
    try:
      value = data_dict["message"]["properties"][0]["property"][3]["Value"]
      print(value if value else "Retorno nulo ou vazio")

      if not value:
        continue

      with open("result", "r") as result_file:
        content = result_file.read()
        content_split = content.split("\n")

        # for c in content_split:
        #   if c.strip():
        #     data.append([c, c])

        if value not in content_split:
          with open("result", "a") as file_append:
            file_append.write(f"{value}\n")
            data.append([value, value])
    except Exception as e:
      print(e)

  except Exception as e:
    print(e)
  finally:
    i += 1

    if i > max_indices:
      ok = False


# Criar o arquivo CSV
with open("pessoas.csv", "w", newline="", encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(data)

print("Arquivo CSV criado com sucesso")
