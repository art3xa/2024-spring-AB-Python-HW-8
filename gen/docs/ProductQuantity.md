# ProductQuantity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **str** |  | 
**quantity** | **int** |  | 

## Example

```python
from openapi_client.models.product_quantity import ProductQuantity

# TODO update the JSON string below
json = "{}"
# create an instance of ProductQuantity from a JSON string
product_quantity_instance = ProductQuantity.from_json(json)
# print the JSON string representation of the object
print(ProductQuantity.to_json())

# convert the object into a dict
product_quantity_dict = product_quantity_instance.to_dict()
# create an instance of ProductQuantity from a dict
product_quantity_from_dict = ProductQuantity.from_dict(product_quantity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


