# Aula criptografia 08-29-2024

Uma senha encriptada pode ser facilmente detectada de acordo com o website https://crackstation.com; pois senhas fracas já estão inseridas em wordlists que casam o valor dos hashes com a senha (pois o processo de hash é de via unica), ou seja, para detectar qual a senha que gerou o hash o atacante irá comparar o hash com padrões de hashes presetes em bancos de senhas (wordlists).

aPara evitar a facil detecção da senha basta inserir o conceito de 'salt', que é o incremento de um valor específico ao texto plano da senha antes de encriptar, o que faz com que o padrão de hash no final seja alterado e saia do padrão, fazendo com que o padrão não seja detectado em wordlists.

hmac -> muito mais seguro, usa como se fossee o salt, em provedores de nuvem e (esqueci o outro).

Nas atividades fazremos o processo de configurar o OpeSSL e tratar o processo como um processo de criptografia pura.
