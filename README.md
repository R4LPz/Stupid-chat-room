# Chat room

Este repositório consistem em uma CLI construída em python para simular um sistema de chat publico em tempo real.
*PS: Este é um código com finalidade de aprendizado e não deve ser usado em produção*

## Sobre

```
.
├── app
│   ├── backups
│   ├── client.py
│   ├── logs
│   │   └── 2022-07-05.log
│   └── server.py
└── README.md
 
```

O projeto foi construido para ser o mais simples possível, basicamente seu funcionamento consiste em criar um ponto de acesso que recebe uma conexão e cria uma thread que permite que a mesma envie e receba mensagens em tempo real. 

A estrutura consiste em dois arquivos principais, o servidor, responsável por estabelecer uma interface de comunicação entre pontos conectados e o cliente, responsável por entregar ao usuário uma CLI passível de leitura e escrita de mensagens no chat publico do server.

## Execução 

Para executar o projeto você precisará instalar o python em sua máquina. [Documentação](https://www.python.org/downloads/)

Inicialmente execute o comando a seguir para executar o servidor e disponibilizar uma porta de conexão:

``` 
$ pyhton ./app/server.py
```

Para se conectar ao servidor por um cliente execute o arquivo client.py:

``` 
$ python ./app/client.py 
```

## Documentação e links úteis

Para mais informações, você pode visitar a documentação da biblioteca [Socket](https://docs.python.org/pt-br/3/howto/sockets.html) do python e a própria [Documentação](https://docs.python.org/3/) da linguagem.

Além disso o [artigo](https://www.geeksforgeeks.org/simple-chat-room-using-python/) da GeeksForGeeks pode ser útil.