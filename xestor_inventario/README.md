# Xestor de Inventario - Tenda de zapatillas de deporte

## Descripción

Esta aplicación, desenvolvida en Python 3.14.0, permite xestionar o inventario e os pedidos dunha tenda de zapatillas de deporte.
O proxecto traballa sobre un arquivo .json que contén todas as categorías, modelos, cores, tallas e pedidos. Todas as modificacións feitas polo usuario na aplicación afectan directamente a este arquivo, permitindo simular de forma realista a xestión dunha tenda.

O sistema proporciona un menú interactivo na consola co que se poden realizar todas as operacións necesarias para o bo funcionamento dunha tenda de zapatillas.

Estas, de forma resumida, son:

- Ver os distintos modelos de zapatillas
- Ver zapatillas en orde de máis a menos vendidas
- Ver se un determinado modelo está dispoñible
- Dar de alta modelo
- Dar de baixa modelo
- Dar de alta cor de modelo
- Dar de baixa cor de modelo
- Vender unha talla
- Ver pedidos pendentes
- Facer un pedido
- Marcar un pedido como recibido
- Cancelar un pedido pendente

## Regras de negocio

As regras de negocio implementadas son as seguintes:

1. **Categorías de deporte:**

   - Cada zapatilla pertence a unha categoría como Running, Baloncesto, Fútbol, Tenis ou Ximnasio.

2. **Modelos de zapatilla:**

   - Cada categoría contén varios modelos de zapatilla (mímimo ten que ter 1 modelo)
   - Os modelos son supostamente **unisex**.
   - Un modelo terá un atributo de marca
   - Un modelo terá un atributo de ventas que reflexa cantas zapatillas de ese modelo se venderon

3. **Características do modelo:**

   - Cada modelo ten unha serie de atributos ou características como tipo de pisada, superficie recomendada, amortiguación, peso, etc.
   - As características a determinar dun modelo varían según a categoría á que pertence

4. **Cores e tallas:**

   - Cada modelo ten unha lista de cores dispoñibles (mínimo 1)
   - Cada cor ten unha lista de tallas, que indica a dispoñibilidade en stock.
   - Se unha lista de tallas está vacía, esa cor non está dispoñible para a venda en tenda (habería que facer un pedido)

5. **Pedidos e stock**

   - Se unha determinada talla non está dispoñible en tenda, pode solicitarse online mediante un pedido.
   - Os pedidos cando cheguen márcanse como entregados e deixan de ser pedidos pendentes.
   - A cantidade de produtos indicada nun pedido que se marca como entregado vaise reflexar no modelo indicado
   - Os pedidos pendentes pódense cancelar

6. **Xestión de modelos e cores:**

   - Pódense **engadir ou eliminar modelos**, por exemplo, cando un modelo queda descatalogado (só se pode eliminar se non está en pedidos pendentes)
   - Pódense **engadir ou eliminar cores** dun modelo se deixan de estar dispoñibles (só se pode eliminar se non está en pedidos pendentes)
   - Pódense **eliminar as tallas vendidas** e o atributo de ventas do modelo incrementa por cada talla vendida

7. **Busca de datos**

   - Pódense visualizar todos os modelos por categorías de forma que se vexa cales están dispoñibles (teñen stock en polo menos unha cor na tenda)
   - Pódense visualizar os modelos máis vendidos e a súa dispoñibilidade na tenda
   - Pódese ver a dispoñibilidade dun modelo en especifico e en que cores
   - Pódese ver os pedidos pendentes

## Funcionalidades

A aplicación conta con un menú interactivo que permite xestionar o inventario e os pedidos dunha forma completa. As funcionalidades dispoñibles son:

1. **Ver todos os modelos por categoría:**

   - Mostra os modelos organizados por categorías (Running, Baloncesto, Fútbol, Tenis, Ximnasio).
   - Indica visualmente cales teñen polo menos unha talla dispoñible, permitindo ao usuario identificar rapidamente o stock dispoñible en tenda.

2. **Ver modelos máis vendidos:**

   - Lista os modelos ordenados de maior a menor número de vendas.
   - Permite consultar cantas unidades se venderon de cada modelo, útil para análise de popularidade e toma de decisións de reposición.
   - Visualiza tamén a marca e a categoría de cada un dos modelos, tamén útil para posteriores análises.

3. **Ver pedidos pendentes:**

   - Mostra todos os pedidos que aínda non se entregaron.
   - Inclúe detalles como id, marca, modelo, cor, talla e cantidade.
   - Axuda a controlar os pedidos en curso e prever futuros cambios no stock.

4. **Ver dispoñibilidade dun modelo:**

   - Permite seleccionar un modelo e ver todas as cores dispoñibles.
   - Para cada cor indica cantas unidades hai por talla no caso de haber stock dispoñible
   - Facilita a consulta rápida para atender a clientes ou xestionar reposición de stock.

5. **Dar de alta un novo modelo:**

   - Engade un novo modelo ao inventario.
   - Solicita a marca e as características do modelo según a categoría da zapatilla que se quere inserir.
   - Solicita cantas cores queren darse de alta nese novo modelo e os seus nomes
   - Útil para incorporar novidades ou coleccións novas á tenda.

6. **Dar de baixa un modelo:**

   - Elimina un modelo do inventario pero **só se non ten stock dispoñible, non hai pedidos pendentes e non é o único da súa categoría**.
   - Evita eliminar produtos que todavía poden ser vendidos ou que teñen compromisos de pedido.

7. **Dar de alta unha nova cor de modelo:**

   - Engade unha nova cor a un modelo xa existente.
   - Solicita o modelo e o nome da nova cor.
   - Útil para incorporar novidades ou coleccións novas á tenda.

8. **Dar de baixa unha cor de modelo:**

   - Elimina unha cor dun modelo do inventario pero \*_só se o modelo acabará tendo mínimo 1 cor, se a cor non ten stock e se non aparece en pedidos pendentes_.
   - Evita eliminar produtos que todavía poden ser vendidos ou que teñen compromisos de pedido.

9. **Quitar unha zapatilla vendida:**

   - Permite vender unha talla específica dun modelo e cor determinada.
   - Reduce o stock correspondente e aumenta o contador de vendas do modelo.
   - Asegura que no inventario se vexa sempre o stock real dispoñible.

10. **Facer un pedido:**

    - Permite crear un pedido de zapatillas cando non hai stock dispoñible dunha talla e cor concreta dun modelo de zapatilla
    - Selecciónase modelo, cor e talla.
    - Rexístrase o pedido co número de unidades e queda pendente ata a súa recepción.

11. **Marcar pedido como recibido:**

    - Permite indicar que un pedido pendente chegou á tenda.
    - Actualiza automaticamente o stock sumando as unidades do pedido recibido.
    - Evita erros de inventario e mantén a información actualizada.

12. **Cancelar un pedido pendente:**
    - Permite cancelar un pedido que aínda non foi entregado.
    - Evita problemas de duplicidade e facilita a xestión de pedidos non desexados ou incorrectos.

## Instrucións de instalación

1. Clona o repositorio ou descarga o proxecto.
2. Abre a terminal na carpeta do proxecto.
3. Crea e activa unha contorna virtual:

**Para Windows (PowerShell):**

```powershell
python -m venv venv
venv\Scripts\activate
```

**Para Linux/Mac:**

```bash

python -m venv venv
source venv/Scripts/activate

```

4. Instala as dependencias necesarias con:

```bash

pip install -r requirements.txt

```

## Instrucións de uso

Unha vez temos a contorna virtual activa, executamos a aplicación:

```bash

python main.py

```

## Autoría

O código deste proxecto foi desenvolvido integramente por Diana Ramos Torrado co fin de entregalo para avaliación nas materias de ECP e CSP.
A autoría inclúe a idea do proxecto, regras de negocio e todas as funcionalidades adaptadas ao contexto dunha tenda realista de zapatillas de deporte.
