# Automação de Teclas em Python

Automação de teclado desenvolvida em Python para executar uma sequência repetitiva de teclas **A + D** e **E**, com temporização controlada e repetição contínua.

## Funcionalidades

- Pressionamento automatizado das teclas `A` e `D`.
- Alternância da ordem em que `A` e `D` são pressionadas.
- Pressionamento automatizado da tecla `E`.
- Intervalos aleatórios entre determinadas ações.
- Espera inicial de 3 segundos para selecionar a janela de destino.
- Pausa de 5 minutos ao final de cada ciclo.
- Execução contínua até interrupção manual.

## Tecnologias

- Python 3
- `keyboard`
- `time`
- `random`

## Instalação

Clone o repositório:

```bash
git clone https://github.com/SEU-USUARIO/automacao-teclas-python.git
cd automacao-teclas-python
```

Crie e ative um ambiente virtual, se desejar:

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux/macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

## Execução

```bash
python src/automacao.py
```

Ao iniciar, o programa aguarda 3 segundos para que a janela desejada seja colocada em foco.

## Funcionamento

O ciclo principal segue esta lógica:

```text
Início
  ↓
Aguarda 3 segundos
  ↓
A + D
  ↓
Intervalo aleatório
  ↓
E
  ↓
Intervalo aleatório
  ↓
A + D
  ↓
Intervalo aleatório
  ↓
E
  ↓
Aguarda 5 minutos
  ↓
Repete
```

A ordem de `A` e `D` é alternada entre as chamadas da função responsável pela sequência.

## Parâmetros atuais

| Parâmetro | Valor |
|---|---:|
| Espera inicial | 3 s |
| Intervalo entre A/D | 0,005 s |
| Tempo com A/D pressionadas | 0,08 s |
| Intervalos entre ações | 0,15–0,35 s |
| Pausa do ciclo | 300 s / 5 min |

## Interrupção

O programa utiliza um loop contínuo (`while True`) e não possui uma condição interna de encerramento.

Quando executado pelo terminal, pode ser interrompido com:

```text
Ctrl + C
```

## Limitações

- Depende da janela correta estar em foco.
- Não verifica se a aplicação destino recebeu ou processou as teclas.
- Não possui tratamento de exceções no código original.
- Os tempos são definidos diretamente no código.
- Não existe sistema de logging persistente.
- O comportamento da biblioteca `keyboard` pode variar conforme o sistema operacional e as permissões disponíveis.

## Melhorias futuras

- Adicionar mecanismo de parada segura.
- Tornar os tempos configuráveis.
- Adicionar tratamento de exceções.
- Criar logging em arquivo.
- Separar configurações da lógica principal.
- Adicionar testes automatizados para as partes que não dependem diretamente do teclado.
- Adicionar documentação de compatibilidade por sistema operacional.

## Aviso

Este projeto é disponibilizado para fins de estudo e automação em ambientes nos quais o usuário tenha autorização para executar scripts de entrada de teclado. Verifique as regras da aplicação ou serviço onde a automação será utilizada.

## Licença

Este projeto está disponível sob a licença MIT. Consulte [`LICENSE`](LICENSE).
