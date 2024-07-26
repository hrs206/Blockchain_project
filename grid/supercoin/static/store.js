// JavaScript logic for the Store page
document.addEventListener('DOMContentLoaded', function () {
  const productList = document.querySelector('.product-list');

  // Simulated product data
  const productsData = [
      { image: 'product1.png', description: 'Product A description', price: '$50.00' },
      { image: 'product2.png', description: 'Product B description', price: '$30.00' },
      // Add more product items as needed
  ];

  // Dynamically generate product items
  productsData.forEach(product => {
      const productItem = document.createElement('div');
      productItem.classList.add('product-item');

      const productImage = document.createElement('img');
      productImage.classList.add('product-image');
      productImage.src = product.image;
      productImage.alt = 'Product Image';

      const productDescription = document.createElement('p');
      productDescription.classList.add('product-description');
      productDescription.innerHTML = `${product.description}<br><br>Price: ${product.price}`;

      const buyNowButtonContainer = document.createElement('div');
      buyNowButtonContainer.classList.add('buy-now-button-container');

      const buyNowButton = document.createElement('button');
      buyNowButton.classList.add('buy-now-button');
      buyNowButton.textContent = 'Buy Now';

      buyNowButtonContainer.appendChild(buyNowButton);

      productItem.appendChild(productImage);
      productItem.appendChild(productDescription);
      productItem.appendChild(buyNowButtonContainer);
      productList.appendChild(productItem);
  });
});
