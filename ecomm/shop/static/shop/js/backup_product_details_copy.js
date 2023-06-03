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
            console.log("New item quantity is being added");
            quantity = cart[item_id][0] + 1;
            var item_price = document.getElementById("discounted-price" + item_id);
            cart[item_id][0] = quantity;
            cart[item_id][2] = parseFloat(cart[item_id][2]) + parseFloat(item_price.innerHTML);

        } else {
            console.log("New item is being added : ", item_id);

            var item_price = document.getElementById("discounted-price" + item_id);
            quantity = 1;
            name = document.getElementById("as" + item_id).innerHTML.trim();
            price = parseFloat(item_price.innerHTML);
            cart[item_id] = [quantity, name, price];
        }
        console.log("Updated cart : ", cart);
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
    console.log("Updated cart : ", cart);
});