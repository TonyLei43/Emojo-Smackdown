
    function changeCatImage() {
        // Assuming you have images named img1.jpg, img2.jpg, etc.
        const numberOfImages = 20; // Update this with the number of images you have
        const randomIndex = Math.floor(Math.random() * numberOfImages) + 1; // Generate a random index between 1 and numberOfImages
        const newImageUrl = `../static/cat_images/${randomIndex}.jpeg`; // Construct the new image URL

        const robotImage = document.getElementById('robot');
        robotImage.src = newImageUrl; // Update the image source
    }

    setInterval(changeCatImage, 10000); // Change image every 10 seconds



    
