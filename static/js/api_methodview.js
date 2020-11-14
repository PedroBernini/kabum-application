function getAllProducts() {
    $.ajax({
        type: 'GET',
        url: '/product/',
        success: function (data) {
            products = data.products
            popSuccess('GET All Products', products);
            hideLoader();
        },
        error: function (data) {
            tratarErro(data);
        }
    });
}

function getProductById() {
    Swal.fire({
        title: 'ID do Produto',
        input: 'text',
        showCancelButton: true,
        confirmButtonText: 'GET',
        cancelButtonText: 'Cancelar',
        preConfirm: (idProduct) => {
            $.ajax({
                type: 'GET',
                url: '/product/' + idProduct,
                success: function (data) {
                    product = data.product
                    popSuccess('GET Product By ID', product);
                    hideLoader();
                },
                error: function (data) {
                    tratarErro(data);
                }
            });
        }
    });
}   