usuario = {
    'nome' : 'Monicke',
    'idade' : 32,
    'departamento' : 'TI'
}

print(usuario) 
print(usuario['nome']) # Para buscar informação específica
print(usuario['idade'])
print(usuario['departamento'])

usuario['idade'] = 33 # Para alterar informação

print(usuario)

usuario['cidade'] = 'Porto Alegre' # Adiciona nova key + valor
