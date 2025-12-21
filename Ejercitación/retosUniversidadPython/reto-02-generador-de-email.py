nombre_usuario = 'Leandro Villalba'
nombre_usuario_normalizado = nombre_usuario.lower().replace(' ','.')
dominio = '.com'
nombre_empresa = 'Empresa X'
dominio_email_normalizado = nombre_empresa.lower().replace(' ','') + dominio

print('*** Generador de email ***')
print(f'Nombre de usuario: {nombre_usuario}')
print(f'Nombre usuario normalizado: {nombre_usuario_normalizado}\n')
print(f'Nombre de empresa: {nombre_empresa}')
print(f'Extensión de dominio: {dominio}')
print(f'Dominio de email normalizado: {dominio_email_normalizado}\n')
print(f'Email final generado: {nombre_usuario_normalizado}@{dominio_email_normalizado}')