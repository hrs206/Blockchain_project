document.addEventListener('DOMContentLoaded', function () {
    const supercoinsElement = document.getElementById('supercoins');
  
    // Simulated reward data
    const earnedSupercoins = 100; // You can dynamically update this value from the backend
  
    supercoinsElement.textContent = `${earnedSupercoins} Supercoins`;
  
    const calculateButton = document.getElementById('calculateButton');
    calculateButton.addEventListener('click', function () {
      calculateButton.textContent = 'Calculating...';
      
      // Simulate an API call to calculate total rewards
      setTimeout(() => {
        const totalRewardsElement = document.getElementById('totalRewards');
        const totalRewards = calculateTotalRewards(); // Your reward calculation logic here
        totalRewardsElement.textContent = `Total Rewards Earned: ${totalRewards}`;
        calculateButton.textContent = 'Calculate Total Rewards';
      }, 2000); // Simulated delay for demonstration purposes
    });
  });
  
  function calculateTotalRewards() {
    // Simulated calculation logic
    return Math.floor(Math.random() * 500) + 100;
  }
  