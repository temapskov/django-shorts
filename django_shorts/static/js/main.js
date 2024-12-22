document.addEventListener('DOMContentLoaded', function() {
    const videoContainer = document.getElementById('videos-container');
    let campaignId = 1;  // Например, ID кампании

    fetch(`/api/shorts/campaigns/${campaignId}/videos`)
        .then(response => response.json())
        .then(data => {
            data.forEach(video => {
                const videoElement = document.createElement('div');
                videoElement.classList.add('video-item');
                videoElement.innerHTML = `
                    <video src="${video.video_file}" autoplay loop muted></video>
                `;
                videoContainer.appendChild(videoElement);
            });

            let currentIndex = 0;
            const videos = document.querySelectorAll('.video-item');
            function showNextVideo() {
                if (currentIndex < videos.length - 1) {
                    videos[currentIndex].style.display = 'none';
                    currentIndex++;
                    videos[currentIndex].style.display = 'block';
                }
            }

            function showPreviousVideo() {
                if (currentIndex > 0) {
                    videos[currentIndex].style.display = 'none';
                    currentIndex--;
                    videos[currentIndex].style.display = 'block';
                }
            }

            // Плавный скроллинг видео
            videoContainer.addEventListener('wheel', function(event) {
                if (event.deltaY > 0) {
                    showNextVideo();
                } else {
                    showPreviousVideo();
                }
            });

            // Изначально показываем первое видео
            videos[currentIndex].style.display = 'block';
        });
});