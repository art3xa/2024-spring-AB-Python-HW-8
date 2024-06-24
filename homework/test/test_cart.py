def test_get_cart_by_id(default_api):
    create_cart_response = default_api.create_cart_carts_post()
    cart_id = create_cart_response.id

    get_cart_response = default_api.get_cart_carts_id_get(id_=cart_id)

    assert get_cart_response.id == cart_id
    assert get_cart_response.products == []
