// Move the JavaScript code inside a function
function populateFormItems() {
    // JavaScript to get the cart items from local storage
    if (localStorage.getItem('cart') === null) {
        var cart = {};
    } else {
        cart = JSON.parse(localStorage.getItem('cart'));
    }

    console.log("cart items are: ", cart);
    let total = 0;
    for (var item in cart) {
        let name = cart[item][1].trim(); // Trim the leading and trailing whitespaces
        let quantity = cart[item][0];
        let price = cart[item][2]
        total = total + price;
        var itemString = `<li class="list-group-item d-flex justify-content-between align-items-center">${name}
            <span class="badge rounded-pill text-bg-primary"> ${quantity} </span>
            <span class="badge bg-secondary"><b>INR ${price}</b></span></li>`;
        $("#item_list").append(itemString);
    }
    totalPrice = `<li class="list-group-item d-flex justify-content-between align-items-center"><b>Total Cart value </b> INR ${total}</li>`;
    $("#totalPrice").val(total);
    $("#item_list").append(totalPrice);
    $("#items").val(JSON.stringify(cart));
    console.log("Cart at checkout: " + JSON.stringify(cart));
}

populateFormItems();
