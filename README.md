# Chat room

O projeto consiste em uma sala de chat pública via linha de comando, através da conexão feita por sockets, é possível se comunicar com outros usuários online e executar comandos dentro da sala. 
A construção foi baseada nos antigos IRC's, porém de forma simplista, sendo ela construída em python3 e utilizando a interface de sockets da linguagem.

*PS: Este é um código com finalidade de aprendizado e não deve ser usado em produção*

## Sobre

Como dito anteriormente, o  projeto foi construido para ser o mais simples possível, funcionando sobre uma interface de sockets, o código consiste basicamente na criação de uma arquitetura client-servidor onde o servidor atua como um ponto de acesso, recebendo conexões e criando para cada uma delas, uma thread que permite com que o usuário envie e receba mensagens instantâneas, bem como execute comandos predefinidos pelo servidor. 

A estrutura é composta por dois arquivos principais, e dois diretórios auxiliares. Sendo que o serve atua como um intermediados dos comando enviados pelos vários clients conectados a ele. A seguir a estrutura de diretórios que o sistema opera:

```
    .
    ├── app
    │   ├── backups
    │   ├── logs
    │   ├── client.py
    │   └── server.py
    └── README.md
 
```

## Execução 

Para a execução do projeto, é necessário que você tenha o python3 instalado em sua máquina. Caso não tenha, efetue o download e instalação seguindo a [Documentação](https://www.python.org/downloads/).

Com o python instalado, você deve querer executar inicialmente o servidor, isso pode ser feito através do comando a seguir:

``` 
$ pyhton ./app/server.py
```

Com o servidor operando corretamente, a porta 6666 estará em uso e é nela onde o client deve se conectar, para isso execute o seguinte comando:

``` 
$ python ./app/client.py 
```

## Documentação e links úteis

Para mais informações, você pode visitar a documentação da biblioteca [Socket](https://docs.python.org/pt-br/3/howto/sockets.html) do python e a própria [Documentação](https://docs.python.org/3/) da linguagem.

Além disso o [artigo](https://www.geeksforgeeks.org/simple-chat-room-using-python/) da GeeksForGeeks pode ser útil.