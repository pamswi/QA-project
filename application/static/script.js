function submitForm() {
    var name = document.getElementById("name").value;
    var email = document.getElementById("email").value;
    var subject = document.getElementById("subject").value;
    var message = document.getElementById("message").value;

    var resultDiv = document.getElementById("result");

    // You can perform further validation here if needed
    
    // Display a loading message
    resultDiv.innerHTML = "Sending...";

    // Simulate an asynchronous process (e.g., sending data to a server)
    setTimeout(function () {
        var successMessage = "Thank you, " + name + "! Your message has been sent.";
        resultDiv.innerHTML = successMessage;
        
        // Clear the form fields after successful submission
        document.getElementById("name").value = "";
        document.getElementById("email").value = "";
        document.getElementById("subject").value = "";
        document.getElementById("message").value = "";
    }, 2000);
}

// Function to calculate and update the grand total
function updateGrandTotal() {
    var totalElements = document.querySelectorAll('.product-total');
    var grandTotal = 0;

    totalElements.forEach(function(element) {
        grandTotal += parseFloat(element.getAttribute('data-product-total'));
    });

    var basketTotalElement = document.getElementById('basketTotal');
    basketTotalElement.innerHTML = '£' + grandTotal.toFixed(2);
    basketTotalElement.setAttribute('data-basket-total', grandTotal.toFixed(2));
}

// Call the function to calculate and update the grand total initially
updateGrandTotal()