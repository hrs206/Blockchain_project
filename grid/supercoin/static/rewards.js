// JavaScript logic for the Rewards page
document.addEventListener('DOMContentLoaded', function () {
    const rewardList = document.querySelector('.reward-list');
  
    // Dynamically generate reward items
    rewardsData.forEach(reward => {
      const rewardItem = document.createElement('div');
      rewardItem.classList.add('reward-item');
  
      const rewardImage = document.createElement('img');
      rewardImage.classList.add('reward-image');
      rewardImage.src = reward.image;
      rewardImage.alt = 'Reward Image';
  
      const rewardDescription = document.createElement('p');
      rewardDescription.classList.add('reward-description');
      rewardDescription.textContent = reward.description;
  
      rewardItem.appendChild(rewardImage);
      rewardItem.appendChild(rewardDescription);
      rewardList.appendChild(rewardItem);
    });
  });
  