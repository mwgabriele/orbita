# Eventos da astronomia e astronáutica -> Banco de Dados

## O Orbita:
Banco de dados SQLite. Tabelas:

**Eventos astronômicos**
- id
- nome_evento
- tipo_evento
- descricao
- data
- horario_utc3 (UTC-3)
- local_visivel (onde poderá ser observado -> a definir! ex.: América do Sul, apenas Hemisfério Norte...)
- duracao (se aplicável. Eclipse, chuva de meteóro, etc...)
- corpo_principal
- frequencia
- observacao_popular/comum (?) (visível a olho nu, binóculo, telescópio...)

**Lançamentos espaciais**
- id
- nome_missao (ex.: Apollo)
- veiculo_lancador (ex.: Saturn V)
- nome_agencia
- carga (ex.: satélite, sonda, telescópio, tripulação)
- destino 
- data
- horario_utc3
- local_lancamento
- resultado (sucesso, falha, adiado)
- descricao

**Agências**
- id
- nome_agencia
- pais

**objeto**
- id


Ordem de páginas usadas no preenchimento de nome_missao do banco:
1. spaceflight now
1. roscosmos
1. everyday astronaut
1. supercluster

dados para apagar:
Long March 2C/YZ-1S | Unknown Payload
Falcon 9 Block 5 | Starlink Group 17-12
Falcon 9 Block 5 | Starlink Group 10-61
New Shepard | NS-35
Falcon 9 Block 5 | Starlink Group 10-27
Falcon 9 Block 5 | NROL-48
HASTE | JENNA
Falcon 9 Block 5 | IMAP & others       
Atlas V 551 | Project Kuiper (KA-03)   
Falcon 9 Block 5 | Starlink Group 17-11