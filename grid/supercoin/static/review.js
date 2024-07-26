document.addEventListener("DOMContentLoaded", function () {
    const reviewText = document.getElementById("reviewText");
    const postReviewButton = document.getElementById("postReviewButton");
    const popup = document.getElementById("popup");
    const closePopupButton = document.getElementById("closePopupButton");
    const emojiOptions = document.querySelectorAll(".emoji-option");
  
    let selectedEmojiContainer = null;
  
    emojiOptions.forEach((emojiOption) => {
      emojiOption.addEventListener("click", function () {
        if (selectedEmojiContainer) {
          selectedEmojiContainer.classList.remove("selected");
        }
        emojiOption.classList.add("selected");
        selectedEmojiContainer = emojiOption;
      });
    });
  
    postReviewButton.addEventListener("click", function () {
      if (reviewText.value.length > 0 && selectedEmojiContainer) {
        selectedEmojiContainer.style.backgroundColor = "rgba(0, 255, 0, 0.3)";
        showPopup();
      }
    });
  
    closePopupButton.addEventListener("click", function () {
      hidePopup();
    });
  
    function showPopup() {
      popup.style.display = "flex";
    }
  
    function hidePopup() {
      popup.style.display = "none";
    }
  });
  