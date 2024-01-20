# Project_for_earning_purposes

# Flask API Documentation

## CEP Query Endpoint

#### This API provides an endpoint for querying Brazilian ZIP codes (CEP) using the ViaCep API.

### Endpoint

- **URL:** `/api/consulta-cep/<cep>`
- **Method:** `GET`
- **Description:** Query details for a specific Brazilian ZIP code (CEP).

### Request

- **Parameters:**
  - `<cep>` (Path Parameter): The Brazilian ZIP code to query.

### Response

- **Success Response:**
  - **Code:** 200 OK
  - **Content:**
    ```json
    {
      "cep": "12345-678",
      "logradouro": "Rua Example",
      "bairro": "Example District",
      "localidade": "Example City",
      "uf": "EX",
      "ibge": "1234567",
      "gia": "9876",
      "ddd": "99",
      "siafi": "8765"
    }
    ```

- **Error Responses:**
  - **Code:** 500 Internal Server Error
    - **Content:**
      ```json
      {
        "erro": "Error querying the CEP"
      }
      ```

### Example

**Request:**

```bash
curl -X GET http://localhost:5000/api/consulta-cep/12345-678


#### Logging The API logs debug and error messages for better troubleshooting. Check the application log file (app.log) for details.

## Note: Replace http://localhost:5000 with the actual base URL where your Flask API is hosted.

## Order Management API Documentation

This API provides endpoints for managing orders.

## Orders Resource

### Get Orders

- **Endpoint:** `/api/pedidos`
- **Method:** `GET`
- **Description:** Retrieve a list of all orders.

#### Request

No additional parameters required.

#### Response

- **Success Response:**
  - **Code:** 200 OK
  - **Content:**
    ```json
    {
      "pedidos": [
        {"id": 1, "produto": "Produto A", "quantidade": 100, "data_hora": "2024-01-20 15:30:00"},
        {"id": 2, "produto": "Produto B", "quantidade": 10, "data_hora": "2024-01-20 15:35:00"},
        {"id": 3, "produto": "Produto C", "quantidade": 20, "data_hora": "2024-01-20 15:40:00"},
        {"id": 4, "produto": "Produto D", "quantidade": 45, "data_hora": "2024-01-20 15:45:00"},
        {"id": 5, "produto": "Produto F", "quantidade": 230, "data_hora": "2024-01-20 15:50:00"},
        {"id": 100, "produto": "Produto Z", "quantidade": 1025, "data_hora": "2024-01-20 15:55:00"}
      ]
    }
    ```

### Create Order

- **Endpoint:** `/api/pedidos`
- **Method:** `POST`
- **Description:** Create a new order.

#### Request

- **Content:**
  ```json
  {
    "produto": "Produto X",
    "quantidade": 50
  }
### Response

- **Success Response:**
  - **Code:** 201 OK
  - **Content:**
  - **Mensagem: Order created successfully**
    ```json
	{"mensagem": "Order created successfully"}

    ```

### Update Order
- **Endpoint:** `/api/pedidos/<pedido_id>`
- **Method:** `PUT`
- **Description:** Update an existing order.
 
### Request
- **Content:**
    ```json
	{"produto": "produtoN-1"
	{"quantidade": 75}
    ```
### Response
- **Success Response:**
  - **Code:** 200 OK
  - **Content:**
    ```json
	{"mensagem": "Order updated successfully"}
    ```
### Error Response
  - **Code:** 404 Not Found
  - **Content:**
    ```json
	{ "mensagem": "Order not found" }
    ```

### Delete Order
- **Endpoint:** `/api/pedidos/<pedido_id>`
- **Method:** `DELETE`
- **Description:** Delete an order.

#### Response

- **Success Response:**
  - **Code:** 200 OK
  - **Content:**
  - **Mensagem:  deleted successfully**
{
  "mensagem": "Order excluído com sucesso"
}
### Error Response:

  - **Code:**404 Not Found
  - **Content:**
- **Mensagem: Fuel deleted successfully**
{
  "mensagem": "Order not found"
}


# Fuel Station Management API Documentation

## This API provides endpoints for managing fuel inventory at a gas station.

## Simulating a list of fuels (replace with a database):

## Fuel Inventory

### Get All Fuels

- **Endpoint:** `/combustiveis`
- **Method:** `GET`
- **Description:** Retrieve a list of all fuels in the inventory.

#### Response

- **Success Response:**
  - **Code:** 200 OK
  - **Content:**
    ```json
    "combustivel": {
      [
      {"id": 1, "tipo": "Gasolina", "quantidade": 3, "preco": 5.0, "valor_total": 15, "operador": "Silas Vascconcelos", "data_hora": "2024-01-20 15:30:00"},
      {"id": 2, "tipo": "Álcool", "quantidade": 5, "preco": 4.5, "valor_total": 22.5, "operador": "pqrs", "data_hora": "2024-01-20 15:35:00"},
      {"id": 3, "tipo": "Diesel", "quantidade": 7,  "preco": 4.0, "valor_total": 28, "operador": "wvu", "data_hora": "2024-01-20 15:40:00"},
      {"id": 4, "tipo": "Gasolina", "quantidade": 10, "preco": 5.0, "valor_total": 50, "operador": "Fulano", "data_hora": "2024-01-20 15:45:00"},
      {"id": 5, "tipo": "Álcool", "quantidade": 5,  "preco": 4.5, "valor_total": 22.5, "operador": "Beltrano", "data_hora": "2024-01-20 15:50:00"},
      {"id": 6, "tipo": "Diesel", "quantidade": 100,  "preco": 4.0, "valor_total": 400, "operador": "Ciclano", "data_hora": "2024-01-20 15:55:00"}
      ]
    }
    ```

### Get Single Fuel

- **Endpoint:** `/combustiveis/<int:combustivel_id>`
- **Method:** `GET`
- **Description:** Retrieve details of a specific fuel by ID.

#### Response

- **Success Response:**
  - **Code:** 200 OK
  - **Content:**
    ```json
    "combustivel":
    {
        {
          "id": 1,
          "tipo": "Gasolina",
          "quantidade": 3,
          "preco": 5.0,
          "valor_total": 15,
          "operador": "Silas Vasconcelos",
          "data_hora": "2024-01-20   15:30:00"
       }
    }
    ```

- **Error Response:**
  - **Code:** 404 Not Found
  - **Content:**
    ```json
    {"error": "Combustível não encontrado"}
    ```

### Add Fuel

- **Endpoint:** `/combustiveis`
- **Method:** `POST`
- **Description:** Add a new fuel to the inventory.

#### Request

- **Content:**
  ```json
  {
    "tipo": "Diesel",
    "quantidade": 10,
    "preco": 4.0,
    "operador": "pqrs"
  }

#### Response

- **Success Response:**
  - **Code:** 201 OK
  - **Content:**
  - **Mensagem: Fuel added successfully**
    ```json
     "combustivel":
    {
       "id": 7,
       "tipo": "Gasolina Aditivada",
       "quantidade":  10,
       "preco": 4.0,
       "valor_total": 40.0,
       "operador": "pqrs",
       "data_hora": "2024-01-20 16:00:00"
    }
    ```

### Update Fuel

- **Endpoint:** `/combustiveis/<int:combustivel_id>`
- **Method:** `PUT`
- **Description:** Update details for an existing fuel.

#### Request

- **Content:**
  ```json
  {
    "tipo": "Diesel",
    "quantidade": 20,
    "preco": 4.0,
    "operador": "uvw"
  }

#### Response

- **Success Response:**
  - **Code:** 200 OK
  - **Content:**
  - **Mensagem: Fuel updated successfully**
    ```json
  	"combustivel":
    {
      "id": 7,
      "tipo": "Gasolina Aditivada",
      "quantidade": 20,
      "preco": 4.0,
      "valor_total": 80.0,
      "operador": "uvw",
      "data_hora": "2024-01-20 16:15:00"
  	}
    ```
### Error Response
  - **Code:** 404 Not Found
  - **Content:**
    ```json
	{ "mensagem": "Fuel not found" }
    ```

### Delete Fuel

- **Endpoint:** `/combustiveis/<int:combustivel_id>`
- **Method:** `DELETE`
- **Description:** Delete a fuel entry.

#### Response

- **Success Response:**
  - **Code:** 200 OK
  - **Content:**
    ```json
	{ "mensagem": "Fuel deleted successfully" }
    ```
# Project_for_earning
