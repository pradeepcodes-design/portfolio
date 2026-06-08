/* ==========================================
   Product Data — an array of product objects
   ========================================== */
// Each product has: id, name, price, and image filename (using placeholder images)
const products = [
  {
    id: 1,
    name: "Face Cream",
    price: 599,
    image: "https://images.unsplash.com/photo-1620916566398-39f1143ab7be?w=400&h=300&fit=crop"
  },
  {
    id: 2,
    name: "Lipstick",
    price: 449,
    image: "https://images.unsplash.com/photo-1586495777744-4413f21062fa?w=400&h=300&fit=crop"
  },
  {
    id: 3,
    name: "Face Wash",
    price: 399,
    image: "https://images.unsplash.com/photo-1556228578-0d85b1a4d571?w=400&h=300&fit=crop"
  },
  {
    id: 4,
    name: "Perfume",
    price: 1299,
    image: "https://images.unsplash.com/photo-1541643600914-78b084683601?w=400&h=300&fit=crop"
  },
  {
    id: 5,
    name: "Sunscreen",
    price: 699,
    image: "https://images.unsplash.com/photo-1556228578-0d85b1a4d571?w=400&h=300&fit=crop"
  },
  {
    id: 6,
    name: "Hair Serum",
    price: 549,
    image: "https://images.unsplash.com/photo-1535585209827-a15fcdbc4c2d?w=400&h=300&fit=crop"
  }
];

/* ==========================================
   Display Products — loop through the array
   and create HTML for each product card
   ========================================== */
function displayProducts() {
  // Get the container where product cards will go
  const grid = document.getElementById("productsGrid");

  // Clear any existing content inside the grid
  grid.innerHTML = "";

  // Loop over each product in the array
  products.forEach(function(product) {
    // Create a new <div> element for the product card
    const card = document.createElement("div");
    card.classList.add("product-card");

    // Fill the card with HTML content using the product data
    card.innerHTML = `
      <img src="${product.image}" alt="${product.name}">
      <h3>${product.name}</h3>
      <p>₹${product.price}</p>
    `;

    // Append (add) the card to the grid
    grid.appendChild(card);
  });
}

/* ==========================================
   Contact Form — handle submission
   ========================================== */
function setupContactForm() {
  // Get the form element by its ID
  const form = document.getElementById("contactForm");

  // Listen for the "submit" event (when user clicks Send Message)
  form.addEventListener("submit", function(event) {
    // Prevent the page from reloading (default form behavior)
    event.preventDefault();

    // Get the values the user typed in
    const name = document.getElementById("name").value.trim();
    const email = document.getElementById("email").value.trim();
    const message = document.getElementById("message").value.trim();

    // Simple validation: make sure all fields are filled
    if (name === "" || email === "" || message === "") {
      alert("Please fill in all fields.");
      return;  // stop here
    }

    // Show a success message
    alert(`Thank you, ${name}! Your message has been received.`);
    
    // Reset the form fields to empty
    form.reset();
  });
}

/* ==========================================
   Initialize — runs when the page loads
   ========================================== */
// Wait for the HTML document to be fully loaded before running our code
document.addEventListener("DOMContentLoaded", function() {
  displayProducts();   // show all products on the page
  setupContactForm();  // enable the contact form
});
