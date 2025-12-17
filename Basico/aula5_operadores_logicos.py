# and
# or
# not

usuario = input('Digite seu usuário: ')
senha = input('Digite sua senha')

login_valido = usuario == 'Admin' and senha = '123admin'

print(f'Login Permitido: {login_valido}')