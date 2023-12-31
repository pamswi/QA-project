
// submitForm() function handles contact form submission
function submitForm() {
    var name = document.getElementById("name").value;
    var email = document.getElementById("email").value;
    var subject = document.getElementById("subject").value;
    var message = document.getElementById("message").value;

    var resultDiv = document.getElementById("result");


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

// updateGrandTotal() function calculates and updates the grand total in the basket and on the checkout page
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


// the below event listener handles fixed vs sticky footer across pages
window.addEventListener('scroll', function() {
    const footer = document.querySelector('.footer');
    const contentWrapper = document.querySelector('.content-wrapper');
    const threshold = contentWrapper.offsetHeight - window.innerHeight;

    if (window.scrollY >= threshold) {
      footer.classList.add('sticky');
    } else {
      footer.classList.remove('sticky');
    }
  });