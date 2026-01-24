# Programação Orientada a Objetos (POO)

A Programação Orientada a Objetos é um paradigma de programação que organiza o código em estruturas chamadas **classes** e **objetos**, permitindo maior organização, reutilização, manutenção e escalabilidade do software.

---

## Classe

Uma **classe** é um molde ou modelo que define como um objeto será estruturado.  
Ela descreve:

- **Atributos**: características ou propriedades do objeto
- **Métodos**: comportamentos ou ações que o objeto pode executar

A classe não é o objeto em si, mas sim a definição dele.

---

## Objeto

Um **objeto** é uma **instância de uma classe**.  
Ao criar um objeto, ele passa a existir na memória com seus próprios valores de atributos, seguindo a estrutura definida pela classe.

Cada objeto é independente, mesmo quando criado a partir da mesma classe.

---

## Método Construtor (`__init__`)

O método `__init__` é o **construtor da classe**.  
Ele é executado automaticamente sempre que um novo objeto é criado.

Sua principal função é:

- Inicializar os atributos do objeto
- Definir o estado inicial da instância.

---

## `self`

O `self` é uma **referência à instância atual da classe**.

Ele é utilizado para:

- Acessar atributos da instância
- Chamar outros métodos da mesma classe
- Diferenciar atributos da instância de variáveis locais

Sem o `self`, os atributos não pertencem ao objeto, mas apenas ao escopo do método.

---

## Herança

A **herança** é um mecanismo que permite que uma classe (subclasse) herde atributos e métodos de outra classe (superclasse).

Ela é utilizada para:

- Reaproveitamento de código
- Criação de hierarquias entre classes
- Extensão de funcionalidades existentes

A subclasse pode usar, modificar ou adicionar novos comportamentos à classe herdada.

---

## Encapsulamento

O **encapsulamento** é o conceito de proteger os dados de uma classe, controlando o acesso aos seus atributos e métodos.

Seu objetivo é:

- Aumentar a segurança do código
- Evitar modificações indevidas
- Melhorar a organização e manutenção

### Atributos públicos
São acessíveis livremente fora da classe.

### Atributos privados
São utilizados internamente pela classe e não devem ser acessados diretamente de fora.

Em Python, utiliza-se a **convenção de sublinhado (`_`)** para indicar atributos e métodos que não devem ser acessados externamente.

---

## Polimorfismo

O **polimorfismo** permite que métodos com o mesmo nome tenham comportamentos diferentes, dependendo do contexto ou da classe em que estão implementados.

Esse conceito facilita:

- Flexibilidade no código
- Uso de interfaces semelhantes
- Substituição de comportamentos sem alterar a estrutura principal

O polimorfismo geralmente está associado à herança e à sobrescrita de métodos.

---

## Conclusão

A Programação Orientada a Objetos é fundamental para o desenvolvimento de sistemas organizados e reutilizáveis.  
Os pilares da POO — **classes, objetos, herança, encapsulamento e polimorfismo** — trabalham juntos para criar códigos mais claros, seguros e fáceis de manter.
