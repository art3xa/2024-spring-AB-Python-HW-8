# openapi_client.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_product_to_cart_carts_id_products_product_id_post**](DefaultApi.md#add_product_to_cart_carts_id_products_product_id_post) | **POST** /carts/{id_}/products/{product_id} | Add Product To Cart
[**change_product_quantity_carts_id_products_product_id_put**](DefaultApi.md#change_product_quantity_carts_id_products_product_id_put) | **PUT** /carts/{id_}/products/{product_id} | Change Product Quantity
[**create_cart_carts_post**](DefaultApi.md#create_cart_carts_post) | **POST** /carts | Create Cart
[**delete_cart_carts_id_delete**](DefaultApi.md#delete_cart_carts_id_delete) | **DELETE** /carts/{id_} | Delete Cart
[**get_cart_carts_id_get**](DefaultApi.md#get_cart_carts_id_get) | **GET** /carts/{id_} | Get Cart
[**get_product_products_id_get**](DefaultApi.md#get_product_products_id_get) | **GET** /products/{id_} | Get Product
[**get_products_products_get**](DefaultApi.md#get_products_products_get) | **GET** /products | Get Products


# **add_product_to_cart_carts_id_products_product_id_post**
> Cart add_product_to_cart_carts_id_products_product_id_post(id_, product_id)

Add Product To Cart

Endpoint to add a product to a cart

### Example


```python
import openapi_client
from openapi_client.models.cart import Cart
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    id_ = 'id__example' # str | 
    product_id = 'product_id_example' # str | 

    try:
        # Add Product To Cart
        api_response = api_instance.add_product_to_cart_carts_id_products_product_id_post(id_, product_id)
        print("The response of DefaultApi->add_product_to_cart_carts_id_products_product_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->add_product_to_cart_carts_id_products_product_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_** | **str**|  | 
 **product_id** | **str**|  | 

### Return type

[**Cart**](Cart.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_product_quantity_carts_id_products_product_id_put**
> Cart change_product_quantity_carts_id_products_product_id_put(id_, product_id, quantity)

Change Product Quantity

Endpoint to change the quantity of a product in a cart

### Example


```python
import openapi_client
from openapi_client.models.cart import Cart
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    id_ = 'id__example' # str | 
    product_id = 'product_id_example' # str | 
    quantity = 56 # int | 

    try:
        # Change Product Quantity
        api_response = api_instance.change_product_quantity_carts_id_products_product_id_put(id_, product_id, quantity)
        print("The response of DefaultApi->change_product_quantity_carts_id_products_product_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->change_product_quantity_carts_id_products_product_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_** | **str**|  | 
 **product_id** | **str**|  | 
 **quantity** | **int**|  | 

### Return type

[**Cart**](Cart.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cart_carts_post**
> Cart create_cart_carts_post()

Create Cart

Endpoint to create a new cart

### Example


```python
import openapi_client
from openapi_client.models.cart import Cart
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Create Cart
        api_response = api_instance.create_cart_carts_post()
        print("The response of DefaultApi->create_cart_carts_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_cart_carts_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Cart**](Cart.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cart_carts_id_delete**
> Cart delete_cart_carts_id_delete(id_)

Delete Cart

Endpoint to delete a cart by ID

### Example


```python
import openapi_client
from openapi_client.models.cart import Cart
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    id_ = 'id__example' # str | 

    try:
        # Delete Cart
        api_response = api_instance.delete_cart_carts_id_delete(id_)
        print("The response of DefaultApi->delete_cart_carts_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_cart_carts_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_** | **str**|  | 

### Return type

[**Cart**](Cart.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cart_carts_id_get**
> Cart get_cart_carts_id_get(id_)

Get Cart

Endpoint to get a cart by ID

### Example


```python
import openapi_client
from openapi_client.models.cart import Cart
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    id_ = 'id__example' # str | 

    try:
        # Get Cart
        api_response = api_instance.get_cart_carts_id_get(id_)
        print("The response of DefaultApi->get_cart_carts_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_cart_carts_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_** | **str**|  | 

### Return type

[**Cart**](Cart.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_products_id_get**
> Product get_product_products_id_get(id_)

Get Product

Endpoint to get a product by ID

### Example


```python
import openapi_client
from openapi_client.models.product import Product
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    id_ = 'id__example' # str | 

    try:
        # Get Product
        api_response = api_instance.get_product_products_id_get(id_)
        print("The response of DefaultApi->get_product_products_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_product_products_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_** | **str**|  | 

### Return type

[**Product**](Product.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_products_products_get**
> List[Product] get_products_products_get()

Get Products

Endpoint to get the list of products

### Example


```python
import openapi_client
from openapi_client.models.product import Product
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Get Products
        api_response = api_instance.get_products_products_get()
        print("The response of DefaultApi->get_products_products_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_products_products_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Product]**](Product.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

