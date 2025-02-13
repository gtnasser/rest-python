**REST** é um acrônimo para **Representational State Transfer**, um conjunto de princípios arquiteturais usados para criar serviços web.
Apresentado por Roy Fielding em 2000, tem sido amplamente usado para o desenvolvimento de APIs permitindo a comunicação entre sistemas diversos.

A seguir um resumo do artigo [Python and REST APIs: Interacting With Web Services](https://realpython.com/api-integration-in-python/) publicado por Jason Van Schooneveld.

### REST Architecture

REST stands for [representational state transfer](https://en.wikipedia.org/wiki/Representational_state_transfer) and is a software architecture style that defines a pattern for client and server communications over a network. REST provides a set of constraints for software architecture to promote performance, scalability, simplicity, and reliability in the system.

REST defines the following architectural constraints:

* **Stateless:** The server won’t maintain any state between requests from the client.
* **Client-server:** The client and server must be decoupled from each other, allowing each to develop independently.
* **Cacheable:** The data retrieved from the server should be cacheable either by the client or by the server.
* **Uniform interface:** The server will provide a uniform interface for accessing resources without defining their representation.
* **Layered system:** The client may access the resources on the server indirectly through other layers such as a proxy or load balancer.
* **Code on demand (optional):** The server may transfer code to the client that it can run, such as JavaScript for a single-page application.

Note, REST is not a specification but a **set of guidelines** on how to architect a network-connected software system.

### REST APIs and Web Services

A REST web service is any web service that adheres to REST architecture constraints. These web services expose their data to the outside world through an API. REST APIs provide access to web service data through public web URLs. You access data from a REST API by sending an HTTP request to a specific URL and processing the response.

### HTTP Methods

REST APIs listen for [HTTP methods](https://realpython.com/python-https/#what-is-http) like GET, POST, and DELETE to know which operations to perform on the web service’s resources. A resource is any data available in the web service that can be accessed and manipulated with HTTP requests to the REST API. The HTTP method tells the API which action to perform on the resource.

While there are many HTTP methods, the five methods listed below are the most commonly used with REST APIs:

HTTP method|Description
---|---
GET|Retrieve an existing resource.
POST|Create a new resource.
PUT|Update an existing resource.
PATCH|Partially update an existing resource.
DELETE|Delete a resource.

A REST API client application can use these five HTTP methods to manage the state of resources in the web service.

## Status Codes

Once a REST API receives and processes an **HTTP request**, it will return an **HTTP response**. Included in this response is an **HTTP status code**. This code provides information about the results of the request. An application sending requests to the API can check the status code and perform actions based on the result. These actions could include handling errors or displaying a success message to a user.

Below is a list of the most common status codes returned by REST APIs:

Code|Meaning|Description
---|---|---
200|OK|The requested action was successful.
201|Created|A new resource was created.
202|Accepted|The request was received, but no modification has been made yet.
204|No Content|The request was successful, but the response has no content.
400|Bad Request|The request was malformed.
401|Unauthorized|The client is not authorized to perform the requested action.
404|Not Found|The requested resource was not found.
415|Unsupported Media Type|The request data format is not supported by the server.
422|Unprocessable Entity|The request data was properly formatted but contained invalid or missing data.
500|Internal Server Error|The server threw an error when processing the request.

These ten status codes represent only a small subset of the available [HTTP status codes](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes). Status codes are numbered based on the category of the result:

Code range|Category
---|---
2xx|Successful operation
3xx|Redirection
4xx|Client error
5xx|Server error

HTTP status codes come in handy when working with REST APIs as you’ll often need to perform different logic based on the results of the request.

API Endpoints
A REST API exposes a set of public URLs that client applications use to access the resources of a web service. These URLs, in the context of an API, are called endpoints.

To help clarify this, take a look at the table below. In this table, you’ll see API endpoints for a hypothetical CRM system. These endpoints are for a customer resource that represents potential customers in the system:

HTTP method|API endpoint|Description
---|---|---
GET|/customers|Get a list of customers.
GET|/customers/<customer_id>|Get a single customer.
POST|/customers|Create a new customer.
PUT|/customers/<customer_id>|Update a customer.
PATCH|/customers/<customer_id>|Partially update a customer.
DELETE|/customers/<customer_id>|Delete a customer.
Each of the endpoints above performs a different action based on the HTTP method.

    Note: The base URL for the endpoints has been omitted for brevity. In reality, you’ll need the full URL path to access an API endpoint:

    https://api.example.com/customers

    This is the full URL you’d use to access this endpoint. The base URL is everything besides /customers.

You’ll note that some endpoints have <customer_id> at the end. This notation means you need to append a numeric customer_id to the URL to tell the REST API which customer you’d like to work with.

The endpoints listed above represent only one resource in the system. Production-ready REST APIs often have tens or even hundreds of different endpoints to manage the resources in the web service.


