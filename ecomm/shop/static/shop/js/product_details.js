// JQuery for Add to cart Functionality
console.log("Amitabh's 1st JavaScript");
if (localStorage.getItem('cart') == null) {
    var cart = {};
} else {
    cart = JSON.parse(localStorage.getItem('cart'));
}

$(document).ready(function() {
    $(document).on('click', '.atc', function() {
        console.log("The add to cart button is clicked");
        var item_id = this.id.toString();
        console.log(item_id);
        
        if (cart[item_id] != undefined) {
            quantity = cart[item_id][0] + 1;
            cart[item_id][0] = quantity;
        } else {
            quantity = 1;
            name = document.getElementById("as"+item_id).innerHTML.trim();
            cart[item_id] = [quantity, name];
        }
        console.log(cart);
        localStorage.setItem('cart', JSON.stringify(cart));
        document.getElementById("cart").innerHTML = "Cart(" + Object.keys(cart).length + ")";
    });
    
    $('#cart').on('click', function () {
        $(this).popover('show');
    });
    
    // DisplayCart(cart);
    function DisplayCart(cart) {
        var cartString = "";
        cartString += "<h5>Cart Details</h5><br>"
        var cart_index = 1;
        for(var x in cart) {
            cartString += cart_index + document.getElementById("as" + x).innerHTML.trim() + ". Qty : " + cart[x][0] + "<br>";
            cart_index += 1;
        }
        cartString += "<br>"
        cartString += "<a href='" + checkoutUrl + "' class='btn btn-warning' id='checkout'>Checkout</a>";
        console.log("cartString is : " + cartString);
        
        var element = document.getElementById("cart");
        console.log("Element is : " + element); // Print the element to the console

        // Check if the element is null or undefined
        if (element) {
            element.setAttribute('data-content', cartString);
        } else {
            console.log("Element not found"); // Handle the case when the element is not found
        }

        $('[data-toggle="popover"]').popover({
            html: true,
            content: cartString
        });
    }
    DisplayCart(cart);
});