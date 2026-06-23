// ==========================
// MOBILE MENU TOGGLE
// ==========================

const menuToggle = document.querySelector(".menu-toggle");
const navLinks = document.querySelector(".nav-links");

if (menuToggle && navLinks) {
    menuToggle.addEventListener("click", function () {
        navLinks.classList.toggle("active");
    });
}


// ==========================
// SEARCH FILTER (Find Tutors Page)
// ==========================

const searchInput = document.querySelector("input[name='search']");
const cards = document.querySelectorAll(".card");

if (searchInput && cards.length > 0) {

    searchInput.addEventListener("input", function () {

        let filter = searchInput.value.toLowerCase();
        let found = false;

        cards.forEach(card => {

            let text = card.innerText.toLowerCase();

            if (text.includes(filter)) {
                card.style.display = "block";
                found = true;
            } else {
                card.style.display = "none";
            }

        });

        // No results message
        let msg = document.getElementById("no-results");

        if (!msg) {
            msg = document.createElement("p");
            msg.id = "no-results";
            msg.style.textAlign = "center";
            msg.style.marginTop = "20px";
            msg.style.color = "red";
            document.querySelector(".card-container")?.after(msg);
        }

        msg.innerText = found ? "" : "No tutors available for this subject";

    });
}


// ==========================
// BOOK BUTTON FUNCTION (opens booking modal)
// ==========================

const bookingModal = document.getElementById('bookingModal');
const bookingForm = document.getElementById('bookingForm');
const bookingTutorInput = document.getElementById('bookingTutor');

document.querySelectorAll('.card button, .book-btn').forEach(button => {
    button.addEventListener('click', function () {
        const card = button.closest('.card');
        const tutorName = card?.querySelector('h3')?.innerText || '';
        if (bookingTutorInput) bookingTutorInput.value = tutorName;
        if (bookingModal) bookingModal.classList.add('active');
    });
});

// Cancel button 
document.addEventListener('click', function (e) {
    if (e.target && e.target.id === 'bookingCancel') {
        if (bookingModal) bookingModal.classList.remove('active');
    }
});

// Close modal when clicking outside the dialog
if (bookingModal) {
    bookingModal.addEventListener('click', function (e) {
        if (e.target === bookingModal) bookingModal.classList.remove('active');
    });
}



// ==========================
// LOGIN VALIDATION
// ==========================

document.querySelectorAll("form").forEach(form => {

    form.addEventListener("submit", function (e) {

        let email = form.querySelector("input[type='email']");
        let password = form.querySelector("input[type='password']");

        if (email && password) {

            if (email.value.trim() === "" || password.value.trim() === "") {
                e.preventDefault();
                alert("Please fill all fields.");
            }

        }

    });

});