let updateBtns = document.getElementsByClassName('update-cart')

for (let i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function (e) {
        e.preventDefault()
        let productId = this.dataset.product
        let data_action = this.dataset.action
        if (user === 'AnonymousUser') {
            window.location.href = '/login/'
        } else {
            updateUserOrder(productId, data_action)
        }
    })
}

function updateUserOrder(product_id, data_action) {
    let url = "/update_item/"
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({
            'product_id': product_id,
            'data_action': data_action
        })
    })

        .then((response) => {
            return response.json()
        })

        .then((data) => {
            location.reload()
        })
}
