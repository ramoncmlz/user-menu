🇧🇷 Português | 🇺🇸 [English](README.md)

## 📌 Sobre o SimpleAuth

SimpleAuth é uma **API de autenticação de usuários desenvolvida com FastAPI**, criada com o objetivo de evoluir um sistema de login que antes rodava apenas no terminal para uma **arquitetura baseada em requisições HTTP**.

O uso do FastAPI permite separar a lógica de autenticação da interface, tornando o sistema mais organizado, reutilizável e preparado para futuras integrações, como aplicações web, mobile ou frontends em geral.

Atualmente, os dados dos usuários são mantidos **em memória**, simulando o funcionamento de um sistema real enquanto os conceitos são aprendidos.

---

## ⚙️ Funcionalidades atuais

- 🧑‍💻 Registro de usuários via endpoint (`/register`)
- 🔐 Login com controle de tentativas inválidas
- ⏳ Bloqueio temporário após exceder o número de tentativas
- 🚪 Logout de usuários autenticados
- ✏️ Alteração de nome de usuário
- 🔄 Alteração de senha
- 🛡️ Usuário administrador com permissões especiais
- ❌ Exclusão de usuários (somente admin)
- 📋 Listagem de usuários (somente admin)
- 🌐 API REST usando FastAPI

---

## 🧠 Como o sistema funciona

- Cada usuário é representado por uma **classe `User`**, contendo:
  - `user_id`
  - `username`
  - `password`
  - `is_logged`
  - `attempts`
  - `blocked_until`

- Os usuários são armazenados em uma **lista em memória** (`user_list`).
- A API expõe endpoints que manipulam esses usuários através de requisições HTTP.
- O controle de autenticação é feito por estado (`is_logged`), simulando sessões.
- O sistema implementa:
  - validação de nome do usuário
  - validação de senha
  - controle de tentativas
  - bloqueio temporário usando `datetime` e `timedelta`

---

## 🆕 O que há de novo em relação à versão anterior

- 🔁 O sistema deixou de ser apenas um menu de terminal
- 🌐 Passou a funcionar como uma **API REST**
- 🧱 Uso de **FastAPI** para estruturar rotas e regras de negócio
- 🧠 Separação clara entre:
  - validação
  - regras de autenticação
  - controle de usuários
- 🚀 Código preparado para persistência real de dados

---

## 🎯 Por que FastAPI foi usado

O FastAPI foi escolhido para:
- aprender como sistemas de login funcionam em **backends reais**
- expor funcionalidades via HTTP
- preparar o projeto para integração com banco de dados
- facilitar testes com ferramentas como Postman ou Swagger
- tornar o código mais escalável e organizado

---

## 🚧 Próximos passos

- 🗄️ Implementar um **banco de dados relacional (SQLite)** para persistência de usuários
- 🔒 Adicionar **hashing de senhas** (ex: bcrypt)
- 🧩 Substituir armazenamento em memória por **camada de persistência**
- 🔑 Implementar autenticação baseada em **tokens (JWT)**
- 🧪 Melhorar tratamento de erros e validações

---

## ▶️ Como executar

```bash
uvicorn main:app --reload

