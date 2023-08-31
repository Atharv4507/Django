window.addEventListener('DOMContentLoaded', function () {
    var links = document.querySelectorAll('.left-nav a');
    for (var i = 0; i < links.length; i++) {
        links[i].addEventListener('click', function () {
            this.classList.add('visited-link');
            links[i].stroke();
        });
    }
});


// document.addEventListener('DOMContentLoaded', () => {
//     const courseLinks = document.querySelectorAll('.left-nav a');
//     const progressElement = document.getElementById('progress');
//     const totalCourses = courseLinks.length;
//     let visitedCourses = 0;

//     // Event listener for each course link
//     courseLinks.forEach((link) => {
//         link.addEventListener('click', () => {
//             visitedCourses++;
//             updateProgress();
//         });
//     });

//     function updateProgress() {
//         const progress = (visitedCourses / totalCourses) * 100;
//         progressElement.textContent = `${progress}%`;
//     }
// });

document.addEventListener('DOMContentLoaded', () => {
    const courseLinks = document.querySelectorAll('.left-nav a');
    const progressElement = document.getElementById('progress');
    const totalCourses = courseLinks.length;
    let visitedCourses = 0;
    const visitedCoursesStr = localStorage.getItem('visitedCourses');
    if (visitedCoursesStr) {
        visitedCourses = parseInt(visitedCoursesStr);
    }
    courseLinks.forEach((link) => {
        link.addEventListener('click', () => {
            visitedCourses++;
            localStorage.setItem('visitedCourses', visitedCourses);
            updateProgress();
        });
    });

    function updateProgress() {
        const progress = (visitedCourses / totalCourses) * 100;
        progressElement.textContent = `${progress}%`;
    }

    updateProgress();
});