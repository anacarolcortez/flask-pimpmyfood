# API com Flask Restful "Pimp My Food"
CRUD de receitas para reaproveitamento de partes de alimentos que costumamos jogar fora, como cascas e talos, que são altamente nutritivas e econômicas.

* Flask
* Flask-Restful
* SQL Alckemy (ORM)

#### Instalação
* Criar ambiente virtual
    ```
    $ virtualenv venv --python=3.10
    ```
    Linux
    ```
    $ source venv/bin/activate
   ```
   Windows
    ```
    $ .\venv\Scripts\activate
   ```
* Instalar bibliotecas
     ```
     $ pip install -r requirements.txt
     ```
### Execução localhost
  ```
  $ python app.py
   ```

   * Arquivo "/tests" contém requisições http que podem ser executadas diretamente no vscode, ou facilitar criação de rotas no Postman/Insomnia
