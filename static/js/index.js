function registerProduct() {
    Swal.fire({
        title: 'JSON do Produto',
        input: 'text',
        showCancelButton: true,
        confirmButtonText: 'Registrar',
        cancelButtonText: 'Cancelar',
        preConfirm: (textJsonProduct) => {
            $.ajax({
                type: 'POST',
                url: '/register_product/',
                dataType: 'json',
                data: {textJsonProduct: textJsonProduct},
                success: function (data) {
                    product = data.product;
                    $('#contentProducts').append(`
                        <tr id="product_${product['id']}">
                            <td class="font-weight-bold font-20">${product['id']}</td>
                            <td><img src="${product['foto']}" class="img-thumbnail"></td>
                            <td>${product['nome']}</td>
                            <td>
                                <span class="text-success font-20 font-weight-bold">R$ ${product['preco_desconto']} à vista</span><br>
                                <span class="text-primary-color font-weight-bold">R$ ${product['preco']}</span>
                            </td>
                            <td><a type="button" href="https://kabum.com.br${product['link_descricao']}" target="_blank" class="btn btn-deep-orange">Acessar</a></td>
                            <td><a type="button" data-id="${product['id']}" onclick="deleteProduct(this.getAttribute('data-id'))"><i class="fas fa-trash-alt fa-2x text-danger"></i></a></td>
                        </tr>
                    `);
                    popSuccess('Registro', data.msg);
                    hideLoader();
                },
                error: function (data) {
                    tratarErro(data);
                }
            });
        }
    });
}

function deleteProduct(idProduct) {
    $.ajax({
        type: 'POST',
        url: '/delete_product/',
        dataType: 'json',
        data: {idProduct: idProduct},
        success: function (data) {
            popSuccess('Exclusão', data.msg);
            $('#product_' + idProduct).remove();
            hideLoader();
        },
        error: function (data) {
            tratarErro(data);
        }
    });
}