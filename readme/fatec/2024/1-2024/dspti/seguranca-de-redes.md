# Segurança de Redes

Maiores problemas de redes que podemos ter:

o meio broadcast, placas de rede em modo promíscuo (captura todos os dados, podem ser lidos sejam eles criptografados ou não)

correlação de chaves: d-b(e-b(m))) sendo que m = mensagem, e = criptogragia, d = decriptografia

encriptar com a chave publica e decriptar com a chave privada em caso de autenticidade encriptar com a chave privada e decriptar com a chave publica em caso de confidencialidade

Um chave publica é trocada através de um servidor confiavel, ou centro de distribuição de chaves confiável (KDC) Para confirmar que uma chave publica é de aguém basta verificar em uma autiridade certificadora confiável (CA)

Procurar o sistema de estágio da faculdade para conseguir concluir o período de estágio da faculdade como um padrão

script para trabalhar com hashing no python:

import hashlib

string2hash = Texto result = hashlib.md5(sting2hash.encode()) print(result.hexdigest())

result = hashlib.sha256(sting2hash.encode()) print(result.hexdigest())

Comando para acompanhar os logs em tempo real: watch -n 1 cat var/log/syslog